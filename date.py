import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import subprocess

def update_csv(date_str):
    try:
        df = pd.read_csv('copy.csv')
        df[date_str] = 'A'
        df.to_csv('copy.csv', index=False)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def on_update_click():
    date_str = date_entry.get() or datetime.now().strftime("%d-%m-%y")
    update_csv(date_str)
    subprocess.run(['python', 'Mark_attendance.py'], input=date_str, text=True)

root = tk.Tk()
root.title("Update CSV Date")
root.configure(bg="black")

image = tk.PhotoImage(file="download.png")
tk.Label(root, image=image, bg="black").pack(pady=10)

tk.Label(root, text="Enter date (DD-MM-YYYY):", bg="black", fg="white").pack(pady=10)
date_entry = tk.Entry(root)
date_entry.insert(0, datetime.now().strftime('%d-%m-%y'))
date_entry.pack(pady=10)

tk.Button(root, text="Update CSV", command=on_update_click, bg="red", fg="yellow").pack(pady=20)

root.mainloop()
