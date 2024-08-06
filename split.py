import os
import shutil
from sklearn.model_selection import train_test_split
import sys
num = sys.argv[1]
dataset_directory = f'D:/Minor 2/Preprocessing/cropped face/{num}'

# Set the path to the directory where you want to create the train and test directories
output_directory = 'D:/Minor 2/Preprocessing/splitdataset'

# Set the ratio for train-test split (e.g., 80% train, 20% test)
train_ratio = 0.8

# Get the list of all image files in the dataset directory
all_images = [f for f in os.listdir(dataset_directory) if os.path.isfile(os.path.join(dataset_directory, f))]

# Split the list of images into train and test sets
train_images, test_images = train_test_split(all_images, train_size=train_ratio, test_size=1 - train_ratio, random_state=42)

# Create train and test directories
train_directory = os.path.join(output_directory, 'new folder')
test_directory = os.path.join(output_directory, f'test/{num}')

os.makedirs(train_directory, exist_ok=True)
os.makedirs(test_directory, exist_ok=True)

# Move images to train directory
for image in train_images:
    src_path = os.path.join(dataset_directory, image)
    dest_path = os.path.join(train_directory, image)
    shutil.copy(src_path, dest_path)

# Move images to test directory
for image in test_images:
    src_path = os.path.join(dataset_directory, image)
    dest_path = os.path.join(test_directory, image)
    shutil.copy(src_path, dest_path)

import os
import shutil
from sklearn.model_selection import train_test_split

# Set the path to your dataset directory
dataset_directory = 'D:/Minor 2/Preprocessing/splitdataset/new folder'

# Set the path to the directory where you want to create the train and test directories
output_directory = 'D:/Minor 2/Preprocessing/splitdataset'

# Set the ratio for train-test split (e.g., 80% train, 20% test)
train_ratio = 0.8

# Get the list of all image files in the dataset directory
all_images = [f for f in os.listdir(dataset_directory) if os.path.isfile(os.path.join(dataset_directory, f))]

# Split the list of images into train and test sets
train_images, test_images = train_test_split(all_images, train_size=train_ratio, test_size=1 - train_ratio, random_state=42)

# Create train and test directories
train_directory = os.path.join(output_directory, f'train/{num}')
test_directory = os.path.join(output_directory, f'valid/{num}')

os.makedirs(train_directory, exist_ok=True)
os.makedirs(test_directory, exist_ok=True)

# Move images to train directory
for image in train_images:
    src_path = os.path.join(dataset_directory, image)
    dest_path = os.path.join(train_directory, image)
    shutil.copy(src_path, dest_path)

# Move images to test directory
for image in test_images:
    src_path = os.path.join(dataset_directory, image)
    dest_path = os.path.join(test_directory, image)
    shutil.copy(src_path, dest_path)

try:
    shutil.rmtree('D:/Minor 2/Preprocessing/splitdataset/new folder')
    print("Directory  successfully deleted.")
except OSError as e:
    print("Error:")