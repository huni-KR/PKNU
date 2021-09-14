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

# Gaussian filter
def gaussian_filter(img, K_size=3, sigma=1.3):

    if len(img.shape) == 3:
        H, W, C = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        H, W, C = img.shape

    # Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)

    # prepare Kernel
    K = np.zeros((K_size, K_size), dtype=np.float)

    for x in range(-pad, -pad + K_size):
        for y in range(-pad, -pad + K_size):
            K[y + pad, x +
                pad] = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))

    K /= (2 * np.pi * sigma * sigma)
    K /= K.sum()
    tmp = out.copy()

    # 필터링
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x,
                    c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])

    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out


# 이미지 읽기
img = cv2.imread("image1.jpg")
gray = BGR2GRAY(img)

# Gaussian Filter
out = gaussian_filter(gray, K_size=3, sigma=1.3)

# 이미지 출력
cv2.imshow("image", img)
cv2.imshow("gray", gray)
cv2.imshow("result", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
