import os
import shutil

from_dir="C:/Users/DELL/Downloads"
to_dir="C:/UsersDELL/Downloads/wh"

list_of_files=os.listdir(from_dir)
#print(list_of_files)


for file_name in list_of_files:
    name, extension = os.path.splitext(file_name) 
    print(name)
    print(extension)

    if extension == '':
        # Jump to the next file
        continue
    # If the extension is not blank, check if it's in the list of valid extensions
    
if extension in ['.txt’, ‘.doc’, ‘.docx’, ‘.pdf']:
    
    path1=from_dir + '/' + file_name
    path2=to_dir + '/' + "Document_Files" 
    path3=to_dir + '/' +"Document_Files" + '/' + file_name
    print("path1 ",path1)
    print("path3 ",path3)


if os.path.exists(path2):
    print("Moving ", file_name, ".......")
    shutil.move(path1, path3)
else:
    os.makedirs(path2)
    print("Moving" + file_name + "......")
    shutil.move(path1,path3)
    #print("Destination directory does not exist.")
