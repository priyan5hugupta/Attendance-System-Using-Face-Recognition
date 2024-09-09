import tkinter as tk
from tkinter import PhotoImage
import subprocess

def new_data_entry():
    
    subprocess.run(['python', 'data_entry.py'], text=True, capture_output=True)

def mark_attendance():
    # Example subprocess command 2
    subprocess.run(['python', 'date.py'],  text=True, capture_output=True)


# Create the main window
root = tk.Tk()
root.title("Tkinter Interface Example")
root.configure(bg='black')

image = tk.PhotoImage(file="download.png")
tk.Label(root, image=image, bg="black").pack(pady=10)



# Create the first button
button1 = tk.Button(root, text="Register New Student", command=new_data_entry, bg='red', fg='yellow')
button1.pack(side=tk.LEFT, padx=20, pady=10)

# Create the second button
button2 = tk.Button(root, text="Mark The Attendance", command=mark_attendance, bg='red', fg='yellow')
button2.pack(side=tk.RIGHT, padx=20, pady=10)

# Start the Tkinter main loop
root.mainloop()
