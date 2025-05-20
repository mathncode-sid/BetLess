import os
from dotenv import load_dotenv

load_dotenv()

def get_groq_key():
    return os.getenv("GROQ_API_KEY")

print("GROQ API Key loaded: ", os.getenv("GROQ_API_KEY"))
