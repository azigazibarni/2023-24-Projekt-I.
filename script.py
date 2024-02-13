from tkinter import *

window = Tk()
def HelloWorld(str):
    print(str)

HelloWorld('print')
sysInput = int(input('Add meg az átváltandó számrendszert (2, 8, 10, 16): '))
numInput = str(input('Add meg az átváltandó számot: '))
destInput = int(input('Add meg az átváltandó számrendszert (2, 8, 10, 16): '))

# sys: 2, 8, 10, 16

def tizesbe(num, sys):
    if sys == 2:
        print(':3')

    elif sys == 8:
        print(':3')

    elif sys == 10:
        print(':3')

    elif sys == 16:
        print(':3')
    else:
        return

window.mainloop()