from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict, List
import sqlite3
import os
import json
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression

app = FastAPI()
templates = Jinja2Templates(directory="templates")
if os.path.exists("static"): app.mount("/static", StaticFiles(directory="static"), name="static")

# --- ML MODEL SETUP ---
X_train = np.array([[5], [10], [30], [60], [120], [300]]).reshape(-1, 1)
y_train = np.array([20, 60, 95, 85, 70, 40])
model = LinearRegression()
model.fit(X_train, y_train)

def get_db_connection():
    conn = sqlite3.connect('exam_system.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- DATA MODELS ---
class QuestionModel(BaseModel):
    text: str; options: List[str]; correct: str
class CreateExamModel(BaseModel):
    title: str; creator: str; questions: List[QuestionModel]
class ExamSubmission(BaseModel):
    exam_id: int; username: str; answers: Dict[str, str]; tab_switches: int; time_log: Dict[str, float]

# --- PAGE ROUTES ---
@app.get("/", response_class=HTMLResponse)
async def home(request: Request): return templates.TemplateResponse("login.html", {"request": request})
@app.get("/student/dashboard", response_class=HTMLResponse)
async def s_dash(request: Request): return templates.TemplateResponse("student_dashboard.html", {"request": request})
@app.get("/teacher/dashboard", response_class=HTMLResponse)
async def t_dash(request: Request): return templates.TemplateResponse("teacher_dashboard.html", {"request": request})
@app.get("/instructions", response_class=HTMLResponse)
async def instr(request: Request): return templates.TemplateResponse("instructions.html", {"request": request})
@app.get("/exam", response_class=HTMLResponse)
async def exam(request: Request): return templates.TemplateResponse("exam.html", {"request": request})

# --- API ROUTES ---
@app.post("/login")
async def login(request: Request):
    data = await request.json()
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username=? AND password=?', (data['username'], data['password'])).fetchone()
    conn.close()
    if user: return JSONResponse({"status": "success", "role": user['role'], "username": user['username']})
    return JSONResponse({"status": "error"}, status_code=401)

@app.post("/api/create_exam")
async def create_exam(exam: CreateExamModel):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO exams (title, created_by, created_at) VALUES (?, ?, ?)", (exam.title, exam.creator, datetime.now().strftime("%Y-%m-%d")))
    eid = cursor.lastrowid
    for q in exam.questions:
        cursor.execute("INSERT INTO questions (exam_id, question_text, option_a, option_b, option_c, option_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?, ?)", (eid, q.text, *q.options, q.correct))
    conn.commit(); conn.close()
    return {"message": "Created"}

@app.get("/api/exams")
async def get_exams():
    conn = get_db_connection(); exams = conn.execute("SELECT * FROM exams ORDER BY id DESC").fetchall(); conn.close()
    return [dict(e) for e in exams]

@app.get("/api/exam/{eid}")
async def get_questions(eid: int):
    conn = get_db_connection(); qs = conn.execute("SELECT * FROM questions WHERE exam_id=?", (eid,)).fetchall(); conn.close()
    return [dict(q) for q in qs]

@app.post("/api/submit")
async def submit(sub: ExamSubmission):
    conn = get_db_connection()
    qs = conn.execute("SELECT * FROM questions WHERE exam_id=?", (sub.exam_id,)).fetchall()
    
    score = 0
    total = len(qs)
    for q in qs:
        qid = str(q['id'])
        if qid in sub.answers and sub.answers[qid] == q['correct_answer']:
            score += 1
            
    status = "Safe"
    if sub.tab_switches > 1: status = "Malpractice"
    
    # SAVE ANSWERS FOR REVIEW (Feature 1)
    # We pack the answers into the detailed_log JSON
    log_data = {"user_answers": sub.answers, "time_log": sub.time_log}
    
    conn.execute("INSERT INTO submissions (exam_id, student_name, score, total_questions, tab_switches, anomaly_score, detailed_log, submitted_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                 (sub.exam_id, sub.username, score, total, sub.tab_switches, status, json.dumps(log_data), datetime.now().strftime("%Y-%m-%d")))
    conn.commit(); conn.close()
    return {"score": score}

@app.get("/api/teacher_stats")
async def teacher_stats():
    conn = get_db_connection()
    subs = conn.execute("SELECT * FROM submissions ORDER BY id DESC").fetchall()
    exams = conn.execute("SELECT * FROM exams").fetchall()
    conn.close()
    return {"submissions": [dict(s) for s in subs], "exams": [dict(e) for e in exams]}

@app.get("/api/history/{user}")
async def my_history(user: str):
    conn = get_db_connection()
    hist = conn.execute("SELECT s.*, e.title as exam_title FROM submissions s JOIN exams e ON s.exam_id=e.id WHERE s.student_name=?", (user,)).fetchall()
    conn.close()
    return [dict(h) for h in hist]

# --- NEW: EXAM REVIEW API (Feature 1) ---
@app.get("/api/review/{exam_id}/{username}")
async def review_exam(exam_id: int, username: str):
    conn = get_db_connection()
    sub = conn.execute("SELECT * FROM submissions WHERE exam_id=? AND student_name=?", (exam_id, username)).fetchone()
    qs = conn.execute("SELECT * FROM questions WHERE exam_id=?", (exam_id,)).fetchall()
    conn.close()
    
    if not sub: return []
    
    # Extract stored answers
    try:
        log = json.loads(sub['detailed_log'])
        user_answers = log.get('user_answers', {})
    except:
        user_answers = {}
        
    review_data = []
    for q in qs:
        qid = str(q['id'])
        review_data.append({
            "question": q['question_text'],
            "correct": q['correct_answer'],
            "selected": user_answers.get(qid, "-"),
            "is_correct": user_answers.get(qid) == q['correct_answer']
        })
    return review_data

@app.get("/api/analytics/predict")
async def predict_performance():
    pred = model.predict(np.array([[35]]))
    return {"predicted_score": round(pred[0], 2)}
