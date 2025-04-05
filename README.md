# Generative AI Showcase App

Welcome to the **Generative AI Showcase App**! This application demonstrates various Generative AI techniques, encapsulating the knowledge and skills acquired during my Generative AI coursework.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Acknowledgments](#acknowledgments)

## Overview

This Streamlit-based application serves as an interactive platform to explore and demonstrate multiple Generative AI functionalities, including text generation, image creation, sentiment analysis, and more. Each feature is modularized, reflecting best practices in software development and showcasing a range of AI capabilities.

## Features

- **Sentiment Analysis:** Analyze the sentiment of user-provided text inputs.
- **Text Generation:** Generate coherent and contextually relevant text based on prompts.
- **Image Generation:** Create images from textual descriptions using advanced AI models.
- **Image Analysis:** Extract meaningful insights from uploaded images.
- **Clustering:** Group similar data points together to identify patterns.
- **Persuasion Scoring:** Evaluate the persuasive strength of textual content.
- **A/B Testing Simulator:** Simulate and analyze A/B testing scenarios.
- **Video Analysis:** Derive insights from video content.
- **Conversational AI Agent:** Engage with an AI-powered chatbot for interactive conversations.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **AI Models:** OpenAI's GPT, DALL·E, and others
- **APIs and Libraries:** OpenAI API, Streamlit, and custom utility modules

## Installation

To run this application locally, follow these steps (in your terminal):

1. **Clone the Repository:**
   git clone https://github.com/yourusername/genai-showcase-app.git

2. **Navigate to the Project Directory:**
   cd genai-showcase-app

3. **Install the Required Dependencies:**
   pip install -r requirements.txt

4. **Set Up API Keys:**

* Obtain API keys from the respective AI service providers (e.g., OpenAI).
* Store them securely, for example, using Streamlit's Secrets Management.

5. **Launch the Appllication:**
streamlit run streamlit_app.py

## Project Strcuture
```
genai-showcase-app/
├── streamlit_app.py            # Main entry point for the Streamlit app
├── requirements.txt            # List of Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
├── modules/                    # Directory containing modular feature implementations
│   ├── sentiment_analysis.py
│   ├── text_generation.py
│   ├── image_generation.py
│   ├── image_analysis.py
│   ├── clustering.py
│   ├── persuasion.py
│   ├── ab_testing.py
│   ├── video_analysis.py
│   ├── chatbot_agent.py
├── utils/                      # Utility modules and helper functions
│   ├── genai.py
│   ├── chatgpt.py
│   ├── elevenlabs_client.py
│   ├── movieai.py
```

## Acknowledgements

This project was developed as part of the Generative AI course curriculum. Special thanks to Prof. [Tauhid Zaman](https://som.yale.edu/faculty-research/faculty-directory/tauhid-zaman) for the invaluable guidance and to the creators of the utilized AI models and tools for their contributions to the field.
