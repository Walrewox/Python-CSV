from re import findall
from withLibrary import write_header

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
          'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

def read_array(fileObject,values):
    """Convert file to string format and find values using regular expressions

    Keyword arguments:
    fileName - name of input file
    values which may be readed: 0 - names, 1 - dates
    """
    string = fileObject.read()
    pattern = r"[A-Za-z]{1,10} [A-Za-z]{2,10}," if values == 0 else r"[A-Za-z]{3} \d{2} \d{4}"
    finded = findall(pattern,string)
    array = []
    for i in finded:
        if(i not in array):
            array.append(i)
    return array


def main(inputCSV):
    IFO = open(inputCSV,"r")
    names = read_array(IFO,0)
    names.pop(0)
    names.sort()
    dates = read_array(IFO,1)
    print(dates)
    outputFile = write_header("resultWithout",dates)
    outputFile.close()

if __name__ == "__main__":
    input = "acme_worksheet.csv"
    main(input)
