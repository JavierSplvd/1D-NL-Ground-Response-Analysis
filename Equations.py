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


# Solving the differential equation with an explicit finite differences scheme
def get_velocity_next_time_step(time_step, width, density, velocity_list, tau_list, index, number_elements,
                                rock_velocity):
    # Since the boundary condition of the ground surface is free surface tau_list[0] = 0
    if index == 0:
        v = velocity_list[i] + time_step / density / width * (tau_list[index + 1])
    # The bottom surface has the same velocity as the rock layer.
    if index == number_elements - 1:
        v = rock_velocity
    v = velocity_list[i] + time_step / density / width * (tau_list[index + 1] - tau_list[index])


def get_strain(velocity_time_history, element_number, time_step, width):
    velocity_node_over_time_element_1 = [velocity_column[element_number] for velocity_column in velocity_time_history]
    velocity_node_over_time_element_2 = [velocity_column[element_number + 1] for velocity_column in
                                         velocity_time_history]
    displacement_list_element_1 = integrate(velocity_node_over_time_element_1, time_step)
    displacement_list_element_2 = integrate(velocity_node_over_time_element_2, time_step)
    strain = (displacement_list_element_2[-1] - displacement_list_element_1[-1]) / width
    return strain
