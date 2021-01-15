import cv2
import numpy as np

# Color 이미지 -> gray 이미지
def make_gray(img):
    row=np.shape(img)[0]
    col=np.shape(img)[1]
    new_img=np.zeros((row,col),np.uint8)
    for i in range(row):
        for j in range(col):
            new_img.itemset(i,j,sum(img[i,j])//3)
    return new_img

# gray 이미지 -> 앤드 인 탐색 기법
def make_new_image(img):

    h = np.zeros((img.shape[0], img.shape[1]), np.uint8)    
    row=np.shape(img)[0]
    col=np.shape(img)[1]
    for i in range(row):
        for j in range(col):
            h[img[i,j]] += 1

    low = 255
    for i in range(row):
        tmp = min( h[i] )
        if low > tmp :
            low = tmp

    high = 0
    for i in range(row):
        tmp = max( h[i] )
        if high < tmp :
            high = tmp

    new_img = np.zeros((img.shape[0], img.shape[1]), np.uint8) 
    for i in range(row):
        for j in range(col):
            if img[i,j] <= low :
                new_img.itemset( i, j, 0 )
            elif img[i,j] >= high :
                new_img.itemset( i, j, 255 )
            else :
                new_img.itemset( i,j, ( img[i,j] - low ) / (high - low ) * 255)

    return new_img

# 이미지 읽기
img = cv2.imread('image1.jpg')
gray = make_gray( img )
new_img = make_new_image(gray)

# 이미지 출력
cv2.imshow( 'img', img )
cv2.imshow( 'gray', gray )
cv2.imshow( 'new image', new_img )

cv2.waitKey(0)
cv2.destroyAllWindows()