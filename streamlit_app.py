# streamlit_app.py

import streamlit as st
from modules.sentiment_analysis import analyze_sentiment

st.set_page_config(page_title="GenAI Emotion Analyzer", page_icon="🧠")
st.title("🧠 Emotion-Aware Sentiment Analyzer")

st.markdown("""
Welcome to the Emotion Analyzer! 🎭  
Type in any sentence, and we'll tell you:
- Whether it's Positive / Negative / Neutral
- Why it feels that way (if you want)
- How intense each basic emotion is (Happiness, Sadness, Anger, etc.)

**Instructions:**
1. Enter your sentence.
2. Click **Analyze**.
3. Switch modes to see labels, explanations, or emotion scores.
""")

# Session state initialization
if "result" not in st.session_state:
    st.session_state.result = {}
if "last_text" not in st.session_state:
    st.session_state.last_text = ""

# Input area
text = st.text_area("✏️ Enter some text to analyze:")

# Analysis mode selector
mode = st.selectbox("🔎 Select analysis mode:", ["label", "explanation", "emotion_scores"])

# Only run if new input or user clicks Analyze
if st.button("🔍 Analyze") or (text and text != st.session_state.last_text):
    if text.strip():
        st.session_state.last_text = text
        with st.spinner("Analyzing with OpenAI..."):
            try:
                st.session_state.result["label"] = analyze_sentiment(text, "label")
                st.session_state.result["explanation"] = analyze_sentiment(text, "explanation")
                st.session_state.result["emotion_scores"] = analyze_sentiment(text, "emotion_scores")
            except Exception as e:
                st.error(f"Error: {e}")
                st.session_state.result = {}

# Render result
if text and text == st.session_state.last_text and mode in st.session_state.result:
    st.divider()
    st.markdown("### 🎯 Analysis Result")

    if mode in ["label", "explanation"]:
        st.markdown(f"**{mode.capitalize()}**: {st.session_state.result[mode]}")

    elif mode == "emotion_scores":
        emotions = {
            "Happiness": "😊",
            "Sadness": "😢",
            "Anger": "😠",
            "Fear": "😨",
            "Disgust": "🤢",
            "Surprise": "😲"
        }

        scores = st.session_state.result["emotion_scores"]

        if isinstance(scores, dict) and "error" not in scores:
            for emotion, emoji in emotions.items():
                value = scores.get(emotion, 0)
                score_10 = round(value * 10)

                color = "red" if score_10 <= 3 else "orange" if score_10 <= 6 else "green"

                st.markdown(f"**{emoji} {emotion}: {score_10}/10**")
                st.progress(value, text=f"{int(value*100)}% intensity")
        else:
            st.error("Could not parse emotion scores.")

