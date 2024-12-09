import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from database import create_tables
from sales_rep_management import add_sales_rep, list_sales_reps, remove_sales_rep, update_sales_data
from kpi_calculations import calculate_kpis


def add_rep():
   rep_id = entry_id.get()
   name = entry_name.get()
   num_calls = entry_num_calls.get() or 0
   show_count = entry_show_count.get() or 0   
   offer_count = entry_offer_count.get() or 0
   close_count = entry_close_count.get() or 0


   if rep_id and name:
       try:
           rep_id = int(rep_id)
           num_calls = int(num_calls) if num_calls else 0
           show_count = int(show_count) if show_count else 0
           offer_count = int(offer_count) if offer_count else 0
           close_count = int(close_count) if close_count else 0
           add_sales_rep(rep_id, name)
           entry_id.delete(0, tk.END)
           entry_name.delete(0, tk.END)
           entry_num_calls.delete(0, tk.END)
           entry_show_count.delete(0, tk.END)
           entry_offer_count.delete(0, tk.END)
           entry_close_count.delete(0, tk.END)
           list_reps()
       except ValueError:
           messagebox.showwarning("Input Error", "Please enter valid data.")
   else:
       messagebox.showwarning("Input Error", "Please fill in all fields.")




def list_reps():
   reps = list_sales_reps()
   listbox_reps.delete(0, tk.END)
   for rep in reps:
       listbox_reps.insert(tk.END, f"ID: {rep[0]:04d} - Name: {rep[1]}")




def show_kpis():
   selected_rep = listbox_reps.curselection()
   if selected_rep:
       rep_id = int(listbox_reps.get(selected_rep).split()[1])
       kpis = calculate_kpis(rep_id)
       if kpis:
           kpi_text = '\n'.join([f"{key}: {value:.2f}" for key, value in kpis.items()])
           messagebox.showinfo("KPIs", kpi_text)
       else:
           messagebox.showinfo("No Data", "No data available for the selected sales rep.")
   else:
       messagebox.showwarning("Selection Error", "Please select a sales rep.")




def remove_rep():
   selected_rep = listbox_reps.curselection()
   if selected_rep:
       rep_id = int(listbox_reps.get(selected_rep).split()[1])
       remove_sales_rep(rep_id)
       messagebox.showinfo("Success", f"Sales rep with ID '{rep_id:04d}' removed successfully!")
       list_reps()
   else:
       messagebox.showwarning("Selection Error", "Please select a sales rep.")




def update_kpi_data():
   selected_rep = listbox_reps.curselection()
   if selected_rep:
       rep_id = int(listbox_reps.get(selected_rep).split()[1])
       num_calls = entry_num_calls.get()
       show_count = entry_show_count.get()
       offer_count = entry_offer_count.get()
       close_count = entry_close_count.get()
       cash_collected = entry_cash_collected.get()


       if num_calls and show_count and offer_count and close_count and cash_collected:
           try:
               num_calls = int(num_calls)
               show_count = int(show_count)
               offer_count = int(offer_count)
               close_count = int(close_count)
               cash_collected = float(cash_collected)
               update_sales_data(rep_id, num_calls, show_count, offer_count, close_count, cash_collected)
               messagebox.showinfo("Success", "KPI data updated successfully!")
               entry_num_calls.delete(0, tk.END)
               entry_show_count.delete(0, tk.END)
               entry_offer_count.delete(0, tk.END)
               entry_close_count.delete(0, tk.END)
               entry_cash_collected.delete(0, tk.END)
           except ValueError:
               messagebox.showwarning("Input Error", "Please enter valid data.")
       else:
           messagebox.showwarning("Input Error", "Please fill in all fields.")
   else:
       messagebox.showwarning("Selection Error", "Please select a sales rep.")
      


def center_window(root, width=900, height=600):
   screen_width = root.winfo_screenwidth()
   screen_height = root.winfo_screenheight()
   x = (screen_width // 2) - (width // 2)
   y = (screen_height // 2) - (height // 2)
   root.geometry(f'{width}x{height}+{x}+{y}')




def draw_revenue_comparison():
   reps = list_sales_reps()
   rep_ids = [rep[0] for rep in reps]
   rep_names = [rep[1] for rep in reps]
   avg_made_per_call_values = []

   for rep_id in rep_ids:
       kpis = calculate_kpis(rep_id)
       if kpis:
           avg_made_per_call_values.append(kpis['avg_made_per_call'])
       else:
           avg_made_per_call_values.append(0)

   plt.figure(figsize=(10, 6))
   bars = plt.bar(rep_ids, avg_made_per_call_values, color='blue')
   plt.xlabel('Sales Rep ID')
   plt.ylabel('Average Made Per Call')
   plt.title('Average Made Per Call for Each Sales Rep')

   for bar, rep_name in zip(bars, rep_names):
       yval = bar.get_height()
       plt.text(bar.get_x() + bar.get_width()/2, yval, rep_name, ha='center', va='bottom')

   plt.show()

def main():
   create_tables()


   global entry_id, entry_name, listbox_reps, entry_num_calls, entry_show_count, entry_offer_count, entry_close_count, entry_cash_collected


   root = tk.Tk()
   root.title("Sales Rep Management")
   center_window(root)


   frame = tk.Frame(root)
   frame.pack(pady=10)


   tk.Label(frame, text="Sales Rep ID:").grid(row=0, column=0, padx=5, pady=5)
   entry_id = tk.Entry(frame)
   entry_id.grid(row=0, column=1, padx=5, pady=5)


   tk.Label(frame, text="Sales Rep Name:").grid(row=1, column=0, padx=5, pady=5)
   entry_name = tk.Entry(frame)
   entry_name.grid(row=1, column=1, padx=5, pady=5)


   tk.Button(frame, text="Add Sales Rep", command=add_rep).grid(row=0, column=2, rowspan=2, padx=5, pady=5)


   tk.Label(frame, text="Sales Reps:").grid(row=2, column=0, padx=5, pady=5)
   listbox_reps = tk.Listbox(frame, width=50)
   listbox_reps.grid(row=2, column=1, columnspan=2, padx=5, pady=5)


   tk.Button(frame, text="Show KPIs", command=show_kpis).grid(row=3, column=1, pady=10)
   tk.Button(frame, text="Remove Sales Rep", command=remove_rep).grid(row=3, column=2, pady=10)


   tk.Label(frame, text="Number of Calls:").grid(row=4, column=0, padx=5, pady=5)
   entry_num_calls = tk.Entry(frame)
   entry_num_calls.grid(row=4, column=1, padx=5, pady=5)


   tk.Label(frame, text="Show Count:").grid(row=5, column=0, padx=5, pady=5)
   entry_show_count = tk.Entry(frame)
   entry_show_count.grid(row=5, column=1, padx=5, pady=5)


   tk.Label(frame, text="Offer Count:").grid(row=6, column=0, padx=5, pady=5)
   entry_offer_count = tk.Entry(frame)
   entry_offer_count.grid(row=6, column=1, padx=5, pady=5)


   tk.Label(frame, text="Close Count:").grid(row=7, column=0, padx=5, pady=5)
   entry_close_count = tk.Entry(frame)
   entry_close_count.grid(row=7, column=1, padx=5, pady=5)


   tk.Label(frame, text="Cash Collected:").grid(row=8, column=0, padx=5, pady=5)
   entry_cash_collected = tk.Entry(frame)
   entry_cash_collected.grid(row=8, column=1, padx=5, pady=5)


   tk.Button(frame, text="Update KPI Data", command=update_kpi_data).grid(row=9, column=2, pady=10)
   tk.Button(frame, text="Draw Avg Made Per Call Chart", command=draw_revenue_comparison).grid(row=9, column=1, pady=10)


   list_reps()


   root.mainloop()


if __name__ == '__main__':
   main()

