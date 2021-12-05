# import sympy 
from sympy import * 
from cmath import polar
from math import pi
j=1j
rad2deg=180/pi
##############################################################
# Degrees (True) or Radians (False)
mode = True
# input number of decimal digits to round to
decimal_digits = 2
# input matrix (change this as needed)
matrix=[
    [1, 0, 2.3456 - 2.3456j],
    [0, 1, 1+2j]
]
##############################################################
assert type(mode) is bool, "set mode to True for degrees or False for radians"
#show the input matrix
print("input Matrix:")
for row in matrix:
    print(row)
print()   

# Use sympy.Matrix() class and sympy.rref() method 
M = Matrix([row for row in matrix])
mat = str(M.rref()[0]).split('[')
mat = mat[2:]
mat[-1] = mat[-1][0:-2]

# show the rref matrix (old method)
'''print("rref matrix:")
for row in mat:
    print('[', row, sep = '')
print()'''

# convert to processbale form (lst of lst)
sq_matrix = []    # square coordinate matrix
for row in mat:
    row = ''.join(row.split()).strip(',').strip(']').split('*I')        # Format changes
    
    #replace *I with j
    if row[-1] == '':
        row.pop()
        row[-1] += 'j'
        
    # code is only replacing last complex *I with j as the need, so other cases are not implemented
    assert len(row)==1, "Square section of Matrix must be reducible to identity matrix"
    row = row[0].split(',')
    for i in range(len(row)):
        if row[i] == '0' or row[i] == '1':
            row[i] = int(row[i])
        else:
            row[i] = complex(row[i])
    sq_matrix.append(row)
    #sq_matrix.append(list(map(complex, row.split(','))))


# print sq_matrix
print("square coordinate matrix:")
for row in sq_matrix:
    for i in range(len(row)):
        element = row[i]
        if type(element) is float or type(element) is complex:
            row[i] = round(element.real, decimal_digits) + round(element.imag, decimal_digits) * 1j
    print(row) 
print()

# create polar matrix
pol_matrix = []
for row in sq_matrix:
    for i in range(len(row)):
        if not (row[i] == 1 or row[i] == 0):
            row[i] = polar(row[i])
    pol_matrix.append(row)

print("polar coordinate matrix:  (Magnitude, ",end = '')
if mode:
    print("degrees", ')', sep='')
else:
    print("radians", ')', sep='')
for row in pol_matrix:
    for i in range(len(row)):
        element = row[i]
        if type(element) is float:
            row[i] = round(row[i], decimal_digits)
        elif type(element) is tuple:
            if mode:
                row[i] = (round(row[i][0], decimal_digits), round(row[i][1]*rad2deg, decimal_digits))
            else:
                row[i] = (round(row[i][0], decimal_digits), round(row[i][1], decimal_digits))
    print(row) 
