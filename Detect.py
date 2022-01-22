import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression


def detect_people(file_name: str) -> None:
    # Initializing the HOG person detection
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Reading image
    image = cv2.imread(file_name)

    # Resizing the Image
    image = imutils.resize(image, width=min(400, image.shape[1]))

    # Detecting all the regions in the image with pedestrians
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                            padding=(8, 8), scale=1.05)

    # Applying non-maxima suppression
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    # Drawing final boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    # Showing information about number of people detected
    print("[FOUND] : {} people.".format(len(pick)))

    # Showing output images
    cv2.imshow("People detection", image)
    cv2.waitKey(0)
