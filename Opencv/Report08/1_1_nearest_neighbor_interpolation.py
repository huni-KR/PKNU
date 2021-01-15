import cv2

# 이미지 읽기
src = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)

# cv2.INTER_NEAREST로 이웃보간법 사용
result = cv2.resize(src, dsize=(512, 512), interpolation=cv2.INTER_NEAREST)

# 이미지 출력
cv2.imshow("src", src)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()