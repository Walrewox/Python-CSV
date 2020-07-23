import csv
import re

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08',
'Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
def readAndWrite(fileName):
    """ Open and read information from CSV file,
    parse it and write header of columns to new file """
    fileObj = open(fileName,"r")
    readHead = csv.reader(fileObj)
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
    fileObj.close()
    fileObj = open(fileName,'r')
    readBody = csv.reader(fileObj)
    name = 0
    for row in readBody:
        if(row[0] != name):
            name = row[0]
            result.write(f"{name},\n")

# def writeBody(fileObj):
#     """ Read information from CSV file and
#     write Names and Work Hours to file created in writeHead() function """
#     writeBody = csv.reader(fileObj)
#     next(writeBody)
#     name = 0
#     for row in writeBody:
#         print("bar")
#         if(row[0] != name):
#             name = row[0]
#             result.write(f"{name}",)

csvName = "acme_worksheet.csv"
readAndWrite(csvName)
