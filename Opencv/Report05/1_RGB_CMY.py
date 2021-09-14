import cv2
import numpy as np

def RGB_to_CMY(img):

    result_img = img.copy() # 원본과 동일한 크기의 이미지 생성

    # 원본 이미지 가로 세로 저장
    height = img.shape[0]
    width = img.shape[1]

    # 화소 단위 순회
    for h in range(height):
        for w in range(width):
            b, g, r = img[h][w] # r g b 추출
            C = 1 - r;
            M = 1 - g;
            Y = 1 - b;
            result_img[h][w] = [C, M, Y]
    
    return result_img   # 결과 이미지 return

#이미지 읽기
img_src = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)

img_CMY = RGB_to_CMY(img_src)

#결과 이미지 출력
cv2.imshow( 'origianl', img_src )
cv2.imshow( 'CMY_image', img_CMY )

cv2.waitKey(0)
cv2.destroyAllWindows()