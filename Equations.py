import numpy as np
import scipy.interpolate as interp


# Trapezoidal integration of a given array with equal spacing between points.
def integrate(function, step):
    size = len(function)
    integral = np.zeros(size)
    for i in range(size):
        if i == 0:
            continue
        integral[i] = (function[i] + function[i - 1]) / 2 * step + integral[i - 1]
    return integral


# Stress interpolation for a given strain. The stress-strain curve is embedded in the function.
def get_stress(strain):
    stress_points = [0, 100]
    strain_points = [0, 1]
    f = interp.interp1d(strain_points, stress_points)
    return f(strain)
