import glob 
import json
import os

datasetPath = ".\dataset"
# annPaths = glob.glob(datasetPath + "\**\.json", recursive=True)
annPaths = glob.glob(datasetPath + "\*\*\*.json")
parsedAnnPath = ".\parsedAnnotations"
try:
    (os.mkdir(parsedAnnPath))
except OSError as error:
    pass

classIdMapper = {9993505:0,
                 9993514:1, 
                 9993506:2, 
                 9993507:3,
                 9993508:4,
                 9993509:5,
                 9993510:6,
                 9993511:7,
                 9993512:8,
                 9993513:9}

for annPath in annPaths:
    with open(annPath, "r", encoding="utf8") as ann:
        formatedAnns = []
        annData = json.loads(ann.read())
        imgHeight = annData["size"]["height"]
        imgWidth = annData["size"]["width"]
        for obj in annData["objects"]:
            classId = str(classIdMapper[int(obj["classId"])])
            points = obj["points"]["exterior"]
            p1 = points[1]
            p0 = points[0] 
            objWidth = p1[0] - p0[0]
            objHeight = p1[1] - p0[1]

            objCenterXNorm = (p0[0] + (objWidth/2) )/imgWidth
            objCenterYNorm = (p0[1] + (objHeight/2) )/imgHeight
            objWidthNorm = objWidth / imgWidth
            objHeightNorm = objHeight / imgHeight

            formatedAnns.append(" ".join([str(classId),
                                        str(objCenterXNorm),
                                        str(objCenterYNorm),
                                        str(objWidthNorm),
                                        str(objHeightNorm),
                                        "\n"]))

        filename = os.path.basename(annPath)
        filenameWoExtension = filename.split(".")[0]

        with open(parsedAnnPath + f"\{filenameWoExtension}.txt", "w", encoding="utf8") as formatedAnnTxt:
            formatedAnnTxt.writelines(formatedAnns)