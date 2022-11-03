# importing the required module
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#xArray=[]
#yArray=[]
#zArray=[]
#arr = []
#length= 1
#def getPoints():#take (x,y,z) points out of file and convert into useable arrays

file = open("points.txt", "r")
triplets=file.read().split(" " and "," and "\n")
#for i in range(0,len(triplets)):
#	triplets[i]=triplets[i].split(',')
#triplets.remove(\n)
length = len(triplets)
arr = np.array(triplets)
xArray = arr[0 : length : 3]
yArray = arr[1 : length : 3]
zArray = arr[2 : length : 3]
print("xarray", xArray, "\n")
print("yarray", yArray, "\n")
print("zarray", zArray, "\n")
print("triplets", triplets, "\n")
print("arr",arr,"\n")
    #return xArray
    #return yArray
    #return zArray
    #return arr
    #return length

#getPoints()
#xArray = arr[0 : length : 3]
#yArray = arr[1 : length : 3]
#zArray = arr[2 : length : 3]
x = np.array(xArray)
y = np.array(yArray)
z = np.array(zArray)
#x = array("i", xArray)
#y = array("i", yArray)
#z = array("i", zArray)
#x = xArray
#y = yArray
#z = zArray

print("x",x)
print("y",y)
print("z",z)

# function to show the plot
fig = plt.figure(figsize=(7, 4.5))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('none')
ax.plot(x, y, z, '.:')
ax.plot(x, y, z, '-')
plt.show()
