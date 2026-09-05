# 🎙️ Voice Notes → Action Items

A Streamlit application that converts voice notes into a clear transcript, concise summary, actionable tasks, and important dates or deadlines.

## 🚀 Live Demo

**Try the application:**  
(https://voice-notes-action-items-ksn3mm8tkk2rrxcdgjhdv8.streamlit.app/)
## 📌 Project Overview

Voice notes are often unstructured and difficult to turn into actionable information.

This project provides a simple workflow:

**Voice Note → Transcript → Summary → Action Items → Important Dates**

The application accepts either an uploaded audio file or a voice recording made directly in the browser. Gemini is used to understand the audio and generate structured information from the resulting transcript.

## ✨ Features

- Upload an audio file
- Record a voice note directly in the browser
- Convert speech to text using Gemini audio understanding
- Generate a concise summary
- Extract explicit action items
- Identify important dates, deadlines, times, and durations
- Display the transcript and generated results in a simple Streamlit interface
- Handle empty or speechless audio
- Handle transcription and AI-processing failures
- Handle Gemini API quota/rate-limit errors with a user-friendly message

## 🧠 How It Works

The application follows this pipeline:

```text
User
  ↓
Upload or Record Audio
  ↓
Gemini Audio Understanding
  ↓
Transcript
  ↓
Gemini 2.5 Flash
  ↓
Summary + Action Items + Important Dates
```

### Processing Flow

1. The user uploads an audio file or records a voice note.
2. The audio is temporarily stored for processing.
3. Gemini processes the audio and produces a transcript.
4. The transcript is passed to Gemini 2.5 Flash with a structured prompt.
5. The model generates:
   - A concise summary
   - Explicit action items
   - Important dates, deadlines, times, and durations
6. The results are displayed in the Streamlit interface.

## 🛠️ Tech Stack

- **Python 3.11**
- **Streamlit**
- **Google Gemini API**
- **google-genai**
- **python-dotenv**

## 📁 Project Structure

```text
voice-notes-action-items/
├── app.py
├── services/
│   ├── llm.py
│   └── transcription.py
├── utils/
│   └── prompts.py
├── .gitignore
├── README.md
└── requirements.txt
```

### Main Components

**`app.py`**

Contains the Streamlit user interface and coordinates the application workflow.

**`services/transcription.py`**

Handles audio processing and Gemini-based speech transcription.

**`services/llm.py`**

Sends the transcript to Gemini 2.5 Flash and generates the structured result.

**`utils/prompts.py`**

Contains the prompt used to guide the model's summary, action-item, and date extraction behavior.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/rishi4842/voice-notes-action-items.git
cd voice-notes-action-items
```

### 2. Create a virtual environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Do not commit the `.env` file or expose the API key publicly.

The `.env` file is excluded from Git using `.gitignore`.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## ☁️ Deployment

The application is deployed using Streamlit Community Cloud.

Deployment configuration:

- **Repository:** `rishi4842/voice-notes-action-items`
- **Branch:** `main`
- **Entry point:** `app.py`
- **Python:** 3.11

The Gemini API key is configured through Streamlit Community Cloud secrets rather than being committed to the repository.

## 🧩 LLM Prompt Design

The prompt is designed to keep the generated output grounded in the transcript and reduce hallucinations.

The model is instructed to:

- Create a concise summary.
- List only actions explicitly stated or strongly implied.
- Extract only dates, deadlines, times, or durations mentioned in the transcript.
- Never invent information.
- Preserve important names, numbers, dates, and durations.
- Keep the response concise and easy to scan.

The output is divided into three sections:

```text
Summary

Action Items

Important Dates or Deadlines
```

If no action items or dates are present, the model is instructed to explicitly state that none were identified rather than inventing information.

## 🎧 Speech Processing Approach

The assessment suggested using Whisper or faster-whisper for speech-to-text.

For this implementation, Gemini's audio understanding capability is used for transcription.

This was a deliberate implementation choice because:

- It keeps the speech and language processing workflow within one API provider.
- It avoids requiring a separate speech-to-text service.
- It simplifies the overall architecture.
- It allowed the project to be developed and tested using an available Gemini API free tier.

The trade-off is that the application depends on Gemini API availability and free-tier quotas.

## 🛡️ Error Handling

The application handles several failure cases:

### Empty or speechless audio

If no transcript is produced, the application displays an appropriate error instead of sending empty input to the LLM.

### Transcription failures

Audio-processing/API errors are caught and displayed to the user.

### Empty AI responses

If the model does not return a usable response, the application reports the failure.

### Gemini API quota/rate limits

Gemini free-tier limits can temporarily prevent additional model requests.

When a quota/rate-limit error occurs, the application displays a user-friendly warning instead of exposing the raw API error.

Example:

```text
⚠️ Gemini API quota has been reached.
Please try again after the free-tier quota resets.
```

## 🧪 Testing

The application was tested locally and after deployment.

### Audio Upload Test

Tested with an uploaded MP3 file.

Verified:

- Audio upload ✅
- Audio playback ✅
- Speech transcription ✅
- Summary generation ✅
- Action-item extraction ✅
- Important date/duration extraction ✅

### Browser Recording Test

Tested using the browser's microphone recording feature.

Verified:

- Browser recording ✅
- Recording playback ✅
- Speech transcription ✅

The final LLM processing step can be temporarily unavailable when the Gemini free-tier request quota has been exhausted.

## 🔐 Security

- API keys are stored in environment variables locally.
- `.env` is excluded using `.gitignore`.
- The Gemini API key is stored using Streamlit Community Cloud secrets for deployment.
- No API key is hard-coded into the application source code.

## 🤖 AI Coding Assistant Usage

AI coding assistance was used during development for:

- Debugging and improving the audio-upload flow
- Structuring the project into separate service and utility modules
- Improving prompt design
- Adding error handling
- Reviewing implementation details
- Debugging the recording workflow

All generated suggestions were reviewed, adapted where necessary, and tested as part of the development process.

## 📊 Current Status

The core MVP is implemented and deployed.

### Completed

- [x] Audio upload
- [x] Browser-based audio recording
- [x] Audio playback
- [x] Speech transcription
- [x] Summary generation
- [x] Action-item extraction
- [x] Important date/deadline extraction
- [x] Error handling
- [x] Gemini quota handling
- [x] Streamlit deployment
- [x] Documentation

## 🚧 Limitations

- The application depends on the Gemini API.
- Gemini free-tier quotas can temporarily prevent processing.
- Audio quality can affect transcription accuracy.
- The current version processes one voice note at a time.
- The application does not currently provide persistent storage for processed notes.

## 🔮 Future Improvements

Possible extensions include:

- Batch processing multiple recordings
- Exporting results as PDF
- Downloading a shareable note
- Persistent storage for previous voice notes
- Improved visual organization of summary and action items
- Additional audio-format validation
- More robust handling of very long recordings

## 📄 License

This project was created as a take-home assessment project.
