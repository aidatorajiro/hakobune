import numpy as np
import matplotlib.pyplot as plt

a = 0.01  # E+S -> ES
b = 0.001 # ES -> E+S
c = 0.01  # E+S -> E+P

update_matrix = np.array(
    [[1-a,b   ,0],
     [a ,1-b-c,0],
     [0 ,c    ,1]]
  )


# E+S, ES, E+P
current_state = np.array([10.0, 0.0, 0.0])

log = []

for i in range(0, 600):
    dot = np.dot(update_matrix, current_state)
    log.append(dot)
    current_state = dot

log = np.array(log)

plt.plot(log[:,0], label="E+S")
plt.plot(log[:,1], label="ES")
plt.plot(log[:,2], label="E+P")
plt.xlabel('Time')
plt.ylabel('Concentration')

plt.legend()

plt.show()