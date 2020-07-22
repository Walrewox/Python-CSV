import csv
import re

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08',
'Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
def readAndWrite(fileObj):
    """ Open and read information from CSV file,
    parse it and write to new file """
    reader = csv.reader(fileObj)
    result = open("withResult.txt","w")
    result.write("Name/Date,")
    date = 0
    name = 0
    for row in reader:
        if(row[1] != date):
            date = row[1]
            year = re.search(r"\d{4}",date)
            month = re.search(r"\D\S{3}",date)
            day = re.search(r"\d{2}",date)
            print(f"{year} {month} {day}")

            # result.write(f"{year.group(0)}-{months[month.group(0)]}-{day.group(0)}")
    for row in reader:
        if(row[0] != name):
            name = row[0]
            result.write(f"{name},\n")

csvName = "acme_worksheet.csv"
file = open(csvName,"r")
readAndWrite(file)
