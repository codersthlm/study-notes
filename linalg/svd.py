import numpy as np
import scipy.linalg


C = np.array([[5,5],
              [-1,7]
          ])

U, s, V = np.linalg.svd(C, full_matrices=False)

# Calculate 
# C = U * Sigma * V.T
# 1. C.T.dot(C) = V *   Sigma.T * Sigma * V.T
# 2. C * V = U * Sigma

CTransposeC = C.T.dot(C)

# WE should calculate eigenvector, eigenvalue.  Will only calculate the eigenvectors.

(l, eigv) = np.linalg.eig(CTransposeC)

lamda1 = l[0]
lamda2 = l[1]

lamda1Vector = lamda1 * (np.identity(2))
sol1 = CTransposeC - lamda1Vector

lamda2Vector = lamda2 * (np.identity(2))
sol2 = CTransposeC - lamda2Vector


# We will solve a type of Bx = 0. That is solve for N(B), The Nullspace of B. 

V1 = scipy.linalg.null_space(sol1)
V2 = scipy.linalg.null_space(sol2)

V = np.column_stack((V1, V2))

sigma1 = np.sqrt(l[0])
sigma2 = np.sqrt(l[1])

Diag = np.array(
    [[sigma1, 0],
    [0, sigma2]
    ])


DiagInverse = np.linalg.inv(Diag)

U = C.dot(V).dot(DiagInverse)  

C2 =  U.dot((Diag.dot(V)))

assert np.allclose(C2, C)