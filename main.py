import os

def display_text(msg):
    print("-"*25)
    print(msg)
    print("-"*25)

def get_folder_path():
    folder_path = input("Enter folder path: ")
    return folder_path

def validate_folder(folder_path):
    if os.path.exists(folder_path):
        return True
        
    else:
        return False
        
        
def main():
    display_text("File Organizer Started")
    
    folder_path = get_folder_path()
    
    if validate_folder(folder_path):
        display_text("Folder Found 🥳")
    else:
        display_text("OOOPs! Folder does not exist.")
        
main()