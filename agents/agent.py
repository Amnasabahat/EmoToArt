
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
from groq import Groq
from agents.art_prompts_template import art_prompt

load_dotenv()

# Initialize Groq LLM
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_art_idea(mood, style=""):
    prompt = art_prompt(mood, style)
    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.8
)

    return response.choices[0].message.content
