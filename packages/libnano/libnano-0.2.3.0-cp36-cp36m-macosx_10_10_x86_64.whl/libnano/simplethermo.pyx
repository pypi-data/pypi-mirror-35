from libnano.seqstr import reverseComplement as _rc
import math as _math
# ~~~~~~~~~~~~~~~~~~~~ GENERAL CONSTANTS AND CALCULATIONS ~~~~~~~~~~~~~~~~~~~ #

cdef float R = 1.9872e-3  # Gas constant (1 / kcal * mol)
cdef float KELVIN = 273.15


def cToK(deg_c):
    ''' Convert degrees Celsius to degrees Kelvin

    Args:
        deg_c (float): temperature in [Celsius]

    Returns:
        float: temperature in [Kelvin]
    '''
    return deg_c + KELVIN


def kToC(deg_k):
    ''' Convert degrees Kelvin to degrees Celsius

    Args:
        deg_k (float): temperature in [Kelvin]

    Returns:
        float: temperature in [Celsius]
    '''
    return deg_k - KELVIN


cdef calcKa(dg, deg_c):
    ''' Return the association constant at a given temperature

    Args:
        dg (float): the free energy in [kcal/mol]
        deg_c (float): temperature in [Celsius]

    Returns:
        float: the association constant at a given temperature
    '''
    return _math.exp**(-dg/(R * cToK(deg_c)))


def calcDg(ds, dh, deg_c):
    ''' Return the dg at a given temp using the provided ds and dh

    Args:
        ds (float): the entropy in [kcal/mol]
        dh (float): enthalpy in in [kcal/mol]
        deg_c (float): temperature in [Celsius]

    Returns:
        float: the dg at a given temp using the provided ds and dh
    '''
    return dh - ds * cToK(deg_c)


def calcRandCoil(dg, deg_c):
    ''' Return the percent of randomly coiled oligo with dg at deg_c degrees

    Args:
        dg (float): the free energy in [kcal/mol]
        deg_c (float): temperature in [Celsius]

    Returns:
        float: the percent of randomly coiled oligo with dg at deg_c degrees
    '''
    return 1/(calcKa(dg, deg_c) + 1)


# ~~~~~~~~~~~~~~~~~ PYTHON EQUIVALENT OF PRIMER3 OLIGOTM  ~~~~~~~~~~~~~~~~ #

cdef float divalentToMonovalent(float divalent, float dntp):
    ''' Calculate equivalent monovalent effect for a given
    divalent parameters

    Args:
        divalent (float):
        dntp (float):

    Returns:
        float: equivalent monovalent concentration percent
    '''
    if divalent == 0.:
        dntp = 0.
    if divalent < dntp:
        divalent = dntp
    return 120. * _math.sqrt(divalent - dntp)

def calcThermo(seq, conc_nm=50, monovalent=50, divalent=0.01, dntp=0.0):
    ''' Return the thermo parameters for DNA under specified salt cond.
        Data is from referenced from PRIMER3

    Args:
        seq (str): the sequence to analyze
        conc_nm (Optional[int]): percent concentration
        monovalent (Optional[int]): percent concentration
        divalent (Optional[float]): fractional concentration of Mg2+
        dntp (Optional[float]): fractional concentration dntp

    Returns:
        Tuple[float]: (dH, dS, Tm)
    '''
    cdef float dH, dS
    cdef float monovalent_use, tm
    cdef Py_ssize_t idx
    # Calculate oligo symmetry
    cdef bint sym = seq == _rc(seq)
    dH = dS = 0.
    monovalent_use = monovalent
    enthalpies = {
        'AA': 79, 'AT': 72, 'AG': 78, 'AC': 84,
        'TA': 72, 'TT': 79, 'TG': 85, 'TC': 82,
        'GA': 82, 'GT': 84, 'GG': 80, 'GC': 98,
        'CA': 85, 'CT': 78, 'CG': 106, 'CC': 80
    }
    entropies = {
        'AA': 222, 'AT': 204, 'AG': 210, 'AC': 224,
        'TA': 213, 'TT': 222, 'TG': 227, 'TC': 222,
        'GA': 222, 'GT': 224, 'GG': 199, 'GC': 244,
        'CA': 227, 'CT': 210, 'CG': 272, 'CC': 199
    }
    # Calculate NN uncorrected dS and dH for oligo
    for idx in range(len(seq) - 1):
        dH += enthalpies[seq[idx:idx + 2]]
        dS += entropies[seq[idx:idx + 2]]
    # Terminal AT penalty and initiation parameters (combined)
    if seq[0] in 'AT':
        dH += -23
        dS += -41
    else:
        dH += -1
        dS += 28
    if seq[-1] in 'AT':
        dH += -23
        dS += -41
    else:
        dH += -1
        dS += 28
    if sym:
        dS += 14
    dH *= -100.0
    dS *= -0.1
    # Convert divalent salt and dntp conc. to monovalent equivalencies
    monovalent_use += divalentToMonovalent(divalent, dntp)
    dS = dS + 0.368 * (len(seq) - 1) * _math.log(monovalent / 1000.0)
    # Account for oligo symmetry and calculate tm
    if sym:
        tm = dH / (dS + 1.987 * _math.log(conc_nm/1.0e9)) - KELVIN
    else:
        tm = dH / (dS + 1.987 * _math.log(conc_nm/4.0e9)) - KELVIN
    return dH, dS, tm

def calcTm(seq, conc_nm=50, monovalent=50, divalent=0.01, dntp=0.0):
    _, _, tm = calcThermo(seq, conc_nm=conc_nm, monovalent=monovalent,
            divalent=divalent, dntp=dntp)
    ''' same as `calcThermo` but returns just the melting temperature

    Returns:
        float: Melting temperature in [Celcius]
    '''
    return tm
