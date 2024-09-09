import cv2
import face_recognition
from tkinter import Tk, Button, Label
from PIL import Image, ImageTk
import numpy as np

import sys

#sapid = sys.stdin.read().strip()
sapid = 500

class FaceCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Capture")

        # Set the background color of the window
        self.root.configure(bg='black')

        self.video_source = 0  # Use 0 for the default camera
        self.vid = cv2.VideoCapture(self.video_source)

        self.canvas = Label(root, bg='black')
        self.canvas.pack()

        self.btn_capture = Button(root, text="Capture", width=10, command=self.capture, bg='red', fg='white')
        self.btn_capture.pack()

        self.update()

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            # Convert the frame to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Detect faces
            face_locations = face_recognition.face_locations(rgb_frame)

            # Draw rectangles around detected faces
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Convert frame to ImageTk format
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.config(image=self.photo)

        self.root.after(10, self.update)

    def capture(self):
        ret, frame = self.vid.read()
        if ret:
            # Convert the frame to RGB (face_recognition expects RGB images)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Detect faces
            face_locations = face_recognition.face_locations(rgb_frame)
            if face_locations:
                face_encoding = face_recognition.face_encodings(rgb_frame)
                print(face_encoding)
                np.savetxt(f'Data/{sapid}.txt',face_encoding, fmt='%.6f')
                # Take the first face found
                top, right, bottom, left = face_locations[0]

                # Crop the image to the face
                cropped_face = frame[top-100:bottom+30, left-30:right+30]

                # Save the cropped face
                filename = f"Face Data/{sapid}.png"
                cv2.imwrite(filename, cropped_face)
                self.vid.release()
                cv2.destroyAllWindows()
                self.root.destroy()
            else:
                print("No faces found in the captured image.")
            
            

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

if __name__ == "__main__":
    root = Tk()
    app = FaceCaptureApp(root)
    root.mainloop()
