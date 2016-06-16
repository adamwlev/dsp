# Matrix Algebra

import numpy as np


# ##Definitions

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.matrix([[6,2,-3,5]])
v = np.matrix([[3,5,-1,4]])
w = np.matrix([[1],[8],[0],[5]])


# ##Question 1

print '1.1:\n',A.shape,'\n'
#Answer: (2, 3) 
print '1.2:\n',B.shape,'\n'
#Answer: (2, 2) 
print '1.3:\n',C.shape,'\n'
#Answer: (3, 2)
print '1.4:\n',D.shape,'\n'
#Answer: (2, 3) 
print '1.5:\n',u.shape,'\n'
#Answer: (1, 4) 
print '1.6:\n',w.shape
#Answer: (4, 1)


# ##Question 2

alpha = 6
print '2.1:\n',u+v,'\n'
#Answer: [[ 9  7 -4  9]]
print '2.2:\n',u-v,'\n'
#Answer: [[ 3 -3 -2  1]] 
print '2.3:\n',alpha*u,'\n'
#Answer: [[ 36  12 -18  30]] 
print '2.4:\n',np.inner(u,v).tolist()[0][0],'\n'
#Answer: 51
print '2.5:\n',np.linalg.norm(u)
#Answer: 8.60232526704


# ##Question 3

print '3.1:\n','A + C is undefined.','\n'
#Answer: A + C is undefined.
print '3.2:\n',A-np.transpose(C),'\n'
#Answer: [[-4 -7 -3]
# 		    [ 3  6  4]]
print '3.3:\n',np.transpose(C)+3*D,'\n'
#Answer: [[14  3  3]
#         [ 2  7  9]]
print '3.4:\n',B*A,'\n'
#Answer: [[-1 -5 -1]
#		      [ 2  7  4]] 
print '3.5:\n','B*t(A) is undefined.','\n'
#Answer: B*t(A) is undefined. 
print '3.6:\n','B*C is undefined.','\n'
#Answer: B*C is undefined.
print '3.7:\n',C*B,'\n'
#Answer: [[ 5 -6]
# 		    [ 9 -8]
#		      [ 6 -6]]
print '3.8:\n',B**4,'\n'
#Answer: [[ 1 -4]
#		      [ 0  1]] 
print '3.9:\n',A*np.transpose(A),'\n'
#Answer: [[14 28]
#		      [28 69]]
print '3.10\n',np.transpose(D)*D
#Answer: [[10 -4  0]
# 		    [-4  8  8]
# 		    [ 0  8 10]]
