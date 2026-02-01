# 🚀 stanCode Python Projects

A comprehensive collection of Python projects developed during the **stanCode** program. 
This repository documents my journey from mastering programming fundamentals to building complex algorithms and applications. It demonstrates proficiency in **Python**, **computational logic**, and **software engineering principles**.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Key Concepts:** * Algorithms & Data Structures
    * Object-Oriented Programming (OOP)
    * Image Processing
    * String Manipulation & Cryptography
    * File I/O & Data Analysis

---

## 📂 Project Structure

This repository is organized into five main domains:

### 1. 🤖 Karel Robot Logic
Implements complex logic control and pathfinding algorithms using the Stanford Karel environment.
* **StoneMasonKarel:** Algorithms for structural repair and decomposition. Automatically detects and repairs damaged pillars.
* **CheckerboardKarel:** Solves the problem of creating a checkerboard pattern on a map of any dimension.
* **MidpointKarel:** Finds the midpoint of a world using geometric logic without variables.

### 2. 🖼️ Image Processing
Manipulates pixel data (RGB) to achieve visual effects and analysis.
* **Fire Detection (`fire.py`):** An algorithm that detects fire in images based on color thresholds (`HURDLE_FACTOR`) and highlights the hazardous areas.
* **Mirror Lake:** Generates a vertical reflection of an image by manipulating pixel arrays.

### 3. 🔤 String Algorithms
Focuses on text processing, search algorithms, and encryption.
* **Hangman (`hangman.py`):** An interactive console game featuring random word generation, input validation, and game loop control.
* **Caesar Cipher:** Implementation of the classic encryption technique for secure message passing.
* **DNA Similarity:** Algorithms to compare genetic sequences for similarity.

### 4. 🖥️ Console Applications
Utilities for mathematical computation and logic verification.
* **Weather Master:** Analyzes user-input weather data to compute extremums and averages.
* **Quadratic Solver:** Solves quadratic equations with precision.

---

## 🌟 Featured Projects

### 🔥 Fire Detection System
* **Location:** `stanCode-001-Project/Image_Processing/fire.py`
* **Description:** A prototype for disaster detection. It iterates through every pixel of an image to calculate the average brightness. If a pixel's red intensity exceeds the dynamic threshold, it is identified as fire and highlighted, while non-fire regions are converted to grayscale.
* **Code Snippet:**
    ```python
    if pixel.red > avg * HURDLE_FACTOR:
        pixel.red = 255  # Highlight fire
        pixel.green = 0
        pixel.blue = 0
    ```

### 🎮 The Hangman Game
* **Location:** `stanCode-001-Project/String_Algorithms/hangman.py`
* **Description:** A robust CLI (Command Line Interface) game. Players have limited attempts to guess a hidden word.
* **Features:**
    * Random word selection from a predefined dictionary.
    * Real-time dashboard updates (e.g., `D-M-C--C-`).
    * Input sanitization and error handling.

---

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/alanliang666/stancodeproject.git](https://github.com/alanliang666/stancodeproject.git)
    cd stancodeproject
    ```

2.  **Run a script (e.g., Hangman):**
    ```bash
    python3 stanCode-001-Project/String_Algorithms/hangman.py
    ```

---

## 👨‍💻 Author

**Alan Liang**
* Passionate about software development and algorithmic problem solving.
* Open to collaboration and code reviews.
