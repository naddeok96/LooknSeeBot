# This script will experiment with YOLO using OpenCV #
#----------------------------------------------------#

# Imports
import cv2

# Initialize Cam and Window
cam = cv2.VideoCapture(0)
cv2.namedWindow("Look n' See")

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Watch
for _ in range(1):
    ret, frame = cam.read()

    if not ret: 
        print("Failed to grab frame.")
        break

    # Convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow("Look n' See", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
    

