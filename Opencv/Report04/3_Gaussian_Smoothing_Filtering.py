import cv2 
import numpy as np
from numpy.core.fromnumeric import shape

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


# smoothing
def smoothing(img, K_size=3):
    H, W = img.shape

    # zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img_gray.copy().astype(np.float)
    tmp = out.copy()

    # emboss kernel
    K = [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]]

    # filtering
    for y in range(H):
        for x in range(W):
            out[pad + y, pad + x] = np.sum(1/9 * (tmp[y: y + K_size, x: x + K_size]))

    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out

#이미지 읽기
img_src = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
img_noise = noise_redution(img_gray)
img_smoothing = smoothing(img_noise, 3);


#결과 이미지 출력
cv2.imshow( 'Origianl', img_src )
cv2.imshow( 'Gray', img_gray )
cv2.imshow( 'Noise', np.uint8(img_noise))
cv2.imshow( 'Smoothing', np.uint8(img_smoothing))

cv2.waitKey(0)
cv2.destroyAllWindows()