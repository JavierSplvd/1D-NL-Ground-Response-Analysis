import numpy as np
from Equations import *

width = 1
time_step = 0.02
rho = 20
node_number = 3

ground_motion_velocity = [1, 1, 1]
ground_motion_displacement = integrate(ground_motion_velocity, 0.02)

velocity_time_history = []
velocity_time_history.append([])
for i in range(node_number):
    velocity_time_history[0].append(0)

print(velocity_time_history)

# Iteration
temp = []
for i in range(node_number):
    tau_column = create_tau_column(velocity_time_history, node_number, time_step, width, ground_motion_displacement[0])
    temp.append(
        get_velocity_next_time_step(time_step, width, rho, velocity_time_history[0], tau_column, i, node_number,
                                    ground_motion_velocity[0]))
velocity_time_history.append(temp)
print(velocity_time_history)
