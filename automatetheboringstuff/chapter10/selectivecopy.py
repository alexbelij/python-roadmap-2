import os, shutil

def movefiles(olddir, newdir):
    extension = ['.jpg', '.pdf']
    print(olddir)

    for ext in extension:
        for folders, subfolders, filenames in os.walk(olddir):
            for filename in filenames:
                if filename.lower().endswith(ext):
                    os.chdir(folders)
                    shutil.move(filename, newdir)
                    print("moved: ", filename)

if __name__ == "__main__":
    ######################################
    # CHANGE OS.DIR() and NEW_DIR
    os.chdir('/oldfolder')
    new_dir = '/newfolder'
    my_dir = os.getcwd()
    movefiles(my_dir, new_dir)