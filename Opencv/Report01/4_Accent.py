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

# gray 이미지 -> Accent 이미지
def make_accent(img):

    accent_start = 128
    accent_end = 192

    row=np.shape(img)[0]
    col=np.shape(img)[1]
    new_img=np.zeros((row,col),np.uint8)
    for i in range(row):
        for j in range(col):
            if img[i,j] >= accent_start and img[i,j] <= accent_end :
                new_img.itemset(i,j,255)
            else:
                new_img.itemset(i,j, img[i,j] )
    return new_img

# 이미지 읽기
img = cv2.imread("image1.jpg")

gray = make_gray(img)
accent_img = make_accent(gray)

# 이미지 출력
cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("accent image", accent_img)

cv2.waitKey(0)
cv2.destroyAllWindows()