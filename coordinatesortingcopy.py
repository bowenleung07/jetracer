import matplotlib.pyplot as plt
import os

arr = os.listdir('.')
arr.remove('.DS_Store')
arr.remove('coordinatesortingcopy.py')
arrx = []
arry = []

for i in range(len(arr)):
    name = arr[i]
    xname = name.split("_", 1)
    xcoord = xname[0]
    arrx.append(xcoord)

for i in range(len(arr)):
    name = arr[i]
    yname = name.split("_", 2)
    ycoord = yname[1]
    arry.append(ycoord)

for i in range(len(arr)):
    im = plt.imread(arr[i])
    implot = plt.imshow(im)
    plt.scatter(arrx[i], arry[i])
    plt.savefig(arr[i])
    plt.close()