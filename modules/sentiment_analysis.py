# modules/sentiment_analysis.py

import os
from utils.chatgpt import generate_text
import openai

# Load API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=OPENAI_API_KEY)

def analyze_sentiment(text: str, mode: str = "label", model: str = "gpt-4o") -> str:
    """
    Analyze the sentiment of input text using OpenAI's API.

    Args:
        text (str): Input text to analyze.
        mode (str): 'label' returns Positive/Neutral/Negative.
                    'explanation' returns a natural language sentiment explanation.
        model (str): The OpenAI model to use.

    Returns:
        str: Sentiment label or explanation.
    """
    if mode == "label":
        instructions = (
            "You are a sentiment classifier. Only respond with one word: "
            "Positive, Negative, or Neutral. Do not explain."
        )
    elif mode == "explanation":
        instructions = (
            "You are an expert sentiment analyst. Analyze the sentiment of the following text. "
            "Describe whether it is positive, negative, or neutral, and explain why in 1–2 sentences."
        )
    else:
        raise ValueError("Invalid mode. Choose 'label' or 'explanation'.")

    result = generate_text(
        prompt=text,
        instructions=instructions,
        client=client,
        model=model,
        output_type="text"
    )

    return result.strip()

