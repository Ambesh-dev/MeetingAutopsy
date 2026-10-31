# 🔬 MeetingAutopsy AI — Meeting Intelligence & Speech Transcription

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)
[![UI: Modern Dark/Light](https://img.shields.io/badge/UI-Glassmorphism-emerald.svg)]()

> **Dissect your meeting's DNA** — Upload any meeting audio or video recording to get high-accuracy speech transcription, meeting health scores, key decisions, action items, speaker breakdowns, timeline milestones, and an interactive Q&A assistant.

---

## ✨ Features

- 👤 **Deep Neural Face Recognition & Participant Biometrics**: Powered by OpenCV YuNet (Face Detection) and SFace (Deep Neural Embeddings). Samples video frames across the timeline to detect faces, cluster identities, count exact unique video members, and generate real avatar crops.
- ⏱️ **Active Speaker Time Mapping ("Kis Time Kon Bol Raha Hai")**: Correlates speech timestamps with visible webcam/camera frames to generate an interactive timeline showing exactly which member was speaking during each interval.
- 🧠 **Intelligent Video & Content Classification**: Distinguishes between **Website / UX Reviews (Screen Recordings)**, **Technical Demos & Code Reviews**, **Solo Presentations**, **Team Meetings**, and **General Media Clips** automatically with visual frame analysis & speech NLP.
- 👤 **Accurate Solo Speaker Verification**: Fixes speaker count hallucination — if 1 person is speaking in a solo video/screen recording, it strictly identifies **1 Speaker (100% voice share)** with zero fake second speaker.
- 🌐 **Context-Adaptive Reports & Action Items**: For a Website Review screen recording, it generates UX observations, design critique, and UI/UX fix action items rather than generic corporate meeting tasks!
- 🎙️ **Real Speech-to-Text Transcription**: Local audio extraction via `ffmpeg` + multi-segment speech recognition with >85% accuracy (supports English, Hindi/Hinglish, and global accents).
- ⚡ **Zero Mandatory Cloud Costs**: Fully functional local Python AI engine without requiring paid external API keys.
- 🌐 **Optional Gemini Cloud Integration**: Easily connect a Google Gemini API key if you want cloud multimodal reasoning.
- 📊 **Contextual Health Score**: Automatic scoring (0-100) tailored to the content type (e.g. Website Usability Score vs Meeting Health Score).
- 🎯 **Key Decisions & Action Items**: Auto-extracted takeaways with owners, deadlines, and priorities.
- 📅 **Interactive Timeline**: Timestamped milestone breadcrumbs mapping out walkthrough flow.
- 💬 **Interactive Q&A Chatbot**: Ask questions about whether it's a meeting, how many people spoke, face detection, active speaker timeline, or action items in Hindi or English!
- 🎨 **Glassmorphism UI**: Sleek dark and light mode toggle, animated gradients, and responsive layout.


---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd "meeting Ai"
```

### 2. Set up Python environment
```bash
python -m venv venv

# Windows:
.\venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the local server
- **Windows (1-Click)**: Double-click `start_server.bat`
- **Or via Terminal**:
```bash
python server.py
```

Open your browser and navigate to:
```
http://localhost:8000
```


---

## 📁 Project Architecture

```
meeting-ai/
├── index.html              # Main frontend application entry point
├── am.html                 # Companion application template
├── style.css               # Glassmorphism design system & animations
├── app.js                  # Frontend controller & API bridge
├── server.py               # Local Python HTTP API server
├── meeting_analyzer.py     # Speech-to-text, classification & semantic analysis engine
├── face_tracker.py         # OpenCV YuNet & SFace face recognition & active speaker tracker
├── models/                 # Pretrained ONNX vision models (YuNet & SFace)
├── start_server.bat        # 1-click Windows server launcher
├── requirements.txt        # Python package dependencies
├── .gitignore              # Ignored files (venv, pycache, etc.)
└── README.md               # Documentation
```

---

## 🛠️ Supported Formats
- **Audio**: `.mp3`, `.wav`, `.m4a`, `.ogg`, `.aac`, `.flac`
- **Video**: `.mp4`, `.webm`, `.mov`, `.mkv`

---

## 📄 License
MIT License. Free to use, modify, and distribute.
