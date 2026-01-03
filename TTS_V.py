# @title Interactive Voice Generator (Run Me)
import soundfile as sf
from kokoro_onnx import Kokoro
import numpy as np
from IPython.display import Audio, display, clear_output
import re
import sys

# --- 1. SETUP VOICES ---
# Dictionary mapping friendly names to model IDs
VOICES = {
    "1": {"name": "American Male",       "id": "am_michael", "desc": "Standard, Clear"},
    "2": {"name": "American Female",     "id": "af_sarah",   "desc": "Standard, Professional"},
    "3": {"name": "Gentleman (British)", "id": "bm_george",  "desc": "Deep, Formal, Elder"},
    "4": {"name": "Lady (British)",      "id": "bf_emma",    "desc": "Polite, Elegant"},
    "5": {"name": "Young/Childlike",     "id": "af_bella",   "desc": "Soft, High-pitch"},
    "6": {"name": "Narrator",            "id": "am_adam",    "desc": "Deep, Storytelling"},
}

# --- 2. LOAD MODEL (Once) ---
# We check if 'kokoro' exists to avoid reloading it every time you run the cell
if 'kokoro' not in globals():
    print("Loading AI Model (this takes 2 seconds)...")
    try:
        kokoro = Kokoro("kokoro-v0_19.onnx", "voices.json")
    except Exception as e:
        print("Error: Model files not found. Please run the Installer script from the previous step first.")
        sys.exit()

# --- 3. HELPER FUNCTIONS ---
def get_user_choice():
    print("\n--- SELECT A VOICE ---")
    for key, val in VOICES.items():
        print(f"[{key}] {val['name']} \t({val['desc']})")
    
    choice = input("\nEnter the number of the voice (or 'q' to quit): ").strip()
    return choice

def split_text(text):
    # Splits text into sentences to handle long inputs
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

# --- 4. MAIN LOOP ---
while True:
    # 1. Clear previous output to keep it clean
    clear_output(wait=True)
    
    # 2. Get Voice Selection
    user_choice = get_user_choice()
    
    if user_choice.lower() == 'q':
        print("Exiting program. Goodbye!")
        break
    
    if user_choice not in VOICES:
        print("Invalid selection. Please try again.")
        continue
    
    selected_voice = VOICES[user_choice]
    print(f"\n>> Selected: {selected_voice['name']}")
    
    # 3. Get Text Input
    print("\nPaste your text below (Press Enter when done):")
    user_text = input("Text to read: ")
    
    if not user_text.strip():
        print("Text cannot be empty.")
        continue

    # 4. Generate Audio
    print("\nGenerating audio... Please wait.")
    
    try:
        sentences = split_text(user_text)
        audio_segments = []
        
        for sentence in sentences:
            audio, sample_rate = kokoro.create(
                text=sentence,
                voice=selected_voice['id'],
                speed=1.0,
                lang="en-us"
            )
            audio_segments.append(audio)
        
        # 5. Play Audio
        if audio_segments:
            final_audio = np.concatenate(audio_segments)
            output_filename = "interactive_output.wav"
            sf.write(output_filename, final_audio, sample_rate)
            
            print("Done! Listening to audio:")
            display(Audio(output_filename, autoplay=True))
            
            input("\nPress Enter to create a new one...")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to continue...")
