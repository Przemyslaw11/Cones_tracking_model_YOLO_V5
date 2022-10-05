import glob 
import shutil
import os

datasetPath = ".\dataset"
# imgPaths = glob.glob(datasetPath + "\**\.*[!.json]", recursive=True)
imgPaths = glob.glob(datasetPath + "\*\*\*.*[!.json]")
allImgsPath = ".\\extractedImages"

try:
    (os.mkdir(allImgsPath))
except OSError as error:
    pass

for path in imgPaths:
    filename = os.path.basename(path)
    newPath = allImgsPath + f"\\{filename}"
    shutil.copy(path, newPath)