from re import findall
from withLibrary import write_header
from withLibrary import write_row

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
          'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

def read_array(fileString,values):
    """Return values finded using regular expressions in string of input file

    Keyword arguments:
    fileName - name of input file
    values which may be readed: 0 - names, 1 - dates
    """
    pattern = r"[A-Za-z]{1,10} [A-Za-z]{2,10}" if values == 0 else r"[A-Za-z]{3} \d{2} \d{4}"
    finded = findall(pattern,fileString)
    array = []
    for i in finded:
        if(i not in array):
            array.append(i)
    return array

def create_list(fileString):
    """ Convert input file to list which will be contain indexed values """
    list = []
    pattern = r"[A-Za-z]{1,10} [A-Za-z]{2,10},[A-Za-z]{3} \d{2} \d{4},\d.?\d?"
    rows = findall(pattern,fileString)
    for row in rows:
        list.append(row.split(","))
    return list

def main(inputCSV,outputName,outputType):
    """ Uses functions of with-library version for write output file """
    IFS = open(inputCSV,"r").read() # IFS - input file string
    names = read_array(IFS,0)
    names.pop(0) # Delete "Emloyee Name" value
    names.sort()
    names.pop(-1) # Delete "Work Hours" value
    dates = read_array(IFS,1)
    readList = create_list(IFS)
    outputFile = write_header(outputName,dates,outputType)
    for name in names:
        write_row(name,dates,readList,outputFile)
    outputFile.close()

if __name__ == "__main__":
    csvName = "acme_worksheet.csv"
    outName = "withoutLib"
    outType = 0
    main(csvName,outName,outType)
