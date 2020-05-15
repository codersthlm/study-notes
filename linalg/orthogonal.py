import numpy as np
A = np.array([1,0, 0])

B = np.array([0, 1, 0])

#Are A and B orthoganal?

dot_product = np.dot(A , B)

assert dot_product == 0

#Then we can use the transpose 
assert np.matmul(A.T, B) == 0 


#These vectors are the x and y axel. But how do we get a vector that is normal to the xy -plane?
# We use the crossproduct of the vectors.

cross_product = np.cross(A,B)
print(cross_product)

#It is the z axel. 
#[0, 0, 1]







