from os import stat
import tkinter as tk                    
from tkinter import OptionMenu, Scrollbar, StringVar, ttk
from tkinter import IntVar
from tkinter.constants import CENTER, END, LEFT, RIGHT, VERTICAL, Y
import webbrowser

def tab_3(tabControl):
    tab3 = ttk.Frame(tabControl, style='new.TFrame')
    tabControl.add(tab3, text ='So sánh các ngành học giữa các trường')
    # tabControl.pack(expand = 1, fill ="both")

    
    # table
    table_ = ttk.Treeview(tab3, columns=(1,2,3,4,5,6), show='headings', height=20)
    table_.place(x = 20, y = 70)

    table_.heading(1, text="Trường" ,anchor=CENTER)
    table_.heading(2, text="Khối ngành",anchor=CENTER)
    table_.heading(3, text="điểm chuẩn",anchor=CENTER)
    table_.heading(4, text="chỉ tiêu",anchor=CENTER)
    table_.heading(5, text="học phí",anchor=CENTER)
    table_.heading(6, text="preview",anchor=CENTER)
    
    table_.column(1,  anchor=CENTER)
    table_.column(2,  anchor=CENTER)
    table_.column(3,  anchor=CENTER)
    table_.column(4,  anchor=CENTER)
    table_.column(5,  anchor=CENTER)
    table_.column(6,  anchor=CENTER)
    
    # thanh lăn
    sb = Scrollbar(tab3, orient=VERTICAL, command=table_.yview)
    sb.pack(side='right', fill = 'y')
    table_.configure(yscrollcommand=sb.set)

    # open link
    link = []
    def link_tree(event):
        input_id = table_.selection()
        str = input_id[-1][-3:]
        input_item = table_.item(input_id,"text")

        #for opening the link in browser
        import webbrowser
        webbrowser.open(link[int(str, 16)-1].format(input_item))
    # menu majors
    def OptionMenu_CheckButton(event):

        if variable.get() == "Cntt":
            # clear old data
            for record in table_.get_children():
                table_.delete(record)
            # insert data
            f = open('chuyen_nganh/CNTT.csv', 'r',encoding='utf8')
            line = f.readline()
            for line in f.readlines():
                line = line.replace('\n', '').replace('"', '')
                line = line.split(',')
                table_.insert('','end',values=(line[0],line[1],line[2],line[3],line[4],line[5]))
                table_.bind("<Double-1>", link.append(line[5]))
            table_.bind("<Double-1>", link_tree)


        if variable.get() == "Quản trị kinh doanh":
            # clear old data
            for record in table_.get_children():
                table_.delete(record)
            # insert data
            f = open('chuyen_nganh/QTKD.csv', 'r',encoding='utf8')
            line = f.readline()
            for line in f.readlines():
                line = line.replace('\n', '').replace('"', '')
                line = line.split(',')
                table_.insert('','end',values=(line[0],line[1],line[2],line[3],line[4],line[5]))
                table_.bind("<Double-1>", link.append(line[5]))
            table_.bind("<Double-1>", link_tree)

        if variable.get() == "y dược":
            # clear old data
            for record in table_.get_children():
                table_.delete(record)
            # insert data
            f = open('chuyen_nganh/Dược.csv', 'r',encoding='utf8')
            line = f.readline()
            for line in f.readlines():
                line = line.replace('\n', '').replace('"', '')
                line = line.split(',')
                table_.insert('','end',values=(line[0],line[1],line[2],line[3],line[4],line[5]))
                table_.bind("<Double-1>", link.append(line[5]))
            table_.bind("<Double-1>", link_tree)
        pass

    variable = StringVar()
    variable.set("Chọn ngành học") # default value
    option = [ "Cntt", "Tài chính - kế toán", "y dược","Vật liệu","Quản trị kinh doanh"]
    OptionMenu(tab3, variable, *(option), command =OptionMenu_CheckButton).place(x= 500, y = 20)
    

    
   
    

    

