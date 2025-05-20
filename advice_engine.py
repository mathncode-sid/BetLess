import requests
from utils import get_groq_key

def chat_with_groq(chat_history):
    headers = {
        "Authorization": f"Bearer {get_groq_key()}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": chat_history,
        "temperature": 0.6
    }

    try:
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Groq API Chat Error:", res.text)
        return "⚠️ Sorry, I had trouble responding just now."
