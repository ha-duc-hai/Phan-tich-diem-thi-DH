import tkinter as tk                    
from tkinter import Label, ttk
from tkinter import IntVar


def tab_2(tabControl):
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text ='Chọn trường đại học theo điểm')
    tabControl.pack(expand = 1, fill ="both")

    b_1 = tk.Entry(tab2)
    b_2 = tk.Entry(tab2)
    b_3 = tk.Entry(tab2)
    b_4 = tk.Entry(tab2)
    b_5 = tk.Entry(tab2)
    b_6 = tk.Entry(tab2)
    b_7 = tk.Entry(tab2)
    b_8 = tk.Entry(tab2)
    b_9 = tk.Entry(tab2)

    lab_1 = Label(tab2, text = 'Toán :')
    lab_2 = Label(tab2, text = 'Văn :')
    lab_3 = Label(tab2, text = 'Anh :')
    lab_4 = Label(tab2, text = 'Lý :')
    lab_5 = Label(tab2, text = 'Hóa :')
    lab_6 = Label(tab2, text = 'Sinh :')
    lab_7 = Label(tab2, text = 'Sử :')
    lab_8 = Label(tab2, text = 'Địa :')
    lab_9 = Label(tab2, text = 'GDCD :')

    b_1.place(x=100, y=20)
    b_2.place(x=100, y=70)
    b_3.place(x=100, y=120)
    b_4.place(x=350, y=20)
    b_5.place(x=350, y=70)
    b_6.place(x=350, y=120)
    b_7.place(x=650, y=20)
    b_8.place(x=650, y=70)
    b_9.place(x=650, y=120)

    lab_1.place(x=50, y=20)
    lab_2.place(x=50, y=70)
    lab_3.place(x=50, y=120)
    lab_4.place(x=300, y=20)
    lab_5.place(x=300, y=70)
    lab_6.place(x=300, y=120)
    lab_7.place(x=600, y=20)
    lab_8.place(x=600, y=70)
    lab_9.place(x=600, y=120)
