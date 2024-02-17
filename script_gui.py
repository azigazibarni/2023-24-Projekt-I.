from tkinter import *
from tkinter import ttk
from conversions import *

root = Tk()
root.geometry('')
root.title('Converter')

global inputNum, sysList, calcBtn, outNum, destSysList, opList, inputNum2, sysList2

def homePage():
    global frame

    frame = Frame(root)
    frame.grid(row=0,column=0, sticky=W+E)
    
    proceed = ttk.Button(frame, text='converter', command=converting)
    proceed.grid(row=0, column=0)

    proceed2 = ttk.Button(frame, text='operations', command=operations)
    proceed2.grid(row=0, column=1)

    root.geometry('')


def converting():
    global frame2, inputNum, sysList, calcBtn, outNum, destSysList

    frame2 = Frame(root)
    frame2.grid(row=0,column=0, sticky=W+E)
    
    backBtn = Button(frame2, width=5, text='Vissza', relief='groove', command=lambda: [homePage(), deleteConvWidgets()])
    backBtn.grid(row=0, column=0, columnspan=5, sticky=W, padx=(15, 0)) 

    title = Label(frame2, text='Átváltás', font=("Fira Code Medium", 15), justify='center')
    title.grid(row = 0, column = 0, columnspan=5, pady=(0, 30))

    inputNum = Entry(frame2, width=15, borderwidth=1, relief='solid', justify= 'center', )
    inputNum.grid(row= 2, column = 0, padx=(15, 0), pady = (0, 60))

    sysList = ttk.Combobox(frame2, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = clear)
    sysList.grid(row = 2, column = 1, padx=(0, 10), pady = (0, 60))

    calcBtn = Button(frame2, width = 5, text = '->', relief = 'groove', command = calculate)
    calcBtn.grid(row = 2, column = 2, pady = (0, 60))

    outNum = Label(frame2, width=15, borderwidth=1, relief='solid')
    outNum.grid(row = 2, column = 3, padx=(10, 0), pady = (0, 60))

    destSysList = ttk.Combobox(frame2, state='readonly', values=['2', '8', '10', '16'], width=5)
    destSysList.grid(row = 2, column = 4, padx=(0, 15), pady = (0, 60))


def operations():
    global frame3, inputNum, sysList, opList, inputNum2, sysList2, calcBtn, outNum, destSysList

    frame3 = Frame(root)
    frame3.grid(row=0,column=0, sticky=W+E)

    backBtn = Button(frame3, width=5, text='Vissza', relief='groove', command=lambda: [homePage(), deleteOpWidgets()])
    backBtn.grid(row=0, column=0, columnspan=8, sticky=W, padx=(15, 0))

    title = Label(frame3, text='Műveletek', font=("Fira Code Medium", 15), justify='center')
    title.grid(row = 1, column = 0, columnspan=8, pady=(0, 30))

    inputNum = Entry(frame3, width=15, borderwidth=1, relief='solid', justify= 'center')
    inputNum.grid(row= 2, column = 0, padx=(15, 0), pady = (0, 60))

    sysList = ttk.Combobox(frame3, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = clear)
    sysList.grid(row = 2, column = 1, padx=(0, 10), pady = (0, 60))

    opList = ttk.Combobox(frame3, state='readonly', width = 5, values=['+', '-', '*', '/'])
    opList.grid(row = 2, column = 2, pady = (0, 60))

    inputNum2 = Entry(frame3, width=15, borderwidth=1, relief='solid', justify= 'center')
    inputNum2.grid(row= 2, column = 3, padx=(15, 0), pady = (0, 60))

    sysList2 = ttk.Combobox(frame3, state='readonly', values=['2', '8', '10', '16'], width=5)
    sysList2.grid(row = 2, column = 4, padx=(0, 15), pady = (0, 60))

    calcBtn = Button(frame3, width = 5, text = '=', relief = 'groove', command = calculate)
    calcBtn.grid(row = 2, column = 5, pady = (0, 60))

    outNum = Label(frame3, width=15, borderwidth=1, relief='solid')
    outNum.grid(row = 2, column = 6, padx=(10, 0), pady = (0, 60))

    destSysList = ttk.Combobox(frame3, state='readonly', values=['2', '8', '10', '16'], width=5)
    destSysList.grid(row = 2, column = 7, padx=(0, 15), pady = (0, 60))


def calculate():
    numInput = inputNum.get()
    global out

    # convert to decimal
    if destSysList.get() == '10':

        if sysList.get() == '2':
            out = decimal(numInput, 2)
        elif sysList.get() == '8':
            out = decimal(numInput, 8)
        elif sysList.get() == '10':
            out = numInput
        elif sysList.get() == '16':
            out = decimal(numInput, 16)

    #convert to binary
    elif destSysList.get() == '2':
        
        if sysList.get() == '2' :
            out == numInput
        elif sysList.get() == '8':
            out = binary(int(numInput), 8)
        elif sysList.get() == '10':
            out = binary(numInput, 10)
        elif sysList.get() == '16':
            out = binary(numInput, 16)

    #convert to octal
    elif destSysList.get() == '8':
        #valamiért a kövi sor kell neki C:
        out = numInput

        if sysList.get() == '2' :
            out = octal(int(numInput), 2)
        elif sysList.get() == '8':
            out == numInput
        elif sysList.get() == '10':
            out = octal(numInput, 10)
        elif sysList.get() == '16':
            out = octal(numInput, 16)
    outNum.config(text=out)


def clear():
    outNum.config(text = '')


def deleteConvWidgets():
    for widgets in frame2.winfo_children():
        widgets.grid_remove()


def deleteOpWidgets():
    for widgets in frame3.winfo_children():
        widgets.grid_remove()

homePage()
root.mainloop()