#Calcul de la distance au contour le plus proche (fucked)
import cv2
import numpy as np
from mss import mss
from PIL import Image


def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    
    # Extract edges with canny
    canny_edges = cv2.Canny(img_gray_blur, 10, 250)
    
    # Dilate the edges to close gaps
    kernel = np.ones((3,3),np.uint8)
    dilated_edges = cv2.dilate(canny_edges, kernel, iterations=1)

    return dilated_edges

def distance(point, contours):
    # Find the contour directly to the right of the point
    closest_contour_point = None
    closest_distance = np.inf
    for contour in contours:
        for point_on_contour in contour:
            x, y = point_on_contour[0]
            if x > point[0] and abs(y - point[1]) <= 10:  # Only look on the same x-axis and within 10 pixels of the point
                distance = np.sqrt((x - point[0]) ** 2 + (y - point[1]) ** 2)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_contour_point = point_on_contour[0]
    return closest_distance, closest_contour_point



bounding_box = {'top': 60, 'left': 40, 'width': 620, 'height': 450}
sct = mss()

while True:
    # Capture screenshot of the specified region of the screen
    sct_img = sct.grab(bounding_box)
    # Convert the screenshot to a PIL Image
    img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
    # Convert the PIL Image to a NumPy array
    img_np = np.array(img)
    # Apply edge detection to the captured image
    edges = sketch(img_np)
    # Find contours of the edges
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw the contours on the original image
    cv2.drawContours(img_np, contours, -1, (0, 255, 0), 3)
    
    # Center point of the bounding box
    point = (310, 250)
    
    # Calculate the distance to the closest contour to the right of the point
    #dist = distance(point, contours)
    dist, closest_contour_point = distance(point, contours)

    closest_point = tuple(closest_contour_point)

    # Draw a circle at the point to indicate it
    cv2.circle(img_np, point, 5, (255, 0, 0), -1)
    # Draw a circle at the closest_points to idicate it
    cv2.circle(img_np, closest_point , 5, (255, 0, 0), -1)
    #print(closest_contour_point)
    # Display the results in a window named "screen"
    cv2.imshow('screen', img_np)
    # Print the distance to the closest contour to the right of the point
    print(f"The distance between the point {point} and the closest contour directly on its right is {dist}.")
    
    if (cv2.waitKey(1) & 0xFF) == ord('²'):
        cv2.destroyAllWindows()
        break
