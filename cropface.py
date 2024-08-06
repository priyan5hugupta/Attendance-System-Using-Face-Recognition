import os
import cv2
import sys
import face_recognition
from PIL import Image
num = '500096748'
def detect_and_crop_faces(input_directory, output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each image in the input directory
    for file_name in os.listdir(input_directory):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Load the image using face_recognition
            image_path = os.path.join(input_directory, file_name)
            img = face_recognition.load_image_file(image_path)

            # Find all face locations in the image
            face_locations = face_recognition.face_locations(img)

            # Crop and save each detected face
            for i, (top, right, bottom, left) in enumerate(face_locations, 1):
                face_image = img[top:bottom, left:right]
                pil_image = Image.fromarray(face_image)
                output_path = os.path.join(output_directory, f"{os.path.splitext(file_name)[0]}_face{i}.png")
                pil_image.save(output_path)
                print(f"Face detected and saved: {output_path}")
                
# Example usage: replace 'input_images' and 'output_faces' with your actual directory paths
detect_and_crop_faces(f'D:/Minor 2/Data/{num}', f'D:/Minor 2/Preprocessing/cropped face/{num}')
