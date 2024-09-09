import os
import numpy as np
import face_recognition
import cv2
import pygame
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Label, Button

# Load encodings from files in the 'Data' directory
directory = 'Data'
file_list = [f.replace('.txt', '') for f in os.listdir(directory) if f.endswith('.txt')]
encoding = [np.loadtxt(os.path.join(directory, f'{file}.txt')) for file in file_list]

# Load and process the image with unknown faces
unknown_image = face_recognition.load_image_file("captured_image.png")
unknown_face_encodings = face_recognition.face_encodings(unknown_image)
face_locations = face_recognition.face_locations(unknown_image)
unknown_image_bgr = cv2.cvtColor(unknown_image, cv2.COLOR_RGB2BGR)

name = "Unknown"
for (top, right, bottom, left), face_encoding in zip(face_locations, unknown_face_encodings):
    matches = face_recognition.compare_faces(encoding, face_encoding)
    if True in matches:
        name = file_list[matches.index(True)]
    
    cv2.rectangle(unknown_image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(unknown_image_bgr, name, (left, bottom + 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

cv2.imwrite("output_image.png", unknown_image_bgr)

# Play the corresponding sound
pygame.mixer.init()
sound_path = f"Audio/{name}.mp3"
sound = pygame.mixer.Sound(sound_path)
sound.play()
pygame.time.wait(int(sound.get_length() * 1000))

pygame.mixer.init()
sound_path = "present.mp3"
sound = pygame.mixer.Sound(sound_path)
sound.play()
pygame.time.wait(int(sound.get_length() * 1000))

# Tkinter GUI to display the image and provide options to mark attendance
def mark():
    with open("name.txt", "a") as file:
        file.write(f"{name}\n")
    root.destroy()

def close():
    root.destroy()

root = tk.Tk()
root.title("Display Image")
root.configure(bg='black')

try:
    image = Image.open("output_image.png")
    photo = ImageTk.PhotoImage(image)
    Label(root, image=photo).pack()
except Exception as e:
    print(f"Error loading image: {e}")
    root.destroy()
    exit()

Button(root, text="Mark", command=mark, bg='red', fg='yellow').pack(side=tk.LEFT, padx=20, pady=10)
Button(root, text="Wrong", command=close, bg='red', fg='yellow').pack(side=tk.RIGHT, padx=20, pady=10)

root.mainloop()
