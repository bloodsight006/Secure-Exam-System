import sqlite3

def init_db():
    conn = sqlite3.connect('exam_system.db')
    c = conn.cursor()
    
    # Create Tables
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, role TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS exams (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, created_by TEXT, created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, exam_id INTEGER, question_text TEXT, option_a TEXT, option_b TEXT, option_c TEXT, option_d TEXT, correct_answer TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS submissions (id INTEGER PRIMARY KEY AUTOINCREMENT, exam_id INTEGER, student_name TEXT, score INTEGER, total_questions INTEGER, tab_switches INTEGER, anomaly_score TEXT, detailed_log TEXT, submitted_at TEXT)''')
    
    # Add Default Users
    users = [('teacher1', 'admin123', 'teacher'), ('student1', 'pass1', 'student'), ('student2', 'pass2', 'student'), ('student3', 'pass3', 'student')]
    for u in users:
        try: c.execute("INSERT INTO users VALUES (?, ?, ?)", u)
        except: pass
            
    conn.commit()
    conn.close()
    print("Database Updated Successfully!")

if __name__ == "__main__":
    init_db()
    
