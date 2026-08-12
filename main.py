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
            extension = get_extension(item)
            category = get_category(extension)
            print(item)
            print("Extension:", extension)
            print("Category:", category)
            print("\n")
            found_file = True
            
    if not found_file:
        display_text("NO Files")
        
def get_extension(filename):
        extension = os.path.splitext(filename)[1].lower()
        if not extension:
            return None
        return extension
CATEGORY_TABLE = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    ".mp3": "Music",
    ".wav": "Music",

    ".zip": "Archives",
    ".rar": "Archives",
    
    ".py" : "Python",
    ".html": "HTML",
    
    
}

def get_category(extension):
    category = CATEGORY_TABLE.get(extension, "Others")
    return category

def create_category_folder(folder_path,category):
    check_folder_path = os.path.join(folder_path,category)
    if os.path.exists(check_folder_path):
        return True
    else :
        os.makedirs(check_folder_path)
        if os.path.exists(check_folder_path):
            return True
        return False    

def create_category_folders(folder_path,items):
     for item in items:
        item_path = os.path.join(folder_path,item)
            
        if os.path.isfile(item_path):
            extension = get_extension(item)
            category = get_category(extension)
            create_category_folder(folder_path,category)
    
def main():
    display_text("File Organizer Started")
    
    folder_path = get_folder_path()
    
    if validate_folder(folder_path):
        display_text("Folder Found 🥳")
        items = scan_folder(folder_path)
        display_files(folder_path,items)
        create_category_folders(folder_path,items)
    else:
        display_text("OOOPs! Folder does not exist.")
        
main()

