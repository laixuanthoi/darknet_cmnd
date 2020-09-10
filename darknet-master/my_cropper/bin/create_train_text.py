import glob
import os


def getImagesInDir(dir_path):
    image_list = []
    for filename in glob.glob(dir_path + '/*.jpg'):
        image_list.append(filename)

    return image_list


DATA_DIR = "dataset/yolo_dataset"
text_file = open("train.txt", 'w')

for path in getImagesInDir(DATA_DIR):
    f_path = os.path.join("my_cropper", path)
    text_file.write(f_path + "\n")

text_file.close()
