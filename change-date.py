import os
import datetime

def change_last_modified_date(folder_path):
    print(f"Starting in Folder: {folder_path}")

    current_date = datetime.datetime.now()
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"File: {file_path} - Done")
            os.utime(file_path, (current_date.timestamp(), current_date.timestamp()))

    print("Changing Last modified: DONE")

if __name__ == "__main__":
    while True:
        folder_path = input("Enter Path: ")
        change_last_modified_date(folder_path)

        response = input("Want to change another folder? (Y/N): ")
        if response.lower() != "Y":
            break
