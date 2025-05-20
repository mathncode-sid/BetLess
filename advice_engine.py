import requests
from utils import get_groq_key

def chat_with_groq(chat_history):
    headers = {
        "Authorization": f"Bearer {get_groq_key()}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "temperature": 0.6
    }

    try:
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=10  # avoids hanging
        )
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"].strip()

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error:", res.text if 'res' in locals() else http_err)
    except requests.exceptions.RequestException as req_err:
        print("Request error:", req_err)
    except Exception as e:
        print("Unexpected error:", str(e))

    return "⚠️ Sorry, I couldn't respond at the moment. Please try again later."
