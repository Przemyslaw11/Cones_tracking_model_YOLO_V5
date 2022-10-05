import os
import shutil
from sklearn.model_selection import train_test_split
from pathlib import Path

imgs_path = "extractedImages"
annotations_path = "parsedAnnotations" 
images = [os.path.join(imgs_path, x) for x in os.listdir(imgs_path)]
print(len(images))
annotations = [ os.path.join(annotations_path, x) for x in os.listdir(annotations_path)]
print(len(annotations))


train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size=0.2, random_state=210)
val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size=0.5, random_state=420)

try:
    Path("./yolov5/images/train/").mkdir(parents=True)
    Path("./yolov5/images/val/").mkdir(parents=True)
    Path("./yolov5/images/test/").mkdir(parents=True)
    Path("./yolov5/labels/train/").mkdir(parents=True)
    Path("./yolov5/labels/val/").mkdir(parents=True)
    Path("./yolov5/labels/test/").mkdir(parents=True)
except OSError as error:
    print(error)

def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False

move_files_to_folder(train_images, './yolov5/images/train/')
move_files_to_folder(val_images, './yolov5/images/val/')
move_files_to_folder(test_images, './yolov5/images/test/')
move_files_to_folder(train_annotations, './yolov5/labels/train/')
move_files_to_folder(val_annotations, './yolov5/labels/val/')
move_files_to_folder(test_annotations, './yolov5/labels/test/')