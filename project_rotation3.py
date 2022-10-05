import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.pyplot import plot, ion, show
np.set_printoptions(linewidth=100) #shows each row on one line in shell output

#data matrix (homogenous coordinates)
D=np.array([[-6.5,-6.5,-6.5,-6.5,-2.5,-2.5,-0.75,-0.75,3.25,3.25, 4.5,4.5, 6.5,6.5,6.5, 6.5],
            [  -2,  -2, 0.5, 0.5, 0.5, 0.5,    2,    2,   2,   2, 0.5,0.5, 0.5,0.5, -2,  -2],
            [-2.5, 2.5, 2.5,-2.5,-2.5, 2.5, -2.5,  2.5,-2.5, 2.5,-2.5,2.5,-2.5,2.5,2.5,-2.5],
            [   1,   1,   1,   1,   1,   1,    1,    1,   1,   1,   1,  1,   1,  1,  1,  1]])

#adjacency matrix
C=np.array([[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]])

#45 degrees of rotation
phi=math.pi/4
#z axis rotation matrix
Az=np.array([[math.cos(phi),-math.sin(phi),0,0],
             [math.sin(phi), math.cos(phi),0,0],
             [            0,             0,1,0],
             [            0,             0,0,1]])

#rotated data matrix
AzD=np.matmul(Az,D)

#center of projection
b=0
c=10
d=25

#perspective projection
P=np.array([[1,0,-b/d,0],
            [0,1,-c/d,0],
            [0,0,   0,0],
            [0,0,-1/d,1]])

#rotated data matrix from center of projection
PAzD=np.matmul(P,AzD)

for i in range(16): #number of columns = 16
    PAzD[:,i]=PAzD[:,i]/PAzD[3,i] #convert to homogenous coordinates(each entry in each column
                            #is divided by the value in the 4th row of that column
                            #and then the quotient is assigned to the entry)  

f,toyota=plt.subplots() #create figure
f.set_size_inches(9,3.5) #change figure size to look more stretched like the examples
toyota.plot(PAzD[0,:],PAzD[1,:],'r.') #plot x y with red dots
for x in range(16): #number of columns = 16
    for y in range(x):
        if C[x,y]==1:
            toyota.plot([PAzD[0,x],PAzD[0,y]],[PAzD[1,x],PAzD[1,y]],'b') #connect x y with blue lines
show()
