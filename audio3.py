import sys
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

from pydub import AudioSegment
from pydub.generators import Sine

def generate_tone(frequency, duration_ms, file_name):
    tone = Sine(frequency).to_audio_segment(duration=duration_ms)
    tone.export(file_name, format="mp3")

generate_tone(440, 3000, "videoplayback.mp3")
generate_tone(550, 3000, "videoplayback_2.mp3")
generate_tone(660, 3000, "videoplayback_3.mp3")

print("MP3 files generated successfully!")
