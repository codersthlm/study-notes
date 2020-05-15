
# https://www.youtube.com/watch?v=QVKj3LADCnA&list=PL221E2BBF13BECF6C&index=7
# Solve 
# x + 2y + z = 2
# 3x + 8y + z = 12
# 4y + z = 2


import numpy as np

rows = [[1, 2, 1], 
        [3, 8, 1], 
        [ 0, 4,  1 ]]
A = np.array(rows)
det_A = np.linalg.det(A)

# If determinant != 0 there exist an unique solution and an inverse.
assert det_A != 0 

# Find inverse
inv_A = np.linalg.inv(A)

B = np.array([[2, 12, 2]])

# By multiplying by the inverse we solve the linear system.
X = np.dot(inv_A, B.T)

print(X)

#x = 2, y =1, z = -2 
