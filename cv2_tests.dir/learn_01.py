import cv2
import sys
from pathlib import Path


if __name__ == '__main__':
    # png = Path(r'image1.png')

    img = cv2.imread(sys.argv[1])

    # Blur image:
    blurred_img = cv2.GaussianBlur(img, (5,5), 0)

    cv2.imshow('Picture: ', img)
    cv2.imshow('Blurred: ', blurred_img)
    cv2.waitKey(0)
