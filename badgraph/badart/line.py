import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

SEGMENTS = 10
ERROR_INV = 80

def smooth(x, y, swap = False):
    if swap:
        x, y = y, x

    x_mod = np.linspace(x.min(), x.max(), 300) 

    spl = make_interp_spline(x, y, k=3)
    y_mod = spl(x_mod)

    if swap:
        return y_mod, x_mod

    return x_mod, y_mod

# Returns bad horizontal line approximately between (x0, y) and (x1, y)
# If precisePoint is true, the leftmost point is in the correct position
def getHorizontal(x0, x1, y, precisePoint = True):
    d = (x1 - x0) / ERROR_INV
    rand = np.random.uniform(size=SEGMENTS, low=-d, high=d)

    x_arr = np.linspace(x0, x1, SEGMENTS)
    y_arr = np.empty(SEGMENTS)
    if precisePoint:
        rand[0] = 0

    y_arr[0] = y + rand[0]
    for i in range(1, SEGMENTS):
        y_arr[i] = y_arr[i - 1] + rand[i]

    return smooth(x_arr, y_arr)

# Returns bad vertical line approximately between (x, y0) and (x, y1)
# If precisePoint is true, the leftmost point is in the correct position
def getVertical(y0, y1, x, precisePoint = True):
    d = (y1 - y0) / ERROR_INV
    rand = np.random.uniform(size=SEGMENTS, low=-d, high=d)

    y_arr = np.linspace(y0, y1, SEGMENTS)
    x_arr = np.empty(SEGMENTS)
    if precisePoint:
        rand[0] = 0

    x_arr[0] = x + rand[0]
    for i in range(1, SEGMENTS):
        x_arr[i] = x_arr[i - 1] + rand[i]

    return smooth(x_arr, y_arr, swap = True)
