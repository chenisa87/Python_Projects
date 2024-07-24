import os
import shutil

def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def clean_folder(folder_path):

    for filename in os.listdir(folder_path):
        # get full path
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            # print(full_path)
            file_extension = filename.split(".")[-1].lower()
            # print(file_extension)
            if file_extension:
                # name
                subfolder_name = f"{file_extension.upper()} Files"
                # Create folder and return folder location
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                # move file to folder
                shutil.move(full_path, subfolder_path)


if __name__ == "__main__":
    print("Desktop Cleaner Script")
    folder_path = "C:/Users/User/Downloads"
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning complete")
    else:
        print("Invalid folder path: Please ensure the path is correct and try again.")