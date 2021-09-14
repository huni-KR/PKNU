import cv2

# 원본 이미지
img_source = cv2.imread('image1.jpg')
cv2.imshow("original", img_source)

# 2배 이미지
img_result = cv2.resize(img_source, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("x2", img_result)


# INTER_CUBIC를 사용해 확대한 2배 이미지를 0.5배한 이미지
img_result1 = cv2.resize(img_result, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
cv2.imshow("x0.5 INTER_AREA", img_result1)

img_result2 = cv2.resize(img_result, None, fx=0.5, fy=0.5) # cv2.INTER_LINEAR
cv2.imshow("x0.5 INTER_LINEAR", img_result2)

cv2.waitKey(0)
cv2.destroyAllWindows()

