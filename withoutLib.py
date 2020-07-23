import re

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08',
'Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

def write(names,dates):
    result = open("withoutResult.csv","w")
    result.write()
def readNames(fileName):
    string = open(fileName,"r").read()
    finded = re.findall(r"[A-Za-z]{4,10} [A-Za-z]{2,10},",string)
    result = []
    for i in finded:
        if(i not in result):
            result.append(i)
    return result


worksheet = "acme_worksheet.csv"
names = readNames(worksheet)
testFile = open("test.txt","w")
for i in names:
    testFile.write(f"{i}\n")
