import numpy as np
import cv2

# 이미지 읽기
img = cv2.imread("image1.jpg")
cv2.imshow("original",img)

Z = img.reshape((-1,3))
Z = np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# k = 2인 k-means 생성
K1 = 2
attempts=10
ret,label,center=cv2.kmeans(Z,K1,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

# k = 2인 이미지 출력
cv2.imshow("k=2",res2)


# k = 6인 k-means 생성
K2 = 6
attempts=10
ret,label,center=cv2.kmeans(Z,K2,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res3 = res.reshape((img.shape))

# k = 6인 이미지 출력
cv2.imshow("k=6",res3)

cv2.waitKey()
cv2.destroyAllWindows()