import numpy as np
import matplotlib.pyplot as plt

x = np.array([10, 1, 5, 6, 2, 4, 6, 3, 7, 6, 4, 2, 3, 6, 4, 5, 9, 1, 2, 8, 7])
y = np.array([45, 20, 36, 34, 40, 31, 26, 24, 42, 49, 37, 10, 15, 35, 27, 20, 46, 6, 40, 38, 30])

plt.xlabel('x')
plt.ylabel('y')

plt.scatter(x, y, color = "m", marker = "o", s = 30)

plt.show()
