from google import genai
from dotenv import load_dotenv
import os

from prompt_handler import create_classification_prompt

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_answer(prompt):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text