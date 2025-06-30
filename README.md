🚀 IU Facial Recognition Attendance System (I.U.F.R.A.S )
I.U.F.R.A.S is a Python‑based facial-recognition attendance tracking system featuring a full web interface. It leverages OpenCV, Haar Cascade, and lightweight ML techniques to detect and recognize faces, faithfully logging attendance.

🔍 Key Features
Facial Detection & Recognition – Implemented via OpenCV + Haar Cascade classifier.

Attendance Recording – Logs recognized faces with timestamps into CSV for tracking.

User Registration – Add new users via webcam, automatically capturing face data.

Login Module – Authenticate users using facial verification.

Modular Architecture – Separate scripts for training, face logic, registration, and UI.

Pure-Python Implementation – Easy to deploy locally or on-prem web servers.

🧱 Tech Stack
Python – Core scripting language

OpenCV – Real-time image processing + face detection

Haar Cascade – Pre-trained XML classifier for face localization

CSV – Attendance data storage (johnson.csv)

Modular Scripts – Includes main.py, attendance.py, register.py, train.py, etc.

📁 Project Structure

├── classifier.xml*              # Trained face data model
├── haarcascade_frontalface_default.xml  # Face detection classifier
├── main.py                      # Launches the web UI / control panel
├── register.py                  # Captures & stores new face images
├── train.py                     # Trains face recognition model
├── face_recognition.py          # Core detection/recognition logic
├── attendance.py                # Logs attendance on recognition
├── login.py                     # Face-based login process
├── developer.py, help.py        # Support scripts & utilities
├── johnson.csv                  # Sample attendance log file
├── college_images/              # Dataset of face samples per user
└── __pycache__/                 # Cache folder
* The classifier.xml is generated from train.py using stored face images.

⚙️ How It Works
Register Users – Run register.py to capture face data for each new user.

Train Model – Run train.py to produce the classifier.xml via LBPH/other ML technique.

Launch System – Run main.py, which handles face detection in real time.

Preserve Attendance – On successful recognition, attendance is appended to the CSV file.

Manage Users – The modular structure allows easy user additions and maintenance.

🛠️ Getting Started
Clone Repository
git clone https://github.com/johnsontirkey/iufras.git
cd iufras

Install Dependencies
pip install opencv-python

Register a User
python register.py

Train the Model
python train.py

Start the App
python main.py
Check Attendance

Open johnson.csv to review logged entries with timestamps.

🔧 Use Cases
Perfect for:

Classroom attendance tracking for small-to-medium institutions

Workplace employee check-in/out via facial recognition

Secure lab or facility entry with identity verification

✔️ To Improve/Fork:
✅ Add Flask/fastAPI frontend for a modern web UI

✅ Use a database (SQLite, MongoDB) instead of CSV

✅ Integrate more advanced face embeddings (e.g. FaceNet)

✅ Support multi-face and multi-user detection simultaneously

✅ Add manual override/admin dashboard

📩 Contact
Created by: Johnson Tirkey
Repo: https://github.com/johnsontirkey/iufras
Feel free to open issues, submit pull requests, or ask questions!

