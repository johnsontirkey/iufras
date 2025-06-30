# 🚀 IU Facial Recognition Attendance System (I.U.F.R.A.S )
I.U.F.R.A.S is a Python‑based facial-recognition attendance tracking system featuring a full web interface. It leverages OpenCV, Haar Cascade, and lightweight ML techniques to detect and recognize faces, faithfully logging attendance.

## 🔍 Key Features
#### Facial Detection & Recognition – Implemented via OpenCV + Haar Cascade classifier.

#### Attendance Recording – Logs recognized faces with timestamps into CSV for tracking.

#### User Registration – Add new users via webcam, automatically capturing face data.

#### Login Module – Authenticate users using facial verification.

#### Modular Architecture – Separate scripts for training, face logic, registration, and UI.

#### Pure-Python Implementation – Easy to deploy locally or on-prem web servers.

## 🧱 Tech Stack
#### Python – Core scripting language

#### OpenCV – Real-time image processing + face detection

#### Haar Cascade – Pre-trained XML classifier for face localization

#### CSV – Attendance data storage (johnson.csv)

#### Modular Scripts – Includes main.py, attendance.py, register.py, train.py, etc.

## 📁 Project Structure

| **File/Folder**                       | **Purpose**                                       |
| ------------------------------------- | ------------------------------------------------- |
| `main.py`                             | Entry point; launches the control panel GUI       |
| `register.py`                         | Captures user images and stores them in folders   |
| `train.py`                            | Trains the model and generates `classifier.xml`   |
| `face_recognition.py`                 | Real-time face detection and recognition logic    |
| `attendance.py`                       | Handles attendance logging to `johnson.csv`       |
| `login.py`                            | Handles face-based login authentication           |
| `college_images/`                     | Stores face datasets per user                     |
| `johnson.csv`                         | Output CSV file for attendance data               |
| `haarcascade_frontalface_default.xml` | Pre-trained Haar Cascade model for face detection |
| `classifier.xml`                      | Trained model for face recognition                |

* The classifier.xml is generated from train.py using stored face images.

## ⚙️ How It Works
#### Register Users – Run register.py to capture face data for each new user.

#### Train Model – Run train.py to produce the classifier.xml via LBPH/other ML technique.

#### Launch System – Run main.py, which handles face detection in real time.

#### Preserve Attendance – On successful recognition, attendance is appended to the CSV file.

#### Manage Users – The modular structure allows easy user additions and maintenance.

## 🛠️ Getting Started
#### Clone Repository
```bash
git clone https://github.com/johnsontirkey/iufras.git
cd iufras
```
#### Install Dependencies
```bash
pip install opencv-python
```
#### Register a User
```bash
python register.py
```
#### Train the Model
```bash
python train.py
```
#### Start the App
```bash
python main.py
```
#### Check Attendance
Open johnson.csv to review logged entries with timestamps.

## 🔧 Use Cases
#### Perfect for:
- Classroom attendance tracking for small-to-medium institutions
- Workplace employee check-in/out via facial recognition
- Secure lab or facility entry with identity verification

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

