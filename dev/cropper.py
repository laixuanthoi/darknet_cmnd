import cv2
import numpy as np
from detector import Detector


class CROPPER:
    def __init__(self, configPath, weightPath, classPath):
        self.cardWidth = 430
        self.cardHeight = 270
        self.detector = Detector(configPath, weightPath, classPath)

    def cropCard(self, image, points):
        # top left - top right - bot right - bot left
        src_points = np.float32(points)
        dst_points = np.float32([[0, 0],                 [self.cardWidth, 0],
                                 [0, self.cardHeight],   [self.cardWidth, self.cardHeight]])
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        return cv2.warpPerspective(image, matrix, (self.cardWidth, self.cardHeight))

    def detectCardInImage(self, image, confidence_threshold, nms_threshold):
        classes, scores, boxes = self.detector.predict(
            image, confidence_threshold, nms_threshold)

        off_set = 2
        tls = []
        trs = []
        bls = []
        brs = []

        for clss, box in zip(classes, boxes):
            c_x = (box[0] + (box[0]+box[2]))//2
            c_y = (box[1] + (box[1]+box[3]))//2
            if clss[0] == 0:
                tls.append((c_x - off_set, c_y - off_set))
            if clss[0] == 1:
                trs.append((c_x + off_set, c_y - off_set))
            if clss[0] == 2:
                bls.append((c_x - off_set, c_y + off_set))
            if clss[0] == 3:
                brs.append((c_x + off_set, c_y + off_set))

        if len(tls) <= 0 or len(trs) <= 0 or len(bls) <= 0 or len(brs) <= 0:
            return
        # group the point
        four_point_corners = [
            tls[0], trs[0], bls[0], brs[0]
        ]
        cropped = self.cropCard(image, four_point_corners)
        cv2.imshow("cropped", cropped)

        self.drawing(image, classes, scores, boxes)

    def drawing(self, image, classes, scores, boxes):
        drawed = image.copy()
        COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
        for (classid, score, box) in zip(classes, scores, boxes):
            color = COLORS[int(classid) % len(COLORS)]
            label = "%s : %f" % (self.detector.class_names[classid[0]], score)
            cv2.rectangle(drawed, box, color, 1)
            cv2.putText(drawed, label, (box[0], box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        cv2.imshow("drawed image", drawed)
