Hackathon Project Title : Secure Intelligent Online Examination System

Project Overview :
To build an AI-enabled online examination platform that ensures examination integrity,minimizes malpractice, and enhances assessment quality through intelligent content retrieval,automated evaluation, adaptive testing, and post-exam analytics.

Key Features
Role-Based Access: Secure login for Students and Faculty.

I) AI Anti-Cheat System:
     Detects tab switching and window minimization.
     Tracks focus loss and logs malpractice incidents.
     Enforces full-screen mode constraints.
II) ML Performance Analytics:
     Uses **Linear Regression (Scikit-Learn)** to predict future scores based on response time patterns.
     Visualizes skill gaps and score trends using **Chart.js**.
III) Faculty Dashboard:
Create and publish dynamic exams.
Real-time monitoring of malpractice flags.
"Hardest Question" analysis to identify learning gaps.
Export results to CSV.
IV) Gamification and Rewards:
Student Leaderboards for top performers.
Auto-generated, printable **Certificates** upon passing.

 Tech Stack : 

1) Backend: Python 3.13.5, FastAPI, Uvicorn, SQLite3
2) Frontend: HTML5, CSS3 (Glassmorphism UI), Vue.js (Reactive UI), Chart.js
3) Machine Learning: Scikit-Learn, NumPy
4) Tools: VS Code, Git

 Installation & Setup :

1.  Clone the repository:
    bash
    git clone https://github.com/bloodsight006/Secure-Exam-System.git
    cd Secure-Exam-System
    

2.  Install Dependencies:
    bash
    pip install -r requirements.txt
    

3.  Initialize Database:
    bash
    python database.py
    

4.  Run the Server:
    bash
    uvicorn main:app --reload
    

5.  Access the App:
    Open your browser and go to `http://127.0.0.1:8000`

 Default Credentials: 

| Role | Username | Password |
| :--- | :--- | :--- |
| **Teacher** | teacher1 | admin123 |
| **Student** | student1 | pass1 |

Screenshots
<img width="1500" height="818" alt="image" src="https://github.com/user-attachments/assets/6047d954-6b1b-4af1-99d9-3a66dff404e9" />

<img width="1918" height="1013" alt="image" src="https://github.com/user-attachments/assets/92025064-6a0d-4375-b1f3-a6b19e864fd9" />

<img width="1912" height="1017" alt="image" src="https://github.com/user-attachments/assets/b642db4c-af18-4551-882d-18831f6195a3" />

<img width="1917" height="913" alt="image" src="https://github.com/user-attachments/assets/03e17dc7-1f40-4140-85a8-27673e596642" />

<img width="1912" height="957" alt="image" src="https://github.com/user-attachments/assets/709db1d5-0824-4bff-bd9a-ce657f2cab7f" />

<img width="1917" height="915" alt="image" src="https://github.com/user-attachments/assets/661ed558-8e3c-49b6-b044-b824e3853f1c" />

<img width="1917" height="1015" alt="image" src="https://github.com/user-attachments/assets/2eb24b19-3842-4439-979d-e86a7a874d1b" />




This is a sample protoype website Built for Hackathon 2026. 
