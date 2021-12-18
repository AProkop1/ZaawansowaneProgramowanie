import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

# lab_9
def get_text(image_path: str) -> str:
    img_1 = cv2.imread(image_path)
    cv2.imshow('image', img_1)
    cv2.waitKey(0)
    text_1 = pytesseract.image_to_string(img_1)
    return text_1


# lab_10
img_2 = cv2.imread('images/img_5.png')
gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)

# converted_img
converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(gray, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
cv2.imshow('image', converted_img)
cv2.waitKey(0)

text = pytesseract.image_to_string(converted_img)
print(text)
