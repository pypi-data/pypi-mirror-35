import math


def θy(φy, Ls, av, z, h, db, fy, fc):
    """

    Args:
        φy (float): Καμπυλότητα διαρροής
        Ls (float): Μήκος διάτμησης [m]
        av (float):
        z (float): Ο μοχλοβραχίονας των εσωτερικών δυνάμεων [m]
        h (float):
        db (float):
        fy (float):
        fc (float):

    Returns:
        float: Given using the expression:

        .. math:: θ_y=φ_y\dfrac{L_s+a_vz}{3}+0.0014 \Big(1+1.5\dfrac{h}{L_s} \Big)+\dfrac{φ_yd_bf_y}{8\sqrt{f_c}}
    """
    return φy * (Ls + av * z) / 3 + 0.0014 * (1 + 1.5 * h / Ls) + φy * db * fy / (8 * math.pow(fc, 0.5))


def θumcalc(ν, ωtot, ω2, αs, α, ρs, ρd, fc, fyw):
    part1 = (fc * max(0.01, ω2) / max(0.01, (ωtot-ω2)))**0.225
    part2 = αs**0.35
    part3 = 25.0**(α * ρs * fyw / fc)
    part4 = 1.25**(100 * ρd)
    return 0.016 * 0.3**ν * part1 * part2 * part3 * part4


def αcalc(sh, bc, hc, Σbi2):
    return (1-sh/(2*bc))*(1-sh/(2*hc))*(1-Σbi2/(6*bc*hc))