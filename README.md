# 🚀 Python Projects

A comprehensive collection of Python projects developed during the **stanCode** program.
This repository documents my journey from mastering programming fundamentals to building complex algorithms and applications. It demonstrates proficiency in **Python**, **computational logic**, and **software engineering principles**.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Key Concepts:**
    * Algorithms & Data Structures
    * Object-Oriented Programming (OOP)
    * Algorithmic Image Processing
    * String Manipulation & Cryptography
    * File I/O & Data Analysis

---

## 📂 Project Structure

This repository is organized into distinct domains based on functionality:

### 1. 🖼️ Algorithmic Image Processing
Manipulates pixel data (RGB) to achieve visual effects and analysis.
* **Fire Detection System (`fire.py`):** An algorithm that detects fire in images based on color thresholds and highlights hazardous areas while gray-scaling the background.
* **StanCodoshop:** A photo editing tool capable of object removal (ghosting) and image composition.
* **Mirror Lake:** Generates a vertical reflection of an image by manipulating pixel arrays.

### 2. 🎮 Game Development
Interactive applications built with event-driven programming.
* **Breakout Arcade:** A fully functional brick-breaking game with physics-based collision detection.
* **Hangman (`hangman.py`):** An interactive console game featuring random word generation and input validation.

### 3. 📊 Data Analytics
* **Baby Names Analyzer:** Processes decades of social security data to visualize name popularity trends using nested dictionaries.

### 4. 🔤 String Algorithms & Cryptography
* **Caesar Cipher:** Implementation of the classic encryption technique for secure message passing.
* **DNA Similarity:** Algorithms to compare genetic sequences for similarity.

### 5. 🤖 Algorithmic Foundations (Karel & Utils)
* **Karel Robot:** Solves complex pathfinding and logic control problems (e.g., `StoneMasonKarel`, `CheckerboardKarel`).
* **Math Utilities:** Tools for prime checking, quadratic equations, and statistical analysis.

---

## 🌟 Featured Projects

### 🖼️ StanCodoshop (Object Removal App)
* **Location:** `Python-Portfolio-Projects/Algorithmic_Image_Processing/Object_Removal_App/stanCodoshop.py`
* **Description:** An advanced image manipulation tool that removes unwanted "ghosting" objects (e.g., pedestrians) from a set of photos taken at the same location.
    * **Algorithm:** It calculates the **Euclidean distance** of pixel colors to identify outliers and reconstructs the clean background using the "best" pixel from the dataset.
* **Code Snippet:**
    ```python
    def get_best_pixel(pixels):
        """
        Given a list of pixels, returns the pixel with the smallest
        color distance from the average pixel of the list.
        """
        avg = get_average(pixels)
        best_pixel = None
        min_dist = float('inf')
        
        for pixel in pixels:
            dist = get_pixel_dist(pixel, avg)
            if dist < min_dist:
                min_dist = dist
                best_pixel = pixel
        return best_pixel
    ```
* **Demo:**
  *(Showcasing the removal of moving people from a landmark photo)*
  
  | Input (Cluttered) | Output (Clean Background) |
  | :---: | :---: |
  | <img src="https://github.com/user-attachments/assets/11f13eb4-26f2-48e9-ae90-17365776b6fa" width="300"> | <img src="https://github.com/user-attachments/assets/c1bd3025-181d-4c92-8a54-80c299ef9b7f" width="300"> |

### 🧱 Breakout Arcade Game
* **Location:** `Python-Portfolio-Projects/Game_Development/Breakout_Arcade/breakout.py`
* **Description:** A classic brick-breaking game built from scratch using **Object-Oriented Programming (OOP)**.
    * **Physics Engine:** Implements a custom collision detection system that calculates the ball's position relative to the paddle, bricks, and walls in every animation frame.
    * **State Management:** Handles game states (lives, levels, game over) and prevents bugs like the "sticky paddle" effect.
* **Code Snippet:**
    ```python
    # Collision detection at 4 corners of the ball
    obj_left_top = graphics.window.get_object_at(ball.x, ball.y)
    # ... (checking other corners)

    if hitter is not None:
        if hitter is graphics.paddle:
            # Physics fix: Only bounce if moving downwards
            if dy > 0: 
                graphics.setter_dy(-dy)
        else:
            graphics.setter_dy(-dy)
            graphics.window.remove(hitter) # Remove brick
            brick_break += 1
    ```
* **Demo:**
  
  <img src="https://github.com/user-attachments/assets/7f3f91c1-6db2-4ce1-8214-567e02f33804" alt="Breakout Gameplay" width=300>

### 👶 Baby Names Trends Analyzer
* **Location:** `Python-Portfolio-Projects/Data_Analytics_BabyNames/babynames.py`
* **Description:** A data analytics tool that processes large datasets of Social Security records to visualize name popularity over decades.
    * **Data Structure:** Utilizes **nested dictionaries** (`{name: {year: rank}}`) to optimize data retrieval, achieving **O(1)** time complexity for rank lookups.
    * **Data Cleaning:** Handles inconsistent formatting and merges data from multiple text files into a unified database.
* **Code Snippet:**
    ```python
    def add_data_for_name(name_data, year, rank, name):
        """
        Efficiently stores rank data, handling existing entries
        to ensure the highest rank (smallest number) is kept.
        """
        if name in name_data:
            if year in name_data[name]:
                # Keep the better rank (e.g., 5 is better than 10)
                if int(rank) < int(name_data[name][year]):
                    name_data[name][year] = rank
            else:
                name_data[name][year] = rank
        else:
            name_data[name] = {year: rank}
    ```
* **Demo:**

  <img src="https://github.com/user-attachments/assets/26800001-0d1e-467a-990c-383a465738c0" alt="Baby Names Graph" width="600">

### 🔥 Fire Detection System
* **Location:** `Python-Portfolio-Projects/Algorithmic_Image_Processing/Fire_Detection_System/fire.py`
* **Description:** A disaster detection prototype. The algorithm iterates through every pixel to calculate the average brightness. It utilizes a dynamic threshold (`HURDLE_FACTOR`) to distinguish fire pixels from the background.
    * **Logic:** If `pixel.red > average * 1.05`, the pixel is highlighted as pure red. Otherwise, it is converted to grayscale to emphasize the contrast.
* **Code Snippet:**
    ```python
    avg = (pixel.red + pixel.green + pixel.blue) // 3
    if pixel.red > avg * HURDLE_FACTOR:
        pixel.red = 255  # Highlight fire
        pixel.green = 0
        pixel.blue = 0
    else:
        pixel.red = avg  # Grayscale background
        pixel.green = avg
        pixel.blue = avg
    ```
* **Demo:**
  
  | Original Image | Processed (Highlight Fire) |
  | :---: | :---: |
  | <img src="https://github.com/user-attachments/assets/18bca155-1457-49d0-ba19-a2246603d4a3" width="300"> | <img src="https://github.com/user-attachments/assets/17b4877b-e662-4b2a-8680-3f8cff1a4559" width="300"> |

### 🎮 The Hangman Game
* **Location:** `Python-Portfolio-Projects/Game_Development/Hangman_CLI/hangman.py`
* **Description:** A robust CLI (Command Line Interface) game where players have limited attempts to guess a hidden word.
* **Features:**
    * Random word selection from a predefined dictionary.
    * Real-time dashboard updates (e.g., `D-M-C--C-`).
    * Input sanitization and error handling.
* **Demo:**

  <img src="https://github.com/user-attachments/assets/ff6d2051-5057-4168-a73c-c4e3e207d349" alt="Hangman Gameplay" width="600">

---

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/alanliang666/stancodeproject.git](https://github.com/alanliang666/stancodeproject.git)
    cd stancodeproject
    ```

2.  **Run the Fire Detection Script:**
    *(Note: Requires the `simpleimage` module)*
    ```bash
    python3 Python-Portfolio-Projects/Algorithmic_Image_Processing/Fire_Detection_System/fire.py
    ```

---

## 👨‍💻 Author

**Alan Liang**
* Passionate about software development and algorithmic problem solving.
* Open to collaboration and code reviews.
