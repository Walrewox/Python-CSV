from tkinter import *
from tkinter.filedialog import askopenfilename as Open
import withLibrary
import withoutLib

def import_file(str):
    fileName = Open()
    str.set(f"{fileName}")
def export_file(str,method,OFN,OFT):
    """ Starts the algorithm according to the selected parameters

    Keyword arguments:
    str - StringVar which contain name (path to) of input file
    method - int by which the algorithm is selected
    OFN - output file name
    OFT - output file type: 0 - .csv, 1 - .txt
    """
    inputFileName = str.get()
    if(method == 0):
        withLibrary.read_and_write(inputFileName,OFN,OFT)
    else:
        withoutLib.main(inputFileName,OFN,OFT)

root = Tk()
root.title("CSV-worksheet parser")
root.geometry("600x200")
root.resizable(False,False)

choiceFrame = Frame(root)
choiceFrame.pack()
choiceButton = Button(choiceFrame,text = "Обрати файл:",
                      command = lambda:import_file(fileString))
choiceButton.pack(side = "left")
fileString = StringVar()
fileLabel = Label(choiceFrame,textvariable = fileString).pack(side = "right")


methodFrame = Frame(root)
methodFrame.pack()
methodLabel = Label(methodFrame,text = "Оберіть метод обробки:")
methodLabel.pack(side = "left")
method = IntVar()
method.set(1)
methodRadio1 = Radiobutton(methodFrame,text = 'З модулем csv',
                       variable = method, value = 0).pack()
methodRadio2 = Radiobutton(methodFrame,text = 'Без модуля',
                       variable = method, value = 1).pack()
fileFrame = Frame(root)
fileFrame.pack()
fileLabel = Label(fileFrame,text = "Оберіть розширення\nвихідного файлу:")
fileLabel.pack(side = "left")
file = IntVar()
file.set(1)
fileRadio1 = Radiobutton(fileFrame,text = '.csv',
                       variable = file, value = 0).pack()
fileRadio2 = Radiobutton(fileFrame,text = '.txt',
                       variable = file, value = 1).pack()

exportFrame = Frame(root)
exportFrame.pack()
nameLabel = Label(exportFrame, text = "Введіть ім'я файлу без розширення: ")
nameLabel.pack(side="left")
fieldName = Entry(exportFrame)
fieldName.pack(side = 'right')
processButton = Button(root,text = "Створити!",
                       command = lambda:export_file(fileString,method.get(),
                                                    fieldName.get(),file.get()))
processButton.pack(side = "left")
root.mainloop()
