## Hackathon Project Title : Secure Intelligent Online Examination System

## Project Overview
To build an AI-enabled online examination platform that ensures examination integrity,minimizes malpractice, and enhances assessment quality through intelligent content retrieval,automated evaluation, adaptive testing, and post-exam analytics.

## Key Features
* **Role-Based Access:** Secure login for Students and Faculty.
* **AI Anti-Cheat System:**
    * Detects tab switching and window minimization.
    * Tracks focus loss and logs malpractice incidents.
    * Enforces full-screen mode constraints.
* **ML Performance Analytics:**
    * Uses **Linear Regression (Scikit-Learn)** to predict future scores based on response time patterns.
    * Visualizes skill gaps and score trends using **Chart.js**.
* **Faculty Dashboard:**
    * Create and publish dynamic exams.
    * Real-time monitoring of malpractice flags.
    * "Hardest Question" analysis to identify learning gaps.
    * Export results to CSV.
* **Gamification and Rewards:**
    * Student Leaderboards for top performers.
    * Auto-generated, printable **Certificates** upon passing.

## Tech Stack
* **Backend:** Python 3.13.5, FastAPI, Uvicorn, SQLite3
* **Frontend:** HTML5, CSS3 (Glassmorphism UI), Vue.js (Reactive UI), Chart.js
* **Machine Learning:** Scikit-Learn, NumPy
* **Tools:** VS Code, Git

##  Installation & Setup

1.  **Clone the repository:**
    bash
    git clone https://github.com/bloodsight006/Secure-Exam-System.git
    cd Secure-Exam-System
    

2.  **Install Dependencies:**
    bash
    pip install -r requirements.txt
    

3.  **Initialize Database:**
    bash
    python database.py
    

4.  **Run the Server:**
    bash
    uvicorn main:app --reload
    

5.  **Access the App:**
    Open your browser and go to `http://127.0.0.1:8000`

##  Default Credentials

| Role | Username | Password |
| :--- | :--- | :--- |
| **Teacher** | teacher1 | admin123 |
| **Student** | student1 | pass1 |

##  Screenshots
*(Add your screenshots here later)*

This is Built for Hackathon 2026 
