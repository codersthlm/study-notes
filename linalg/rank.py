import numpy as np
rows = [[1, 2, 1], [3, 8, 1], [0, 4,  1]]

A = np.array(rows)
rank_A = np.linalg.matrix_rank(A)
assert rank_A == 3

## So the vectors are linear independent. And they span R3. The vectors form a basis in R3.

#Check the dimension  
dim_A = A.shape

assert dim_A[0] == 3
assert dim_A[1] == 3


print(dim_A)


