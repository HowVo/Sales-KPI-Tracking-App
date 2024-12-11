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


def update_sales_data(rep_id, num_calls, show_count, offer_count, close_count, cash_collected):
   conn = connect_db()
   cursor = conn.cursor()
   cursor.execute('''
       INSERT OR REPLACE INTO sales_data (rep_id, num_calls, show_count, offer_count, close_count, cash_collected)
       VALUES (?, ?, ?, ?, ?, ?)
   ''', (rep_id, num_calls, show_count, offer_count, close_count, cash_collected))
   conn.commit()
   conn.close()



