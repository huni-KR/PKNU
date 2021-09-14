import cv2
import numpy as np

# RGB -> Gray
def make_gray(img):
    row=np.shape(img)[0]
    col=np.shape(img)[1]
    new_img=np.zeros((row,col),np.uint8)
    for i in range(row):
        for j in range(col):
            new_img.itemset(i,j,sum(img[i,j])//3)
    return new_img

# 이미지 읽기
img_ori = cv2.imread( "image1.jpg" )
img_gray = make_gray( img_ori )

img0 = img_gray.copy()
img1 = img_gray.copy()
img2 = img_gray.copy()
img3 = img_gray.copy()
img4 = img_gray.copy()
img5 = img_gray.copy()
img6 = img_gray.copy()
img7 = img_gray.copy()

h, w = img_gray.shape

# bit plane 연산
for y in range(0, h) :
    for x in range(0, w) :
        img0[y, x] = 255 if ( img_gray[y, x] ) & ( 1 << 7) else 0
        img1[y, x] = 255 if ( img_gray[y, x] ) & ( 1 << 6) else 0
        img2[y, x] = 255 if ( img_gray[y, x] ) & ( 1 << 5) else 0
        img3[y, x] = 255 if ( img_gray[y, x] ) & ( 1 << 4) else 0
        img4[y, x] = 255 if ( img_gray[y, x] ) & ( 1 << 3) else 0
        img5[y, x] = 255 if ( img_gray[y, x] ) & ( 1 << 2) else 0
        img6[y, x] = 255 if ( img_gray[y, x] ) & ( 1 << 1) else 0
        img7[y, x] = 255 if ( img_gray[y, x] ) & ( 1 << 0) else 0
            
# 이미지 출력
cv2.imshow( 'ori', img_gray )
cv2.imshow( 'img0', img0 )
cv2.imshow( 'img1', img1 )
cv2.imshow( 'img2', img2 )
cv2.imshow( 'img3', img3 )
cv2.imshow( 'img4', img4 )
cv2.imshow( 'img5', img5 )
cv2.imshow( 'img6', img6 )
cv2.imshow( 'img7', img7 )

cv2.waitKey(0)
cv2.destroyAllWindows()