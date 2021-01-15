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
    
# Roberts filter 
def Roberts_filter(img, K_size=3): 
    if len(img.shape) == 3: 
        H, W, C = img.shape 
    else:
        img = np.expand_dims(img, axis=-1) 
        H, W, C = img.shape 
        
    # Zero padding 
    pad = K_size // 2 
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float) 
    out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float) 
    tmp = out.copy() 
    out_l = out.copy() 
    out_r = out.copy() 
    
    ## Roberts Left to middle
    Kl = [[-1., 0., 0.],[0., 1., 0.], [0., 0., 0.]] 
    
    ## Roberts Right to middle
    Kr = [[0., 0., -1.],[0., 1., 0.],[0., 0., 0.]] 
     
    # filtering 
    for y in range(H): 
        for x in range(W):
            out_l[pad + y, pad + x] = np.sum(Kl * (tmp[y: y + K_size, x: x + K_size])) 
            out_r[pad + y, pad + x] = np.sum(Kr * (tmp[y: y + K_size, x: x + K_size])) 
    
    out_l = np.clip(out_l, 0, 255) 
    out_r = np.clip(out_r, 0, 255) 
    
    out_l = out_l[pad: pad + H, pad: pad + W].astype(np.uint8) 
    out_r = out_r[pad: pad + H, pad: pad + W].astype(np.uint8) 
    
    return out_l, out_r 
    
# Read image 
img = cv2.imread("image1.jpg")

# grayscale 
gray = BGR2GRAY(img) 

# Roberts filtering 
out_l, out_r = Roberts_filter(gray, K_size=3) 

# Save result 
cv2.imshow("image", img)
cv2.imshow("gray", gray)
cv2.imshow("result_l", out_l)
cv2.imshow("result_r", out_r) 

cv2.waitKey(0) 
cv2.destroyAllWindows()