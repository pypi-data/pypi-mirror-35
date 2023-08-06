def beff(bw, beff1, beff2, b):
    return min(bw + beff1 + beff2, b)


def beffi(bi, l0):
    return min(0.2 * bi + 0.1 * l0, 0.2 * l0, bi)


def l0(l1 =0 , l2 = 0, l3 = 0, zero_moments_case = 0):
    _l0 = 0
    if zero_moments_case==0: _l0 = 1.00 * l1 # αμφιέρειστη
    if zero_moments_case==1: _l0 = 0.85 * l1 # ακραίο άνοιγμα
    if zero_moments_case==2: _l0 = 0.70 * l2 # μεσαίο άνοιγμα
    if zero_moments_case==3: _l0 = 0.15 * (l1 + l2) # μεσαία στήριξη
    if zero_moments_case==4: _l0 = 0.15 * l2 + l3 # στήριξη προβόλου

    return _l0
