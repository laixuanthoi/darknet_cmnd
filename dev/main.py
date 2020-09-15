import numpy as np
import argparse
import time
import cv2
from cropper import CROPPER
from detector import DETECTOR
import glob
# from reader import READER

cropper_config = {
    "classPath": "bin/classes.names",
    "weightPath": "bin/tiny_yolo4_darknet_backbone_2700.weights",
    "configPath": "bin/tiny_yolo4_darknet_backbone.cfg",
    "confidence_threshold": 0.5,
    "nms_threshold": 0.3
}

detector_config = {
    "classPath": "detector/classes.names",
    "weightPath": "detector/tiny_yolo4_darknet_backbone_4700.weights",
    "configPath": "detector/tiny_yolo4_darknet_backbone.cfg",
    "confidence_threshold": 0.5,
    "nms_threshold": .5
}


cropper = CROPPER(cropper_config["configPath"],
                  cropper_config["weightPath"], cropper_config["classPath"])

detector = DETECTOR(detector_config["configPath"],
                    detector_config["weightPath"], detector_config["classPath"])

# reader = READER()
# capture = cv2.VideoCapture(0)

# while 1:
#     _, frame = capture.read()
#     cropper.detectCardInImage(
#         frame, cropper_config["confidence_threshold"], cropper_config["nms_threshold"])
#     cv2.imshow("frame", frame)
#     cv2.waitKey(1)
# image = cv2.imread("bin/4.jpg")
# cropper.detectCardInImage(
#     image, cropper_config["confidence_threshold"], cropper_config["nms_threshold"])
# the tuple of file types
# imagePaths = glob.glob('image/*.jpg')

# for path in imagePaths:
#     image = cv2.imread(path)
#     H, W = image.shape[:2]
#     if H > 500 or W > 500:
#         image = cv2.resize(image, (W//2, H//2))
#     cropper.detectCardInImage(
#         image, cropper_config["confidence_threshold"], cropper_config["nms_threshold"])
#     cv2.imshow("image", image)
#     cv2.waitKey(1)

# IMAGE_DIR = 'image/*.jpg'
IMAGE_DIR = "image/*.jpg"

imagePaths = glob.glob(IMAGE_DIR)

for path in imagePaths:
    image = cv2.imread(path)
    H, W = image.shape[:2]
    if H > 500 or W > 500:
        image = cv2.resize(image, (W//2, H//2))
    cropped_image = cropper.detectCardInImage(
        image, cropper_config["confidence_threshold"], cropper_config["nms_threshold"])

    if cropped_image is not None:

        # cropped_image = cv2.resize(
        #     cropped_image, (cropped_image.shape[1]*2, cropped_image.shape[0]*2))
        classes, scores, boxes = detector.detect(
            cropped_image, detector_config["confidence_threshold"], detector_config["nms_threshold"])

        # names = []
        # box_offset = 5
        # for clss, box in zip(classes, boxes):
        #     if clss == 2:
        #         x, y, w, h = box
        #         rect = cropped_image[y - box_offset:y +
        #                              h + box_offset, x - box_offset:x+w+box_offset]
        #         # rect = cv2.GaussianBlur(rect, (3, 3), 9)
        #         rect = cv2.medianBlur(rect, 3)
        #         hh, ww = rect.shape[:2]
        #         cv2.imshow("rect", rect)
        #         text = reader.readName(rect)
        #         print(text)
        #         names.append(text.encode('utf-8').decode('utf-8'))
        #         cv2.waitKey(0)

        # print(names)
    # cv2.imshow("image", image)
    cv2.waitKey(0)
