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
    
# homogeneity filter 
def homogeneity_filter(img, K_size=3): 
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
    out = out.copy() 
         
    # filtering 
    for y in range(1, H-1): 
        for x in range(1, W-1):
            out[pad + y, pad + x] = max( abs( img[y][x] - img[y - 1][x - 1] ), abs( img[y][x] - img[y - 1][x] ), abs( img[y][x] - img[y - 1][x + 1] ), abs( img[y][x] - img[y][x - 1] ), abs( img[y][x] - img[y][x + 1] ), abs( img[y][x] - img[y + 1][x - 1] ), abs( img[y][x] - img[y + 1][x] ), abs( img[y][x] - img[y + 1][x + 1] )  )
    
    out = np.clip(out, 0, 255)  
    
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8) 
    
    return out
    
# Read image 
img = cv2.imread("image1.jpg")

# grayscale 
gray = BGR2GRAY(img) 

# Homogeneity filtering 
out = homogeneity_filter(gray, K_size=3) 

# Save result 
cv2.imshow("image", img)
cv2.imshow("gray", gray)
cv2.imshow("result", out)

cv2.waitKey(0) 
cv2.destroyAllWindows()