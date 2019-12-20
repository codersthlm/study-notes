import numpy as np

a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a*b

print(c)
print(np.shape(c))


A = np.random.randn(4,3)
B = np.sum(A, axis = 1, keepdims = True)


print(np.shape(B))
