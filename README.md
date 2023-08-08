# Cartonization

Writing a program that converts an image to a cartoon!

## K-means Clustering
This code performs image cartoonization using the K-means clustering algorithm. Here's a breakdown of what the code does:

1. The required libraries are imported, including `cv2` for image processing, `numpy` for numerical operations, `matplotlib` for visualization, and `sklearn` for K-means clustering.

2. The `convert_to_cartoon` function is defined, which takes an image path as input.

3. The image specified by the image path is read using `cv2.imread`.

4. The image is converted from the default BGR color space to the RGB color space using `cv2.cvtColor`.

5. Canny edge detection is applied to the RGB image using `cv2.Canny`, which detects the edges in the image.

6. The RGB image is reshaped into a 2D array of pixel values using `image_rgb.reshape((-1, 3))`.

7. The pixel values are converted to `float32` data type.

8. The K-means clustering algorithm is applied to the pixel values using `cv2.kmeans`. The number of clusters is specified as 10, but you can change this value. The algorithm assigns each pixel to one of the clusters based on its color similarity.

9. The centers of the clusters are extracted.

10. The pixel values are replaced with the values of the cluster centers to obtain the cartoonized image.

11. The cartoon image is reshaped back to the original shape of the RGB image.

12. The edges image is converted to the BGR color space using `cv2.cvtColor`.

13. The cartoon image is combined with the edges image to create a cartoonized version of the original image.

14. The brightness of the cartoonized image is adjusted using `cv2.convertScaleAbs`.

15. The original image and the cartoonized image are displayed side by side using `matplotlib.pyplot.imshow`.

16. The function `convert_to_cartoon` is called with the provided image path.

Overall, the code reads an image, applies edge detection and K-means clustering to create a cartoonized version of the image, and then displays the original and cartoonized images.

## Average Filter
This code performs image cartoonization using the average filter and edge detection. Here's a breakdown of what the code does:

1. The required libraries are imported, including `cv2` for image processing, `numpy` for numerical operations, and `matplotlib` for visualization.

2. The `convert_to_cartoon` function is defined, which takes an image path as input.

3. The image specified by the image path is read using `cv2.imread`.

4. The image is converted from the default BGR color space to the RGB color space using `cv2.cvtColor`.

5. An average filter is applied to the RGB image using `cv2.blur`. The size of the filter kernel is specified as (10, 10), but you can change this value. The average filtering operation reduces noise and smooths the image.

6. The smoothed image is converted to grayscale using `cv2.cvtColor`.

7. Canny edge detection is applied to the grayscale image using `cv2.Canny`, which detects the edges in the image.

8. The edges image is converted to the BGR color space using `cv2.cvtColor`.

9. The edges image is combined with the smoothed image to create a cartoonized version of the original image. This combines the edges with the smoothed regions to create a cartoon-like appearance.

10. The original image and the cartoonized image are displayed side by side using `matplotlib.pyplot.imshow`.

11. The function `convert_to_cartoon` is called with the provided image path.

Overall, the code reads an image, applies average filtering, edge detection, and combines the edges with the smoothed image to create a cartoonized version of the image. The original and cartoonized images are then displayed.
## Bilateral Filter
This code performs image cartoonization using the bilateral filter and Canny edge detection. Here's a breakdown of what the code does:

1. The required libraries are imported, including `cv2` for image processing, `numpy` for numerical operations, and `matplotlib` for visualization.

2. The `convert_to_cartoon` function is defined, which takes an image path as input.

3. The image specified by the image path is read using `cv2.imread`.

4. The image is converted from the default BGR color space to the RGB color space using `cv2.cvtColor`.

5. The bilateral filter is applied to the RGB image using `cv2.bilateralFilter`. The bilateral filter reduces noise while preserving edges. The parameters used for the filter are a diameter of 31, and sigma values of 250 for color space and intensity space. You can adjust these values for different effects.

6. The smoothed image is converted to grayscale using `cv2.cvtColor`.

7. Canny edge detection is applied to the grayscale image using `cv2.Canny`, which detects the edges in the image.

8. The edges image is converted to the BGR color space using `cv2.cvtColor`.

9. A black image of the same size as the original image is created using `np.zeros_like`.

10. The edges image is combined with the smoothed image to create a cartoonized version of the original image. This combines the edges with the smoothed regions to create a cartoon-like appearance.

11. The original image and the cartoonized image are displayed side by side using `matplotlib.pyplot.imshow`.

12. The function `convert_to_cartoon` is called with the provided image path.

Overall, the code reads an image, applies the bilateral filter to reduce noise while preserving edges, performs Canny edge detection, and combines the edges with the smoothed image to create a cartoonized version of the image. The original and cartoonized images are then displayed.

-------------------

<p align="center">
  <img src="image3.jpg" alt="Alt Text">
</p>
