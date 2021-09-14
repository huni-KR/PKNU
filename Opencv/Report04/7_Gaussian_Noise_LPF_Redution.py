import cv2 
import numpy as np
from numpy.core.fromnumeric import shape

# 저주파 통과필터 마스크값
lpf_mask = np.array( [ [1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9] ] )

def noise_redution(img):

    height = img.shape[0]
    width = img.shape[1]

    tmp = np.zeros(img.shape, dtype=np.float64)
    img_noise = np.zeros(img.shape, dtype=np.float64)

    # 가우시안 노이즈를 입힌 이미지의 픽셀을 누적 n회 tmp list에 더하기
    for i in range(height):
        for j in range(width):            
            noise_value = img[i, j] + np.random.normal() * 16
            if noise_value > 255:
                tmp[i, j] = 255
            elif noise_value < 0:
                tmp[i, j] = 0
            else:
                tmp[i, j] += noise_value

    # 복사
    for i in range(height):
        for j in range(width):
            img_noise[i, j] = tmp[i, j]
    
    # 잡음제거 2회 / 6회 / 10회 이미지에 옮겨 담기
    for i in range(height):
        for j in range(width):
            if img_noise[i, j] < 0:
               img_noise[i, j] = 0
            elif img_noise[i, j] >255:
               img_noise[i, j] = 255

    return img_noise


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
img_noise = noise_redution(img_gray)
img_lpf = lpf_sharpening(img_noise)


#결과 이미지 출력
cv2.imshow( 'Origianl', img_src )
cv2.imshow( 'Gray', img_gray )
cv2.imshow( 'Noise', np.uint8(img_noise))
cv2.imshow( 'LPF Reduction', np.uint8(img_lpf))

cv2.waitKey(0)
cv2.destroyAllWindows()