import tkinter as tk
from tkinter import messagebox, PhotoImage
import pandas as pd
from gtts import gTTS
import subprocess

def save_to_csv():
    data = {label: entry.get() for label, entry in entries.items()}
    
    if all(data.values()):
        new_data = pd.DataFrame([data])
        
        try:
            df = pd.read_csv('copy.csv')
            df = pd.concat([df, new_data], ignore_index=True)
        except FileNotFoundError:
            df = new_data

        df.to_csv('copy.csv', index=False)

        gTTS(text=data['Name'], lang='en', slow=False).save(f"Audio/{data['SAP ID']}.mp3")
        subprocess.run(['python', 'run_camera.py'], input=data['SAP ID'], text=True, capture_output=True)
        
        for entry in entries.values():
            entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Data saved successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")

root = tk.Tk()
root.title("Data Entry Form")
root.configure(bg="black")

image = PhotoImage(file="download.png")
tk.Label(root, image=image, bg="black").grid(row=0, columnspan=2, pady=10)

labels = ['SAP ID', 'Roll No', 'Name', 'Degree', 'Course', 'Specialization', 'Semester', 'Batch']
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label, bg="black", fg="white").grid(row=i+1, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    entries[label] = entry

tk.Button(root, text="Save to CSV", command=save_to_csv, bg="red", fg="yellow").grid(row=len(labels)+1, columnspan=2, pady=10)

root.mainloop()
