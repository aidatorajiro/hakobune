import numpy as np
import matplotlib.pyplot as plt

# E+S, ES, E+P
current_state = [10.0, 0.0, 0.0]

log = []

for i in range(0, 600):
    x = current_state[0]
    y = current_state[1]
    z = current_state[2]
    result = [,,]
    log.append(result)
    current_state = result

log = np.array(log)

plt.plot(log[:,0], label="E+S")
plt.plot(log[:,1], label="ES")
plt.plot(log[:,2], label="E+P")
plt.xlabel('Time')
plt.ylabel('Concentration')

plt.legend()

plt.show()