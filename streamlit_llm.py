#########################
## OpenAI in Streamlit ##
#########################

# Importing Libraries
import streamlit as st
from openai import OpenAI
import os
import random

# Inject custom CSS to change the sidebar color
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #ADD8E6;  /* Light blue */
        }
        [data-testid="stSidebar"] h2 {
            color: #FFFFFF;  /* White text for header */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Setting up OpenAI

# Mac terminal: export OPENAI_API_KEY = 
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=key)

# Fun facts about music
fun_facts = [
    "Did you know? The world's longest concert lasted 639 years! It's called 'Organ²/ASLSP' by John Cage.",
    "Mozart wrote his first symphony when he was just 8 years old!",
    "The Beatles hold the record for the most number-one hits on the Billboard Hot 100 chart.",
    "Listening to music can increase workout performance by up to 15%!",
    "The world's largest orchestra consisted of 8,097 musicians, performed in Taiwan in 2013.",
    "Music therapy is a legitimate treatment for stress, anxiety, and even PTSD.",
    "A single violin is made from over 70 different pieces of wood.",
    "Queen's 'Bohemian Rhapsody' was the first music video ever broadcast on MTV.",
    "The most expensive musical instrument ever sold is a Stradivarius violin for $15.9 million."
]

# Streamlit App

st.title('OpenAI Music Assistant')

st.write('This app will allow you to input an artist and a genre and receive a song lyric.')

# We will start with a side bar to ask the user for a genre

st.sidebar.header ("🎵 Music Sidebar")

genre = st.sidebar.selectbox(
    'Select a genre:', 
    ['pop', 'rock', 'rap', 'country', 'jazz', 'metal', 'blues', 'folk', 'classical', 'reggae']
)

# We will then ask the user for an artist

artist = st.sidebar.text_input('Enter an artist:', 'Sabrina Carpenter')

st.sidebar.write("Here's a random music fact for you:")
st.sidebar.success(random.choice(fun_facts))

# Now we need a place to display the lyrics

lyrics = st.empty()

# Now we need a button to generate the lyrics

if st.sidebar.button('Generate Lyrics'):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a lyrical genius."},
            {
                "role": "user",
                "content": f"Write a song lyric in the {genre} genre by {artist}."
            }
        ]
    )
    lyrics.write(completion.choices[0].message.content)

# Check it out: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-chatgpt-like-app