import cv2
import numpy as np
image = cv2.imread("C:/Users/F A R H A N/Documents/Dataset/Rose.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
laplacian_kernel = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]], dtype=np.float32)

sharpened_image = cv2.filter2D(gray_image, -1, laplacian_kernel)
sharpened_image = cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.imwrite('sharpened_image.jpg', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
