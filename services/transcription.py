import os
import tempfile

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def transcribe_audio(audio_file) -> str:
    audio_bytes = audio_file.getvalue()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(audio_file.name)[1],
    ) as temp_file:
        temp_file.write(audio_bytes)
        temp_path = temp_file.name

    try:
        uploaded_file = client.files.upload(
            file=temp_path,
            config={
                "mime_type": audio_file.type,
            },
        )

        prompt = """
Transcribe this audio accurately.

Return only the spoken words as plain text.
Do not summarize.
Do not add explanations.
Do not add information that was not spoken.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[uploaded_file, prompt],
        )

        return response.text.strip()

    finally:
        os.remove(temp_path)