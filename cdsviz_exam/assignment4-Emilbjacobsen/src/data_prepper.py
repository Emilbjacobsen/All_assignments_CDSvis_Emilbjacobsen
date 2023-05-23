import os
import shutil
import random
from PIL import Image


# Define the source and destination directories
source_dir = '../data/dataset/dataset_updated/validation_set'
destination_dir = '../data/dataset/dataset_updated/training_set'

# Iterate over subdirectories in the source directory
for subdir in os.listdir(source_dir):
    # Check if the item in the source directory is a directory itself
    if os.path.isdir(os.path.join(source_dir, subdir)):
        # Construct the paths for the corresponding subdirectories in the destination directory
        source_subdir_path = os.path.join(source_dir, subdir)
        destination_subdir_path = os.path.join(destination_dir, subdir)

        # Iterate over files in the source subdirectory
        for file_name in os.listdir(source_subdir_path):
            # Construct the source and destination file paths
            source_file_path = os.path.join(source_subdir_path, file_name)
            destination_file_path = os.path.join(destination_subdir_path, file_name)

            # Move the file to the corresponding subdirectory in the destination directory
            shutil.move(source_file_path, destination_file_path)

# Remove validation_set and musemart directories
shutil.rmtree(source_dir)
shutil.rmtree('../data/musemart/')

# Move training_set to dataset directory
shutil.move(destination_dir, '../data/dataset/')

# Rename dataset_updated to all_files
os.rename('../data/dataset/training_set', '../data/dataset/all_files')




# Set the path to the directory containing the dataset
dataset_dir = '../data/dataset/all_files'

# Set the path to the directory where you want to save the train, validation, and test sets
output_dir = '../data'

# Set the desired split ratios (e.g., 70% train, 15% validation, 15% test)
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create the train, validation, and test directories within the output directory
train_dir = os.path.join(output_dir, 'train')
val_dir = os.path.join(output_dir, 'validation')
test_dir = os.path.join(output_dir, 'test')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Iterate over the subdirectories in the dataset directory
for subdir in os.listdir(dataset_dir):
    subdir_path = os.path.join(dataset_dir, subdir)
    if not os.path.isdir(subdir_path):
        continue
    
    # Create the corresponding subdirectories in the train, validation, and test directories
    train_subdir = os.path.join(train_dir, subdir)
    val_subdir = os.path.join(val_dir, subdir)
    test_subdir = os.path.join(test_dir, subdir)
    
    os.makedirs(train_subdir, exist_ok=True)
    os.makedirs(val_subdir, exist_ok=True)
    os.makedirs(test_subdir, exist_ok=True)
    
    # Get the list of files in the current subdirectory
    files = os.listdir(subdir_path)
    random.shuffle(files)
    
    # Split the files into train, validation, and test sets based on the ratios
    train_files = files[:int(train_ratio * len(files))]
    val_files = files[int(train_ratio * len(files)):int((train_ratio + val_ratio) * len(files))]
    test_files = files[int((train_ratio + val_ratio) * len(files)):]
    
    # Move the files to the corresponding subdirectories in the train, validation, and test directories
    for file in train_files:
        src_path = os.path.join(subdir_path, file)
        dest_path = os.path.join(train_subdir, file)
        shutil.copy(src_path, dest_path)
    
    for file in val_files:
        src_path = os.path.join(subdir_path, file)
        dest_path = os.path.join(val_subdir, file)
        shutil.copy(src_path, dest_path)
    
    for file in test_files:
        src_path = os.path.join(subdir_path, file)
        dest_path = os.path.join(test_subdir, file)
        shutil.copy(src_path, dest_path)

dataset_rm = os.path.join("..", "data", "dataset")

shutil.rmtree(dataset_rm)




def process_images(directory):
    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        # Create the full file path
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            # If the current item is a subdirectory, recursively call the function
            process_images(file_path)
        else:
            try:
                # Attempt to open the image using Pillow
                image = Image.open(file_path)

                

                # Close the image after viewing
                image.close()

            except Exception as e:
                # Print the error message if an exception occurs
                print(f"Error opening image: {file_path}")
                print(f"Error message: {str(e)}")

                # Delete the file if an error occurs
                os.remove(file_path)


# Specify the directory path containing the images
directory = "../data/"

# Call the function to process images in the directory and its subdirectories
process_images(directory)






