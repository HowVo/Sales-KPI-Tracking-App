# sales_rep_management.py
from database import connect_db

def add_sales_rep(rep_id, name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sales_reps (id, name) VALUES (?, ?)', (rep_id, name))
    conn.commit()
    conn.close()

def list_sales_reps():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sales_reps')
    reps = cursor.fetchall()
    conn.close()
    return reps

def remove_sales_rep(rep_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sales_reps WHERE id = ?', (rep_id,))
    conn.commit()
    conn.close()

def update_sales_data(rep_id, show_count, offer_count, close_count, cash_per_call, revenue_per_call):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO sales_data (rep_id, show_count, offer_count, close_count, cash_per_call, revenue_per_call)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (rep_id, show_count, offer_count, close_count, cash_per_call, revenue_per_call))
    conn.commit()
    conn.close()