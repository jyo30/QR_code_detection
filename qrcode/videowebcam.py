# import cv2
# from pyzbar import pyzbar

# import json

# def decode_qr_code(image):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Find QR codes in the image
#     qr_codes = pyzbar.decode(gray)

#     # Loop over detected QR codes
#     for qr_code in qr_codes:
#         # Extract the data from the QR code
#         data = qr_code.data.decode("utf-8")
#         print("QR Code Data:", data)

#         # Check if the data is in JSON format
#         try:
#             json_data = json.loads(data)
#             print("Decoded JSON data:", json_data)
#         except json.JSONDecodeError:
#             pass

#         # Draw a bounding box around the QR code
#         (x, y, w, h) = qr_code.rect
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         # Draw the QR code data on the image
#         cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # Display the image with bounding boxes and data
#     cv2.imshow("QR Code Scanner", image)

# # Initialize the webcam
# cap = cv2.VideoCapture(0)

# # Check if the webcam is successfully opened
# if not cap.isOpened():
#     print("Failed to open webcam")
#     exit()

# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()

#     # If the frame was not successfully read, exit the loop
#     if not ret:
#         break

#     # Decode the QR code from the frame
#     decode_qr_code(frame)

#     # Check for 'q' key press to exit the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# cap.release()
# cv2.destroyAllWindows()






###########################detecting qr codes from a video######################
# import cv2
# from pyzbar import pyzbar

# import json

# detected_data = []  # Create a list to store the detected data

# def decode_qr_code(image):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Find QR codes in the image
#     qr_codes = pyzbar.decode(gray)

#     # Loop over detected QR codes
#     for qr_code in qr_codes:
#         # Extract the data from the QR code
#         data = qr_code.data.decode("utf-8")
#         print("QR Code Data:", data)

#         # Check if the data is in JSON format
#         try:
#             json_data = json.loads(data)
#             print("Decoded JSON data:", json_data)
#             detected_data.append(json_data)  # Append the decoded data to the list
#         except json.JSONDecodeError:
#             pass

#         # Draw a bounding box around the QR code
#         (x, y, w, h) = qr_code.rect
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         # Draw the QR code data on the image
#         cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # Display the image with bounding boxes and data
#     cv2.imshow("QR Code Scanner", image)


# # Initialize the webcam
# cap = cv2.VideoCapture(0)

# # Check if the webcam is successfully opened
# if not cap.isOpened():
#     print("Failed to open webcam")
#     exit()

# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()

#     # If the frame was not successfully read, exit the loop
#     if not ret:
#         break

#     # Decode the QR code from the frame
#     decode_qr_code(frame)

#     # Check for 'q' key press to exit the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# cap.release()
# cv2.destroyAllWindows()









#############################webcam detecting video without repetation###############
# import cv2
# from pyzbar import pyzbar
# import warnings 
# warnings.filterwarnings('ignore')
# import json

# detected_data = set()  # Create a set to store the detected data

# def decode_qr_code(image):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Find QR codes in the image
#     qr_codes = pyzbar.decode(gray)

#     # Loop over detected QR codes
#     for qr_code in qr_codes:
#         # Extract the data from the QR code
#         data = qr_code.data.decode("utf-8")

#         # Check if the data is already detected
#         if data in detected_data:
#             continue  # Skip if the data is a duplicate

#         # Add the data to the detected set
#         detected_data.add(data)

#         print("QR Code Data:", data)

#         # Check if the data is in JSON format
#         try:
#             json_data = json.loads(data)
#             print("Decoded JSON data:", json_data)
#         except json.JSONDecodeError:
#             pass

#         # Draw a bounding box around the QR code
#         (x, y, w, h) = qr_code.rect
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         # Draw the QR code data on the image
#         cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # Display the image with bounding boxes and data
#     cv2.imshow("QR Code Scanner", image)

# # Initialize the webcam
# cap = cv2.VideoCapture(0)

# # Check if the webcam is successfully opened
# if not cap.isOpened():
#     print("Failed to open webcam")
#     exit()

# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()

#     # If the frame was not successfully read, exit the loop
#     if not ret:
#         break

#     # Decode the QR code from the frame
#     decode_qr_code(frame)

#     # Check for 'q' key press to exit the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# cap.release()
# cv2.destroyAllWindows()






###################webcam video detection with exceptional handling###########
import cv2
from pyzbar import pyzbar
import warnings
import json

detected_data = set()  # Create a set to store the detected data

def decode_qr_code(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find QR codes in the image
    qr_codes = pyzbar.decode(gray)

    #print(len(qr_codes))

    # Loop over detected QR codes
    for qr_code in qr_codes:
        # Extract the data from the QR code
        data = qr_code.data.decode("utf-8")

        # Check if the data is already detected
        if data in detected_data:
            continue  # Skip if the data is a duplicate

        # Add the data to the detected set
        detected_data.add(data)

        print("QR Code Data:", data)

        # Check if the data is in JSON format
        try:
            json_data = json.loads(data)
            print("Decoded JSON data:", json_data)
        except json.JSONDecodeError as e:
            print("Failed to decode JSON data:", e)

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

warnings.filterwarnings("ignore", category=UserWarning)  # Ignore UserWarnings



while True:
    # Read frames from the video (webcam)

    ret, frame = cap.read()

    # If the frame was not successfully read, exit the loop
    if not ret:
        break

    # Verify and Decode the QR code from the frame
    try:
        decode_qr_code(frame)
    except AssertionError as e:
        print("AssertionError occurred:", e)
    except Exception as e:
        print("An error occurred:", e)
    
    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()







############################barcode and qrcode#################
# import cv2
# from pyzbar import pyzbar
# import warnings
# import json

# detected_data = set()

# def decode_code(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     codes = pyzbar.decode(gray)
    
#     for code in codes:
#         data = code.data.decode("utf-8")
        
#         if data in detected_data:
#             continue
        
#         detected_data.add(data)
        
#         print("Code Data:", data)
        
#         try:
#             json_data = json.loads(data)
#             print("Decoded JSON data:", json_data)
#         except json.JSONDecodeError as e:
#             print("Failed to decode JSON data:", e)
        
#         (x, y, w, h) = code.rect
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
#     cv2.imshow("Code Scanner", image)

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Failed to open webcam")
#     exit()

# warnings.filterwarnings("ignore", category=UserWarning)

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     try:
#         decode_code(frame)
#     except AssertionError as e:
#         print("AssertionError occurred:", e)
#     except Exception as e:
#         print("An error occurred:", e)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
# cap.release()
# cv2.destroyAllWindows()
