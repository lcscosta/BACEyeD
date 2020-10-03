
## Algorithm
# 8. Detect Pupil and Iris using Circle Hough
# 9. Deduce ratio and dilation from measurements
# 10.Display Stats, Graphs and Images


import cv2 
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction 


def detect_iris_and_pupil(image):
  if image is None:
    print("Image is empty")
    return
    
  # Use one image for detecting the iris, pupil
  iris_detection = image.copy()
  pupil_detection = image.copy()
  final_detection = image.copy()	

  # Find the iris
  gray_cropped = blur_grayscale(iris_detection, 7)
  iris = cv2.HoughCircles(gray_cropped, cv2.HOUGH_GRADIENT, 1, iris_detection.shape[0], param1=1, param2=2, minRadius=0, maxRadius=150)
  iris_detection, ix, iy, ir = draw_detection(iris_detection, iris)

  # Find the pupil
  gray_cropped = blur_grayscale(pupil_detection, 5)
  pupil = cv2.HoughCircles(gray_cropped, cv2.HOUGH_GRADIENT, 1, pupil_detection.shape[0], param1=1, param2=1, minRadius=0, maxRadius=ir-100)
  pupil_detection, px, py, pr = draw_detection(pupil_detection, pupil)

  # draw the final detection
  cv2.circle(final_detection, (ix, iy), 2, (0, 0, 255), 2)
  cv2.circle(final_detection, (ix, iy), ir, (255, 0, 0), 2)
  cv2.circle(final_detection, (px, py), pr, (255, 0, 0), 2)

  # Get ratio in pixels and millimeters
  pupil_px, iris_px, pupil_mm, iris_mm = get_ratio(pr, ir)

  return final_detection, pupil_px, iris_px, pupil_mm, iris_mm, gray_cropped

# Convert an image to grayscale and apply a blur for the Circle Hough Transform
def blur_grayscale(image, blur):
  blurred_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  return cv2.medianBlur(blurred_image, blur)

# Detect the iris or pupil
def draw_detection(image, detection):
  try:
    detection = np.uint16(np.around(detection))
    x, y, r = detection[0, 0]
    cv2.circle(image, (x, y), 2, (0, 0, 255), -1)
    cv2.circle(image, (x, y), r, (255, 0, 0), 1)
  except:
	  print("No circles were found")
   
  return image, x, y, r

# Calculate the ratio, simplify it and then return the numerator and denominator
def get_ratio(pr, ir):
  # Radius in millimeters
  iris_mm = 6.5

  ratio = Fraction(pr, ir)
  pupil_px = ratio.numerator
  iris_px = ratio.denominator

  # Using the ratio of millimeters : pixels for the iris,
  # we can use this factor to find the size in mm of the pupil
  # since we know its size in pixels
  px_to_mm_factor = iris_mm / iris_px
  pupil_mm = pr * px_to_mm_factor

  return pupil_px, iris_px, pupil_mm, iris_mm

def display_results(cropped_normal_eye, grey_cropped, final_detection, pupil_px, iris_px, pupil_mm, iris_mm):
    
    plt.figure(figsize=(30,20))
    grid = plt.GridSpec(3, 3)
    plt.subplot(grid[1,1])
    plt.imshow(cropped_normal_eye)
    plt.xlabel('Cropped normal eye')

    plt.subplot(grid[1,2])
    plt.imshow(cv2.cvtColor(grey_cropped , cv2.COLOR_GRAY2RGB))
    plt.xlabel('Grey eye')


    plt.subplot(grid[2,0])
    plt.imshow(cv2.cvtColor(final_detection , cv2.COLOR_BGR2RGB))
    plt.xlabel('Circle Hough')

    plt.subplot(grid[2, 1:3])
    plt.axis("off")
    plt.xlabel('')
    plt.ylabel('')
    plt.text(0, 0.5, f'Ratio of dilation in pixels is {pupil_px}px : {iris_px}px\nRatio of dilation in mm is {pupil_mm}mm : {iris_mm}mm', style='italic',
            bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 20},  fontsize=10)
    plt.show()

def measure_dilation(color_path="./images/índice.jpeg"):
    #infrared = cv2.imread(infrared_path, 1)
    color = cv2.imread(color_path, 1)

    cropped_normal_eye = color.copy()

    final_detection, pupil_px, iris_px, pupil_mm, iris_mm, grey_cropped = detect_iris_and_pupil(color)
    display_results(cropped_normal_eye, grey_cropped, final_detection, pupil_px, iris_px, pupil_mm, iris_mm)

measure_dilation()