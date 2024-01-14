import cv2
import numpy as np

# Tulis Kodingan kalian dibawah
def process_image(image_path):
    # Read image
    img = cv2.imread(image_path)

    # Blur the image
    img_blur = cv2.GaussianBlur(img, (3, 3), 100)

    # Apply Canny edge detection algorithm
    canny = cv2.Canny(img_blur, 125, 175)

    # Find contours
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Select a contour (you may want to add more logic here to handle different cases)
    selected_contour = contours[7]

    # Draw contours on the image
    img_contours = img.copy()
    cv2.drawContours(img_contours, [selected_contour], 0, (0, 0, 0), 3)

    # Approximate the contour to get the number of sides
    epsilon = 0.02 * cv2.arcLength(selected_contour, True)
    approx = cv2.approxPolyDP(selected_contour, epsilon, True)

    # Add text with the number of sides in the top-left corner of the image
    img_with_text = img_contours.copy()
    cv2.putText(img_with_text, str(len(approx)), (10, 125), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 2, cv2.LINE_AA)

    # Display the images
    cv2.imshow("Image with Contour", img_with_text)
    cv2.imshow("Canny Edge Detection", canny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the image path
image_path = "magang bayucaraka/tugas cv/tugas2.jpg"

# Call the function with the image path
process_image(image_path)
