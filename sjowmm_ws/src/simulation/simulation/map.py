import numpy as np 
import cv2

def main(args=None):
    img = cv2.imread('/home/student/map4.png', cv2.IMREAD_UNCHANGED)
    width = 500
    height = 500
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    filename = "savedImage.png"

    cv2.imwrite(filename, resized)

    cv2.imshow('Resized Dimensions : ', resized)
    cv2.waitKey(0)



if __name__ == '__main__':
    main()
