import os
import subprocess



directory_path = 'D:/Minor 2/Data'  # Replace with your actual directory path
contents = os.listdir(directory_path)

for _ in contents:
    inputvalue = _
    subprocess.run(['python','D:/Minor 2/Preprocessing/Code/renamefile.py',inputvalue])
    subprocess.run(['python','D:/Minor 2/Preprocessing/Code/cropface.py',inputvalue])
    subprocess.run(['python','D:/Minor 2/Preprocessing/Code/split.py',inputvalue])

subprocess.run(['python','D:/Minor 2/Preprocessing/Code/preprocessing.py',inputvalue])
    
      