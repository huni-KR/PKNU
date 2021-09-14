import cv2 
import numpy as np

# Gaussian filter 
def gaussian_filter(img, K_size=3, sigma=1.3): 
    if len(img.shape) == 3: 
        H, W, C = img.shape 
    else: 
        img = np.expand_dims(img, axis=-1) 
        
    H, W, C = img.shape 
    
    ## Zero padding 
    pad = K_size // 2 
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float) 
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float) 
    
    ## prepare Kernel 
    K = np.zeros((K_size, K_size), dtype=np.float) 
    
    for x in range(-pad, -pad + K_size): 
        for y in range(-pad, -pad + K_size): 
            K[y + pad, x + pad] = np.exp( -(x ** 2 + y ** 2) / (2 * (sigma ** 2))) 
    
    K /= (2 * np.pi * sigma * sigma)
    K /= K.sum() 
    
    tmp = out.copy() 
            
    # filtering
    for y in range(H): 
        for x in range(W): 
            for c in range(C): 
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c]) 
                
    out = np.clip(out, 0, 255) 
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8) 
    
    return out 
    
# Read image 
img = cv2.imread("image1.jpg") 

# Gaussian Filter 
gaussian1 = gaussian_filter(img, K_size=3, sigma=1.3) 
gaussian2 = gaussian_filter(img, K_size=3, sigma=2.1) 

result = abs(gaussian2 - gaussian1)

# Show image 
cv2.imshow("image", img) 
cv2.imshow("gaussian1", gaussian1) 
cv2.imshow("gaussian2", gaussian2) 
cv2.imshow("result", result) 


cv2.waitKey(0) 
cv2.destroyAllWindows()