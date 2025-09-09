import os
import shutil

def organize_folder(folder_path):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar'],
        'Scripts': ['.py', '.js'],
        'Others': []  # for uncategorized files
    }

    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            moved = False
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    moved = True
                    break
            # If no match → move to "Others"
            if not moved:
                target_folder = os.path.join(folder_path, "Others")
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))

    print("✅ Folder organized successfully!")

# 👉 Path to your js folder on Desktop
folder_to_organize = r"C:\Users\fawzan\Desktop\js"
organize_folder(folder_to_organize)
