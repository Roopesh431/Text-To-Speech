# @title 🎛️ AI Voice Control Panel (Fixes All Input Issues)
import os
import subprocess
import sys
import datetime
import ipywidgets as widgets
from IPython.display import display, Audio, clear_output

# --- 1. HIDDEN INSTALLER & WORKER SCRIPT ---
# This runs in the background to ensure libraries are always fixed.
def setup_environment():
    """Ensures dependencies are installed without restarting."""
    if not os.path.exists("worker_gui.py"):
        # Create the worker script that isolates the AI from Colab's errors
        worker_code = """
import argparse
import soundfile as sf
from kokoro_onnx import Kokoro
import numpy as np
import re

def run(text, voice, speed, gap, filename):
    try:
        kokoro = Kokoro("kokoro-v0_19.onnx", "voices.json")
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

        audio_segments = []
        sample_rate = 24000
        silence = np.zeros(int(sample_rate * gap))

        for i, s in enumerate(sentences):
            audio, _ = kokoro.create(text=s, voice=voice, speed=speed, lang="en-us")
            audio_segments.append(audio)
            if i < len(sentences) - 1:
                audio_segments.append(silence)

        if audio_segments:
            final_audio = np.concatenate(audio_segments)
            sf.write(filename, final_audio, sample_rate)
            print("SUCCESS")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--text", type=str); p.add_argument("--voice", type=str)
    p.add_argument("--speed", type=float); p.add_argument("--gap", type=float)
    p.add_argument("--out", type=str)
    a = p.parse_args()
    run(a.text, a.voice, a.speed, a.gap, a.out)
"""
        with open("worker_gui.py", "w") as f:
            f.write(worker_code)

    # Check and install libraries if missing
    try:
        import kokoro_onnx
    except ImportError:
        print("⚙️ Installing AI Engines (First run)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "kokoro-onnx", "soundfile", "numpy==1.26.4"])
        subprocess.run(["sudo", "apt-get", "-q", "install", "espeak-ng"], check=False)

    # Download Models if missing
    if not os.path.exists("kokoro-v0_19.onnx"):
        subprocess.run(["wget", "-q", "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx"])
        subprocess.run(["wget", "-q", "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json"])

# --- 2. GUI ELEMENTS ---
setup_environment()

# Voice Options
VOICES = [
    ("American Male", "am_michael"), ("American Female", "af_sarah"),
    ("British Gentleman", "bm_george"), ("British Lady", "bf_emma"),
    ("Narrator", "am_adam"), ("Young/Soft", "af_bella")
]

# Create Widgets
header = widgets.HTML("<h2>🎙️ AI Voice Studio</h2>")
voice_drop = widgets.Dropdown(options=VOICES, description="Voice:")
speed_slider = widgets.FloatSlider(value=1.0, min=0.5, max=1.5, step=0.1, description="Speed:")
gap_input = widgets.FloatText(value=0.4, description="Pause (s):", step=0.1)
text_area = widgets.Textarea(placeholder="Type your script here...", layout=widgets.Layout(width='90%', height='150px'))
gen_btn = widgets.Button(description="Generate Audio", button_style='primary', icon='play')
clear_btn = widgets.Button(description="Clear History", button_style='warning')
out_log = widgets.Output()

# --- 3. LOGIC ---
def on_generate_click(b):
    with out_log:
        script = text_area.value.strip()
        if not script:
            print("⚠️ Please enter some text first.")
            return

        # 1. Generate Unique Filename (Fixes download issue)
        timestamp = datetime.datetime.now().strftime("%H-%M-%S")
        filename = f"Audio_{timestamp}.wav"

        print(f"⏳ Generating '{filename}'... (Please wait)")
        gen_btn.disabled = True # Prevent double clicking

        # 2. Run Worker
        try:
            result = subprocess.run(
                [sys.executable, "worker_gui.py", "--text", script, "--voice", voice_drop.value,
                 "--speed", str(speed_slider.value), "--gap", str(gap_input.value), "--out", filename],
                capture_output=True, text=True
            )

            # 3. Display Result
            if "SUCCESS" in result.stdout:
                clear_output(wait=True) # Clear the "Generating..." text
                print(f"✅ Ready: {filename}")
                display(Audio(filename))
            else:
                print("❌ Error:", result.stderr)
        except Exception as e:
            print("❌ System Error:", e)

        gen_btn.disabled = False

def on_clear_click(b):
    out_log.clear_output()

# Connect Buttons
gen_btn.on_click(on_generate_click)
clear_btn.on_click(on_clear_click)

# Display Interface
ui = widgets.VBox([
    header,
    widgets.HBox([voice_drop, speed_slider, gap_input]),
    text_area,
    widgets.HBox([gen_btn, clear_btn]),
    widgets.HTML("<hr>"),
    out_log
])

display(ui)
