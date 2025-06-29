
# 🎙️ VoiceBuddy-AI-Assistant

VoiceBuddy is a beginner-friendly Python-based desktop voice assistant that listens to your voice commands and performs tasks like web search, opening apps, fetching current time, and Wikipedia summaries.

---

## 🚀 Features

- 🎤 Speech recognition from microphone
- 🗣️ Text-to-speech using `pyttsx3`
- 🌐 Opens websites: Google, YouTube, Music, News
- 📖 Wikipedia search and summarization
- 🕒 Tells current time
- 📄 Opens Microsoft Word (Windows)
- 🎵 Plays your favorite song

---

## 🛠️ Technologies Used

- `Python 3.10+`
- `pyttsx3` – text-to-speech
- `speech_recognition` – voice input
- `wikipedia` – fetch summaries
- `webbrowser`, `datetime`, `os` – core modules
- `comtypes.client` – for Windows automation (if needed)
- 🎯 Optional: Django imports (currently unused in logic)

---

## 📦 Installation

1. **Clone this repository**

```bash
git clone https://github.com/your-username/VoiceBuddy-AI-Assistant.git
cd VoiceBuddy-AI-Assistant
```

2. **Install required Python libraries**

```bash
pip install pyttsx3 SpeechRecognition wikipedia comtypes
```

> ⚠️ For `pyttsx3`, use `sapi5` engine on Windows. Ensure your microphone is working.

3. **Run the assistant**

```bash
python VoiceBuddy.py
```

---

## 🧠 How It Works

- VoiceBuddy greets the user based on time.
- It listens for voice input using the microphone.
- Recognizes spoken commands like:
  - “Search *topic* on Wikipedia”
  - “Open YouTube”
  - “Tell me the time”
  - “Open Microsoft Word”
- Performs actions based on recognized keywords.

---

## 📌 Example Commands

- `open google`
- `wikipedia elon musk`
- `time`
- `favourite song`
- `open word`

---

## 🖥️ Windows Specific

- Ensure MS Word path is correct:
  ```python
  os.startfile("C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
  ```
- Update the path if you're using a different Office version.

---

---

## 🧑‍💻 Author

Build by **Logeswar** 

---

