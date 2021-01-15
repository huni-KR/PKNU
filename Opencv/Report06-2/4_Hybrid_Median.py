import cv2
import numpy as np

# Gray scale 
def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    
    # Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b 
    out = out.astype(np.uint8) 

    return out 

def hybrid_median(img):
    height = img.shape[0]
    width = img.shape[1]
 
    out = img.copy()

    # 마스크 초기화
    Mask = []
    for i in range(9):
        Mask.append(0)

    for y in range(1, height-1):
        for x in range(1, width-1):

            Mask[0] = img[y-1][x-1]
            Mask[1] = img[y-1][x+1]
            Mask[2] = img[y][x]
            Mask[3] = img[y+1][x-1]
            Mask[4] = img[y+1][x+1]

            Mask.sort()
            out[y][x] = Mask[2]            

    return out


# Read image
img = cv2.imread("image1.jpg")

# grayscale 
gray = BGR2GRAY(img) 

# Hybrid Median Filter
out = hybrid_median(gray)

# Save result
cv2.imshow("image", img)
cv2.imshow("gray", gray)
cv2.imshow("result", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
