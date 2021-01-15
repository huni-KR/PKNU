import cv2 
import numpy as np
from numpy.core.fromnumeric import shape

# 저주파 통과필터 마스크값
lpf_mask = np.array( [ [1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9] ] )

def lpf_sharpening(img):
    height = img.shape[0]
    width = img.shape[1]
    padding_size = len(lpf_mask) // 2
    tmp = np.zeros((padding_size*2 + height, padding_size*2 + width ), dtype=np.float64) # 경제 마스킹 픽셀값
    lpf_result = np.zeros(img.shape, dtype=np.float64)  # 샤프닝 결과

    # 마스크 크기에 맞게 늘려서 이미지 복사
    # 가장자리는 0
    for i in range(height):
       for j in range(width):
            tmp[padding_size + i, padding_size + j] = img[i, j]

    # 현재 이미지의 [0, 0]은 늘어난 이미지의 [1, 1]로 계산
    for i in range(height):
        for j in range(width):      
            tmp_i = padding_size + i
            tmp_j = padding_size + j
            lpf_result[i, j] = lpf_mask[0, 0] * tmp[tmp_i - 1 , tmp_j - 1] + lpf_mask[1, 0] * tmp[tmp_i, tmp_j - 1] + lpf_mask[2, 0] * tmp[tmp_i + 1 , tmp_j - 1] + lpf_mask[0, 1] * tmp[tmp_i - 1 , tmp_j ] + lpf_mask[1, 1] * tmp[tmp_i , tmp_j ] + lpf_mask[2, 1] * tmp[tmp_i + 1 , tmp_j ] + lpf_mask[0, 2] * tmp[tmp_i - 1 , tmp_j + 1] + lpf_mask[1, 2] * tmp[tmp_i , tmp_j + 1] + lpf_mask[2, 2] * tmp[tmp_i + 1 , tmp_j + 1]
           
            if lpf_result[i , j] > 255:
                lpf_result[i , j] = 255
            elif lpf_result[i , j] < 0:
                lpf_result[i , j] = 0

    return lpf_result
            

#이미지 읽기
img_src = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
img_lpf = lpf_sharpening(img_gray)


#결과 이미지 출력
cv2.imshow( 'Origianl', img_src )
cv2.imshow( 'Gray', img_gray )
cv2.imshow( 'LPF', np.uint8(img_lpf))

cv2.waitKey(0)
cv2.destroyAllWindows()