from tkinter import *
from tkinter import ttk
from conversions import *

root = Tk()
root.geometry('450x200')
root.title('Converter')


def homePage():
    frame = Frame(root, width=450, height=200)
    frame.place(x=0,y=0)
    
    proceed = ttk.Button(frame, text='Temperature converter', command=converting)
    proceed.place(x=150, y=50)

global sysList, calc, outNum, destSysList, inputNum
   
def converting():
    
    frame2 = Frame(root)
    frame2.place(x=0, y=0)

    global sysList, calc, outNum, destSysList, inputNum

    esc = Button(frame2, width=5, text='Vissza', relief='groove', command=homePage)
    esc.grid(row=0, column=0, columnspan=5, sticky=W, padx=(15, 0)) 

    title = Label(frame2, text='Átváltás', font=("Fira Code Medium", 15), justify='center')
    title.grid(row = 0, column = 0, columnspan=5, pady=(0, 30))

    inputNum = Entry(frame2, width=15, borderwidth=1, relief='solid', justify= 'center')
    inputNum.grid(row= 2, column = 0, padx=(15, 0), pady = (0, 60))

    sysList = ttk.Combobox(frame2, state='readonly', values=['2', '8', '10', '16'], width=5, postcommand = '')
    sysList.grid(row = 2, column = 1, padx=(0, 10), pady = (0, 60))

    calc = Button(frame2, width = 5, text = '->', relief = 'groove', command = calculate)
    calc.grid(row = 2, column = 2, pady = (0, 60))

    outNum = Label(frame2, width=15, borderwidth=1, relief='solid')
    outNum.grid(row = 2, column = 3, padx=(10, 0), pady = (0, 60))

    destSysList = ttk.Combobox(frame2, state='readonly', values=['2', '8', '10', '16'], width=5)
    destSysList.grid(row = 2, column = 4, padx=(0, 15), pady = (0, 60))


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





homePage()
root.mainloop()