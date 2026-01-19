# 🎙️ AI Voice Studio (Google Colab Edition)

> **A beginner-friendly, "One-Click" AI Text-to-Speech tool running on Google Colab.** > Generate high-quality, non-generic voices (American, British, Narrator) with speed and pause control.

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Google%20Colab-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Table of Contents
1. [About the Project](#-about-the-project)
2. [Key Features](#-key-features)
3. [The Logic (How it Works)](#-the-logic-architecture)
4. [How to Run (Step-by-Step)](#-how-to-run)
5. [Code Breakdown](#-code-breakdown)
6. [Troubleshooting](#-troubleshooting)

---

## 🧐 About the Project

This project is a Python-based tool that turns text into lifelike speech. Unlike standard robotic voices, this uses the **Kokoro-82M** model, which is capable of emotional intonation, breathing pauses, and distinct accents.

We designed this specifically for **Google Colab** users. It solves common Colab issues like connection timeouts, unstable inputs, and library conflicts by using a custom Graphical User Interface (GUI).

---

## ✨ Key Features

* **100% Free:** Runs entirely on Google Colab's free tier.
* **No "Generic" Voices:** Includes deeply realistic British & American accents.
* **GUI Control Panel:** No more typing "Y/N" in broken text boxes. Use real buttons, sliders, and dropdowns.
* **Smart Pausing:** Automatically inserts natural silence gaps between sentences.
* **One-Click Setup:** Auto-installs dependencies and models. No manual commands needed.

---

## 🧠 The Logic (Architecture)

For freshers/beginners, it is important to understand **why** the code is written this way.

### The Problem
Google Colab recently updated to Python 3.12, which broke many older Audio libraries. Additionally, using standard `input()` functions in a loop often causes the program to freeze if the internet flickers.

### The Solution: "Subprocess Isolation"
We split the program into two distinct parts that talk to each other:

1.  **The Frontend (The GUI):**
    * This is what you see (Buttons, Sliders, Text Box).
    * It uses `ipywidgets` to stay on the screen permanently. It never "freezes" waiting for input.

2.  **The Backend (The Worker):**
    * We create a hidden file called `worker_gui.py`.
    * This script contains the actual AI generation code.
    * **Why?** By running this worker in a separate background process (using `subprocess`), we isolate the heavy AI lifting from the visual interface. This prevents memory leaks and ensures the buttons remain clickable even while audio is generating.

**Flowchart of Logic:**
`User Clicks Button` -> `GUI saves inputs` -> `Launches Worker Script` -> `Worker Generates Audio` -> `GUI displays Audio Player`

---

## 🚀 How to Run

You do not need to install Python on your computer. This runs in the cloud.

### Step 1: Open Google Colab
Go to [Google Colab](https://colab.research.google.com/) and create a **New Notebook**.

### Step 2: GPU Setup (Optional but Recommended)
For faster generation:
1.  Click **Runtime** in the top menu.
2.  Select **Change runtime type**.
3.  Select **T4 GPU**.

### Step 3: Paste the Code
Copy the full Python script (provided in the repository `main.py` or the code block below) and paste it into a cell.

### Step 4: Click Play
Run the cell. Wait about 30 seconds for the first-time installation. The **Control Panel** will appear automatically.

---

## 📂 Code Breakdown

Here is a simplified explanation of the files for beginners:

### 1. `setup_environment()`
This function checks if you are missing libraries (like `kokoro-onnx` or `numpy`). If you are, it installs them silently in the background so you don't have to restart the runtime manually.

### 2. `worker_gui.py` (The Hidden Script)
The code dynamically writes this file to the disk. It accepts arguments like `--text`, `--speed`, and `--voice`. It processes the text, splits it by punctuation, and stitches the audio together.

### 3. `ipywidgets` (The Interface)
Instead of asking users to type inputs, we use Widgets:
* `Dropdown`: For selecting voices.
* `FloatSlider`: For adjusting speed (0.5x to 1.5x).
* `Button`: Triggers the generation function `on_generate_click`.

---

## 🛠️ Troubleshooting

**Q: The "Generate" button is stuck?** A: This happens if the previous audio is huge. Click "Clear History" or refresh the page.

**Q: I get a "Protobuf" error?** A: This means the model download was interrupted. In the code, find the line that downloads `kokoro-v0_19.onnx` and re-run it, or just Factory Reset the runtime (Runtime > Disconnect and Delete Runtime).

**Q: The voice sounds robotic.** A: Try reducing the **Speed** to `0.9` and setting the **Pause Gap** to `0.4`. This gives the AI time to "breathe."

---

## 📜 License

This project is open-source. Feel free to modify and share!
# Results:
<img width="672" height="272" alt="image" src="https://github.com/user-attachments/assets/d6b18582-7bde-4bb2-8964-00abda9979f6" />
I choose Option '4'
and gave Prompt "Hello this is a sample text and you sucessfully generated a Text"
<img width="733" height="392" alt="image" src="https://github.com/user-attachments/assets/658e2843-609f-444c-a678-16359c66280b" />

# Update 

This is an Update which is fully refiend version and it can run in One-Click and we can do tasks 

<img width="1166" height="385" alt="image" src="https://github.com/user-attachments/assets/6d63b1b9-b04f-46af-b44a-2c96f4735957" />
