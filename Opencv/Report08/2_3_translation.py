import cv2
import numpy as np

src = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)

# 이미지 이동
height, width = src.shape[:2]
# 이미지를 오른쪽으로 50, 아래로 50 이동
M = np.float32([[1, 0, 50], [0, 1, 50]])
img_translation = cv2.warpAffine(src, M, (width,height))

# 이미지 출력
cv2.imshow("src", src)
cv2.imshow("result", img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()