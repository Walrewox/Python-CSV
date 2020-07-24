import csv
import re

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08',
'Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
def readAndWrite(fileName):
    """ Open and read information from CSV file,
    parse it and write header of columns to new file """
    headObj = open(fileName,"r")
    readHead = csv.reader(headObj)
    next(readHead)

    result = open("resultWith.csv","w")
    result.write("Name/Date,")
    date = 0
    for row in readHead:
        if(row[1] != date):
            date = row[1]
            year = re.findall(r"\d{4}",date)
            month = re.findall(r"[A-Za-z]{3}",date)
            day = re.findall(r"\d{2}",date)
            result.write(f"{year[0]}-{months[month[0]]}-{day[0]},")
    headObj.close()
    """ End of formating headers """
    nameObj = open(fileName,'r')
    readNames = csv.reader(nameObj)
    next(readNames)
    names = []
    for row in readNames:
        if (row[0] not in names):
            names.append(row[0])
    nameObj.close()
    names.sort()
    """ End of reading names """
    for i in names:
        hourObj = open(fileName,'r')
        readHours = csv.reader(hourObj)
        result.write(f"\n{i},")
        for row in readHours:
            if(i == row[0]):
                result.write(f"{row[2]},")
        hourObj.close()

if __name__ == "__main__":
    csvName = "acme_worksheet.csv"
    readAndWrite(csvName)
