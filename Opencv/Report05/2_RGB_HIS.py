import cv2
import numpy as np

def RGB_to_HSI(rgb):
    
    #r g b 값을 배열로 저장
    b = rgb[0]
    g = rgb[1]
    r = rgb[2]

    I = np.mean(rgb)

    #이미지가 gray의 경우 h, s == 0
    if( r == g == b ):
        H = 0
        S = 0

    else:
        min_rgb = min(rgb)
        S = 1 - ( min_rgb / I )

        tmp = (( r - g ) + ( r - b )) / ( 2 * np.sqrt(( r - g )*( r - g ) + ( r - b )*( r - b )) )
        H = np.arccos(tmp) * 180 / np.pi

        if b > g:
            H = 360 - H
        H /= 360

    return np.array( [H, S, I], dtype=np.float32)   #변환된 H S I 배열로 return
    

#이미지 읽기
img_src = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)

src_height = img_src.shape[0]
src_width = img_src.shape[1]

img_src_tmp = img_src/255
img_HSI = np.zeros(np.shape(img_src), dtype=np.float)   

#HSI로 이미지 변환
for h in range(src_height):
    for w in range(src_width):
        img_HSI[h,w] = RGB_to_HSI( img_src_tmp[h,w] )

#변환한 HSI 이미지를 채널별로 분리( 0 ~ 255 )
img_H = np.uint8( np.clip( img_HSI[:,:,0]*255,0,255))
img_S = np.uint8( np.clip( img_HSI[:,:,0]*255,0,255))
img_I = np.uint8( np.clip( img_HSI[:,:,0]*255,0,255))

#결과 이미지 출력
cv2.imshow( 'origianl', img_src )
cv2.imshow( 'H_image', img_H )
cv2.imshow( 'S_image', img_S )
cv2.imshow( 'I_image', img_I )
cv2.imshow( 'HSI_image', img_HSI )

cv2.waitKey(0)
cv2.destroyAllWindows()