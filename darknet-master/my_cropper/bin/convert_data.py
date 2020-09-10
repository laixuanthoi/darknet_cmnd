import os
import cv2
IMAGE_DIR = "image"
ANNOTATION_DIR = "annotation"

annotation_file = open("annotation.txt", "w")
for root, dirs, files in os.walk(IMAGE_DIR, topdown=False):
    for name in files:
        path = os.path.join(root, name)
        basename = os.path.basename(path)
        fileName, ext = os.path.splitext(
            basename)[0], os.path.splitext(basename)[1]
        image = cv2.imread(path)
        H, W = image.shape[:2]
        print(H, W)
        abs_path = os.path.abspath(path)
        with open("annotation/{}.txt".format(fileName)) as f:
            lines = f.readlines()
        box_string = abs_path + " "
        for l in lines:
            data = l.strip().split(" ")
            classID, xc, yc, w, h = data
            xcc = int(float(xc) * W)
            ycc = int(float(yc) * H)
            ww = int(float(w) * W)
            hh = int(float(h) * H)
            xmin = xcc - ww//2
            xmax = xcc + ww//2
            ymin = ycc - hh//2
            ymax = ycc + hh//2

            box_string += '{},{},{},{},{} '.format(
                xmin, ymin, xmax, ymax, classID)

        box_string = box_string.strip() + "\n"
        # cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        annotation_file.write(box_string)

        cv2.imshow("image", image)
        cv2.waitKey(10)
annotation_file.close()
