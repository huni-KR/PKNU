import cv2
import numpy as np
 
def find_nearest_above(my_array, target):
    diff = my_array - target
    mask = np.ma.less_equal(diff, -1)

    # 마스크 값 찾기
    if np.all(mask):
        c = np.abs(diff).argmin()
        return c
        
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()

def hist_match(original, specified):
 
    oldshape = original.shape
    original = original.ravel()
    specified = specified.ravel()
 
    # 고유 한 픽셀 값 세트와 해당 인덱스 및 개수 가져 오기
    s_values, bin_idx, s_counts = np.unique(original, return_inverse=True,return_counts=True)
    t_values, t_counts = np.unique(specified, return_counts=True)
 
    # original 이미지에 대한 연산
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    
    # specified 이미지에 대한 연산
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]
 
    # 반올림
    sour = np.around(s_quantiles*255)
    temp = np.around(t_quantiles*255)
    
    # 반올림 된 값 매핑
    b=[]
    for data in sour[:]:
        b.append(find_nearest_above(temp,data))
    b= np.array(b,dtype='uint8')
 
    return b[bin_idx].reshape(oldshape)

# 이미지 읽기
original = cv2.imread('image1.jpg',0)
specified = cv2.imread('image2.jpg',0)
 
# 히스토그램 매칭
a = hist_match(original, specified)
 
# 이미지 출력
cv2.imshow('original',original)
cv2.imshow('original specified',specified)
cv2.imshow('result',np.array(a,dtype='uint8'))

cv2.waitKey(0)
cv2.destroyAllWindows()