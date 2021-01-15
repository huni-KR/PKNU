import numpy as np
import cv2

# RGB -> Gray
def make_gray(img):
    row=np.shape(img)[0]
    col=np.shape(img)[1]
    new_img=np.zeros((row,col),np.uint8)
    for i in range(row):
        for j in range(col):
            new_img.itemset(i,j,sum(img[i,j])//3)
    return new_img

# 이진화
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

# XOR 연산
def calcXOR( img1, img2 ):
    row=np.shape(img1)[0]
    col=np.shape(img1)[1]
    new_img=np.copy(img1)
    for i in range(row):
        for j in range(col):
            if ( img1[i,j] == 255 and img2[i,j] == 0 ) or (img1[i,j] == 0 and img2[i,j] == 255 ):
                new_img.itemset(i,j,255)
            else:
                new_img.itemset(i,j,0)
    return new_img

# 이미지 읽기
img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

gray1 = make_gray(img1)
gray2 = make_gray(img2)

binary1 = make_binary(gray1)
binary2 = make_binary(gray2)

new_img = calcXOR( binary1, binary2 )

# 이미지 출력
cv2.imshow("gray1", gray1)
cv2.imshow("gray2", gray2)
cv2.imshow("XOR", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()