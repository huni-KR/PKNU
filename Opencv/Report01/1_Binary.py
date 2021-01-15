import numpy as np
import cv2

# Color 이미지 -> Gray 이미지
def make_gray(img):
    row=np.shape(img)[0]
    col=np.shape(img)[1]
    new_img=np.zeros((row,col),np.uint8)
    for i in range(row):
        for j in range(col):
            new_img.itemset(i,j,sum(img[i,j])//3)
    return new_img

# Gray 이미지 -> Binary 이미지
def make_binary(img):
    value = 128
    row=np.shape(img)[0]
    col=np.shape(img)[1]
    new_img=np.zeros((row,col),np.uint8)
    for i in range(row):
        for j in range(col):
            if value < img[i,j]:
                new_img.itemset(i,j,255)
            else:
                new_img.itemset(i,j,0)
    return new_img

# 이미지 읽기
img = cv2.imread("image1.jpg")

gray = make_gray(img)
binary = make_binary(gray)

# 이미지 출력
cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()