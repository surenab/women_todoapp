import cv2
import numpy as np

# Step 1: Load the image
image_path = "aaaa.png"

img = cv2.imread(image_path)

# Step 2: Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


height, width = gray_img.shape
center_x, center_y = width // 2, height // 2
radius = min(center_x, center_y)  # Using the smaller dimension for radius

mask = np.zeros((height, width), np.uint8)
cv2.circle(mask, (center_x, center_y), radius, (255, 255, 255), -1)


# # Step 4: Use the mask to keep only the circular part of the image
circular_gray_img = cv2.bitwise_and(gray_img, gray_img, mask=mask)


cv2.imwrite("final.png", circular_gray_img)
# Display the result
cv2.imshow("Circular Grayscale Image", circular_gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
