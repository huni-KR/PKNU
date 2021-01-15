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
    
def LoG_Operator(img):
    H = img.shape[0]
    W = img.shape[1]

    pad = 5 // 2
    out = np.zeros(( H + pad * 2, W + pad * 2), dtype = np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
    tmp = out.copy()

    K = [ [0., 0., -1., 0., 0.,],
          [0., -1., -2., -1., 0.],
          [-1., -2., 16., -2., -1.,],
          [0., -1., -2., -1., 0.],
          [0., 0., -1., 0., 0.,] ]

    for y in range(H):
        for x in range(W):
            out[pad + y, pad + x ] = np.sum( K * ( tmp[ y : y+5, x : x + 5 ] ) )
    
    out = np.clip(out,0,255)
    out = out[ pad : pad + H, pad : pad + W ].astype(np.uint8)

    return out

    
# Read image
img = cv2.imread("image1.jpg")

# grayscale
gray = BGR2GRAY(img)

# LoG filtering
out = LoG_Operator(gray)

# Save result
cv2.imshow("imgae", img)
cv2.imshow("gray", gray)
cv2.imshow("result", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
