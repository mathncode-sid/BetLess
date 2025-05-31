# BetLess

**BetLess** is a Streamlit-powered app designed to help users break free from betting addiction. It analyzes uploaded bank or mobile money statements for betting activity, provides feedback, tracks progress with a leaderboard, and offers supportive AI-powered coaching.

---

## Features

- **Statement Analysis:** Upload your bank or mobile money statement (in `.txt` format) to detect betting transactions.
- **Personalized Feedback:** Get instant feedback on your betting activity.
- **Gamification:** Earn or lose points based on your progress. Compete on the leaderboard!
- **AI Coach:** Chat with an AI mentor for encouragement and actionable advice.

---

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

1. **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd BetLess
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file with your Groq API key:
      ```
      GROQ_API_KEY=your_groq_api_key_here
      ```

---

## Usage

1. **Run the app:**
    ```sh
    streamlit run [app.py](http://_vscodecontentref_/0)
    ```

2. **Open in your browser:**  
   Streamlit will provide a local URL (usually http://localhost:8501).

3. **Enter your name** in the sidebar.

4. **Upload your statement** in the "Upload Statement" tab.

5. **View your progress** and check the leaderboard.

6. **Chat with the AI Coach** for support and advice.

---

## File Structure

- `app.py`: Main Streamlit app.
- `analyzer.py`: Detects betting transactions and analyzes progress.
- `gamification.py`: Handles scoring and leaderboard.
- `advice_engine.py`: Connects to Groq API for AI chat.
- `user_data.py`: (Stub) User management.
- `utils.py`: Utility functions (e.g., API key loading).
- `data/scores.json`: Stores user scores.

---
## Demo Video
[Watch Demo Video](https://github.com/mathncode-sid/BetLess/raw/main/demo/demo.mp4)

## Notes

- Only `.txt` statements are supported.
- The AI coach uses the Groq API; ensure your API key is valid.
- User authentication is not implemented—usernames are entered manually.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Groq API](https://console.groq.com/)

---

**Break the cycle. Bet less, live more!**
