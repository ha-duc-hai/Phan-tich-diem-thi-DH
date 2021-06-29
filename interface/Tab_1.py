import tkinter as tk                    
from tkinter import ttk
from tkinter import IntVar


def tab_1(tabControl):
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text ='Biểu đồ điểm từng môn học')
    tabControl.pack(expand = 1, fill ="both")
    
    CheckVar_1 = IntVar()
    CheckVar_2 = IntVar()
    CheckVar_3 = IntVar()
    CheckVar_4 = IntVar()
    CheckVar_5 = IntVar()
    CheckVar_6 = IntVar()
    CheckVar_7 = IntVar()
    CheckVar_8 = IntVar()
    CheckVar_9 = IntVar()
        # creat Checkbox 
    b_1 = tk.Checkbutton(tab1,text='Toán', bg='orange',fg='black', variable = CheckVar_1, onvalue = 1, offvalue = 0)
    b_2 = tk.Checkbutton(tab1,text='Văn', bg='orange',fg='black', variable = CheckVar_2, onvalue = 1, offvalue = 0)
    b_3 = tk.Checkbutton(tab1,text='Anh', bg='orange',fg='black', variable = CheckVar_3, onvalue = 1, offvalue = 0)
    b_4 = tk.Checkbutton(tab1,text='Lý', bg='orange',fg='black', variable = CheckVar_4, onvalue = 1, offvalue = 0)
    b_5 = tk.Checkbutton(tab1,text='Hóa', bg='orange',fg='black', variable = CheckVar_5, onvalue = 1, offvalue = 0)
    b_6 = tk.Checkbutton(tab1,text='Sinh', bg='orange',fg='black', variable = CheckVar_6, onvalue = 1, offvalue = 0)
    b_7 = tk.Checkbutton(tab1,text='Sử', bg='orange',fg='black', variable = CheckVar_7, onvalue = 1, offvalue = 0)
    b_8 = tk.Checkbutton(tab1,text='Địa', bg='orange',fg='black', variable = CheckVar_8, onvalue = 1, offvalue = 0)
    b_9 = tk.Checkbutton(tab1,text='GDCD', bg='orange',fg='black', variable = CheckVar_9, onvalue = 1, offvalue = 0)
        # set posion
    b_1.place(x=50, y=20)
    b_2.place(x=150, y=20)
    b_3.place(x=250, y=20)
    b_4.place(x=350, y=20)
    b_5.place(x=450, y=20)
    b_6.place(x=550, y=20)
    b_7.place(x=650, y=20)
    b_8.place(x=750, y=20)
    b_9.place(x=850, y=20)
