import openai
import base64
import requests
import time 
import streamlit as st


def generate_text(prompt, instructions, client, model="gpt-4o", output_type='text'):
    """
    Generate a text response using OpenAI's chat API.
    """
    completion = client.chat.completions.create(
        model=model,
        response_format={"type": output_type},
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


def generate_image(prompt, client, model="dall-e-3"):
    """
    Generate an image using OpenAI's DALL-E model.
    """
    response_img = client.images.generate(
        model=model,
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    time.sleep(1)
    image_url = response_img.data[0].url
    revised_prompt = response_img.data[0].revised_prompt
    return image_url, revised_prompt


def generate_image_description(image_urls, instructions, client):
    """
    Generate a description of an image or a set of images using OpenAI Vision.
    """
    PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": instructions},
                *map(lambda x: {"type": "image_url", "image_url": {"url": x}}, image_urls),
            ],
        },
    ]
    
    params = {
        "model": "gpt-4o",
        "messages": PROMPT_MESSAGES,
        "max_tokens": 1000,
    }

    response = client.chat.completions.create(**params)
    return response.choices[0].message.content


def encode_image(image_path):
    """
    Encodes an image to base64.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def display_image_url(image_url, width=500, height=500):
    """
    Display an image from a URL using Streamlit.
    """
    response = requests.get(image_url)
    image_data = response.content
    st.image(image_data, width=width, caption="Generated Image")


def display_tweet(text='life is good', screen_name='zlisto'):
    """
    Display a tweet-style card using HTML in Streamlit.
    """
    display_html = f'''
    <div style="background-color:white; color:black; border:1px solid #e1e8ed; border-radius:10px; padding:20px; max-width:500px; font-family:'Helvetica Neue', Helvetica, Arial, sans-serif; box-shadow:0px 0px 10px rgba(0,0,0,0.1);">
        <div style="color:#1da1f2;"><strong>@{screen_name}</strong></div>
        <div><p>{text}</p></div>
    </div>
    '''
    st.markdown(display_html, unsafe_allow_html=True)


def display_IG(caption, image_url, screen_name=None, profile_image_url=None):
    """
    Display an Instagram-style post using HTML in Streamlit.
    """
    display_html = f"""
    <div style='border:1px solid #e1e1e1; border-radius:3px; width:600px; background-color:white; font-family:Helvetica Neue, Helvetica, Arial, sans-serif;'>
        <div style='padding:14px; border-bottom:1px solid #e1e1e1; display:flex; align-items:center;'>
            <img src="{profile_image_url}" alt="Profile pic" style='border-radius:50%; width:32px; height:32px; margin-right:10px;'>
            <span style='font-weight:bold; color:#262626;'>{screen_name}</span>
        </div>
        <img src="{image_url}" alt="Instagram image" style='width:100%; display:block;'>
        <div style='padding:10px; font-size:14px; color:#262626;'>
            <strong>{screen_name}</strong> {caption}
        </div>
        <div style='padding:10px; border-top:1px solid #e1e1e1;'>
            <strong>24 likes</strong>
        </div>
    </div>
    """
    st.markdown(display_html, unsafe_allow_html=True)
