# Reads from text files and transfers the content to a spreadsheet
import os, openpyxl, logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def transfertextsheet(location):
    content = []
    for folders, subfolders, filenames in os.walk(location):
        ctr = len(filenames)
        jtr = 1
        # For loop to retrieve each file.
        for files in filenames:
            # If the file endswith .txt it opens it.
            if files.endswith('.txt'):
                # Opens the text file and assign its items into the content variable.
                with open(files) as text:
                    content = text.readlines()
                text.close()
                logging.debug('contents length here: %s' % (len(files)))
                writetosheet(content, jtr)
                jtr += 1


def writetosheet(lines, col):
    spread_sheet_name = 'texttosheet.xlsx'
    files = os.listdir()

    # This for loop checks if spread_sheet_name "texttosheet.xlsx" exists.
    for fil in files:
        if fil == spread_sheet_name:
            xcel = openpyxl.load_workbook(spread_sheet_name)
        else:
            xcel = openpyxl.Workbook()
    # Retrieves the spreadsheet name and assigns the first sheet to the "sheet" variable.
    wb = xcel.get_sheet_names()
    sheet = xcel.get_sheet_by_name(wb[0])

    logging.debug('lines list: %s' % (lines))
    logging.debug('Sheet: %s' % (sheet))
    rw = 1

    # This for loop iterates through each line in lines list.
    # and then inserts each line to the cell of the spreadsheet.
    for line in lines:
        logging.debug('line here inside loop: %s, rw: %i, col: %i' % (line.rstrip('\n'), rw, col))
        sheet.cell(row=rw, column=col).value = line.rstrip('\n')
        rw += 1
    # Saves the spreadsheet.
    xcel.save(spread_sheet_name)

if __name__ == "__main__":
    os.chdir('/secretfolder')
    main_dir = os.getcwd()
    logging.debug('Start of main.')
    transfertextsheet(main_dir)