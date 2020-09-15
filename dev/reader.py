import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "D:/tesseract-ocr/tesseract.exe"


class READER:
    def readName(self, image):

        config = '--psm 6'
        lang = 'vie'
        return pytesseract.image_to_string(image, lang=lang, config=config)

    def readID(self, image):
        config = '--oem 0  --psm 10 -c tessedit_char_whitelist=1234567890'
        lang = 'eng'
        return pytesseract.image_to_string(image, lang=lang, config=config)
