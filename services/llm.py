import os

from dotenv import load_dotenv
from google import genai
from utils.prompts import ACTION_ITEMS_PROMPT
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_action_items(transcript: str) -> str:
    prompt = ACTION_ITEMS_PROMPT.format(transcript=transcript)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text