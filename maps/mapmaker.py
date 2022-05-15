from os.path import exists
from PIL import Image
import shutil
import os

mapName = input("PLEASE ENTER THE NAME OF YOUR MAP: ")

if(len(mapName.split()) > 1):
    print("THE NAME OF THE MAP MUST HAVE NO SPACES!")
    quit()


fileExists = exists(f"/{mapName}/{mapName}.map")

if(fileExists):
    print("YOU ALREADY HAVE A MAP WITH THAT NAME!")
    quit()

os.mkdir(mapName)

pathToMapImage = input("PLEASE ENTER THE PATH TO IMAGE OF THE MAP: ")

imageExtension = ""
i = len(pathToMapImage)-1

while(1):
    if(i < 0): break
    if(pathToMapImage[i] == "."): break
    imageExtension += pathToMapImage[i]
    i-=1

shutil.copyfile(pathToMapImage, mapName+"/"+mapName+"MapImage."+imageExtension[::-1])


