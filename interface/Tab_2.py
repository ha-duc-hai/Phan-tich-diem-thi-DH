import tkinter as tk
from tkinter import Canvas, Label, OptionMenu, Scrollbar, StringVar, XView, ttk
from tkinter import IntVar
from tkinter.constants import BOTTOM, CENTER, COMMAND, INSIDE, RIGHT, TOP, VERTICAL
from tkinter import font as tkFont

def tab_2(tabControl):
   
    tab2 = ttk.Frame(tabControl, style='new.TFrame')
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

    b_1.place(x=200, y=20)
    b_2.place(x=200, y=70)
    b_3.place(x=200, y=120)
    b_4.place(x=550, y=20)
    b_5.place(x=550, y=70)
    b_6.place(x=550, y=120)
    b_7.place(x=950, y=20)
    b_8.place(x=950, y=70)
    b_9.place(x=950, y=120)

    lab_1.place(x=150, y=20)
    lab_2.place(x=150, y=70)
    lab_3.place(x=150, y=120)
    lab_4.place(x=500, y=20)
    lab_5.place(x=500, y=70)
    lab_6.place(x=500, y=120)
    lab_7.place(x=900, y=20)
    lab_8.place(x=900, y=70)
    lab_9.place(x=900, y=120)

    # table
    table_ = ttk.Treeview(tab2, columns=(1,2,3,4,5,6), show='headings', height=15)
    table_.place(x = 20, y = 220)

    table_.heading(1, text="Trường" ,anchor=CENTER)
    table_.heading(2, text="Khối ngành",anchor=CENTER)
    table_.heading(3, text="điểm chuẩn",anchor=CENTER)
    table_.heading(4, text="chỉ tiêu",anchor=CENTER)
    table_.heading(5, text="học phí",anchor=CENTER)
    table_.heading(6, text="Preview",anchor=CENTER)

    table_.column(1,  anchor=CENTER)
    table_.column(2,  anchor=CENTER)
    table_.column(3,  anchor=CENTER)
    table_.column(4,  anchor=CENTER)
    table_.column(5,  anchor=CENTER)
    table_.column(6,  anchor=CENTER)

    # thanh lăn
    sb = Scrollbar(tab2, orient=VERTICAL, command=table_.yview)
    sb.pack(side='right', fill = 'y')
    table_.configure(yscrollcommand=sb.set)

    # option menu
    search_arr = []
    def OptionMenu_CheckButton(event):
        search_arr.append(variable.get())
        # pass

    variable = StringVar()
    variable.set("Chọn ngành học") # default value
    option = [ "Cntt", "Tài chính - kế toán", "y dược","Vật liệu","Quản trị kinh doanh"]
    OptionMenu(tab2, variable, *(option), command =OptionMenu_CheckButton).place(x = 630, y = 170)

    # setting
    label = tk.Label(tab2, text= "Điểm tổ hợp của bạn: ", font='Helvetica 12 bold')
    label.place(x = 300, y = 170)
    point_arr = []
    def point ():
        arr = []
        arr.append(b_1.get())
        arr.append(b_2.get())
        arr.append(b_3.get())
        arr.append(b_4.get())
        arr.append(b_5.get())
        arr.append(b_6.get())
        arr.append(b_7.get())
        arr.append(b_8.get())
        arr.append(b_9.get())

        sum = 0
        for i in arr:
            if i != "":
                sum += float(i)

        point_arr.append(sum)
        label = tk.Label(tab2, text= "  " + str(sum)+ " ",  font='Helvetica 12 bold')
        label.place(x = 510, y = 170)

    # open link
    link = []
    def link_tree(event):
        
        input_id = table_.selection()
        str = input_id[-1][-3:]
        input_item = table_.item(input_id,"text")
        #for opening the link in browser
        import webbrowser
        webbrowser.open(link[int(str, 16)-1].format(input_item))

    # search in table
    def search_():
        posion = search_arr[len(search_arr)-1]
        num = point_arr[len(point_arr)-1]

        #  cntt data
        if posion == "Cntt":
            # clear old data
            for record in table_.get_children():
                table_.delete(record)
            # insert data
            f = open('chuyen_nganh/CNTT.csv', 'r',encoding='utf8')
            line = f.readline()
            for line in f.readlines():
                line = line.replace('\n', '').replace('"', '')
                line = line.split(',')
                if float(line[2]) <= num:
                    table_.insert('','end',values=(line[0],line[1],line[2],line[3],line[4],line[5]))
                    table_.bind("<Double-1>", link.append(line[5]))
            table_.bind("<Double-1>", link_tree)

        # QTKD data
        if posion== "Quản trị kinh doanh":
            # clear old data
            for record in table_.get_children():
                table_.delete(record)
            # insert data
            f = open('chuyen_nganh/QTKD.csv', 'r',encoding='utf8')
            line = f.readline()
            for line in f.readlines():
                line = line.replace('\n', '').replace('"', '')
                line = line.split(',')
                if float(line[2]) <= num:
                    table_.insert('','end',values=(line[0],line[1],line[2],line[3],line[4],line[5]))
                    table_.bind("<Double-1>", link.append(line[5]))
            table_.bind("<Double-1>", link_tree)

        # Y data
        if posion == "y dược":
            # clear old data
            for record in table_.get_children():
                table_.delete(record)
            # insert data
            f = open('chuyen_nganh/Dược.csv', 'r',encoding='utf8')
            line = f.readline()
            for line in f.readlines():
                line = line.replace('\n', '').replace('"', '')
                line = line.split(',')
                if float(line[2]) <= num:
                    table_.insert('','end',values=(line[0],line[1],line[2],line[3],line[4],line[5]))
                    table_.bind("<Double-1>", link.append(line[5]))
            table_.bind("<Double-1>", link_tree)

    # sreach button
    search_button = tk.Button(tab2, text='Tìm kiếm', command= lambda: [point(), search_()], font='Helvetica 12 bold')
    search_button.place(x = 900, y = 170)



