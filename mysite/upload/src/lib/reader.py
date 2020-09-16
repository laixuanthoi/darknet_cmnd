import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "D:/tesseract-ocr/tesseract.exe"


def sortPosition(arr):
    new_arr = arr
    n = len(arr)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if new_arr[i][0] > new_arr[j][0]:
                tmp = arr[i]
                new_arr[i] = new_arr[j]
                new_arr[j] = tmp
    return new_arr


class READER:

    def readText(self, image):
        config = '--psm 6'
        lang = 'vie'
        return pytesseract.image_to_string(image, lang=lang, config=config)

    def readNumber(self, image):
        config = '--oem 0  --psm 10 -c tessedit_char_whitelist=1234567890'
        lang = 'eng'
        return pytesseract.image_to_string(image, lang=lang, config=config)

    def readNumberCandidates(self, arr):

    def readTextCandidates(self, arr):

        # crop the candidate image text return array

    def cropCandidates(self, image, boxes):
        cands = []
        for box in boxes:
            x, y, w, h = box
            x1 = x - self.crop_offset
            y1 = y - self.crop_offset
            x2 = (x + w) + self.crop_offset
            y2 = (y + h) + self.crop_offset
            cropped =

    def extractInfo(self, image, classes, scores, boxes):
        maso_cadidate_boxes = []
        hoten_candidate_boxes = []
        ngaysinh_candidate_boxes = []
        nguyenquan_candidate_boxes = []
        diachi_candidate_boxes = []
        for clss, box in zip(classes, boxes):
            if clss == 1:  # maso
                maso_cadidates.append(box)
            if clss == 2:  # hoten
                hoten_candidate_boxes.append(box)
            if clss == 3:  # ngaysinh
                ngaysinh_candidate_boxes.append(box)
            if clss == 4:  # diachi
                diachi_candidate_boxes.append(box)
        hoten_candidate_boxes = sortPosition(hoten_candidate_boxes)
