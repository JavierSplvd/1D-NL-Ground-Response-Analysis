import numpy as np


# Trapezoidal integration of a given array with equal spacing between points.
def integrate(function, step):
    size = len(function)
    integral = np.zeros(size)
    for i in range(size):
        if i == 0:
            continue
        integral[i] = (function[i] + function[i - 1]) / 2 * step + integral[i - 1]
    return integral


accel = [x ** 2 for x in np.arange(0, 3.01, 0.01)]
integral = integrate(accel, 0.01)
print(integral)
