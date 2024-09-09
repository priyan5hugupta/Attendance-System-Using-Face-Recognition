import tkinter as tk
from tkinter import Label, Button,messagebox
import cv2
import face_recognition
from PIL import Image, ImageTk
import subprocess
import pandas as pd
import sys

date = sys.stdin.read().strip()


# Create an empty text file
open("name.txt", "w").close()

def update_frame():
    ret, frame = video_capture.read()
    if not ret:
        return

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)

    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    imgtk = ImageTk.PhotoImage(image=img)
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    root.after(10, update_frame)

def capture_image():
    ret, frame = video_capture.read()
    if ret:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if face_recognition.face_locations(rgb_frame):
            cv2.imwrite('captured_image.png', frame)
            subprocess.run(['python', 'review.py'], text=True)

def mark_attendance():
    with open("name.txt", "r") as file:
        ids = [line.strip() for line in file]

    df = pd.read_csv('copy.csv')
    for sap_id in ids:
        df.loc[df['SAP ID'] == int(sap_id), date] = 'P'
    
    messagebox.showinfo("Success", f" Attendance Marked on date {date} successfully!")
    root.destroy()

    df.to_csv('copy.csv', index=False)

root = tk.Tk()
root.title("Face Detection App")
root.configure(bg="black")

video_label = Label(root)
video_label.pack()

Button(root, text="Check", command=capture_image, bg='red', fg='white').pack(side=tk.LEFT, padx=20, pady=10)
Button(root, text="Mark All Attendance", command=mark_attendance, bg='red', fg='white').pack(side=tk.RIGHT, padx=20, pady=10)

video_capture = cv2.VideoCapture(0)
update_frame()

root.mainloop()
video_capture.release()
