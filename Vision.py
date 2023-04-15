

# your sketch generating function
#input: image

import cv2
import numpy as np

#output : mask (the sketched image)
def sketch(image):
    # Convert image to grayscale
    
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  

    # Clean up image using Guassian Blur --> niveau de flou
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    
    # Extract edges with canny th1 10, th 70 --> seuils de binarisation
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    
    # Do an invert binarize the image th 70
    
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)

    return mask


# Initialize webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was sucessful (ret)
# It also contains the images collected from the webcam (frame)
cap = cv2.VideoCapture(0)

while True:
    #read frame by frame
    ret, frame = cap.read()
    #display the results
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
# Release camera and close windows

cap.release()    
cv2.destroyAllWindows()
