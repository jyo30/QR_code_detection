# import cv2
# from pyzbar import pyzbar
# import os

# def extract_qr_codes(image_path, output_folder):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply any necessary preprocessing techniques
#     # e.g., resizing, denoising, or thresholding

#     # Detect QR codes
#     qr_codes = pyzbar.decode(gray)

#     # Iterate through the detected QR codes
#     for i, qr_code in enumerate(qr_codes):
#         qr_data = qr_code.data.decode("utf-8")

#         # Extract the region of the QR code from the original image
#         (x, y, w, h) = qr_code.rect
#         qr_image = image[y:y + h, x:x + w]

#         # Save the extracted QR code as an image
#         output_path = os.path.join(output_folder, f"QRCode_{i}.jpg")
#         cv2.imwrite(output_path, qr_image)

#         # Draw a rectangle around the QR code on the original image
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         # Put the QR code data as text on the original image
#         cv2.putText(image, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#     # Save the annotated image with bounding boxes and text
#     annotated_output_path = os.path.join(output_folder, "Annotated_Image1.jpg")
#     cv2.imwrite(annotated_output_path, image)

# # Usage example
# image_path = 'images.jpg'
# output_folder = 'annotated/'

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Extract QR codes from the image
# extract_qr_codes(image_path, output_folder)


# import cv2
# from pyzbar.pyzbar import decode
# import numpy as np
# #img=cv2.imread('QRCode_ArticleImage3.jpg')
# cap=cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# while True:

#     success, img = cap.read()
#     for barcode in decode(img):
#         myData = barcode.data.decode('utf-8')
#         print(myData)
#         pts = np.array([barcode.polygon],np.int32)
#         pts = pts.reshape((-1,1,2))
#         cv2.polylines(img,[pts],True,(255,0,255),5)
#         pts2 = barcode.rect
#         cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)

#     cv2.imshow('Result',img)
#     cv2.waitKey(1)


# import cv2
# from pyzbar.pyzbar import decode
# import numpy as np
# import os

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

# output_folder = 'detected_qr_codes'
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# count = 0

# while True:
#     success, img = cap.read()

#     for barcode in decode(img):
#         myData = barcode.data.decode('utf-8')
#         print(myData)
#         pts = np.array([barcode.polygon], np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(img, [pts], True, (255, 0, 255), 5)
#         pts2 = barcode.rect
#         cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

#         x, y, w, h = pts2
#         cropped_img = img[y:y + h, x:x + w]

#         output_path = os.path.join(output_folder, f'detected_qr_{count}.jpg')
#         cv2.imwrite(output_path, cropped_img)
#         count += 1

#     cv2.imshow('Result', img)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()






##########################qr code detector webcam###############
import cv2
from pyzbar import pyzbar

import json

def decode_qr_code(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find QR codes in the image
    qr_codes = pyzbar.decode(gray)

    # Loop over detected QR codes
    for qr_code in qr_codes:
        # Extract the data from the QR code
        data = qr_code.data.decode("utf-8")
        print("QR Code Data:", data)

        # Check if the data is in JSON format
        try:
            json_data = json.loads(data)
            print("Decoded JSON data:", json_data)
        except json.JSONDecodeError:
            pass

        # Draw a bounding box around the QR code
        (x, y, w, h) = qr_code.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw the QR code data on the image
        cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the image with bounding boxes and data
    cv2.imshow("QR Code Scanner", image)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is successfully opened
if not cap.isOpened():
    print("Failed to open webcam")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # If the frame was not successfully read, exit the loop
    if not ret:
        break

    # Decode the QR code from the frame
    decode_qr_code(frame)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()







######################detecting on single qr code video#############

import cv2
from pyzbar import pyzbar

def decode_qr_code(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find QR codes in the image
    qr_codes = pyzbar.decode(gray)

    # Loop over detected QR codes
    for qr_code in qr_codes:
        # Extract the data from the QR code
        data = qr_code.data.decode("utf-8")
        print("QR Code Data:", data)

        # Draw a bounding box around the QR code
        (x, y, w, h) = qr_code.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw the QR code data on the image
        cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the image with bounding boxes and data
    cv2.imshow("QR Code Scanner", image)

# Path to the input video file
video_path = "BB_0b0e9748-370a-4fd5-a1df-645a138bfd36_preview.mp4"

# Initialize the video capture
cap = cv2.VideoCapture(video_path)

# Check if the video capture is successfully opened
if not cap.isOpened():
    print("Failed to open video file")
    exit()

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was not successfully read, exit the loop
    if not ret:
        break

    # Decode the QR codes from the frame
    decode_qr_code(frame)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()









# import cv2
# from pyzbar import pyzbar
# import os

# # Function to decode QR codes in an image
# def decode_qr_code(image):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Find QR codes in the image
#     qr_codes = pyzbar.decode(gray)

#     # Set to store unique QR code data
#     unique_codes = set()
#      # List to store bounding box coordinates of QR codes
#     qr_code_boxes = []

#     # Loop over detected QR codes
#     for qr_code in qr_codes:
#         # Extract the data from the QR code
#         data = qr_code.data.decode("utf-8")
#         print("QR Code Data:", data)

#         # Add the data to the set of unique codes
#         unique_codes.add(data)

#         # Draw a bounding box around the QR code
#         (x, y, w, h) = qr_code.rect
#         qr_code_boxes.append((x, y, x + w, y + h))

#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         # Draw the QR code data on the image
#         cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     return image, unique_codes, qr_code_boxes

# # Path to the input video file
# video_path = "istockphoto-1371369676-640_adpp_is_AdobeExpress.mp4"

# # Initialize the video capture
# cap = cv2.VideoCapture(video_path)

# # Check if the video capture is successfully opened
# if not cap.isOpened():
#     print("Failed to open video file")
#     exit()

# # Set to store unique QR code data across frames
# unique_qr_codes = set()

# # Create a directory to store the QR code frames
# output_dir = "qr_frames"
# os.makedirs(output_dir, exist_ok=True)

# # Frame counter
# frame_counter = 0

# while True:
#     # Read a frame from the video
#     ret, frame = cap.read()

#     # If the frame was not successfully read, exit the loop
#     if not ret:
#         break

#     # Increment frame counter
#     frame_counter += 1

#     # Decode the QR codes and get the highlighted frame and unique QR code data
#     result_frame, frame_qr_codes, qr_code_boxes = decode_qr_code(frame)

#     # Update the set of unique QR code data
#     unique_qr_codes.update(frame_qr_codes)
#     # Draw rectangles around the QR codes in the frame
#     for (x1, y1, x2, y2) in qr_code_boxes:
#         cv2.rectangle(result_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

#     # Save the frame with QR codes to the output directory
#     output_path = os.path.join(output_dir, f"frame_{frame_counter}.jpg")
#     cv2.imwrite(output_path, result_frame)

#     # Display the resulting frame with bounding boxes and data
#     cv2.imshow("QR Code Scanner", result_frame)

#     # Check for 'q' key press to exit the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture and close all windows
# cap.release()
# cv2.destroyAllWindows()

# # Print the unique QR code data
# print("Unique QR Code Data:")
# for code in unique_qr_codes:
#     print(code)
