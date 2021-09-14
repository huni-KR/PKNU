import numpy as np
import cv2

# 이미지 읽기
src = cv2.imread('image1.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))

# cv2.dilate 침식 연산
dilate = cv2.dilate(src, kernel, anchor=(-1, -1), iterations=5)

# 이미지 출력
cv2.imshow('imgae', src)
cv2.imshow('dilation', dilate)

cv2.waitKey(0)
cv2.destroyAllWindows()