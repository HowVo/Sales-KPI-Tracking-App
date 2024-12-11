from database import connect_db


def calculate_kpis(rep_id):
   conn = connect_db()
   cursor = conn.cursor()
   cursor.execute('SELECT * FROM sales_data WHERE rep_id = ?', (rep_id,))
   data = cursor.fetchall()
   conn.close()


   if not data:
       print(f"No data found for rep_id {rep_id}")
       return None


   print(f"Data fetched for rep_id {rep_id}: {data}")


   num_calls = data[0][1]
   show_count = data[0][2]
   offer_count = data[0][3]
   close_count = data[0][4]
   cash_collected = data[0][5]


   print(f"Data extracted for rep_id {rep_id}: num_calls={num_calls}, show_count={show_count}, offer_count={offer_count}, close_count={close_count}")


   show_percentage = show_count / num_calls if num_calls else 0
   offer_percentage = offer_count / show_count if show_count else 0
   close_percentage = close_count / offer_count if offer_count else 0
   avg_made_per_call = cash_collected / num_calls if num_calls else 0


   print(f"Calculated KPIs for rep_id {rep_id}: show_percentage={show_percentage}, offer_percentage={offer_percentage}, close_percentage={close_percentage}, cash_collected={cash_collected}, avg_made_per_call={avg_made_per_call}")


   return {
       'show_percentage': show_percentage,
       'offer_percentage': offer_percentage,
       'close_percentage': close_percentage,
       'cash_collected': cash_collected,
       'avg_made_per_call': avg_made_per_call,
       'num_calls': num_calls
   }



