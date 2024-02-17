from tkinter import *
from tkinter import ttk

main = Tk()
main.geometry('200x150')
main.resizable(False, False)

def switch_conv():

    for widgets in main.winfo_children():
        widgets.destroy()

    main.geometry('')
    esc = Button(main, width=5, text='Vissza', relief='groove', command= switch_main)
    esc.grid(row=0, column=0, sticky=W, padx=(15, 0)) 

    title = Label(main, text='Átváltás', font=("Fira Code Medium", 15), justify='center')
    title.grid(row = 0, column = 0, columnspan=5, pady=(0, 30))

    inputNum = Entry(main, width=15, borderwidth=1, relief='solid', justify= 'center')
    inputNum.grid(row= 2, column = 0, padx=(15, 0), pady = (0, 60))

    sysList = ttk.Combobox(main, state='readonly', values=['2', '8', '10', '16'], width=5)
    sysList.grid(row = 2, column = 1, padx=(0, 10), pady = (0, 60))

    calc = Button(main, width = 5, text = '->', relief = 'groove')
    calc.grid(row = 2, column = 2, pady = (0, 60))

    outNum = Label(main, width=15, borderwidth=1, relief='solid')
    outNum.grid(row = 2, column = 3, padx=(10, 0), pady = (0, 60))

    destSysList = ttk.Combobox(main, state='readonly', values=['2', '8', '10', '16'], width=5)
    destSysList.grid(row = 2, column = 4, padx=(0, 15), pady = (0, 60))


def switch_operation():

    for widgets in main.winfo_children():
        widgets.destroy()
        
    main.geometry('')

    esc = Button(main, width=5, text='Vissza', relief='groove', command= switch_main)
    esc.grid(row=0, column=0, sticky=W, padx=(15, 0)) 

    title = Label(main, text='Műveletek', font=("Fira Code Medium", 15), justify='center')
    title.grid(row = 1, column = 0, pady=(0, 30))


def switch_main():
    
    for widgets in main.winfo_children():
        widgets.destroy()

    convButton = Button(main, width=6, text='Átváltás', relief='groove', command= switch_conv)
    convButton.grid(row=0, column=0, padx=(40, 0))

    operButton = Button(main, width=7, text='Műveletek', relief='groove', command= switch_operation)
    operButton.grid(row=0, column=1, padx=(10, 0))


switch_main()
main.mainloop()