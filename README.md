# 🔬 MeetingAutopsy AI — Meeting Intelligence & Speech Transcription

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)
[![UI: Modern Dark/Light](https://img.shields.io/badge/UI-Glassmorphism-emerald.svg)]()

> **Dissect your meeting's DNA** — Upload any meeting audio or video recording to get high-accuracy speech transcription, meeting health scores, key decisions, action items, speaker breakdowns, timeline milestones, and an interactive Q&A assistant.

---

## ✨ Features

- 🎙️ **Real Speech-to-Text Transcription**: Local audio extraction via `ffmpeg` + multi-segment speech recognition with >85% accuracy (supports English, Hindi/Hinglish, and global accents).
- ⚡ **Zero Mandatory Cloud Costs**: Fully functional local Python AI engine without requiring paid external API keys.
- 🌐 **Optional Gemini Cloud Integration**: Easily connect a Google Gemini API key if you want cloud multimodal reasoning.
- 📊 **Meeting Health Score**: Automatic scoring (0-100) based on clarity, participation, sentiment, and decision density.
- 🎯 **Key Decisions & Action Items**: Auto-extracted takeaways with owners, deadlines, and priorities.
- 📅 **Interactive Timeline**: Timestamped milestone breadcrumbs mapping out presentation flow.
- 💬 **Interactive Meeting Q&A**: Ask questions about the meeting ("Who spoke?", "What was decided?", "Summarize points") with grounded answers.
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
├── meeting_analyzer.py     # Speech-to-text, sentiment & semantic analysis engine
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
