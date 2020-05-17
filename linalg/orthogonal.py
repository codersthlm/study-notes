import numpy as np
A = np.array([1, 0, 0])
B = np.array([0, 1, 0])

# Are A and B orthogonal? The dot product should be zero.

dot_product = np.dot(A, B)

assert dot_product == 0

# Then we can use the transpose
assert np.matmul(A.T, B) == 0


# These vectors are the x and y plane. But how do we get a vector that is normal to the xy -plane?
# We use the crossproduct of the vectors.

cross_product = np.cross(A, B)

# It is the z-axis.
#[0, 0, 1]

assert np.allclose(cross_product, [0, 0, 1])

