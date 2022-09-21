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

def makeGrid(im, grid):#Takes the image of the map, and the string that has the grid (like '12x12')
    im = im.convert('RGBA')
    gridImg = Image.new('RGBA', size=im.size, color=(0, 0, 0, 0,))#Makes an image that the grid will be drawn on, which will be merged with the map image later
    pixels = gridImg.load()
    xIndex = grid.index('x')
    pixelsBetweenLines = int(im.size[0]/int(grid[0:xIndex]))#The amount of pixels that will be between every line when drawing the grid
    for x in range(0, im.size[0], pixelsBetweenLines):#This draws all the vertical lines of the grid on the second image
        for y in range(0, im.size[1]):
            pixels[x, y] = (0, 0, 0, 255)
            pixels[x+1, y] = (0, 0, 0, 255)
    for y in range(0, im.size[1], pixelsBetweenLines):#This draws all the horizontal lines of the grid on the second image
        for x in range(0, im.size[0]):
            pixels[x, y] = (0, 0, 0, 255)
            pixels[x, y+1] = (0, 0, 0, 255)
    return Image.alpha_composite(im, gridImg)#Combines the base image and the grid image