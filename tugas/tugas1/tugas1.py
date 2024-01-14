import cv2
import numpy as np

# Tulis Kodingan kalian dibawah
def detect_green_objects(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to HSV format
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the green color range in HSV format
    lower_green = np.array([50, 50, 0])
    upper_green = np.array([100, 255, 255])

    # Create a mask to extract the green color
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Find contours in the mask
    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through all contours and create red bounding boxes
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the original image with red bounding boxes
    cv2.imshow('Green Object Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the image path
image_path = 'tugas/tugas1/tugas1.py'

# Call the function to detect green objects in the specified image
detect_green_objects(image_path)
