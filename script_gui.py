from tkinter import *
from tkinter import ttk

# sysInput = int(input('Add meg az átváltandó szám számrendszerét (2, 8, 10, 16): '))
# numInput = str(input('Add meg az átváltandó számot: '))
# destInput = int(input('Add meg a cél számrendszert (2, 8, 10, 16): '))

# sys: 2, 8, 10, 16

#convert to decimal
def decimal(num, sys):
    out = 0
    #from binary
    if sys == 2:
        num = str(num)
        num = list(num[::-1])
        for i in range(len(num)):
            if int(num[i]) == 1:
                out += 2**i

    #from octal
    elif sys == 8:
        num = list(num[::-1])
        for i in range(len(num)):
            out += int(num[i]) * (8 ** i)

    #from decimal
    elif sys == 10:
        out = num

    #from hexadecimal
    elif sys == 16:
        hex = 0
        num = list(num[::-1])
        for i in range(len(num)):
            if num[i].isdigit() == True:
                out += int(num[i]) * (16 ** i)
            elif num[i].isdigit() == False:
                if num[i].lower() == 'a':
                    hex = 10
                elif num [i].lower() == 'b':
                    hex = 11
                elif num [i].lower() == 'c':
                    hex = 12
                elif num [i].lower() == 'd':
                    hex = 13
                elif num [i].lower() == 'e':
                    hex = 14
                elif num [i].lower() == 'f':
                    hex = 15
                out +=  hex * (16 ** i)
    else:
        return
    return int(out)


#convert to binary
def binary(num, sys):
    out = 0

    #from binary
    if sys == 2:
        out = num

    #from octal
    elif sys == 8:
        out = ''
        num = str(num)
        for i in range(len(num)):
            oct = int(num[i])
            if oct == 0:
                out += '000'
            elif oct == 1:
                out += '001'
            elif oct == 2:
                out += '010'
            elif oct == 3:
                out += '011'
            elif oct == 4:
                out += '100'
            elif oct == 5:
                out += '101'
            elif oct == 6:
                out += '110'
            elif oct == 7:
                out += '111'
            else:
                return

    #from decimal
    elif sys == 10:
        out = ''
        num = int(num)
        while num > 0:
            remind = num % 2
            out = str(remind) + out
            num = num // 2
    
    #from hexadecimal
    elif sys == 16:
        out = ''
        num = str(num)
        for i in range(len(num)):
            hex = str(num[i])
            if hex.isdigit() == True:
                if hex == '0':
                    out += '0000'
                elif hex == '1':
                    out += '0001'
                elif hex == '2':
                    out += '0010'
                elif hex == '3':
                    out += '0011'
                elif hex == '4':
                    out += '0100'
                elif hex == '5':
                    out += '0101'
                elif hex == '6':
                    out += '0110'
                elif hex == '7':
                    out += '0111'
                elif hex == '8':
                    out += '1000'
                elif hex == '9':
                    out += '1001'
            elif hex.isdigit() == False:
                if hex.lower() == 'a':
                    out += '1010'
                elif hex.lower() == 'b':
                    out += '1011'
                elif hex.lower() == 'c':
                    out += '1100'
                elif hex.lower() == 'd':
                    out += '1101'
                elif hex.lower() == 'e':
                    out += '1110'
                elif hex.lower() == 'f':
                    out += '1111'
            else:
                return

    else:
        return
    return int(out)


#convert to octal
def octal(num, sys):
    out = 0
    #from binary
    if sys == 2:

        #add missing 0s to the front
        if 3 - (len(str(num)) % 3) != 3:
            remaind = 3 - (len(str(num)) % 3)
            #return remaind
            num = list(num)
            for i in range(remaind):
                num.insert(0, '0')
            num = ''.join(num)

        oct = ''
        for i in range(0, len(num), 3):
            current = num[i] + num[i+1] + num[i+2]
            if current == '000':
                oct += '0'
            elif current == '001':
                oct += '1'
            elif current == '010':
                oct += '2'
            elif current == '011':
                oct += '3'
            elif current == '100':
                oct += '4'
            elif current == '101':
                oct += '5'
            elif current == '110':
                oct += '6'
            elif current == '111':
                oct += '7'
            else:
                return
        out = int(oct)

    #from octal
    elif sys == 8:
        out = num

    #from decimal
    elif sys == 10:
        out = ''
        for i in range(len(num) + 1):
            quot = int(num) // 8
            remaind = int(num) % 8
            num = quot
            out += str(remaind)
        out = out[::-1]
        out = int(out)

    #from hexadecimal
    elif sys == 16:
        return ':shrug:'

    else:
        return
    return out


def calculate():
    numInput = inputNum.get()

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

        if sysList.get() == '2' :
            out = octal(int(numInput), 2)
        elif sysList.get() == '8':
            out == numInput
        elif sysList.get() == '10':
            out = octal(numInput, 10)
        elif sysList.get() == '16':
            out = octal(numInput, 16)
    outNum.config(text = out)


def clear():
    outNum.config(text = '')


window = Tk()
window.geometry('')
window.resizable(False, False)
window.title('Számrendszerek')

pageMenu = Frame(window, width=300, height=300, bg='black')
pageConvert = Frame(window)
pageOperations = Frame(window)
pageMenu.grid(row=0, column=0)
pageConvert.grid(row=0, column=0)
pageOperations.grid(row=0, column=0)

#menu
menu1 = Button(pageMenu, text='convert',command=lambda: pageConvert.tkraise())
menu1.grid(row=0,column=0)
menu2 = Button(pageMenu, text='operations',command=lambda: pageOperations.tkraise())
menu2.grid(row=1,column=0)


#conversion menu
esc = Button(pageConvert, width=5, text='Vissza', relief='groove', command=lambda: pageMenu.tkraise())
esc.grid(row=0, column=0, columnspan=5, sticky=W, padx=(15, 0)) 

title = Label(pageConvert, text='Átváltás', font=("Fira Code Medium", 15), justify='center')
title.grid(row = 0, column = 0, columnspan=5, pady=(0, 30))

inputNum = Entry(pageConvert, width=15, borderwidth=1, relief='solid', justify= 'center')
inputNum.grid(row= 2, column = 0, padx=(15, 0), pady = (0, 60))

sysList = ttk.Combobox(pageConvert, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = clear)
sysList.grid(row = 2, column = 1, padx=(0, 10), pady = (0, 60))

calc = Button(pageConvert, width = 5, text = '->', relief = 'groove', command = calculate)
calc.grid(row = 2, column = 2, pady = (0, 60))

outNum = Label(pageConvert, width=15, borderwidth=1, relief='solid')
outNum.grid(row = 2, column = 3, padx=(10, 0), pady = (0, 60))

destSysList = ttk.Combobox(pageConvert, state='readonly', values=['2', '8', '10', '16'], width=5)
destSysList.grid(row = 2, column = 4, padx=(0, 15), pady = (0, 60))

pageMenu.tkraise()
window.mainloop()