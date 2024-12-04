# kpi_calculations.py
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

    total_shows = sum(row[2] for row in data)
    total_offers = sum(row[3] for row in data)
    total_closes = sum(row[4] for row in data)
    total_cash = sum(row[5] for row in data)
    total_revenue = sum(row[6] for row in data)

    show_percentage = (total_shows / len(data)) * 100
    offer_percentage = (total_offers / len(data)) * 100
    close_percentage = (total_closes / len(data)) * 100
    cash_per_call = total_cash / len(data)
    revenue_per_call = total_revenue / len(data)

    print(f"Calculated KPIs for rep_id {rep_id}: show_percentage={show_percentage}, offer_percentage={offer_percentage}, close_percentage={close_percentage}, cash_per_call={cash_per_call}, revenue_per_call={revenue_per_call}")

    return {
        'show_percentage': show_percentage,
        'offer_percentage': offer_percentage,
        'close_percentage': close_percentage,
        'cash_per_call': cash_per_call,
        'revenue_per_call': revenue_per_call
    }