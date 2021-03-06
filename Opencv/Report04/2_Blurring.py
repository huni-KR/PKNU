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

# blurring
def blurring(img, K_size=3):
    H, W = img.shape

    # zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float)
    tmp = out.copy()

    # emboss kernel
    K = [[1., 1., 1.], [1., 1., 1.], [1., 1., 1.]]

    # filtering
    for y in range(H):
        for x in range(W):
            out[pad + y, pad + x] = np.sum(1/9 * (tmp[y: y + K_size, x: x + K_size]))

    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out

# 이미지 읽기
img = cv2.imread("image1.jpg")
gray = BGR2GRAY(img)

# blurring
out = blurring(gray, K_size=3)

# 이미지 출력
cv2.imshow("image", img)
cv2.imshow("gray", gray)
cv2.imshow("result", out)

cv2.waitKey(0)
cv2.destroyAllWindows()