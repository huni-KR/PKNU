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
    
def gray_im(imgFile ):
    img = cv2.imread(imgFile)
    img2=make_gray(img)
    return img2

# minus 연산
def minus_img(img1,img2):
    row=np.shape(img1)[0]
    col=np.shape(img1)[1]
    new_img=np.copy(img1)
    for i in range(row):
        for j in range(col):
            tmp = img1[i,j] - img2[i,j]
            if tmp < 0:
                tmp  = 0
            new_img.itemset(i,j,tmp)
    return new_img

# 이미지 읽기
img1=gray_im('image1.jpg')
img2=gray_im('image2.jpg')
img3=minus_img(img1,img2)

# 이미지 출력
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('minus image',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()