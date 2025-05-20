import streamlit as st
from analyzer import detect_betting_transactions, analyze_progress
from gamification import update_score, get_leaderboard
from advice_engine import chat_with_groq

st.set_page_config("BetLess", layout="centered")
st.title("🎯 BetLess – Break Free from Betting")

st.sidebar.header("👤 User Information")
username = st.sidebar.text_input("Enter your name", max_chars=20)

if not username:
    st.warning("Please enter your name in the sidebar to continue.")
    st.stop()

st.sidebar.success(f"Hello, {username} 👋")


tab1, tab2, tab3 = st.tabs(["📤 Upload Statement", "🏆 Leaderboard", "💡 AI Advice"])

with tab1:
    st.subheader("Upload your bank or mobile money statement (text format)")

    uploaded_file = st.file_uploader("Upload file (.txt)", type="txt")

    if uploaded_file:
        content = uploaded_file.read().decode('utf-8')
        betting_lines = detect_betting_transactions(content)
        feedback, result_type = analyze_progress(betting_lines)

        st.markdown(f"### 🧾 Feedback")
        st.info(feedback)

        update_score(username, result_type)

        st.markdown("### 📉 Betting Activity Detected")
        if betting_lines:
            st.code("\n".join(betting_lines))
        else:
            st.success("No suspicious betting activity found.")

        st.session_state.last_result = result_type  # Save latest result for chat context


with tab2:
    st.subheader("🏅 Top 5 Users")
    leaderboard = get_leaderboard()
    for rank, (user, score) in enumerate(leaderboard, 1):
        st.markdown(f"**{rank}. {user}** – {score} pts")

with tab3:
    st.subheader("🧠 Chat with BetLess Coach")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "system", "content": (
                "You are a supportive, insightful mentor helping someone overcome a betting addiction. "
                "Respond with warmth, encouragement, and actionable suggestions."
            )}
        ]

    if "last_result" not in st.session_state:
        st.session_state.last_result = "good"  # fallback in case analysis hasn't run

    # Add latest analysis as context if not already added
    if not any("Analysis Result" in msg["content"] for msg in st.session_state.chat_history):
        st.session_state.chat_history.append({
            "role": "user",
            "content": f"My latest analysis says I'm in a '{st.session_state.last_result}' betting status. Can you help me reflect or improve?"

        })
    
    status_explainer = {
    "good": "You're currently doing great — no betting signs detected!",
    "partial": "You're making progress, but some signs of betting were still found.",
    "chronic": "The report shows continued betting. Let’s work on getting back on track."
}
    
    st.markdown(f"🧭 **Current Status**: `{st.session_state.last_result.upper()}` — {status_explainer[st.session_state.last_result]}")


    user_input = st.chat_input("Talk to the BetLess Coach")

    if user_input:
        from advice_engine import chat_with_groq
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        reply = chat_with_groq(st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

    for msg in st.session_state.chat_history[1:]:  # Skip system message
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Coach:** {msg['content']}")

