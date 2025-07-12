import os
import requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HF_TOKEN")

def generate_image(prompt):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payload = {"inputs": prompt}

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            try:
                img = Image.open(BytesIO(response.content))
                return [img]  # return as list
            except Exception as e:
                return f"Image decode error: {e}"
        else:
            return f"API Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Request failed: {e}"
