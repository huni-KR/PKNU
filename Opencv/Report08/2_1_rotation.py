import cv2

# 이미지 읽기
src = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)

height, width, channel = src.shape

# getRotationMatrix2D 45도 회전
matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
result = cv2.warpAffine(src, matrix, (width, height))

# 이미지 출력
cv2.imshow("src", src)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

