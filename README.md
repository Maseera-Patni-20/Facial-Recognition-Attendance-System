<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

  <h1>Face Recognition Attendance System</h1>

  <p>This project implements a real-time face recognition attendance system using Python and popular libraries like OpenCV and face_recognition. The system captures faces through a webcam feed, recognizes them against a database of known faces, and marks their attendance by logging the timestamp in a CSV file.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>Real-time Face Recognition:</strong> Uses OpenCV and face_recognition to detect and recognize faces in real-time from a webcam feed.</li>
    <li><strong>Attendance Logging:</strong> Records the attendance of recognized individuals by writing their names and timestamp to a CSV file (<code>Attendance.csv</code>).</li>
    <li><strong>Duplicate Entry Prevention:</strong> Implements a cooldown period to prevent duplicate attendance entries within a specified time interval.</li>
    <li><strong>Easy Setup and Usage:</strong> Simply run the Python script with images of individuals placed in the <code>ImagesAttendance</code> folder to begin marking attendance.</li>
  </ul>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>OpenCV (<code>opencv-python</code>)</li>
    <li>NumPy (<code>numpy</code>)</li>
    <li>face_recognition (<code>face-recognition</code>)</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository:</li>
    <pre><code>git clone https://github.com/your_username/face-recognition-attendance.git
cd face-recognition-attendance</code></pre>
    <li>Install the required Python packages:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
  </ol>

  <h2>Usage</h2>
  <ul>
    <li>Place images of individuals in the <code>ImagesAttendance</code> folder. Ensure each image file name corresponds to the name of the person.</li>
    <li>Run the script:</li>
    <pre><code>python attendance.py</code></pre>
    <p>A window will open showing the webcam feed. Faces recognized from the feed will have their attendance marked in real-time. Press <code>q</code> to exit the program.</p>
  </ul>

  <h2>Contributing</h2>
  <p>Contributions are welcome! Please fork the repository and submit pull requests or create issues for bugs, feature requests, or questions.</p>

</body>
</html>
