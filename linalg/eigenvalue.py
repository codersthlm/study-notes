#Ax = lx
#l = lamda

#Rewrite (A - lI)x = 0 
#det(A - lI) = 0 

# Find lamda first.

import numpy as np
import scipy.linalg

A = [[3, 1],
     [1, 3]]

l, eigv = np.linalg.eig(A)



#Another solution det(A - lI) = 0 
#Lamda in diagonal.

#(3-l)(3-l)-1 = 0
#Solve for lamda.

lamda1 = 4
lamda2 = 2

lamda1Vector = lamda1 * (np.identity(2))
sol1 = A - lamda1Vector

lamda2Vector = lamda2 * (np.identity(2))
sol2 = A - lamda2Vector



P, L, U  = scipy.linalg.lu(sol1)
P2, L2, U2  = scipy.linalg.lu(sol2)


print(U2)



