import numpy as np
import cv2

# Color 이미지 -> gray 이미지
def make_gray(img):
    row=np.shape(img)[0]
    col=np.shape(img)[1]
    new_img=np.zeros((row,col),np.uint8)
    for i in range(row):
        for j in range(col):
            new_img.itemset(i,j,sum(img[i,j])//3)
    return new_img

# gray 이미지 -> Reverse 이미지
def make_reverse( img ): 
    row=np.shape(img)[0]
    col=np.shape(img)[1]
    new_img=np.zeros((row,col),np.uint8)
    for i in range(row):
        for j in range(col):
             new_img.itemset(i,j,255-img[i,j])
    return new_img

# 이미지 읽기
img = cv2.imread("image1.jpg")
gray = make_gray(img)
reverse = make_reverse( gray )

# 이미지 출력
cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("reverse", reverse)

cv2.waitKey(0)
cv2.destroyAllWindows()