# Given points (1,1)  (2,2) and  (3,2)
# find best fitting line

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 1],
              [1, 2],
              [1, 3]])

B = np.array([1, 2, 2])

#y = mx + c

m, c = np.linalg.lstsq(A, B)[0]

#By hand?

#y = C + DT 
# C + D = 1
# C + 2D = 2
# C + 3D = 2

A2 = np.array([[1, 1],
              [1, 2],
              [1, 3]])

B2 = np.array([1, 2, 2])

#Use the estimate formula A2.T * A2 * X = A2.T * B2 

U = A2.T.dot(A2)
V = A2.T.dot(B)


# gives equations
# 3C + 6D = 5
# 6C + 14D = 11

# elimination:
# 2D = 1 => D = 1/2 
# C = 2/3
# Best line y = 2/3 + 1/2X


# Plot to show the fitted line

plt.plot(A, B, 'o', label='Original data', markersize=10)
plt.plot(A, m*A + c, 'r', label='Fitted line')
plt.show()