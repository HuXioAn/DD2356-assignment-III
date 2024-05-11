import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data from the user's input
nodes = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536,
         131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216,
         33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]

on_node_times = [
    0.000001086, 0.000000617, 0.000000590, 0.000000584, 0.000000611, 0.000000675,
    0.000000922, 0.000001287, 0.000002170, 0.000003018, 0.000002157, 0.000004537,
    0.000006508, 0.000012500, 0.000025748, 0.000043903, 0.000091261, 0.000169475,
    0.000340688, 0.000698781, 0.001428170, 0.002067761, 0.003105643, 0.005019280,
    0.009332375, 0.017553499, 0.034435326, 0.066967195
]

out_of_node_times = [
    0.000002237, 0.000002186, 0.000002266, 0.000002180, 0.000002776, 0.000003006,
    0.000002895, 0.000003025, 0.000003099, 0.000003252, 0.000003676, 0.000004237,
    0.000007570, 0.000008804, 0.000011603, 0.000017062, 0.000027969, 0.000049676,
    0.000093088, 0.000180057, 0.000359693, 0.000703836, 0.001402947, 0.002813703,
    0.005619822, 0.011232996, 0.022459838, 0.044922639
]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(nodes, on_node_times, label='On-node Time', marker='o')
plt.plot(nodes, out_of_node_times, label='Out-of-node Time', marker='x')

plt.xlabel('Message size(B)')
plt.ylabel('Time (seconds)')
plt.title('Comparison of On-node and Out-of-node Times')
plt.legend()
plt.grid(True)
plt.show()






# Define a linear model for curve fitting
def linear_model(x, a, b):
    return a * x + b

# Fit the linear model to the data
# Convert nodes to log scale for linear fitting, because we're dealing with exponential growth
log_nodes = np.log(nodes)

# Fit the on-node and out-of-node times to a linear model
params_on_time, _ = curve_fit(linear_model, nodes, on_node_times)
params_out_time, _ = curve_fit(linear_model, nodes, out_of_node_times)


print(params_on_time)
print(params_out_time)

import matplotlib.pyplot as plt
import numpy as np

# Data for f and dfdx
f = np.array([0.000000, 0.049066, 0.098014, 0.146726, 0.195085, 0.242973, 0.290276, 0.336880,
              0.382673, 0.427543, 0.471384, 0.514089, 0.555556, 0.595684, 0.634378, 0.671543,
              0.707090, 0.740935, 0.772994, 0.803191, 0.831454, 0.857713, 0.881906, 0.903975,
              0.923866, 0.941532, 0.956929, 0.970022, 0.980777, 0.989170, 0.995180, 0.998793, 1.000000])

dfdx = np.array([1.001484, 0.998394, 0.994785, 0.988780, 0.980393, 0.969644, 0.956559, 0.941169,
                 0.923513, 0.903632, 0.881574, 0.857392, 0.831145, 0.802896, 0.772713, 0.740668,
                 0.706839, 0.671308, 0.634159, 0.595482, 0.555371, 0.513922, 0.471236, 0.427414,
                 0.382562, 0.336789, 0.290204, 0.242921, 0.195052, 0.146713, 0.098021, 0.049093, 0.000046])

# x values from 0 to the length of the arrays
x = np.linspace(0, 32, 33)

# Plotting both f and dfdx
plt.figure(figsize=(10, 6))
plt.plot(x, f, label='f(x)')
plt.plot(x, dfdx, label="f'(x)", linestyle='--')
plt.title('Function f and its derivative df/dx')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
