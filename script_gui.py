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
    
    convPhotoImg = PhotoImage(file = r'pictures\arrows.png').subsample(5, 5)
    proceed = ttk.Button(frame, image=convPhotoImg, command= converting)
    proceed.grid(row=0, column=0, padx=(15, 5), pady=(10, 0))
    proceed.image = convPhotoImg

    convLabel = Label(frame, text='Átváltás', font=("Fira Code Medium", 15))
    convLabel.grid(row = 1, column = 0, pady=(5, 15))

    operPhotoImg = PhotoImage(file = r'pictures\operations.png').subsample(5, 5)
    proceed2 = ttk.Button(frame, image=operPhotoImg, command=operations)
    proceed2.grid(row=0, column=1, padx=(5,15), pady=(10, 0))
    proceed2.image = operPhotoImg

    operLabel = Label(frame, text='Műveletek', font=("Fira Code Medium", 15))
    operLabel.grid(row = 1, column = 1, pady=(5, 15))


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

    root.geometry("{}x{}".format(minimum_width+40, minimum_height-110))


#converting window
def converting():
    global frame2, inputNum, sysList, calcBtn, outNum, destSysList, error, check, sysError
    
    frame2 = Frame(root)
    frame2.grid(row=0,column=0, sticky=N+W)

    backImg = PhotoImage(file = r'pictures\backX.png').subsample(13, 13)
    backBtn = Button(frame2, width=25, height=25, relief='flat', image=backImg, command=lambda: [homePage(), deleteConvWidgets()])
    backBtn.grid(row=0, column=0, sticky=W, padx=(5, 0), pady=(5, 0))
    backBtn.image = backImg

    title = Label(frame2, text='Átváltás', font=("Fira Code Medium", 15), justify='center')
    title.grid(row = 1, column = 0, columnspan=10, pady=(0, 15))

    #string variable to be able to clear output when input changed
    sv = StringVar()
    sv.trace('w', lambda name, index, mode, sv=sv:checkInput())

    inputNum = Entry(frame2, width=15, borderwidth=1, relief='solid', justify= 'center', textvariable = sv)
    inputNum.grid(row= 2, column = 0, padx=(15, 0), pady = (0, 60))

    error= Label(frame2, text='', font=("Fira Code Medium", 10), justify='left', fg = 'red')
    error.grid(row=2, column = 0, pady = (10, 20),  columnspan=2)

    sysList = ttk.Combobox(frame2, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = lambda: [clear(), clearSysError()])
    sysList.grid(row = 2, column = 1, padx=(0, 10), pady = (0, 60))

    calcImg = PhotoImage(file = r'pictures\calcArrow.png').subsample(50, 40)
    calcBtn = Button(frame2, width=35, height=15, image=calcImg, relief = 'groove', command = calc)
    calcBtn.grid(row = 2, column = 2, pady = (0, 60))
    calcBtn.image = calcImg

    outNum = Label(frame2, width=15, borderwidth=1, relief='solid')
    outNum.grid(row = 2, column = 3, padx=(10, 0), pady = (0, 60))

    sysError = Label(frame2, text='', font=("Fira Code Medium", 10), justify='center', fg = 'red')
    sysError.grid(row=2, column = 3, pady = (10, 20), columnspan=2)

    destSysList = ttk.Combobox(frame2, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = lambda: [clear(), clearOutSysError()])
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


#operations window
def operations():
    global frame3, inputNum, sysList, opList, inputNum2, sysList2, calcBtn, outNum, destSysList, error, error2, check, check2, sysError

    frame3 = Frame(root)
    frame3.grid(row=0,column=0, sticky=N)

    backImg = PhotoImage(file = r'pictures\backX.png').subsample(13, 13)
    backBtn = Button(frame3, width=25, height=25, relief='flat', image=backImg, command=lambda: [homePage(), deleteOpWidgets()])
    backBtn.grid(row=0, column=0, sticky=W, padx=(5, 0), pady=(5, 0))
    backBtn.image = backImg

    title = Label(frame3, text='Műveletek', font=("Fira Code Medium", 15), justify='center')
    title.grid(row = 1, column = 0, columnspan=8, pady=(0, 30))

    #string variable to be able to clear output when input changed
    sv = StringVar()
    sv.trace('w', lambda name, index, mode, sv=sv:checkInput())

    inputNum = Entry(frame3, width=15, borderwidth=1, relief='solid', justify= 'center', textvariable = sv)
    inputNum.grid(row= 2, column = 0, padx=(15, 0), pady = (0, 60))

    error= Label(frame3, text='', font=("Fira Code Medium", 10), justify='center', fg = 'red')
    error.grid(row=2, column = 0, pady = (5, 20), columnspan=2)

    sysList = ttk.Combobox(frame3, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = lambda: [checkInput(), clear(), clearSysError()])
    sysList.grid(row = 2, column = 1, padx=(0, 10), pady = (0, 60))

    opList = ttk.Combobox(frame3, state='readonly', width = 5, values=['+', '-', '*', '/'], postcommand = clear)
    opList.grid(row = 2, column = 2, pady = (0, 60))

    #string variable to be able to clear output when input changed
    sv2 = StringVar()
    sv2.trace('w', lambda name, index, mode, sv=sv2:checkInput2())

    inputNum2 = Entry(frame3, width=15, borderwidth=1, relief='solid', justify= 'center', textvariable = sv2)
    inputNum2.grid(row= 2, column = 3, padx=(15, 0), pady = (0, 60))

    error2= Label(frame3, text='', font=("Fira Code Medium", 10), justify='center', fg = 'red')
    error2.grid(row=2, column = 3, pady = (5, 20), columnspan=2)

    sysList2 = ttk.Combobox(frame3, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = lambda: [checkInput2(), clear(), clearSysError2()])
    sysList2.grid(row = 2, column = 4, padx=(0, 15), pady = (0, 60))

    calcBtn = Button(frame3, width = 5, text = '=', relief = 'groove', command = opCalc)
    calcBtn.grid(row = 2, column = 5, pady = (0, 60))

    outNum = Label(frame3, width=15, borderwidth=1, relief='solid')
    outNum.grid(row = 2, column = 6, padx=(10, 0), pady = (0, 60))

    sysError= Label(frame3, text='', font=("Fira Code Medium", 10), justify='center', fg = 'red')
    sysError.grid(row=2, column = 6, pady = (5, 20), columnspan=2)

    destSysList = ttk.Combobox(frame3, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = lambda: [clear(), clearOutSysError()])
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
    

#function for calculations
def calc():
    global out, check

    checkInput()

    outSys = destSysList.get()
    if outSys not in ['2', '8', '10', '16']:
        sysError.configure(text= 'No output system')
        check = False
        return

    numInput = inputNum.get()
    
    if check == True:
        #convert to binary
        if destSysList.get() == '2':
            
            if sysList.get() == '2' :
                out = binary(numInput, 2)
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
                out = octal(numInput, 8)
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
                out = decimal(numInput, 10)
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
                out = hexadecimal(numInput, 16)
    else:
        return

    outNum.config(text=out)



#function for operations
def opCalc():
    global out, check, check2
    outSys = destSysList.get()

    checkInput()
    checkInput2()

    if outSys not in ['2', '8', '10', '16']:
        sysError.configure(text= 'No output system')
        check = False
        return

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

        #subtraction
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
            if decimal(numInput2, sysIn2) == 0:
                check2 = False
                error2.configure(text= 'Division by zero')
                return
            if outList == 2:
                out = binary(decimal(numInput, sysIn) // decimal(numInput2, sysIn2), 10)
            elif outList == 8:
                out = octal(decimal(numInput, sysIn) // decimal(numInput2, sysIn2), 10)
            elif outList == 10:
                out = round(decimal(numInput, sysIn) / decimal(numInput2, sysIn2), 3)
            elif outList == 16:
                out = hexadecimal(decimal(numInput, sysIn) // decimal(numInput2, sysIn2), 10)
    else:
        return

    outNum.config(text=out)


#input checking
def checkInput():
    global check, out
    inNum = inputNum.get()
    
    hexalist = ['a', 'b', 'c', 'd', 'e' ,'f']
    check = True
    out = ''

    try:
        inSys = int(sysList.get())
    except:
        check = False
        error.configure(text= 'No input system')
        return

    if inNum == '':
        check = False
        error.configure(text= 'No entry')
        return

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
    global check2, out
    inNum = inputNum2.get()
    hexalist = ['a', 'b', 'c', 'd', 'e' ,'f']
    check2 = True
    out = ''

    try:
        inSys = int(sysList2.get())
    except:
        check2 = False
        error2.configure(text= 'No input system')
        return

    if inNum == '':
        check2 = False
        error2.configure(text= 'No entry')
        return

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


#clearing output when input changed
def clear():
    outNum.config(text = '')

def clearSysError():
    error.config(text='')

def clearSysError2():
    error2.config(text='')

def clearOutSysError():
    sysError.config(text='')


def deleteConvWidgets():
    for widgets in frame2.winfo_children():
        widgets.grid_remove()


def deleteOpWidgets():
    for widgets in frame3.winfo_children():
        widgets.grid_remove()


homePage()
root.mainloop()
