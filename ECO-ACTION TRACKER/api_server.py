from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# --- Database Setup ---
conn = sqlite3.connect("eco_actions.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action_type TEXT,
    description TEXT,
    date TEXT
)
""")
conn.commit()

# --- Data Model ---
class EcoAction(BaseModel):
    action_type: str
    description: str
    date: str

# --- API Route ---
@app.post("/log")
def log_action(action: EcoAction):
    cursor.execute(
        "INSERT INTO actions (action_type, description, date) VALUES (?, ?, ?)",
        (action.action_type, action.description, action.date)
    )
    conn.commit()
    return {"message": "Action logged successfully"}
