import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

SEGMENTS = 10
ERROR_INV = 120

class Line:
    # x and y are lengths of axes
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.error = x / ERROR_INV
        self.segWidth = x / SEGMENTS

    def smooth(self, x, y, swap = False):
        if swap:
            x, y = y, x

        x_mod = np.linspace(x.min(), x.max(), 300) 

        spl = make_interp_spline(x, y, k=3)
        y_mod = spl(x_mod)

        if swap:
            return y_mod, x_mod

        return x_mod, y_mod

    # Returns bad horizontal line approximately between (x0, y) and (x1, y)
    # If preciseFirst is true, the leftmost point is in the correct position
    # If false, the rightmost point is in correct position
    def getHorizontal(self, x0, x1, y, preciseFirst = True):
        segments = max(5, int((x1 - x0) / self.segWidth))
        rand = np.random.uniform(size=segments, low=-1 * self.error, high=self.error)

        x_arr = np.linspace(x0, x1, segments)
        y_arr = np.empty(segments)

        if preciseFirst:
            y_arr[0] = y
        else:
            y_arr[-1] = y

        for i in range(1, segments):
            if preciseFirst:
                y_arr[i] = y_arr[i - 1] + rand[i]
            else:
                y_arr[segments - i - 1] = y_arr[segments - i] + rand[i]

        return self.smooth(x_arr, y_arr)

    # Returns bad vertical line approximately between (x, y0) and (x, y1)
    # If preciseFirst is true, the top point is in the correct position
    # If false, the bottom point is in correct position
    def getVertical(self, y0, y1, x, preciseFirst = True):
        segments = max(5, int((y1 - y0) / self.segWidth))
        rand = np.random.uniform(size=segments, low=-1 * self.error, high=self.error)

        y_arr = np.linspace(y0, y1, segments)
        x_arr = np.empty(segments)

        if preciseFirst:
            x_arr[0] = x
        else:
            x_arr[-1] = x

        for i in range(1, segments):
            if preciseFirst:
                x_arr[i] = x_arr[i - 1] + rand[i]
            else:
                x_arr[segments - i - 1] = x_arr[segments - i] + rand[i]

        return self.smooth(x_arr, y_arr, swap = True)

    def drawAxes(self):
        xAxis = self.getHorizontal(0, self.x, 0)
        yAxis = self.getVertical(0, self.y, 0)

        plt.plot(xAxis[0], xAxis[1], 'b')
        plt.plot(yAxis[0], yAxis[1], 'b')

    # (x, y) is bottom center of bar
    def drawBar(self, x, y, width, height):
        left = self.getVertical(y, y + height, x - width / 2)
        endX = left[0][-1]
        top = self.getHorizontal(endX, endX + width, y + height)
        endY = top[1][-1]
        right = self.getVertical(y, endY, endX + width, False)

        plt.plot(left[0], left[1], 'b')
        plt.plot(top[0], top[1], 'b')
        plt.plot(right[0], right[1], 'b')
