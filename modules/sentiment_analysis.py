# modules/sentiment_analysis.py

import openai
import streamlit as st
from utils.chatgpt import generate_text
import json

# Load OpenAI client from Streamlit secrets
client = openai.Client(api_key=st.secrets["OPENAI_API_KEY"])

def analyze_sentiment(text: str, mode: str = "label", model: str = "gpt-4o") -> str | dict:
    """ 
    Analyze the sentiment of input text using OpenAI's API.

    Args:
        text (str): Input text to analyze.
        mode (str): 'label', 'explanation', or 'emotion_scores'.
        model (str): The OpenAI model to use.

    Returns:
        str or dict: Sentiment label, explanation, or emotion scores dictionary.
    """ 
    if mode == "label":
        instructions = (
            "You are a sentiment classifier. Only respond with one word: "
            "Positive, Negative, or Neutral. Do not explain."
        )
        output_type = "text"

    elif mode == "explanation":
        instructions = (
            "You are an expert sentiment analyst. Analyze the sentiment of the following text. "
            "Describe whether it is positive, negative, or neutral, and explain why in 1–2 sentences."
        )
        output_type = "text"

    elif mode == "emotion_scores":
        instructions = (
            "You are an expert in emotional tone analysis. "
            "Given a sentence, return a JSON object with scores (from 0 to 1) for these emotions: "
            "Happiness, Sadness, Anger, Fear, Disgust, and Surprise. "
            "Example:\n"
            "{\n"
            "  \"Happiness\": 0.8,\n"
            "  \"Sadness\": 0.1,\n"
            "  \"Anger\": 0.0,\n"
            "  \"Fear\": 0.1,\n"
            "  \"Disgust\": 0.0,\n"
            "  \"Surprise\": 0.2\n"
            "}"
        )
        output_type = "json_object"

    else:
        raise ValueError("Invalid mode. Choose 'label', 'explanation', or 'emotion_scores'.")

    result = generate_text(
        prompt=text,
        instructions=instructions,
        client=client,
        model=model,
        output_type=output_type
    )

    if mode == "emotion_scores":
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return {"error": "Failed to parse emotion scores"}
    else:
        return result.strip()

