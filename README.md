# Real-Time Crowd Monitoring

## 📌 Project Overview
The **Real-Time Crowd Monitoring System** is an AI-powered solution that uses computer vision and deep learning to analyze live or recorded video feeds.  
It detects people in real time, tracks movement patterns, estimates crowd density, and triggers alerts when overcrowding conditions occur.  

This system can be used for **public safety monitoring, event management, and smart surveillance applications**.

---

## 🚀 Features
- **Real-Time Person Detection**: Uses YOLOv5 to detect people in video streams.
- **Crowd Counting**: Tracks and counts people present in the monitored area.
- **Overcrowding Alert System**: Triggers alerts when crowd size exceeds a threshold.
- **Object Tracking**: Tracks individuals using a lightweight tracking algorithm.
- **Flask Web Dashboard**: Displays real-time video stream and crowd analytics.
- **Face Recognition (Optional)**: Expandable module to identify known individuals.

---

## 🛠️ Tech Stack
- **Backend**: Flask (for web interface and video streaming)
- **Machine Learning**: YOLOv5 (PyTorch)
- **Libraries**: OpenCV, NumPy
- **Frontend Visualization**: Chart.js
- **Styling**: TailwindCSS

---

## 📂 Project Structure
```bash
crowd-monitoring-system
│
├── modules/ # Core detection and tracking modules
│ ├── config.py
│ ├── crowd_detection.py
│ ├── tracker.py
│ └── face_recog.py
│
├── photos/ # Images used for face recognition
├── static/ # Static assets for the web UI
├── templates/ # HTML templates for Flask
├── test_videos/ # Sample videos for testing
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
└── README.md
```
---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SIMPLESOMEONE1202/crowd-monitoring-system.git
cd crowd-monitoring-system
```

## Future Improvements

- Face recognition integration
- Multi-camera support
- Crowd density heatmaps

## License

Educational and research purposes.