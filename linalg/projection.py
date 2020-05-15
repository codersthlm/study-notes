# Given points (1,1)  (2,2) and  (3,2)
# find best fitting line

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 1],
              [1, 2],
              [1, 3]])

B = np.array([1, 2, 2])

m, c = np.linalg.lstsq(A, B)[0]

print(m)
print(c)


plt.plot(A, B, 'o', label='Original data', markersize=10)
plt.plot(A, m*A + c, 'r', label='Fitted line')
plt.legend()
plt.show()
