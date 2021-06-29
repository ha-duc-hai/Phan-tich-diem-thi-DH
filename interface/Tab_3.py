import tkinter as tk                    
from tkinter import OptionMenu, Scrollbar, StringVar, ttk
from tkinter import IntVar
from tkinter.constants import CENTER, LEFT, RIGHT, VERTICAL, Y
import webbrowser

def tab_3(tabControl):
    tab3 = ttk.Frame(tabControl)
    tabControl.add(tab3, text ='So sánh các ngành học giữa các trường')
    # tabControl.pack(expand = 1, fill ="both")

    # menu majors
    variable = StringVar(tab3)
    variable.set("Chọn ngành học") # default value
    choose = OptionMenu(tab3, variable, "Cntt", "Tài chính - kế toán", "y dược","Vật liệu","Quản trị kinh doanh")
    choose.place(x = 500, y = 20)
    
    # table
    table_ = ttk.Treeview(tab3, columns=(1,2,3,4,5,6), show='headings', height=20)
    table_.place(x = 50, y = 70)
    # table_.pack(side=LEFT)

    table_.heading(1, text="Trường" ,anchor=CENTER)
    table_.heading(2, text="Khối ngành",anchor=CENTER)
    table_.heading(3, text="điểm chuẩn",anchor=CENTER)
    table_.heading(4, text="chỉ tiêu",anchor=CENTER)
    table_.heading(5, text="học phí",anchor=CENTER)
    table_.heading(6, text="giới thiệu",anchor=CENTER)
    
    table_.column(1,  anchor=CENTER)
    table_.column(2,  anchor=CENTER)
    table_.column(3,  anchor=CENTER)
    table_.column(4,  anchor=CENTER)
    table_.column(5,  anchor=CENTER)
    table_.column(6,  anchor=CENTER)
    
    sb = Scrollbar(tab3, orient=VERTICAL, command=table_.yview)
    sb.pack(side=RIGHT, fill = 'y')
    table_.configure(yscrollcommand=sb.set)
    # table_.config(yscrollcommand=sb.set)
    # sb.config(command=table_.yview)


    

    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    table_.insert('','end',values=('Phenikaa','CNTT','20','1700','10 tr',tk.Entry(tab3)))
    

    

