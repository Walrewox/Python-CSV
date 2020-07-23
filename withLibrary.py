import csv
import re

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08',
'Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
def readAndWrite(fileObj):
    """ Open and read information from CSV file,
    parse it and write to new file """
    writeHead = csv.reader(fileObj)
    next(writeHead)

    result = open("withResult.txt","w")
    result.write("Name/Date,")
    date = 0
    for row in writeHead:
        print("foo")
        if(row[1] != date):
            date = row[1]
            year = re.findall(r"\d{4}",date)
            month = re.findall(r"[A-Za-z]{3}",date)
            day = re.findall(r"\d{2}",date)
            result.write(f"{year[0]}-{months[month[0]]}-{day[0]},")
    writeHead = None
    writeBody = csv.reader(fileObj)
    next(writeBody)
    name = 0
    for row in writeBody:
        print("bar")
        if(row[0] != name):
            name = row[0]
            result.write(f"{name}",)

csvName = "acme_worksheet.csv"
file = open(csvName,"r")
readAndWrite(file)
