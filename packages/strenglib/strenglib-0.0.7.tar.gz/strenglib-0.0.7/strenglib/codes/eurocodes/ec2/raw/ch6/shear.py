import math
from collections import namedtuple


def VRdc_new(CRdc, Asl, fck, σcp, bw, d):
    return VRdc_new_with_intermediates(CRdc, Asl, fck, σcp, bw, d)[0]

def VRdc_new_with_intermediates(CRdc, Asl, fck, σcp, bw, d):
    """ The design value for the shear resistance :math:`V_{Rd,c}` [N]

    Args:
        CRdc (float): 0.18/γc
        Asl (float): [mm2] is the area of the tensile reinforcement
        fck (float): [N/mm2]
        σcp (float):  :math:`σ_{cp}=N_{Ed}/A_c \lt 0.2f_{cd}` [N/mm2]
        bw (float): The second parameter. [mm]
        d (float): The second parameter. [mm]

    Returns:
        tuple (result, list of dictionaries):

        Result in [N]. Given using the expressions

        .. math::
            V_{Rd,c} = max \\left\{\\begin{matrix}
            [C_{Rd,c} \cdot k \cdot(100\cdot ρ_l\cdot f_{ck})^{1/3} + k_1 \cdot σ_{cp}] \cdot b_w \cdot d \\\\
            (v_{min} + k_1 \cdot σ_{cp}) \cdot b_w \cdot d
            \\end{matrix}\\right.

        where:

        - :math:`k=1 + \sqrt{\dfrac{200}{d}} <= 2.0`

        - :math:`ρ_l=\dfrac{A_{sl}}{b_w \cdot d}<=0.02`

        - :math:`k_1 = 0.15`

    """
    ρl = min(Asl / (bw * d), 0.02)
    k = min(1 + (200.0 / d)**0.5, 2.0)
    vmin = 0.035 * k**1.5 * fck**0.5
    k1 = 0.15

    VRdc1 = (CRdc * k * math.pow((100 * ρl * fck), (1/3)) + k1 * σcp) * bw * d
    VRdc2 = (vmin + k1 * σcp) * bw * d

    VRdc = max(VRdc1, VRdc2)

    _log = list()
    _log.append({'quantity':'ρl', 'value':ρl, 'units':''})
    _log.append({'quantity':'k', 'value':k, 'units':''})
    _log.append({'quantity':'vmin', 'value':vmin, 'units':''})
    _log.append({'quantity':'k1', 'value':k1, 'units':''})
    _log.append({'quantity':'VRdc1', 'value':VRdc1, 'units':'N'})
    _log.append({'quantity':'VRdc2', 'value':VRdc2, 'units':'N'})
    _log.append({'quantity':'VRdc', 'value':VRdc, 'units':'N'})


    return VRdc, _log


    # return res(VRdc, ρl, k, vmin, k1, VRdc1, VRdc2)


def VRdc(CRdc, Asl, fck, σcp, bw, d):
    """ The design value for the shear resistance :math:`V_{Rd,c}` [N]
    
    Args:
        CRdc (float): 0.18/γc
        Asl (float): [mm2] is the area of the tensile reinforcement
        fck (float): [N/mm2]
        σcp (float):  :math:`σ_{cp}=N_{Ed}/A_c \lt 0.2f_{cd}` [N/mm2]
        bw (float): The second parameter. [mm]
        d (float): The second parameter. [mm]
    
    Returns:
        tuple (result, string with intermediate calculations):

        Result in [N]. Given using the expressions

        .. math::
            V_{Rd,c} = max \\left\{\\begin{matrix}
            [C_{Rd,c} \cdot k \cdot(100\cdot ρ_l\cdot f_{ck})^{1/3} + k_1 \cdot σ_{cp}] \cdot b_w \cdot d \\\\
            (v_{min} + k_1 \cdot σ_{cp}) \cdot b_w \cdot d
            \\end{matrix}\\right.

        where:

        - :math:`k=1 + \sqrt{\dfrac{200}{d}} <= 2.0`

        - :math:`ρ_l=\dfrac{A_{sl}}{b_w \cdot d}<=0.02`

        - :math:`k_1 = 0.15`

    """

    # logtext = []

    ρl = min(Asl / (bw * d), 0.02)
    k = min(1 + (200.0 / d)**0.5, 2.0)
    vmin = 0.035 * k**1.5 * fck**0.5
    k1 = 0.15

    VRdc1 = (CRdc * k * math.pow((100 * ρl * fck), (1/3)) + k1 * σcp) * bw * d
    VRdc2 = (vmin + k1 * σcp) * bw * d

    _VRdc = max(VRdc1, VRdc2)

    # logtext.append(f'ρl = {ρl:.5f}')
    # logtext.append(f'k = {k:.5f}')
    # logtext.append(f'vmin = {vmin:.5f}')
    # logtext.append(f'k1 = {k1:.5f}')
    # logtext.append(f'VRdc1 = {VRdc1:.2f}N')
    # logtext.append(f'VRdc2 = {VRdc2:.2f}N')
    # logtext.append(f'VRdc = {_VRdc:.2f}N')

    _log = list()
    _log.append(['ρl', ρl, ''])
    _log.append(['k', k, ''])
    _log.append(['vmin', vmin, ''])
    _log.append(['k1', k1, ''])
    _log.append(['VRdc1', VRdc1, 'N'])
    _log.append(['VRdc2', VRdc2, 'N'])
    _log.append(['VRdc', VRdc, 'N'])

    # return _VRdc, ('\n').join((logtext))
    return _VRdc, _log


def VRdmax(bw, d, fck, fyk, fywk, θ, αcw = 1.0, γc = 1.5):
    return VRdmax_with_intermediates(bw, d, fck, fyk, fywk, θ, αcw, γc)[0]

def VRdmax_with_intermediates(bw, d, fck, fyk, fywk, θ, αcw = 1.0, γc = 1.5):
    ## Πρέπει να τσεκάρω τι γίνεται με τα v1. Κυρίως στο Note 1 & 2 της 6.2.3(3)
    ## Μάλλον εννοεί όταν το fywd του εγκάρσιου είναι μικρότερο από το 0.8 του fyk του διαμήκους, δηλαδή όταν χρησιμοποιούνται διαφορετικές ποιότητες χάλυβα

    fck = 0.001*fck
    bw = 1000.*bw
    d = 1000.*d

    z = 0.9 * d
    fcd = fck / γc

    if fywk<0.8*fyk:
        if fck <= 60:
            v1 = 0.6
        else:
            v1 = max(0.5, 0.9-fck/200)
    else:
        v1 = 0.6 * (1-fck/250)

    _VRdmax = αcw * bw * z * v1 * fcd  / (math.tan(θ) + 1/math.tan(θ))

    _log = list()
    _log.append({'quantity': 'z', 'value': z, 'units': 'mm'})
    _log.append({'quantity': 'fcd', 'value': fcd, 'units': 'N/mm2'})
    _log.append({'quantity': 'v1', 'value': v1, 'units': ''})
    _log.append({'quantity': 'VRdmax', 'value': _VRdmax, 'units': 'N'})

    _VRdmax = _VRdmax / 1000.
    _log.append({'quantity': 'VRdmax', 'value': _VRdmax, 'units': 'kN'})

    return _VRdmax, _log


def VRds(nw, diaw, d, fyk, fywk, θ, s, γs = 1.15):
    return VRds_with_intermediates(nw, diaw, d, fyk, fywk, θ, s, γs)[0]

def VRds_with_intermediates(nw, diaw, d, fyk, fywk, θ, s, γs = 1.15):
    diaw = 1000.*diaw
    d = 1000.*d
    fyk = 0.001*fyk
    fywk = 0.001*fywk
    s = 1000.*s

    z = 0.9 * d
    Asw = nw * math.pi * diaw**2 /4

    if fywk<0.8*fyk:
        fywd = min(0.8*fywk, fywk/γs)
    else:
        fywd = fywk/γs

    _VRds = (Asw / s) * z * fywd * (1./math.tan(θ))


    _log = list()
    _log.append({'quantity': 'z', 'value': z, 'units': 'mm'})
    _log.append({'quantity': 'Asw', 'value': Asw, 'units': 'mm2'})
    _log.append({'quantity': 'fywd', 'value': fywd, 'units': 'N/mm2'})
    _log.append({'quantity': 'VRds', 'value': _VRds, 'units': 'N'})

    _VRds = _VRds / 1000.
    _log.append({'quantity': 'VRds', 'value': _VRds, 'units': 'kN'})

    return _VRds, _log