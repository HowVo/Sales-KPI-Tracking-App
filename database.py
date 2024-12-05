# database.py
import sqlite3

def connect_db():
    return sqlite3.connect('sales.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_reps (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_data (
        rep_id INTEGER PRIMARY KEY,
        num_calls INTEGER,
        show_count INTEGER,
        offer_count INTEGER,
        close_count INTEGER,
        cash_collected REAL,
        FOREIGN KEY(rep_id) REFERENCES sales_reps(id)
    )
    ''')

    conn.commit()
    conn.close()