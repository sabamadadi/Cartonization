import cv2
import numpy as np
from matplotlib import pyplot as plt

def convert_to_cartoon(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to RGB color space
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Apply bilateral filtering to reduce noise while preserving edges
    smoothed = cv2.bilateralFilter(image_rgb, 31, 250, 250)

    # Convert the smoothed image to grayscale
    gray = cv2.cvtColor(smoothed, cv2.COLOR_RGB2GRAY)

    # Apply Canny edge detection to extract the edges
    edges = cv2.Canny(gray, 100, 255)

    # Convert the edges to BGR color space
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Create a black image of the same size as the original image
    black_image = np.zeros_like(image_rgb)

    # Combine the edges with the black image
    cartoon = smoothed + edges_bgr

    # Display the original image and the cartoonized image
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(cartoon)
    plt.title('Cartoonized Image')

    plt.show()

# Provide the path to image
image_path = '/content/image3.jpg'

# Convert the image to a cartoon with Canny edge detection
convert_to_cartoon(image_path)
