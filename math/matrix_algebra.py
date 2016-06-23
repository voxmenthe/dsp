# Matrix Algebra

import math
import sympy as sym
import numpy as np

A = sym.Matrix([[1,2,3],[2,7,4]])
B = sym.Matrix([[1,-1],[0,1]])
C = sym.Matrix([[5,-1],[9,1],[6,0]])
D = sym.Matrix([[3,-2,-1],[1,2,3]])
u = sym.Matrix([[6,2,-3,5]])
v = sym.Matrix([[3,5,-1,4]])
w = sym.Matrix([[1],[8],[0],[5]])

# part 1
print("A:", A.shape, "B:", B.shape, "C:", C.shape,
	"D:", D.shape, "u", u.shape, "v:", v.shape, "w:", w.shape)

# A: 2x3 B: 2x2 C: 3x2 D: 2x3 u: 1x4 v: 1x4 w: 4x1


# part 2
u + v # [9, 7, -4, 9]
u - v # [3,-3, -2, 1]
6*u # [36, 12, -18, 30]
u.dot(v) # 51
math.sqrt(sum([x**2 for x in u])) # 8.6023...

# part 3
Ct = sym.Transpose(C)
At = sym.Transpose(A)
Dt = sym.Transpose(D)

A + C # not defined
A - Ct # [[-4, -7, -3],[3, 6, 4]]
Ct + 3D # [[14, 3, 3], [2, 7, 9]]
B * A # [[-1, -5, -1], [2, 7, 4]]
B * At # not defined

# Optional
B * C # not defined
C * B # [[5, -6], [9, -8], [6, -6]]
B**4 # [[1, -4],[0,1]]
A * At # [[14,28],[28, 69]]
Dt * D # [[10, -4,  0],[-4,  8,  8],[ 0,  8, 10]]

