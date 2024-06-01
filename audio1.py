import streamlit as st
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Create a dictionary to map choices to audio files
playlist = {
    1: 'audio1.mp3',
    2: 'audio2.mp3',
    3: 'audio3.mp3'
}

# Function to play the selected song
def play_song(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Streamlit app layout
st.title("Song Playlist")

st.write("Select a song to play:")

# Buttons to play songs
if st.button("Play Song 1"):
    play_song(playlist[1])
    st.write("Playing Song 1...")

if st.button("Play Song 2"):
    play_song(playlist[2])
    st.write("Playing Song 2...")

if st.button("Play Song 3"):
    play_song(playlist[3])
    st.write("Playing Song 3...")

    # Commands of terminal
    # pip install pygame
    #pip install streamlit pygame
    #pip install streamlit
    #streamlit run audio1.py
    