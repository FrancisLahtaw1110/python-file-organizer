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

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".tiff": "Images",
    ".tif": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".ico": "Images",
    ".heic": "Images",
    ".heif": "Images",
    ".raw": "Images",
    ".cr2": "Images",
    ".cr3": "Images",
    ".nef": "Images",
    ".arw": "Images",
    ".dng": "Images",

    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",
    ".tex": "Documents",
    ".md": "Documents",
    ".pages": "Documents",

    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".xlsm": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".ods": "Spreadsheets",
    ".tsv": "Spreadsheets",

    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".pptm": "Presentations",
    ".odp": "Presentations",
    ".key": "Presentations",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".m4v": "Videos",
    ".mpeg": "Videos",
    ".mpg": "Videos",
    ".3gp": "Videos",
    ".3g2": "Videos",

    # Music / Audio
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".aac": "Music",
    ".ogg": "Music",
    ".oga": "Music",
    ".m4a": "Music",
    ".wma": "Music",
    ".aiff": "Music",
    ".aif": "Music",
    ".opus": "Music",
    ".mid": "Music",
    ".midi": "Music",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".bz2": "Archives",
    ".xz": "Archives",
    ".tgz": "Archives",

    # Code / Programming
    ".py": "Code",
    ".pyw": "Code",
    ".js": "Code",
    ".jsx": "Code",
    ".mjs": "Code",
    ".cjs": "Code",
    ".ts": "Code",
    ".tsx": "Code",
    ".java": "Code",
    ".c": "Code",
    ".h": "Code",
    ".cpp": "Code",
    ".cc": "Code",
    ".cxx": "Code",
    ".hpp": "Code",
    ".cs": "Code",
    ".go": "Code",
    ".rs": "Code",
    ".php": "Code",
    ".rb": "Code",
    ".swift": "Code",
    ".kt": "Code",
    ".kts": "Code",
    ".dart": "Code",
    ".r": "Code",
    ".scala": "Code",
    ".pl": "Code",
    ".lua": "Code",

    # Web
    ".html": "Web",
    ".htm": "Web",
    ".css": "Web",
    ".scss": "Web",
    ".sass": "Web",
    ".less": "Web",
    ".vue": "Web",
    ".svelte": "Web",

    # Data
    ".json": "Data",
    ".xml": "Data",
    ".yaml": "Data",
    ".yml": "Data",
    

    # Database
    ".sql": "Database",
    ".db": "Database",
    ".sqlite": "Database",
    ".sqlite3": "Database",

    # Configuration
    ".env": "Configuration",
    ".ini": "Configuration",
    ".cfg": "Configuration",
    ".conf": "Configuration",
    ".toml": "Configuration",

    # Applications / Installers
    ".exe": "Applications",
    ".msi": "Applications",
    ".app": "Applications",
    ".dmg": "Applications",
    ".deb": "Applications",
    ".rpm": "Applications",
    ".apk": "Applications",

    # Disk Images
    ".iso": "Disk Images",
    ".img": "Disk Images",
    ".bin": "Disk Images",

    # Fonts
    ".ttf": "Fonts",
    ".otf": "Fonts",
    ".woff": "Fonts",
    ".woff2": "Fonts",

    # 3D
    ".obj": "3D",
    ".fbx": "3D",
    ".stl": "3D",
    ".blend": "3D",
    ".dae": "3D",
    ".3ds": "3D",

    # CAD
    ".dwg": "CAD",
    ".dxf": "CAD",
    ".step": "CAD",
    ".stp": "CAD",

    # Ebooks
    ".epub": "Ebooks",
    ".mobi": "Ebooks",
    ".azw": "Ebooks",
    ".azw3": "Ebooks",

    # Subtitles
    ".srt": "Subtitles",
    ".vtt": "Subtitles",
    ".ass": "Subtitles",
    ".ssa": "Subtitles",

    # Email
    ".eml": "Email",
    ".msg": "Email",

    # Backups
    ".bak": "Backups",
    ".backup": "Backups",

    # Logs
    ".log": "Logs",
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
    category_counts = {}
    count = 0
    for item in items:
        source_path = os.path.join(folder_path, item)
        
        if os.path.isfile(source_path):
            movefile(folder_path,item)
            count+=1
            extension = get_extension(item)
            category = get_category(extension)
            if category in category_counts:
                category_counts[category]+=1
            else:
                category_counts[category]=1
    return count,category_counts
    
        
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
        
def file_count(folder_path):
    category_counts = {}
    total_count = 0
    items = os.listdir(folder_path)
    for item in items:
        item_path= os.path.join(folder_path,item)
        if os.path.isdir(item_path):
            elements = os.listdir(item_path)
            category_counts[item] = 0
            for element in elements:
                element_path = os.path.join(item_path,element)
                if os.path.isfile(element_path):
                    category_counts[item]+=1
            total_count+=category_counts[item]
    return total_count,category_counts

        


def main():
    display_text("File Organizer Started")
    
    folder_path = get_folder_path()
    
    if validate_folder(folder_path):
        display_text("Folder Found 🥳")
        items = scan_folder(folder_path)
        display_files(folder_path,items)
        create_category_folders(folder_path,items)
        total_count_moved,category_count_moved = move_files(folder_path, items)
        display_text("Organization Complete!")
        display_text("Total moved file number & Numbers of moved files to each folder")
        print("Total files moved: ", total_count_moved)
        for category, count in category_count_moved.items():
            print(f"{category}: {count}")
        total_count,category_count = file_count(folder_path)
        display_text("Total Number of current files and Numbers of current files to each folder")
        print("Total files: ", total_count)
        for category, count in category_count.items():
            print(f"{category}: {count}")  
    else:
        display_text("OOOPs! Folder does not exist.")
        
main()
