import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime, timedelta

# Path to the directory containing images for attendance
path = 'ImagesAttendance'

# Initialize empty lists to store images and corresponding class names
images = []
classNames = []

# Get list of all files (images) in the specified directory
myList = os.listdir(path)
print(myList)

# Loop through all images in the directory
for cl in myList:
    # Read each image
    curImg = cv2.imread(f'{path}/{cl}')
    # Append image to images list
    images.append(curImg)
    # Extract class name (filename without extension) and append to classNames list
    classNames.append(os.path.splitext(cl)[0])

print(classNames)

# Function to find encodings (face embeddings) for all images
def findEncodings(images):
    encodeList = []
    for img in images:
        # Convert image from BGR to RGB (required by face_recognition library)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Find face encodings for all faces in the image
        encode = face_recognition.face_encodings(img)[0]
        # Append face encodings to encodeList
        encodeList.append(encode)
    return encodeList

# Initialize a cooldown time for marking attendance to prevent rapid marking
cooldown_time = timedelta(seconds=30)
# Dictionary to keep track of the last attendance marking time for each person
last_attendance_time = {}

# Function to mark attendance for a person
def markAttendance(name):
    global last_attendance_time
    
    now = datetime.now()
    
    # Check if this person was recently marked within the cooldown period
    if name in last_attendance_time and (now - last_attendance_time[name]) < cooldown_time:
        print(f"{name} attendance already marked recently.")
        return
    
    # Update the attendance marking time for this person
    last_attendance_time[name] = now
    
    # Write attendance data to a CSV file
    with open('Attendance.csv', 'a') as f:
        dtString = now.strftime('%H:%M:%S')
        f.write(f'{name},{dtString}\n')
        print(f"Attendance marked for {name} at {dtString}")

# Find encodings (face embeddings) for all known images
encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Initialize video capture from webcam (index 0)
cap = cv2.VideoCapture(0)

# Main loop to capture frames from the webcam
while True:
    # Read a frame from the video capture
    success, img = cap.read()
    # Resize frame to 1/4 size for faster processing
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    # Convert frame from BGR to RGB
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find face locations in the current frame
    facesCurFrame = face_recognition.face_locations(imgS)
    # Encode (find embeddings) for all faces found in the current frame
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    # Iterate through all detected faces in the current frame
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        # Compare the current face encoding with the known encodings
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        # Calculate face distances to find the best match
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # Find the index of the best match (minimum distance)
        matchIndex = np.argmin(faceDis)

        # If a match is found with sufficient confidence
        if matches[matchIndex]:
            # Get the name corresponding to the matched face
            name = classNames[matchIndex].upper()
            # Extract face location coordinates
            y1, x2, y2, x1 = faceLoc
            # Scale up the face coordinates (since we resized the frame to 1/4)
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            # Draw a rectangle around the face
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Draw a filled rectangle for the name label
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            # Put text with the name on the image
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            # Mark attendance for this person
            markAttendance(name)

    # Display the processed image with rectangles and names
    cv2.imshow('Webcam', img)
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
