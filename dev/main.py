import numpy as np
import argparse
import time
import cv2
from cropper import CROPPER
import glob


cropper_config = {
    "classPath": "bin/classes.names",
    "weightPath": "bin/tiny_yolo4_darknet_backbone_2700.weights",
    "configPath": "bin/tiny_yolo4_darknet_backbone.cfg",
    "confidence_threshold": 0.5,
    "nms_threshold": 0.3
}

cropper = CROPPER(cropper_config["configPath"],
                  cropper_config["weightPath"], cropper_config["classPath"])


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
imagePaths = glob.glob('image/*.jpg')

for path in imagePaths:
    image = cv2.imread(path)
    H, W = image.shape[:2]
    if H > 500 or W > 500:
        image = cv2.resize(image, (W//2, H//2))
    cropper.detectCardInImage(
        image, cropper_config["confidence_threshold"], cropper_config["nms_threshold"])
    cv2.imshow("image", image)
    cv2.waitKey(1)
