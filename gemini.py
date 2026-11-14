from google import genai
from google.genai import types
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path, override=True)   
API_KEY = load_dotenv('GEMINI_API_KEY')
MODEL = "gemini-3.6-flash" 
client = genai.Client(api_key=API_KEY)

try:
    response = client.models.generate_content(model=MODEL, contents="What is c language tell me in short")
    print(response.text)
except Exception as e:
    print("Request failed:", e)
    print("\nFlash models available to your key:")
    for m in client.models.list():
        if "flash" in m.name.lower():
            print(" ", m.name)