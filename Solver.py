# import sympy 
from sympy import * 
j=1j

# input matrix (change this as needed)
matrix=[
    [3+2j,2j,-3,0],
    [0,1,0,5],
    [-3,-j,3+j,10j]
]
#show the input
print("input Matrix:")
for row in matrix:
    print(row)
print()   
    
# Use sympy.Matrix()
M = Matrix([row for row in matrix])

# Use sympy.rref() method 
mat = str(M.rref()[0]).split('[')
mat = mat[2:]
mat[-1] = mat[-1][0:-2]
# show the rref matrix
print("rref matrix:")
for row in mat:
    print('[', row, sep = '')