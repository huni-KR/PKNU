import cv2
import numpy as np 


def kuwahara(img):
    
    pad_size = 2

    height, width, size = img.shape
    
    out = img.copy()

    pad_img = np.zeros(( height + pad_size * 2 , width + pad_size * 2, size ))
    
    for i in range(size):
        pad_img[:, :, i] = np.pad(out[:, :, i], [pad_size, pad_size], 'constant')
    
    for h in range(height):
        for w in range(width):
            for s in range(size):
                point_index = ( h + pad_size, w + pad_size, s )

                # 3 X 3 마스크 총 4개
                sub_mask = np.zeros(( 4, pad_size + 1, pad_size + 1 ) )

                sub_mask[0] = pad_img[ h:(point_index[0] + 1), w:(point_index[1] + 1), s]
                sub_mask[1] = pad_img[ h:(point_index[0] + 1), point_index[1]:(point_index[1] + pad_size + 1), s]
                sub_mask[2] = pad_img[ point_index[0]:(point_index[0] + pad_size + 1), w:(point_index[1] + 1), s]
                sub_mask[3] = pad_img[ point_index[0]:(point_index[0] + pad_size + 1), point_index[1]:(point_index[1] + pad_size + 1), s]

                # 분산 구하기
                std = [ np.std( sub_mask[0]), np.std( sub_mask[1]), np.std( sub_mask[2]), np.std( sub_mask[3]) ]

                # 마스크 영역에서 최소 분산 값 찾기
                min_std_index = np.argwhere( std == np.min(std))[0, 0]

                # 최소 분산값의 마스크의 평균 대입
                out[h, w, s] = np.sum( sub_mask[min_std_index]) / 9

    return out
                
# Read image
img = cv2.imread("image1.jpg")

# Median Filter
out = kuwahara(img)

# Save result
cv2.imshow("image", img)
cv2.imshow("result", out)

cv2.waitKey(0)
cv2.destroyAllWindows()