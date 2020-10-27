# Find files with a given prefix spam###.txt and finds a gap between the numbering.
# It then finds the next number and renames it to fill in the gap.
# Not the best way to do it but this works.
import os, shutil

def find_gap(location):
    '''
    Finds and fills in the numbering gap in a prefix name of a file spam###.txt
    '''
    source = os.path.abspath(location)
    filename = os.listdir(source)
    print("source: ", source)
    filename.sort()
    print("filenames: ", filename)
    indexctr = len(filename)
    print("index: ", indexctr)
    iterator = 1
    numbering = []

    # loop through filename and append items to numbering []
    for x in filename:
        newx = x.strip("spam.txt")
        numbering.append(int(newx))
    print(numbering)


    for f in filename:
        if iterator not in numbering:
            print("Iterator: ", iterator)
            jterator = iterator
            for jterator in range(jterator, len(numbering)+1):
                strjterator = str(jterator)
                fill = strjterator.zfill(3)
                fill = "spam" + fill + ".txt"
                if filename[jterator-1] in os.listdir(location):
                    shutil.move(os.path.join(source, filename[jterator-1]), os.path.join(source, fill))
                    print(os.path.join(source, filename[jterator-1]) + " renamed to " + os.path.join(source, fill))
            break # just needed to find 1 mismatch and all files will be renamed in order.
        iterator += 1

if __name__ == "__main__":
    os.chdir('/secretfolder')
    my_dir = os.getcwd()
    print(my_dir)
    find_gap(my_dir)