import os
import sys
num= sys.argv[1]
def rename_images(directory_path, new_prefix):
    # Get a list of all files in the specified directory
    files = os.listdir(directory_path)

    # Filter out only image files (you can customize this based on your file types)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Iterate through the image files and rename them
    for i, file_name in enumerate(image_files, 1):
        # Get the file extension
        file_ext = os.path.splitext(file_name)[1]

        # Create the new file name with the specified prefix and a sequential number
        new_name = f"{new_prefix}_{i}{file_ext}"

        # Construct the full paths for the old and new names
        old_path = os.path.join(directory_path, file_name)
        new_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {file_name} to {new_name}')

# Example usage: replace 'path_to_images' with your actual directory path and 'new_prefix' with your desired prefix
rename_images(f'D:/Minor 2/Data/{num}', 'img')
