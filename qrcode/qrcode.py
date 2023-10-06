
#####################image code ####################

# import cv2
# from pyzbar import pyzbar
# import os

# def detect_and_save_qr_code(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Detect and decode QR codes
#     qr_codes = pyzbar.decode(gray)

#     # Iterate through the detected QR codes
#     qr_code_found = False
#     for qr_code in qr_codes:
#         qr_data = qr_code.data.decode("utf-8")

#         # Save the QR code as an image
#         (x, y, w, h) = qr_code.rect
#         qr_image = image[y:y + h, x:x + w]
#         output_path = os.path.join(os.getcwd(), "QRCode_ArticleImage31.jpg")
#         cv2.imwrite(output_path, qr_image)
#         qr_code_found = True
#         break

#     if qr_code_found:
#         print("QR code saved successfully.")
#     else:
#         print("No QR code found in the image.")

# # Usage example
# image_path = 'QRCode_ArticleImage3.jpg'

# detect_and_save_qr_code(image_path)











# import cv2

# # Path to the input video file
# video_path = 'istockphoto-1371369676-640_adpp_is.mp4'

# # Create a VideoCapture object
# cap = cv2.VideoCapture(video_path)

# # Define the output video path
# output_path = 'output/video_with_annotations.mp4'

# # Get the video's frame rate and dimensions
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec for the output video
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# # Create a QR code detector
# qr_detector = cv2.QRCodeDetector()

# # Read and process each frame of the video
# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect QR codes in the grayscale frame
#     decoded_info, _, _ = qr_detector.detectAndDecode(gray)

#     # Iterate over detected QR codes and annotate them
#     if isinstance(decoded_info, str):
#         # Split multiple QR codes if they are delimited by commas
#         qr_codes = decoded_info.split(',')

#         for qr_code in qr_codes:
#             # Find the QR code location
#             _, points, _ = qr_detector.detectAndDecode(gray)

#             # Draw bounding box around the QR code
#             if points is not None and len(points) > 0:
#                 pts = points[0].astype(int)
#                 cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

#                 # Optional: Add QR code data as text
#                 cv2.putText(frame, qr_code, (pts[0][0], pts[0][1] - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#     # Write the annotated frame to the output video
#     out.write(frame)

#     # Display the annotated frame (optional)
#     cv2.imshow('Annotated Video', frame)

#     # Exit if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the VideoCapture and VideoWriter objects
# cap.release()
# out.release()

# # Close all OpenCV windows
# cv2.destroyAllWindows()



#####################video highlighting##############
# import cv2

# # Path to the input video file
# video_path = 'istockphoto-1371369676-640_adpp_is_AdobeExpress.mp4'

# # Create a VideoCapture object
# cap = cv2.VideoCapture(video_path)

# # Define the output video path
# output_path = 'output/video_with_annotations.mp4'

# # Get the video's frame rate and dimensions
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec for the output video
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# # Create a QR code detector
# qr_detector = cv2.QRCodeDetector()

# # Read and process each frame of the video
# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect QR codes in the grayscale frame
#     decoded_info, _, _ = qr_detector.detectAndDecode(gray)

#     # Iterate over detected QR codes and annotate them
#     if isinstance(decoded_info, str):
#         # Split multiple QR codes if they are delimited by commas
#         qr_codes = decoded_info.split(',')

#         for qr_code in qr_codes:
#             # Find the QR code location
#             _, points, _ = qr_detector.detectAndDecode(gray)

#             # Draw bounding box around the QR code
#             if points is not None and len(points) > 0:
#                 x, y, w, h = cv2.boundingRect(points)
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#                 # Optional: Add QR code data as text
#                 cv2.putText(frame, qr_code, (x, y - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#     # Write the annotated frame to the output video
#     out.write(frame)

#     # Display the annotated frame (optional)
#     cv2.imshow('Annotated Video', frame)

#     # Exit if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the VideoCapture and VideoWriter objects
# cap.release()
# out.release()

# # Close all OpenCV windows
# cv2.destroyAllWindows()







# import cv2

# def detect_qr_codes(video_path, output_path):
#     # Create a VideoCapture object
#     cap = cv2.VideoCapture(video_path)

#     # Get the video's frame rate and dimensions
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     # Create a QR code detector
#     qr_detector = cv2.QRCodeDetector()

#     # Define the codec for the output video
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

#     # Process each frame of the video
#     frame_count = 0
#     while cap.isOpened():
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detect QR codes in the grayscale frame
#         _, decoded_info, _ = qr_detector.detectAndDecode(gray)

#         # Iterate over detected QR codes and annotate them
#         if decoded_info is not None:
#             for qr_code in decoded_info:
#                 # Draw bounding box around the QR code
#                 cv2.putText(frame, qr_code, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#         # Write the frame to the output video
#         out.write(frame)

#         # Display the frame (optional)
#         cv2.imshow('Video Frame', frame)

#         # Save the frame as an image (optional)
#         cv2.imwrite(f'frame_{frame_count}.jpg', frame)
#         frame_count += 1

#         # Exit if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the VideoCapture and VideoWriter objects
#     cap.release()
#     out.release()

#     # Close all OpenCV windows
#     cv2.destroyAllWindows()

# # Path to your input video file
# video_path = 'istockphoto-1371369676-640_adpp_is_AdobeExpress.mp4'

# # Define the output video path
# output_path = 'output/video_with_annotations.mp4'

# # Call the function to detect and annotate QR codes in the video
# detect_qr_codes(video_path, output_path)






#####################frames###########
# import cv2
# import os
# def save_frames(video_path, output_folder):
#     # Create a VideoCapture object
#     cap = cv2.VideoCapture(video_path)

#     # Create the output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)

#     # Process each frame of the video
#     frame_count = 0
#     while cap.isOpened():
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Save the frame as an image
#         frame_path = os.path.join(output_folder, f'frame_{frame_count}.jpg')
#         cv2.imwrite(frame_path, frame)

#         frame_count += 1

#     # Release the VideoCapture object
#     cap.release()

#     print(f"Saved {frame_count} frames in {output_folder}.")

# # Path to your input video file
# video_path = 'istockphoto-1371369676-640_adpp_is.mp4'

# # Define the output folder path
# output_folder = 'output/frames/'

# # Call the function to convert the video into frames
# save_frames(video_path, output_folder)














# import cv2

# # Path to the input video file
# video_path = 'istockphoto-1371369676-640_adpp_is_AdobeExpress.mp4'

# # Create a VideoCapture object
# cap = cv2.VideoCapture(video_path)

# # Define the output video path
# output_path = 'output/video_with_annotations.mp4'

# # Get the video's frame rate and dimensions
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec for the output video
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# # Create a QR code detector
# qr_detector = cv2.QRCodeDetector()

# # Read and process each frame of the video
# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect QR codes in the grayscale frame
#     decoded_info, _, _ = qr_detector.detectAndDecode(gray)

#     # Iterate over detected QR codes and annotate them
#     if isinstance(decoded_info, str):
#         # Split multiple QR codes if they are delimited by commas
#         qr_codes = decoded_info.split(',')

#         for qr_code in qr_codes:
#             # Find the QR code location
#             _, points, _ = qr_detector.detectAndDecode(gray)

#             # Draw bounding box around the QR code
#             if points is not None and len(points) > 0:
#                 x, y, w, h = cv2.boundingRect(points)
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#                 # Optional: Add QR code data as text
#                 cv2.putText(frame, qr_code, (x, y - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#     # Write the annotated frame to the output video
#     out.write(frame)

#     # Display the annotated frame (optional)
#     cv2.imshow('Annotated Video', frame)

#     # Exit if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the VideoCapture and VideoWriter objects
# cap.release()
# out.release()

# # Close all OpenCV windows
# cv2.destroyAllWindows()



################################highlighting qrcode in a video##################33
# import cv2

# # Path to the input video file
# video_path = 'istockphoto-1371369676-640_adpp_is_AdobeExpress.mp4'

# # Create a VideoCapture object
# cap = cv2.VideoCapture(video_path)

# # Define the output video path
# output_path = 'output/video_with_annotations.mp4'

# # Get the video's frame rate and dimensions
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec for the output video
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# # Create a QR code detector
# qr_detector = cv2.QRCodeDetector()

# # Read and process each frame of the video
# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect QR codes in the grayscale frame
#     decoded_info, _, _ = qr_detector.detectAndDecode(gray)

#     # Iterate over detected QR codes and annotate them
#     if isinstance(decoded_info, str):
#         # Split multiple QR codes if they are delimited by commas
#         qr_codes = decoded_info.split(',')

#         for qr_code in qr_codes:
#             # Find the QR code location
#             _, points, _ = qr_detector.detectAndDecode(gray)

#             # Draw bounding box around the QR code
#             if points is not None and len(points) > 0:
#                 x, y, w, h = cv2.boundingRect(points)

#                 # Draw bounding box and add QR code data as text
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 cv2.putText(frame, qr_code, (x, y - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#     # Write the annotated frame to the output video
#     out.write(frame)

#     # Display the annotated frame (optional)
#     cv2.imshow('Annotated Video', frame)

#     # Exit if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the VideoCapture and VideoWriter objects
# cap.release()
# out.release()

# # Close all OpenCV windows
# cv2.destroyAllWindows()




###################saving single image of a highlighted video####################
# import cv2
# import os

# # Path to the input video file
# video_path = 'istockphoto-1441217402-640_adpp_is.mp4'

# # Create a VideoCapture object
# cap = cv2.VideoCapture(video_path)

# # Define the output video path
# output_path = 'output/video_with_annotations.mp4'

# # Define the output folder for captured images
# output_folder = 'highlighted_images'
# os.makedirs(output_folder, exist_ok=True)

# # Get the video's frame rate and dimensions
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec for the output video
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# # Create a QR code detector
# qr_detector = cv2.QRCodeDetector()

# # Read and process each frame of the video
# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect QR codes in the grayscale frame
#     decoded_info, _, _ = qr_detector.detectAndDecode(gray)

#     # Iterate over detected QR codes and annotate them
#     if isinstance(decoded_info, str):
#         # Split multiple QR codes if they are delimited by commas
#         qr_codes = decoded_info.split(',')

#         for qr_code in qr_codes:
#             # Find the QR code location
#             _, points, _ = qr_detector.detectAndDecode(gray)

#             # Draw bounding box around the QR code
#             if points is not None and len(points) > 0:
#                 x, y, w, h = cv2.boundingRect(points)

#                 # Draw bounding box and add QR code data as text
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 cv2.putText(frame, qr_code, (x, y - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#                 # Capture the highlighted part of the frame if it is within the frame boundaries
#                 if 0 <= y < height and 0 <= x < width and y + h <= height and x + w <= width:
#                     highlighted_image = frame[y:y + h, x:x + w]

#                     # Save the captured image to the output folder
#                     image_path = os.path.join(output_folder, f'highlighted_image_{qr_code}.jpg')
#                     cv2.imwrite(image_path, highlighted_image)

#     # Write the annotated frame to the output video
#     out.write(frame)

#     # Display the annotated frame (optional)
#     cv2.imshow('Annotated Video', frame)

#     # Exit if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the VideoCapture and VideoWriter objects
# cap.release()
# out.release()

# # Close all OpenCV windows
# cv2.destroyAllWindows()






##########################highlighting qr code##########

# import tkinter as tk
# from tkinter import filedialog
# import cv2
# import os

# # Function to detect and annotate QR codes in a video
# def detect_and_annotate_qr_codes(video_path):
#     # Create a VideoCapture object
#     cap = cv2.VideoCapture(video_path)

#     # Define the output video path
#     output_path = 'output/video_with_annotations.mp4'

#     # Define the output folder for captured images
#     output_folder = 'highlighted_images'
#     os.makedirs(output_folder, exist_ok=True)

#     # Get the video's frame rate and dimensions
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     # Define the codec for the output video
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

#     # Create a QR code detector
#     qr_detector = cv2.QRCodeDetector()

#     # Set to store unique QR code data
#     unique_qr_codes = set()

#     # Read and process each frame of the video
#     while cap.isOpened():
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detect QR codes in the grayscale frame
#         decoded_info, _, _ = qr_detector.detectAndDecode(gray)

#         # Iterate over detected QR codes and annotate them
#         if isinstance(decoded_info, str):
#             # Split multiple QR codes if they are delimited by commas
#             qr_codes = decoded_info.split(',')

#             for qr_code in qr_codes:
#                 # Find the QR code location
#                 _, points, _ = qr_detector.detectAndDecode(gray)

#                 # Draw bounding box around the QR code
#                 if points is not None and len(points) > 0:
#                     x, y, w, h = cv2.boundingRect(points)

#                     # Draw bounding box and add QR code data as text
#                     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                     cv2.putText(frame, qr_code, (x, y - 10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#                     # Capture the highlighted part of the frame if it is within the frame boundaries
#                     if 0 <= y < height and 0 <= x < width and y + h <= height and x + w <= width:
#                         highlighted_image = frame[y:y + h, x:x + w]

#                         # Save the captured image to the output folder
#                         image_path = os.path.join(output_folder, f'highlighted_image_{qr_code}.jpg')
#                         cv2.imwrite(image_path, highlighted_image)

#                         # Add the QR code data to the set of unique codes
#                         unique_qr_codes.add(qr_code)

#         # Write the annotated frame to the output video
#         out.write(frame)

#         # Display the annotated frame (optional)
#         cv2.imshow('Annotated Video', frame)

#         # Exit if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the VideoCapture and VideoWriter objects
#     cap.release()
#     out.release()

#     # Close all OpenCV windows
#     cv2.destroyAllWindows()

#     # Print the unique QR code data
#     print("Unique QR Code Data:")
#     for code in unique_qr_codes:
#         print(code)

# # Function to handle the video selection
# def select_video():
#     # Show a file dialog to select a video file
#     file_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4;*.avi;*.mov')])

#     # Check if a file was selected
#     if file_path:
#         print(f"Selected video: {file_path}")
#         detect_and_annotate_qr_codes(file_path)

# # Create the main window
# window = tk.Tk()

# # Set the window title
# window.title("Video QR Code Detection")

# # Create a button to select a video
# select_button = tk.Button(window, text="Select Video", command=select_video)
# select_button.pack(pady=20)

# # Start the GUI main loop
# window.mainloop()




###################################qr code scanning data repeating##########
# import tkinter as tk
# from tkinter import filedialog
# import cv2
# import os

# # Function to detect and annotate QR codes in a video
# def detect_and_annotate_qr_codes(video_path):
#     # Create a VideoCapture object
#     cap = cv2.VideoCapture(video_path)

#     # Get the video's frame rate and dimensions
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     # Create a QR code detector
#     qr_detector = cv2.QRCodeDetector()

#     # Read and process each frame of the video
#     while cap.isOpened():
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detect QR codes in the grayscale frame
#         decoded_info, _, _ = qr_detector.detectAndDecode(gray)

#         # Iterate over detected QR codes and print their data
#         if isinstance(decoded_info, str):
#             # Split multiple QR codes if they are delimited by commas
#             qr_codes = decoded_info.split(',')

#             for qr_code in qr_codes:
#                 print(qr_code)

#         # Display the frame (optional)
#         cv2.imshow('Video', frame)

#         # Exit if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the VideoCapture object
#     cap.release()

#     # Close all OpenCV windows
#     cv2.destroyAllWindows()

# # Function to handle the video selection
# def select_video():
#     # Show a file dialog to select a video file
#     file_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4;*.avi;*.mov')])

#     # Check if a file was selected
#     if file_path:
#         print(f"Selected video: {file_path}")
#         detect_and_annotate_qr_codes(file_path)

# # Create the main window
# window = tk.Tk()

# # Set the window title
# window.title("Video QR Code Detection")

# # Create a button to select a video
# select_button = tk.Button(window, text="Select Video", command=select_video)
# select_button.pack(pady=20)

# # Start the GUI main loop
# window.mainloop()





################qr code scanning and data repetion####
# import tkinter as tk
# from tkinter import filedialog
# import cv2
# import os

# # Function to detect and annotate QR codes in a video
# def detect_and_annotate_qr_codes(video_path):
#     # Create a VideoCapture object
#     cap = cv2.VideoCapture(video_path)

#     # Get the video's frame rate and dimensions
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     # Create a QR code detector
#     qr_detector = cv2.QRCodeDetector()

#     # Set to store unique QR code data
#     unique_qr_codes = set()

#     # Variable to store the previously detected QR code
#     prev_qr_code = None

#     # Read and process each frame of the video
#     while cap.isOpened():
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detect QR codes in the grayscale frame
#         decoded_info, _, _ = qr_detector.detectAndDecode(gray)

#         # Iterate over detected QR codes and print their data
#         if isinstance(decoded_info, str):
#             # Split multiple QR codes if they are delimited by commas
#             qr_codes = decoded_info.split(',')

#             for qr_code in qr_codes:
#                 if qr_code != prev_qr_code:
#                     unique_qr_codes.add(qr_code)
#                     print(qr_code)

#                     # Update the previously detected QR code
#                     prev_qr_code = qr_code

#         # Display the frame (optional)
#         cv2.imshow('Video', frame)

#         # Exit if the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the VideoCapture object
#     cap.release()

#     # Close all OpenCV windows
#     cv2.destroyAllWindows()

# # Function to handle the video selection
# def select_video():
#     # Show a file dialog to select a video file
#     file_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4;*.avi;*.mov')])

#     # Check if a file was selected
#     if file_path:
#         print(f"Selected video: {file_path}")
#         detect_and_annotate_qr_codes(file_path)

# # Create the main window
# window = tk.Tk()

# # Set the window title
# window.title("Video QR Code Detection")

# # Create a button to select a video
# select_button = tk.Button(window, text="Select Video", command=select_video)
# select_button.pack(pady=20)

# # Start the GUI main loop
# window.mainloop()


 




#########################data without repetition######################
import tkinter as tk
from tkinter import filedialog
import cv2

# Function to detect and annotate QR codes in a video
def detect_and_annotate_qr_codes(video_path):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(video_path)

    # Create a QR code detector
    qr_detector = cv2.QRCodeDetector()

    # Set to store unique QR code data
    unique_qr_codes = set()

    # Read and process each frame of the video
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect QR codes in the grayscale frame
        decoded_info, _, _ = qr_detector.detectAndDecode(gray)

        # Print the QR code data if it is detected and not a duplicate
        if isinstance(decoded_info, str) and decoded_info not in unique_qr_codes:
            print(decoded_info)

            # Add the QR code data to the set
            unique_qr_codes.add(decoded_info)

        # Display the frame (optional)
        cv2.imshow('Video', frame)

        # Exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Function to handle the video selection
def select_video():
    # Show a file dialog to select a video file
    file_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4;*.avi;*.mov')])

    # Check if a file was selected
    if file_path:
        print(f"Selected video: {file_path}")
        detect_and_annotate_qr_codes(file_path)

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Video QR Code Detection")

# Create a button to select a video
select_button = tk.Button(window, text="Select Video", command=select_video)
select_button.pack(pady=20)

# Start the GUI main loop
window.mainloop()






