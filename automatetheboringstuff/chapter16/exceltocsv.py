# Reads xlsx files and transfers its content into a csv file.
import csv, openpyxl, os, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def tocsv(location):
    '''
    Locates an .xlsx file and retrieves the sheet name and contents
    will write all content of the sheet to a csv file seperately
    will name every csv file nameofxlsxfile_sheetname.csv
    '''
    files = os.listdir('.')

    for excelFile in files:
        if excelFile.endswith('xlsx'):
            logging.debug('Excel File: %s' % (excelFile))
            xcelObj = openpyxl.load_workbook(excelFile)
            for sheetName in xcelObj.get_sheet_names():
                sheet = xcelObj.get_sheet_by_name(sheetName)
                logging.debug('Sheet: %s' % (sheet))
                # create csv name from excelfilename_sheettitle.csv
                outputFile = open(excelFile.strip('.xlsx') + "_" + sheet.title + '.csv', 'w')
                outputWriter = csv.writer(outputFile)
                for rowNum in range(1, sheet.max_row + 1):
                    rowData = []
                    for colNum in range(1, sheet.max_column + 1):
                        dat = sheet.cell(row=rowNum, column=colNum).value
                        logging.debug('Data: %s, row: %s, column: %s' % (dat, rowNum, colNum))
                        rowData.append(dat)
                    logging.debug('Writing: %s' % (rowData))
                    outputWriter.writerow(rowData)
                outputFile.close()
                

if __name__ == "__main__":
    os.chdir('/secretfolder')
    my_dir = os.getcwd()
    logging.debug('Start of program.\nDirectory is: %s' % (my_dir))
    tocsv(my_dir)
