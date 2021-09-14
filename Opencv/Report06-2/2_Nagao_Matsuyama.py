import cv2
import numpy as np

img=cv2.imread('image1.jpg',0)    # 이미지 불러오기
r, c = img.shape       # 이미지의 높이, 너비

list = ['list_0', 'list_1', 'list_2', 'list_3', 'list_4', 'list_5', 'list_6', 'list_7']

zeros = np.zeros((r+4, c+4), dtype=np.uint8)      # 크기가 r+4, c+4인 검은색 바탕 이미지 생성
nangao_img = np.zeros((r, c), dtype=np.uint8)
zeros[2:r+2, 1:c+1] += img                      # zero padding과 같은 역할을 해줌. 검은 이미지에 원본 이미지 겹치기
std = []

def mask_1(i, a, b):
    list[i] = np.array(a).flatten().tolist()
    list[i].append(b)
    return list[i]

def mask_2(i, a, b, c, d):
    list[i] = np.array(a).flatten().tolist()
    list[i].extend([b, c, d])
    return list[i]

def nagao_Matsuyama(a, b):
    list[0] = mask_1(0, zeros[a-2:a, b-1:b+2], zeros[a, b])     # 영역에 따라 총 8개의 마스크로 분할하여 리스트 생성
    list[1] = mask_1(1, zeros[a-1:a+2, b+1:b+3], zeros[a, b])
    list[2] = mask_1(2, zeros[a+1:a+3, b-1:b+2], zeros[a, b])
    list[3] = mask_1(3, zeros[a-1:a+2, b-2:b], zeros[a, b])
    list[4] = mask_2(4, zeros[a-2:a, b-2:b], zeros[a, b-1], zeros[a, b], zeros[a-1, b])
    list[5] = mask_2(5, zeros[a-2:a, b+1:b+3], zeros[a, b+1], zeros[a, b], zeros[a-1, b])
    list[6] = mask_2(6, zeros[a:a+2, b:b+2], zeros[a+1, b+2], zeros[a+2, b+1], zeros[a+2, b+2])
    list[7] = mask_2(7, zeros[a+1:a+3, b-2:b], zeros[a, b-1], zeros[a, b], zeros[a+1, b])

    index=0
    std = []
    for x in range(0, 8):
        std.append(np.std(list[x]))     # 분산값을 담은 리스트 생성
    min = std[0]

    for x in range(0,8):        # 최소 분산값 찾기
        if min > std[x]:
            min = std[x]
            index = x

    min = np.mean(list[index])        # 최소 분산값의 평균값
    return min

for x in range(2, r+2):
    for y in range(2, c+2):
        nangao_img[x-2, y-2] = nagao_Matsuyama(x, y)

cv2.imshow("original", img)#원본이미지 출력
cv2.imshow("result", nangao_img)#test 이미지 출력

cv2.waitKey(0)#사용자가 키 입력을 할때까지 기다림