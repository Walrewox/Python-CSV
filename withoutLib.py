def Write(values):
    result = open("result.csv","w")
    result.write("Name,Date,Info\nGeorge,July 22 2020,Pudge")
def Read(file):
    print("Hello")

names = []
dates = []
hours = []

worksheet = open("acme_worksheet.csv","r")
Read(worksheet)

worksheet.close()
