# 6. a-trimmed mean 프로그램

from random import random

import cv2, math
import numpy as np

# salt pepper 잡음 생성
def add_salt_and_pepper(image, p):
    h, w, c = images.shape
    output = np.zeros(image.shape, np.uint8)
    thresh = 1 - p
    for i in range(h):
        for j in range(w):
            for z in range(c):
                rdn = random()
                if rdn < p:
                    output[i, j, z] = 0
                elif rdn > thresh:
                    output[i, j, z] = 1
                else:
                    output[i, j, z] = image[i, j, z]
    return output

def change_image_array_shape(image, pad_size):  # padding 을 해줌
    h, w, channel = image.shape
    out_image = image.copy()
    padding_image = np.zeros((h + pad_size * 2, w + pad_size * 2, channel))  # padding 한 이미지 만듬

    # 원래이미지값 넣어줌
    for c in range(channel):
        padding_image[:, :, c] = np.pad(out_image[:, :, c], (pad_size, pad_size), 'constant',
                                        constant_values=0)  # out_image 에서 뽑아낸 값을 padding 해줌
    return padding_image

def a_trimmed_mean_filter(image, out_image, alpha):
    h, w, c = image.shape
    area = np.zeros((3, 3))     # 2차원 3*3 array 를 만듬

    for i in range(1, h+1):
        for j in range(1, w+1):
            for z in range(c):
                # 각 영역 대입
                area[0, 0] = out_image[i - 1, j - 1, z]
                area[1, 0] = out_image[i, j - 1, z]
                area[2, 0] = out_image[i + 1, j - 1, z]
                area[0, 1] = out_image[i - 1, j, z]
                area[1, 1] = out_image[i, j, z]
                area[2, 1] = out_image[i + 1, j, z]
                area[0, 2] = out_image[i - 1, j + 1, z]
                area[1, 2] = out_image[i, j + 1, z]
                area[2, 2] = out_image[i + 1, j + 1, z]
                number = np.ravel(area)     # 2차원 ndarray -> 1차원
                number = np.sort(number)    # 정렬

                # alpha 가 0 이면 평균필터랑 같음 alpha 0.5이면 median 필터랑 같음
                if alpha == 0.5:    # alpha = 0.5 이면 median 필터이므로 중간값으로 픽셀 설정
                    a_sum = number[4]
                elif alpha == 0:    # alpha = 0 이면 mean 필터이므로 평균값 계산
                    a_sum = int(np.mean(number))
                else:   # alpha 가 0도 아니고 0.5 도 아니면 양쪽에 trim_mean 만큼 짜름
                    trim_mean = math.floor(alpha * 9)
                    number = number[trim_mean: -trim_mean]
                    a_sum = int(np.mean(number))
                image[i - 1, j - 1, z] = a_sum  # 구한 평균을 픽셀에 대입
    return image


images = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)
images = cv2.resize(images, (512, 512), interpolation=cv2.INTER_CUBIC)
pad_img = change_image_array_shape(images, 1)   # 이미지 패딩

noise_img = add_salt_and_pepper(images, 0.2)    # 소금, 후추 있는 영상 만듬
result_img1 = a_trimmed_mean_filter(noise_img.copy(), pad_img, 0)   # alpha = 0
result_img2 = a_trimmed_mean_filter(noise_img.copy(), pad_img, 0.3)   # alpha = 0.3
result_img3 = a_trimmed_mean_filter(noise_img.copy(), pad_img, 0.5)   # alpha = 0.5
result_img = np.hstack((result_img1, result_img2, result_img3))     # alpha = 0, 0.3, 0.5 순서

cv2.imshow("original", images)
cv2.imshow("noise_img", noise_img)
cv2.imshow("result", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()