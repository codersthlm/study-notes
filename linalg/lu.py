import numpy as np
import scipy.linalg
import tensorflow as tf

#Consider
# 2X1 + X2 +3X3 = 17
# 4X1 - X2 + 3X3 = 31
# -2X1 + 5X2 + 5X3 = -5


A = np.array([[2., 1., 3.],
             [4., -1., 3.],    
            [-2., 5., 5.]    
])


B = np.array([17., 31., -5.]).T

(P,L,U) = scipy.linalg.lu(A)

L =  np.array([[1,0,0],
             [2,1,0],
             [-1,-2,1]])

U = np.array([[2,1,3],
             [0,-3,-3],
             [0,-0,2]])


Y = np.linalg.solve(L, B)

X = np.linalg.solve(U, Y)

solution = np.linalg.solve(A, B)

assert np.allclose(X,solution)






