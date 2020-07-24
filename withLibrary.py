import csv
from re import findall

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08',
'Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
def readAndWrite(fileName):
    """ Open and read information from CSV file,
    parse it and write header of columns to new file """
    headObj = open(fileName,"r")
    readHead = csv.reader(headObj)
    next(readHead) #skip header-row

    result = open("resultWith.csv","w")
    result.write("Name/Date,")
    dates = []
    for row in readHead:
        if(row[1] not in dates):
            dates.append(row[1])
            year = findall(r"\d{4}",row[1])
            month = findall(r"[A-Za-z]{3}",row[1])
            day = findall(r"\d{2}",row[1])
            result.write(f"{year[0]}-{months[month[0]]}-{day[0]},")
    headObj.close()
    """ End of formating headers """

    nameObj = open(fileName,'r')
    readNames = csv.reader(nameObj)
    next(readNames) #skip header-row
    names = []
    for row in readNames:
        if (row[0] not in names):
            names.append(row[0])
    nameObj.close()
    names.sort()
    """ End of reading names """
    for i in names:
        result.write(f"\n{i},")
        hourObj = open(fileName,'r')
        readHour = csv.reader(hourObj)
        holydays = []
        print(holydays)
        for j in dates:
            for row in readHour:
                if(row[1] not in holydays):
                    print(row[1])
                    print(j)
                    if(j == row[1]):
                        if(i == row[0]):
                            result.write(f"{row[2]},")
                    else:
                        holydays.append(row[1])
                        result.write(f"0,")
                        # break
        hourObj.close()
    print(holydays)

if __name__ == "__main__":
    csvName = "acme_worksheet.csv"
    readAndWrite(csvName)
