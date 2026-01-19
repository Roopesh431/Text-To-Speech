# 🎙️ AI Voice Studio (Google Colab Edition)

> **A beginner-friendly, "One-Click" AI Text-to-Speech tool running on Google Colab.**
> Generate high-quality, non-generic voices (American, British, Narrator) with speed and pause control.

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Google%20Colab-orange)
![License](https://img.shields.io/badge/License-MIT-green)

![AI Voice Studio Interface](screenshots/gui_interface.png)

---

## 📖 Table of Contents
1. [About the Project](#-about-the-project)
2. [Key Features](#-key-features)
3. [The Logic (How it Works)](#-the-logic-architecture)
4. [How to Run (Step-by-Step)](#-how-to-run)
5. [Results Demo](#-results-demo)
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
Copy the full Python script provided in `main.py` and paste it into a cell.

### Step 4: Click Play
Run the cell. Wait about 30 seconds for the first-time installation. The **Control Panel** (shown at the top of this page) will appear automatically.

---

## 📸 Results Demo

Here is an example of the generation process.

**1. The Interface:**
The modern GUI allows you to select voices and speed without restarting the code.

<img width="672" height="272" alt="GUI image" src="https://github.com/user-attachments/assets/d6b18582-7bde-4bb2-8964-00abda9979f6" />

**2. The Output:**
Below is an example of the console log showing a successful generation.

<img width="733" height="392" alt="Console Result" src="https://github.com/user-attachments/assets/658e2843-609f-444c-a678-16359c66280b" />

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

---

## 🛠️ Troubleshooting

**Q: The "Generate" button is stuck?**
A: This happens if the previous audio is huge. Click "Clear History" or refresh the page.

**Q: I get a "Protobuf" error?**
A: This means the model download was interrupted. In the code, find the line that downloads `kokoro-v0_19.onnx` and re-run it.

**Q: The voice sounds robotic.**
A: Try reducing the **Speed** to `0.9` and setting the **Pause Gap** to `0.4`. This gives the AI time to "breathe."

---

## 📜 License

This project is open-source. Feel free to modify and share!
