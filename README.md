# 🎙️ Voice Notes → Action Items

A Streamlit application that converts voice notes into a clear transcript, concise summary, actionable tasks, and important dates or deadlines.

## Features

- Upload an audio file
- Record a voice note directly in the browser
- Convert speech to text using Gemini audio understanding
- Generate a concise summary
- Extract explicit action items
- Identify important dates, deadlines, times, and durations
- Display the results in a simple Streamlit interface
- Handle API quota/rate-limit errors gracefully

## How It Works

The application follows this pipeline:

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

## Tech Stack

- Python 3.11
- Streamlit
- Google Gemini API
- `google-genai`
- `python-dotenv`

## Project Structure

```text
voice-notes-action-items/
├── app.py
├── services/
│   ├── llm.py
│   └── transcription.py
├── utils/
│   └── prompts.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

### 1. Clone the repository

```
git clone <YOUR_REPOSITORY_URL>
cd voice-notes-action-items
```

### 2. Create a virtual environment

```
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure the Gemini API key
Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```
Do not commit the `.env` file or expose your API key publicly.

### 5. Run the application

```
streamlit run app.py
```
The application will open in your browser.

## LLM Prompt Design
The prompt is designed to reduce hallucinations and keep extracted information grounded in the transcript.

The model is instructed to:

- Create a concise summary.
- List only actions explicitly stated or strongly implied.
- Extract only dates, deadlines, times, or durations mentioned in the transcript.
- Never invent information.
- Preserve important names, numbers, dates, and durations.
- Return concise, easy-to-scan output.

## Speech Processing
The assignment suggested Whisper for speech-to-text. For this implementation, Gemini's audio understanding capability is used for both transcription and downstream LLM processing.

This choice keeps the project within a single API provider and avoids requiring a separate paid speech-to-text service.

## Error Handling
The application handles:

- Empty or speechless audio
- Transcription failures
- Empty AI responses
- Gemini API quota/rate-limit errors
When the Gemini free-tier quota is exhausted, the application displays a user-friendly warning instead of exposing the raw API error.

## AI Coding Assistant Usage
AI coding assistance was used during development for:

- Debugging and improving the audio-upload flow
- Structuring the project into separate service and utility modules
- Improving prompt design
- Adding error handling
- Reviewing implementation details
All generated suggestions were reviewed and tested as part of the development process.

## Current Status
The core MVP is implemented and tested for:

- Audio upload
- Browser-based audio recording
- Audio playback
- Speech transcription
- Summary generation
- Action-item extraction
- Important date/deadline extraction

## Future Improvements
Possible extensions include:

- Batch processing multiple recordings
- Exporting results as PDF
- Downloading a shareable note
- Improved visual organization of summary and action items
- Additional audio-format validation