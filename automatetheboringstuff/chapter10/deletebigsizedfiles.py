# "Delete" files that have a file size of more than 100MB.
import os, shutil

def removefiles(oldir):
    for folders, subfolders, filenames in os.walk(oldir):
        for files in filenames:
            os.chdir(folders)
            size = os.path.getsize(files)
            if size >= 100000000:
                print(os.path.abspath(files))
                os.remove(files)
                print("Successfully removed.")

if __name__ == "__main__":
    os.chdir('/secretfolder')
    oldir = os.getcwd()
    removefiles(oldir)
