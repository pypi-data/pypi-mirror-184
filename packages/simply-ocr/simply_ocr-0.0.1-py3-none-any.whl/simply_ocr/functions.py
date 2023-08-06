import cv2
from skimage import io
from pytesseract import pytesseract

def read_image_en(image):

        img_color = io.imread(image)
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        thresh_img = cv2.threshold(img_gray, 120, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)[1]
        invert_image = 255 - thresh_img
        text = pytesseract.image_to_string(invert_image, lang='eng')

        print(text)
        return text

def read_image_es(image):
        
        img_color = io.imread(image)
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        thresh_img = cv2.threshold(img_gray, 120, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)[1]
        invert_image = 255 - thresh_img
        text = pytesseract.image_to_string(invert_image, lang='spa')
        
        print(text)
        return text

