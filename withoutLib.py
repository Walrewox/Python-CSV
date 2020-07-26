import re
from withLibrary import write_header

months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08',
'Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

def read_array(fileName):
    string = open(fileName,"r").read()
    finded = re.findall(r"[A-Za-z]{4,10} [A-Za-z]{2,10},",string)
    array = []
    for i in finded:
        if(i not in array):
            array.append(i)
    array.pop(0) # delete "Employee Name" value
    array.sort()
    return array

worksheet = "acme_worksheet.csv"
names = read_array(worksheet)
file = open("resultWithout.csv","w")
for i in names:
    file.write(f"{i}\n")
