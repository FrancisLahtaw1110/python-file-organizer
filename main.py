import os
import shutil

def display_text(msg):
    print("-"* len(msg))
    print(msg)
    print("-"*len(msg))

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

def move_files(folder_path,items):
    for item in items:
        source_path = os.path.join(folder_path, item)
        
        if os.path.isfile(source_path):
            movefile(folder_path,item)
        
def movefile(folder_path,item):
    source_path = os.path.join(folder_path, item)
    extension = get_extension(item)
    category = get_category(extension)
    destination_folder = os.path.join(folder_path,category)
    destination_path = os.path.join(destination_folder,item)
    destination_path = get_unique_destination(destination_path)
    shutil.move(source_path,destination_path)
    
def get_unique_destination(destination_path):
    counter = 1
    filename, extension = os.path.splitext(destination_path)
    while os.path.exists(destination_path):
        destination_path=filename + "_" + str(counter) + extension
        counter+=1
    return destination_path
        
        


def main():
    display_text("File Organizer Started")
    
    folder_path = get_folder_path()
    
    if validate_folder(folder_path):
        display_text("Folder Found 🥳")
        items = scan_folder(folder_path)
        display_files(folder_path,items)
        create_category_folders(folder_path,items)
        move_files(folder_path, items)
    else:
        display_text("OOOPs! Folder does not exist.")
        
#main()
test_path = "/Users/thantunaung/file_organizer_test"

result = movefile(test_path,"photo.jpg")


print(os.listdir("/Users/thantunaung/file_organizer_test/Images"))
