import csv
from re import findall

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08',
'Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
def readRows(fileName,rowsIndex):
    array = []
    fileObj = open(fileName,"r")
    reader = csv.reader(fileObj)
    next(reader) #skip header-row
    for row in reader:
        if(row[rowsIndex] not in array):
            array.append(row[rowsIndex])
    fileObj.close()
    return array
def writeHeader(nameOfFile,dates):
    file = open(nameOfFile+".csv","w")
    file.write("Name/Date,")
    for date in dates:
        year = findall(r"\d{4}",date)
        month = findall(r"[A-Za-z]{3}",date)
        day = findall(r"\d{2}",date)
        if (date == dates[-1]):
            file.write(f"{year[0]}-{months[month[0]]}-{day[0]}")
        else:
            file.write(f"{year[0]}-{months[month[0]]}-{day[0]},")
    return file
def readAndWrite(fileName):
    """ Open and read information from CSV file,
    parse it and write header of columns to new file """
    names = readRows(fileName,0)
    names.sort()
    dates = readRows(fileName,1)
    result = writeHeader("resultWith",dates)
    """ End of reading dates and names. Created file and header-row. """
    for i in names:
        result.write(f"\n{i},")
        marked = []
        for j in dates:
            hourObj = open(fileName,'r')
            readHour = csv.reader(hourObj)
            next(readHour)
            for row in readHour:
                if(row[1] not in marked):
                    if(j == row[1]):
                        if(i == row[0]):
                            marked.append(row[1])
                            hour = f"{row[2]}" if j == dates[-1] else f"{row[2]},"
                            result.write(hour)
                            break
                    else:
                        marked.append(row[1])
                        zero = "0" if j == dates[-1] else "0,"
                        result.write(zero)
                        break
            hourObj.close()
    result.close()
    """ End writing body of file and close it.  """

if __name__ == "__main__":
    csvName = "acme_worksheet.csv"
    readAndWrite(csvName)
