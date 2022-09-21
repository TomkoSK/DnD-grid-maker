from PIL import Image

def getGridSizes(im):#Gets all possible grid sizes for a given image
    x, y = im.size
    xDivisors = []
    yDivisors = []
    for number in range(x):
        if(number == 0):
            continue
        if(x % number == 0):
            xDivisors.append(number)
    for number in range(y):
        if(number == 0):
            continue
        if(y % number == 0):
            yDivisors.append(number)
    xFinal=[]
    yFinal=[]
    for number in xDivisors:
        xFinal.append(x/number)
    for number in yDivisors:
        yFinal.append(y/number)
    pixelSize = sorted(set(xFinal).intersection(yFinal))#Grabs the numbers that appear in both final lists
    gridSizes = []
    for size in pixelSize:
        gridSizes.append(str(int(x/size))+"x"+str(int(y/size)))#Makes a list of all the possible grid sizes by dividing the
    gridSizes.reverse()#The list looks nicer when it goes from the lowest to the highest grid size
    return gridSizes