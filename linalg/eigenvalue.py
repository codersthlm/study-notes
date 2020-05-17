# Find eigenvalue and eigenvectors of matrix A.
#Ax = lx
#l = lamda

# Rewrite (A - lI)x = 0
# det(A - lI) = 0

# Find lamda first.

import numpy as np
import scipy.linalg


A = np.array([[3, 1],
              [1, 3]])

(l, eigv) = np.linalg.eig(A)

# More by hand 
# Another solution det(A - lI) = 0
# Lamda in diagonal.

# (3-l)² = 1
# Solve for lamda. l1 = 4 and l2 = 2 

lamda1 = l[0]
lamda2 = l[1]

lamda1Vector = lamda1 * (np.identity(2))
sol1 = A - lamda1Vector

lamda2Vector = lamda2 * (np.identity(2))
sol2 = A - lamda2Vector


# We will solve a type of Bx = 0. That is solve for N(B), The Nullspace of B. 

X1 = scipy.linalg.null_space(sol1)
X2 = scipy.linalg.null_space(sol2)

# Need to reshape to compare.
X1 = X1.reshape((2,))
X2 = X2.reshape((2,))

assert np.allclose(X1, eigv[:,0])
assert np.allclose(X2, eigv[:,1])

print(lamda1)