import cv2
import numpy as np
from model import Model


class DETECTOR:
    def __init__(self, configPath, weightPath, classPath):
        self.cardWidth = 430
        self.cardHeight = 270
        self.model = Model(configPath, weightPath, classPath, (1024, 1024))
        self.count_cropped = 1

    def cropCard(self, image, points):
        # top left - top right - bot right - bot left
        src_points = np.float32(points)
        dst_points = np.float32([[0, 0],                 [self.cardWidth, 0],
                                 [0, self.cardHeight],   [self.cardWidth, self.cardHeight]])
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        return cv2.warpPerspective(image, matrix, (self.cardWidth, self.cardHeight))

    def detect(self, image, confidence_threshold, nms_threshold):
        classes, scores, boxes = self.model.predict(
            image, confidence_threshold, nms_threshold)

        self.drawing(image, classes, scores, boxes)

    def drawing(self, image, classes, scores, boxes):
        drawed = image.copy()
        COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
        for (classid, score, box) in zip(classes, scores, boxes):
            color = COLORS[int(classid) % len(COLORS)]
            # label = "%s : %f" % (self.model.class_names[classid[0]], score)
            cv2.rectangle(drawed, box, color, 1)
            # cv2.putText(drawed, label, (box[0], box[1] - 10),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        cv2.imshow("detected", drawed)
