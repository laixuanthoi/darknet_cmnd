import cv2
import numpy as np
from model import Model


class DETECTOR:
    def __init__(self, configPath, weightPath, classPath, input_size=(1024, 1024)):
        self.model = Model(configPath, weightPath,
                           classPath, input_size)
        self.crop_offset = 5

    def cropCandidates(self, image, boxes):
        cands = []
        for box in boxes:
            x, y, w, h = box
            x1 = x - self.crop_offset
            y1 = y - self.crop_offset
            x2 = (x + w) + self.crop_offset
            y2 = (y + h) + self.crop_offset
            cropped = image[y1:y2, x1:x2]
            cands.append(cropped)

    def detect(self, image, confidence_threshold, nms_threshold):
        classes, scores, boxes = self.model.predict(
            image, confidence_threshold, nms_threshold)
        # self.drawing(image, classes, scores, boxes)
        maso_cadidate_boxes = []
        hoten_candidate_boxes = []
        ngaysinh_candidate_boxes = []
        nguyenquan_candidate_boxes = []
        diachi_candidate_boxes = []

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
