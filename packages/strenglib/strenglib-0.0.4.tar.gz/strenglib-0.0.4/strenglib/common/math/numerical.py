import pandas as pd
import numpy as np


def area_under_curve(x, y, x_start, x_end):
    d = {'x': x, 'y': y}
    df = pd.DataFrame(data=d)

    df.loc[-1, 'x'] = x_start
    df = df.sort_values('x').reset_index(drop=True)
    df.loc[-1, 'x'] = x_end
    df = df.sort_values('x').reset_index(drop=True)
    df = df.interpolate()

    df2 = df[(df.x >= x_start) & (df.x <= x_end)]

    xnew = df2.x
    ynew = df2.y

    res = np.trapz(y=ynew, x=xnew)

    return res


def xy_with_endpoints(x, y, x_start, x_end):
    if x_start <= x[0]:
        x_start = x[0]

    if x_end >= x[-1]:
        x_end = x[-1]

        # Για την αρχή
    y_start = float(np.interp(x_start, x, y))
    # Κρατώ μόνο τις τιμές μετά από το x_start
    _x = x[(x > x_start)]
    _y = y[len(y) - len(_x):len(y)]
    # Προσθέτω τα x, y της παρεμβολής
    _x = np.append(x_start, _x)
    _y = np.append(y_start, _y)

    # Για το τέλος
    y_end = float(np.interp(x_end, x, y))
    # Κρατώ μόνο τις τιμές μέχρι μία πρίν από το x_end
    _x = _x[(_x < x_end)]
    _y = _y[0:len(_x)]
    # Προσθέτω τα x, y της παρεμβολής
    _x = np.append(_x, x_end)
    _y = np.append(_y, y_end)

    return _x, _y