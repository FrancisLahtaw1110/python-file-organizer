import os

def display_text(msg):
    print("-"*25)
    print(msg)
    print("-"*25)

def get_folder_path():
    folder_path = input("Enter folder path: ").strip("\"'")
    return folder_path

def validate_folder(folder_path):
    if os.path.exists(folder_path):
        return True
        
    else:
        return False

def scan_folder(folder_path):
    items = os.listdir(folder_path)
    return items

def display_files(folder_path,items):
    found_file = False
    
    for item in items:
        item_path = os.path.join(folder_path,item)
        
        if os.path.isfile(item_path):
            print(item)
            found_file = True
            
    if not found_file:
        display_text("NO Files")
    
def main():
    display_text("File Organizer Started")
    
    folder_path = get_folder_path()
    
    if validate_folder(folder_path):
        display_text("Folder Found 🥳")
        items = scan_folder(folder_path)
        display_files(folder_path,items)
    else:
        display_text("OOOPs! Folder does not exist.")
        
main()