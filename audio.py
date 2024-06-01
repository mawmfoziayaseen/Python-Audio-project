import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize the Pygame mixer
pygame.mixer.init()

# Create the main application window
root = tk.Tk()
root.title('Audio Player')
root.geometry('300x200')

# Function to play the audio file
def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Function to create buttons for playing audio
def create_audio_button(file_path, button_text):
    button = tk.Button(root, text=button_text, command=lambda: play_audio(file_path))
    button.pack(pady=10)

# Add buttons for the provided audio file
create_audio_button("Audio\Afnan 5.wav", 'Play Audio 1')
create_audio_button("Audio\Fatima 3.wav", 'Play Audio 2')
# create_audio_button("Audio\maryyam 2.wav", 'Play Audio 3')
# create_audio_button("Audio\maryyam 6.wav", 'Play Audio 4')
create_audio_button("Audio\Zeeshan 1.wav", 'Play Audio 3')

# Run the Tkinter main loop
root.mainloop()

