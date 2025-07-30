import os
import shutil

# Prompt user for directory to organize
folder_path = input("Enter the directory path to organize: ").strip()

if not os.path.isdir(folder_path):
    print(f"Error: The path '{folder_path}' is not a valid directory.")
    exit(1)

# Scan directory
for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)
    if not os.path.isfile(full_path):
        continue  # skip directories

    # Determine file extension
    name, ext = os.path.splitext(filename)
    ext = ext.lower().lstrip('.')  # remove dot, normalize lower

    if not ext:
        category = 'NoExtension'
    else:
        category = ext.upper()

    # Create category folder if it doesn't exist
    dest_folder = os.path.join(folder_path, category)
    os.makedirs(dest_folder, exist_ok=True)

    # Move file
    dest_path = os.path.join(dest_folder, filename)
    try:
        shutil.move(full_path, dest_path)
        print(f"Moved: {filename} → {category}/")
    except Exception as e:
        print(f"Error moving {filename}: {e}")

print("Organization complete.")
