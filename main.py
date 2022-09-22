import os
from PIL import Image
import gridMaker

imageExtensions = ['jpg', 'jpeg', 'png', 'webp']
directory = 'input'
imgName = None
for file in os.listdir(directory):
    for extension in imageExtensions:
        if(file.endswith(extension)):
            imgName = file
            break
if(not imgName):
    print('Couldn\'t find any images in the input directory, exiting...')
    exit()
im = Image.open(f'input/{imgName}')
print(f'Opened {imgName}')
gridSizeList = gridMaker.getGridSizes(im)
bigGridSizeString = ''
for size in gridSizeList:
    bigGridSizeString += size + ",\n"#Makes a string of all the grid sizes
bigGridSizeString = bigGridSizeString[:-2]
print("What grid size do you want? The options are:\n" + bigGridSizeString)
while(True):
    gridSizeInput = input(":")
    if(gridSizeInput) in gridSizeList:
        break
gridImg = gridMaker.makeGrid(im, gridSizeInput)
fileName = 'output.png'
if(os.path.isfile('./output/output.png')):
    fileNumber = 1
    while(os.path.isfile(f'./output/output{fileNumber}.png')):
        fileNumber += 1
    gridImg.save(f'./output/output{fileNumber}.png')
    print(f'Map with grid saved as output{fileNumber}.png in output directory')
else:
    gridImg.save('./output/output.png')
    print('Map with grid saved as output.png in output directory')