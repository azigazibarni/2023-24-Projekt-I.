from tkinter import *
from tkinter import ttk
import tkinter as tk
from conversions import *

root = Tk()
root.geometry('')
root.title('Converter')
root.resizable(False, False)
global inputNum, sysList, calcBtn, outNum, destSysList, opList, inputNum2, sysList2, out, error, error2, check, check2

def homePage():
    global frame

    frame = Frame(root)
    frame.grid(row=0,column=0, sticky='nsew')
    
    proceed = ttk.Button(frame, text='converter', command= converting)
    proceed.grid(row=0, column=0, padx=(15, 5), pady=(10, 0))

    proceed2 = ttk.Button(frame, text='operations', command=operations)
    proceed2.grid(row=0, column=1, padx=(5,15), pady=(10, 0))


    #resizing window
    widget_list = [proceed, proceed2]

    for widget in widget_list:
        widget.update()

    minimum_height = 0
    for height in widget_list:
        minimum_height += height.winfo_height()

    minimum_width = 0
    for width in widget_list:
        minimum_width += width.winfo_width()

    root.geometry("{}x{}".format(minimum_width+40, minimum_height))



def converting():
    global frame2, inputNum, sysList, calcBtn, outNum, destSysList, error, check
    
    frame2 = Frame(root)
    frame2.grid(row=0,column=0, sticky=N+W)

    backBtn = Button(frame2, width=5, text='Vissza', relief='groove', command=lambda: [homePage(), deleteConvWidgets()])
    backBtn.grid(row=0, column=0, columnspan=5, sticky=W, padx=(15, 0), pady=(5, 0)) 

    title = Label(frame2, text='Átváltás', font=("Fira Code Medium", 15), justify='center')
    title.grid(row = 1, column = 0, columnspan=10, pady=(0, 15))

    #string variable to be able to clear output when input changed
    sv = StringVar()
    sv.trace('w', lambda name, index, mode, sv=sv:checkInput())

    inputNum = Entry(frame2, width=15, borderwidth=1, relief='solid', justify= 'center', textvariable = sv)
    inputNum.grid(row= 2, column = 0, padx=(15, 0), pady = (0, 60))

    error= Label(frame2, text='', font=("Fira Code Medium", 10), justify='center', fg = 'red')
    error.grid(row=2, column = 0, pady = (0, 20), padx = (15, 0))

    sysList = ttk.Combobox(frame2, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = clear)
    sysList.grid(row = 2, column = 1, padx=(0, 10), pady = (0, 60))

    calcBtn = Button(frame2, width = 5, text = '->', relief = 'groove', command = calc)
    calcBtn.grid(row = 2, column = 2, pady = (0, 60))

    outNum = Label(frame2, width=15, borderwidth=1, relief='solid')
    outNum.grid(row = 2, column = 3, padx=(10, 0), pady = (0, 60))

    destSysList = ttk.Combobox(frame2, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = clear)
    destSysList.grid(row = 2, column = 4, padx=(0, 15), pady = (0, 60))

    #resizing window
    widget_list = [inputNum, sysList, calcBtn, outNum, destSysList]

    for widget in widget_list:
        widget.update()

    minimum_height = 0
    for height in widget_list:
        minimum_height += height.winfo_height()

    minimum_width = 0
    for width in widget_list:
        minimum_width += width.winfo_width()

    root.geometry("{}x{}".format(minimum_width+50, minimum_height+40))
    
    check = True



def operations():
    global frame3, inputNum, sysList, opList, inputNum2, sysList2, calcBtn, outNum, destSysList, error, error2, check, check2

    frame3 = Frame(root)
    frame3.grid(row=0,column=0, sticky=N)

    backBtn = Button(frame3, width=5, text='Vissza', relief='groove', command=lambda: [homePage(), deleteOpWidgets()])
    backBtn.grid(row=0, column=0, columnspan=8, sticky=W, padx=(15, 0),  pady=(5, 0))

    title = Label(frame3, text='Műveletek', font=("Fira Code Medium", 15), justify='center')
    title.grid(row = 1, column = 0, columnspan=8, pady=(0, 30))

    #string variable to be able to clear output when input changed
    sv = StringVar()
    sv.trace('w', lambda name, index, mode, sv=sv:checkInput())

    inputNum = Entry(frame3, width=15, borderwidth=1, relief='solid', justify= 'center', textvariable = sv)
    inputNum.grid(row= 2, column = 0, padx=(15, 0), pady = (0, 60))

    error= Label(frame3, text='', font=("Fira Code Medium", 10), justify='center', fg = 'red')
    error.grid(row=2, column = 0, pady = (0, 20), padx = (15, 0))

    sysList = ttk.Combobox(frame3, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = clear)
    sysList.grid(row = 2, column = 1, padx=(0, 10), pady = (0, 60))

    opList = ttk.Combobox(frame3, state='readonly', width = 5, values=['+', '-', '*', '/'], postcommand = clear)
    opList.grid(row = 2, column = 2, pady = (0, 60))

    #string variable to be able to clear output when input changed
    sv2 = StringVar()
    sv2.trace('w', lambda name, index, mode, sv=sv2:checkInput2())

    inputNum2 = Entry(frame3, width=15, borderwidth=1, relief='solid', justify= 'center', textvariable = sv2)
    inputNum2.grid(row= 2, column = 3, padx=(15, 0), pady = (0, 60))

    error2= Label(frame3, text='', font=("Fira Code Medium", 10), justify='center', fg = 'red')
    error2.grid(row=2, column = 3, pady = (0, 20), padx = (15, 0))

    sysList2 = ttk.Combobox(frame3, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = clear)
    sysList2.grid(row = 2, column = 4, padx=(0, 15), pady = (0, 60))

    calcBtn = Button(frame3, width = 5, text = '=', relief = 'groove', command = opCalc)
    calcBtn.grid(row = 2, column = 5, pady = (0, 60))

    outNum = Label(frame3, width=15, borderwidth=1, relief='solid')
    outNum.grid(row = 2, column = 6, padx=(10, 0), pady = (0, 60))

    destSysList = ttk.Combobox(frame3, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = clear)
    destSysList.grid(row = 2, column = 7, padx=(0, 15), pady = (0, 60))

    #resizing window
    widget_list = [inputNum, sysList, opList, inputNum2, sysList2, calcBtn, outNum, destSysList]

    for widget in widget_list:
        widget.update()

    minimum_height = 0
    for height in widget_list:
        minimum_height += height.winfo_height()

    minimum_width = 0
    for width in widget_list:
        minimum_width += width.winfo_width()

    root.geometry("{}x{}".format(minimum_width+75, minimum_height))

    check, check2 = True, True
    

def checkInput():
    global check
    inNum = inputNum.get()
    inSys = int(sysList.get())
    hexalist = ['a', 'b', 'c', 'd', 'e' ,'f']
    check = True

    if inSys == 2:
        checkNum = 0
        for i in range(len(str(inNum))):
            if inNum[i].isdigit() == False:
                check = False
            else:
                if int(inNum[i]) == 0 or int(inNum[i]) == 1:
                    checkNum += 1
        if checkNum < len(inNum):
            check = False
        else:
            check = True

    elif inSys == 8:
        for i in range(len(str(inNum))):
            if inNum[i].isdigit() == False:
                check = False
            else:
                if int(inNum[i]) < 0 or int(inNum[i]) > 7:
                    check = False
            
    elif inSys == 10:
        for i in range(len(str(inNum))):
            if inNum[i].isdigit() == False:
                check = False

    elif inSys == 16:
        for i in range(len(str(inNum))):
            if inNum[i].isdigit() == False:
                if inNum[i].lower() not in(hexalist):
                    check = False
                
    if check == True:
        error.configure(text= '')
        clear()
        
    elif check == False:
        error.configure(text='Input error')
        clear()
    return


def checkInput2():
    global check2
    inNum = inputNum2.get()
    inSys = int(sysList2.get())
    hexalist = ['a', 'b', 'c', 'd', 'e' ,'f']
    check2 = True

    if inSys == 2:
        checkNum = 0
        for i in range(len(str(inNum))):
            if inNum[i].isdigit() == False:
                check2 = False
            else:
                if int(inNum[i]) == 0 or int(inNum[i]) == 1:
                    checkNum += 1
        if checkNum < len(inNum):
            check2 = False
        else:
            check2 = True

    elif inSys == 8:
        for i in range(len(str(inNum))):
            if inNum[i].isdigit() == False:
                check2 = False
            else:
                if int(inNum[i]) < 0 or int(inNum[i]) > 7:
                    check2 = False
            
    elif inSys == 10:
        for i in range(len(str(inNum))):   
            if inNum[i].isdigit() == False:
                check2 = False

    elif inSys == 16:
        for i in range(len(str(inNum))):
            if inNum[i].isdigit() == False:
                if inNum[i].lower() not in(hexalist):
                    check2 = False
                
    if check2 == True:
        error2.configure(text= '')
        clear()
        
    elif check2 == False:
        error2.configure(text='Input error')
        clear()
    return


def calc():
    global out, check
    
    checkInput()

    numInput = inputNum.get()
    
    if check == True:
        #convert to binary
        if destSysList.get() == '2':
            
            if sysList.get() == '2' :
                out = numInput
            elif sysList.get() == '8':
                out = binary(int(numInput), 8)
            elif sysList.get() == '10':
                out = binary(numInput, 10)
            elif sysList.get() == '16':
                out = binary(numInput, 16)

        #convert to octal
        elif destSysList.get() == '8':

            if sysList.get() == '2' :
                out = octal(str(numInput), 2)
            elif sysList.get() == '8':
                out = numInput
            elif sysList.get() == '10':
                out = octal(numInput, 10)
            elif sysList.get() == '16':
                out = octal(numInput, 16)

        # convert to decimal
        elif destSysList.get() == '10':

            if sysList.get() == '2':
                out = decimal(numInput, 2)
            elif sysList.get() == '8':
                out = decimal(numInput, 8)
            elif sysList.get() == '10':
                out = numInput
            elif sysList.get() == '16':
                out = decimal(numInput, 16)
        
        #convert to hexadecimal
        elif destSysList.get() == '16':
            if sysList.get() == '2':
                out = hexadecimal(numInput, 2)
            elif sysList.get() == '8':
                out = hexadecimal(numInput, 8)
            elif sysList.get() == '10':
                out = hexadecimal(numInput, 10)
            elif sysList.get() == '16':
                out = numInput
    else:
        return

    outNum.config(text=out)


#operations
def opCalc():
    global out, check, check2

    checkInput()
    checkInput2()

    numInput = inputNum.get()
    numInput2 = inputNum2.get()
    sysIn = int(sysList.get())
    sysIn2 = int(sysList2.get())
    outList = int(destSysList.get())
    if check == True and check2 == True: 
        #addition
        if opList.get() == '+':
            if outList == 2:
                out = binary(decimal(numInput, sysIn) + decimal(numInput2, sysIn2), 10)
            elif outList == 8:
                out = octal(decimal(numInput, sysIn) + decimal(numInput2, sysIn2), 10)
            elif outList == 10:
                out = decimal(numInput, sysIn) + decimal(numInput2, sysIn2)
            elif outList == 16:
                out = hexadecimal(decimal(numInput, sysIn) + decimal(numInput2, sysIn2), 10)

        #minus
        elif opList.get() == '-':
            if outList == 2:
                out = binary(decimal(numInput, sysIn) - decimal(numInput2, sysIn2), 10)
            elif outList == 8:
                out = octal(decimal(numInput, sysIn) - decimal(numInput2, sysIn2), 10)
            elif outList == 10:
                out = decimal(numInput, sysIn) - decimal(numInput2, sysIn2)
            elif outList == 16:
                out = hexadecimal(decimal(numInput, sysIn) - decimal(numInput2, sysIn2), 10)

        #multiplication
        elif opList.get() == '*':
            if outList == 2:
                out = binary(decimal(numInput, sysIn) * decimal(numInput2, sysIn2), 10)
            elif outList == 8:
                out = octal(decimal(numInput, sysIn) * decimal(numInput2, sysIn2), 10)
            elif outList == 10:
                out = decimal(numInput, sysIn) * decimal(numInput2, sysIn2)
            elif outList == 16:
                out = hexadecimal(decimal(numInput, sysIn) * decimal(numInput2, sysIn2), 10)
        
        #division
        elif opList.get() == '/':
            if outList == 2:
                out = binary(decimal(numInput, sysIn) // decimal(numInput2, sysIn2), 10)
            elif outList == 8:
                out = octal(decimal(numInput, sysIn) // decimal(numInput2, sysIn2), 10)
            elif outList == 10:
                out = decimal(numInput, sysIn) // decimal(numInput2, sysIn2)
            elif outList == 16:
                out = hexadecimal(decimal(numInput, sysIn) // decimal(numInput2, sysIn2), 10)
    else:
        return

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