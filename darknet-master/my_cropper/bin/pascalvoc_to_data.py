import xml.etree.ElementTree as ET
import os

ANNOTATION_DIR = "annotation"
ANNOTATION_TXT = "annotation.txt"

classNames = ["tren_trai", "tren_phai",
              "duoi_trai", "duoi_phai", "the", "quochieu"]

annotation_stream = open(ANNOTATION_TXT, 'w')
for rootT, dirs, files in os.walk(ANNOTATION_DIR, topdown=False):
    for name in files:
        filepath = os.path.join(rootT, name)
        abs_path = os.path.abspath(filepath)
        basename = os.path.basename(abs_path)
        fileName, ext = os.path.splitext(
            basename)[0], os.path.splitext(basename)[1]
        tree = ET.parse(abs_path)
        image_path = os.path.join(
            os.getcwd(), "image", "{}.jpg".format(fileName))
        root = tree.getroot()
        width = root.find("size").find('width').text
        height = root.find("size").find('height').text
        depth = root.find("size").find('depth').text
        anno_class = [image_path]

        for obj in root.findall("object"):
            classname = obj.find("name").text.strip()
            classID = classNames.index(classname)
            bndbox = obj.find("bndbox")
            xmin, ymin, xmax, ymax = bndbox.find("xmin").text, bndbox.find(
                "ymin").text, bndbox.find("xmax").text, bndbox.find("ymax").text
            anno_class.append("{},{},{},{},{}".format(
                xmin, ymin, xmax, ymax, classID))
        txt_str = " ".join(anno_class)
        annotation_stream.write(txt_str + "\n")

annotation_stream.close()
