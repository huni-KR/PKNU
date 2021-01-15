import cv2
import numpy as np

def RGB_to_YCbCr(img):

    result_img = img.copy() # 원본과 동일한 크기의 이미지 생성

    # 원본 이미지 가로 세로 저장
    height = img.shape[0]
    width = img.shape[1]

    # 화소 단위 순회
    for h in range(height):
        for w in range(width):
            b, g, r = img[h][w] # r g b 추출
            Y = 0.299*r + 0.587*g + 0.114*b
            Cb = -0.169*r - 0.331*g + 0.500*b
            Cr = 0.500*r - 0.419*g - 0.0813*b
            result_img[h][w] = [Cr, Cb, Y]
    
    return result_img   # 결과 이미지 return

#이미지 읽기
img_src = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)

img_YCbCr = RGB_to_YCbCr(img_src)

#결과 이미지 출력
cv2.imshow( 'origianl', img_src )
cv2.imshow( 'Y_image', img_YCbCr[:, :, 2] )
cv2.imshow( 'Cb_image', img_YCbCr[:, :, 1] )
cv2.imshow( 'Cr_image', img_YCbCr[:, :, 0] )
cv2.imshow( 'YCbCr_image', img_YCbCr )

cv2.waitKey(0)
cv2.destroyAllWindows()