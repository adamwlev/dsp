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
print '1.2:\n',B.shape,'\n'
print '1.3:\n',C.shape,'\n'
print '1.4:\n',D.shape,'\n'
print '1.5:\n',u.shape,'\n'
print '1.6:\n',w.shape


# ##Question 2

alpha = 6
print '2.1:\n',u+v,'\n'
print '2.2:\n',u-v,'\n'
print '2.3:\n',alpha*u,'\n'
print '2.4:\n',np.inner(u,v).tolist()[0][0],'\n'
print '2.5:\n',np.linalg.norm(u)


# ##Question 3

print '3.1:\n','A + C is undefined.','\n'
print '3.2:\n',A-np.transpose(C),'\n'
print '3.3:\n',np.transpose(C)+3*D,'\n'
print '3.4:\n',B*A,'\n'
print '3.5:\n','B*t(A) is undefined.','\n'
print '3.6:\n','B*C is undefined.','\n'
print '3.7:\n',C*B,'\n'
print '3.8:\n',B**4,'\n'
print '3.9:\n',A*np.transpose(A),'\n'
print '3.10\n',np.transpose(D)*D
