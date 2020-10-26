import os, shutil

######################################
# CHANGE OS.DIR() and NEW_DIR
os.chdir('/oldfolder')
new_dir = '/newfolder'
my_dir = os.getcwd()
extension = ['.jpg', '.pdf']
print(my_dir)


for ext in extension:
    for folders, subfolders, filenames in os.walk(my_dir):
        for filename in filenames:
            if filename.lower().endswith(ext):
                os.chdir(folders)
                shutil.move(filename, new_dir)
                print("moved: ", filename)