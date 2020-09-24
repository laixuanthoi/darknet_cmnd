import numpy as np
import time
import cv2

def drawing(image, classes, scores, boxes):
    drawed = image.copy()
    COLORS = [(0, 255, 0), (0, 0, 255),(0, 255, 255)]
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        cv2.rectangle(drawed, box, color, 1)
    cv2.imshow("detected", drawed)

class Model:
    def __init__(self, configPath, weightPath, classPath, input_size=(608, 608)):
        self.model_input_size = input_size
        self.fps = 0
        self.loadClassNames(classPath)
        self.loadModel(configPath, weightPath)

    def loadClassNames(self, classPath):
        self.class_names = open(classPath).read().strip().split("\n")

    def loadModel(self, configPath, weightPath):
        self.net = cv2.dnn.readNet(weightPath, configPath)
        self.net
        self.model = cv2.dnn_DetectionModel(self.net)
        self.model.setInputParams(
            size=self.model_input_size, scale=1/255.0, swapRB=True)

    def predict(self, image, confidence_threshold, nms_threshold):
        start = time.time()
        classes, scores, boxes = self.model.detect(
            image, confidence_threshold, nms_threshold)
        end = time.time()
        print("Predicted in: {}".format(end - start))
        self.fps = 1/(end - start)
        return classes, scores, boxes

configPath= "bin/yolov4-tiny.cfg"
weightPath = "bin/yolov4-tiny_10000.weights"
classPath = "bin/classes.names"
confidence_threshold = 0.7
nms_threshold = 0.6

# image = cv2.imread("bin/1.jpg")

cap = cv2.VideoCapture("bin/2.mp4")
while 1:
    _, image = cap.read()
    if not _:
        break
    

    model = Model(configPath, weightPath,
                            classPath, (416, 416))
                            
    classes, scores, boxes = model.predict(
                image, confidence_threshold, nms_threshold)
    drawing(image, classes, scores, boxes)
    cv2.waitKey(1)