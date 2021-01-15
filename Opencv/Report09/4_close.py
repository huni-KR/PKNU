import numpy as np
import cv2

# 이미지 읽기
src = cv2.imread('image1.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
# cv2.dilate 침식 연산
dilate = cv2.dilate(src, kernel, anchor=(-1, -1), iterations=5)
# cv2.erode 팽창연산
close = cv2.erode(dilate, kernel, anchor=(-1, -1), iterations=5)

# 이미지 출력
cv2.imshow('image', src)
cv2.imshow('close', close)

cv2.waitKey(0)
cv2.destroyAllWindows()