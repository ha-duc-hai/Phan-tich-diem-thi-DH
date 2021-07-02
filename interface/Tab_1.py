import tkinter as tk
from tkinter import Label, PhotoImage, ttk
from tkinter import IntVar
from tkinter.constants import BOTTOM
from pandas import DataFrame
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk


#  load dữ liệu
def load_data():
    f = open('new_data.csv', 'r')
    line = f.readline()
    toan = []
    van = []
    anh =  []
    ly = []
    hoa = []
    sinh = []
    su = []
    dia = []
    gdcd = []
    for line in f.readlines():
        line = line.split(',')
        if line[3] != '0' :
            toan.append(float(line[3]))
        if line[4] != '0' :
            van.append(float(line[4]))
        if line[5] != '0' :
            anh.append(float(line[5]))
        if line[6] != '0' :
            ly.append(float(line[6]))
        if line[7] != '0' :
            hoa.append(float(line[7]))
        if line[8] != '0' :
            sinh.append(float(line[8]))
        if line[9] != '0' :
            su.append(float(line[9]))
        if line[10] != '0' :
            dia.append(float(line[10]))
        if line[11][0] !='0':
            gdcd.append(float(line[11]))

    return toan, van, anh, ly, hoa, sinh, su, dia , gdcd

# xử lý data
def handling_data(toan, van, anh, ly, hoa, sinh, su, dia , gdcd):
    toan = np.array(toan)
    van = np.array(van)
    anh = np.array(anh)
    ly = np.array(ly)
    hoa = np.array(hoa)
    sinh = np.array(sinh)
    su = np.array(su)
    dia = np.array(dia)
    gdcd = np.array(gdcd)
    return toan, van, anh, ly, hoa, sinh, su, dia , gdcd

# chuẩn hóa dữ liệu
def standard(arr):
    # chuẩn hóa
    def calc(n):
        temp = int(n/1)
        if n % 0.5 != 0:
            if temp + 0.5 > n:
                n = temp + 0.5
            else:
                n = temp + 1
        return n

    # xử lý mảng
    for i in range(0, arr.size):
        arr[i] = calc(arr[i])

    unique = np.unique(arr)
    a = list(arr)
    freq = [a.count(b) for b in unique]

    result = []
    i = 0
    j = 0
    while i < 10 and j <len(freq):
        i+= 0.5
        if unique[j] > i:
            result.append(0)
            continue
        if unique[j] == i:
            result.append(freq[j])
            j += 1
            continue
    if i <10: 
        result.append(0)
    return result



# tạo histogram
def creat_bar_chart(tab1, subject, data):
    data = standard(data)
    data1 = {'Điểm': [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10],
        'Số lượng thí sinh': data
        }
    df1 = DataFrame(data1,columns=['Điểm','Số lượng thí sinh'])


    figure1 = plt.Figure(figsize=(6,6), dpi=90)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, tab1)
    df1 = df1[['Điểm','Số lượng thí sinh']].groupby('Điểm').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Phổ điểm môn ' + subject)
    bar1.get_tk_widget().place(x=390, y=344, anchor='w')



# tab
def tab_1(tabControl):
    # s.configure('Frame1.TFrame', background='red')

    tab1 = ttk.Frame(tabControl, style='new.TFrame')


    # tab1.config(bg="skyblue")
    tabControl.add(tab1, text ='Biểu đồ điểm từng môn học')
<<<<<<< HEAD
    tabControl.pack(expand = 1, fill ="both")
    
=======
    # tabControl.pack(expand = 1, fill ="both")
>>>>>>> 438407581c8494bc114a2dcb3bd4be1e8f61dbb0

    # load data
    toan, van, anh, ly, hoa, sinh, su, dia , gdcd = load_data()
    toan, van, anh, ly, hoa, sinh, su, dia , gdcd = handling_data(toan, van, anh, ly, hoa, sinh, su, dia , gdcd)

    # creat button
    b_1 = tk.Button(tab1, text = 'Toán',bg='orange',fg='black', command = lambda : [creat_bar_chart(tab1, "Toán",toan)], height = 2, width = 7)
    b_2 = tk.Button(tab1, text = 'Văn',bg='orange',fg='black', command = lambda : [creat_bar_chart(tab1, "Văn",van)], height = 2, width = 7)
    b_3 = tk.Button(tab1, text = 'Anh',bg='orange',fg='black', command = lambda : [creat_bar_chart(tab1, "Anh",anh)], height = 2, width = 7)
    b_4 = tk.Button(tab1, text = 'Lý',bg='orange',fg='black', command = lambda : [creat_bar_chart(tab1, "Lý",ly)], height = 2, width = 7)
    b_5 = tk.Button(tab1, text = 'Hóa',bg='orange',fg='black', command = lambda : [creat_bar_chart(tab1, "Hóa",hoa)], height = 2, width = 7)
    b_6 = tk.Button(tab1, text = 'Sinh',bg='orange',fg='black', command = lambda : [creat_bar_chart(tab1, "Sinh",sinh)], height = 2, width = 7)
    b_7 = tk.Button(tab1, text = 'Sử',bg='orange',fg='black', command = lambda : [creat_bar_chart(tab1, "Sử",su)], height = 2, width = 7)
    b_8 = tk.Button(tab1, text = 'Địa',bg='orange',fg='black', command = lambda : [creat_bar_chart(tab1, "Địa",dia)], height = 2, width = 7)
    b_9 = tk.Button(tab1, text = 'GDCD',bg='orange',fg='black', command = lambda : [creat_bar_chart(tab1, "GDCD",gdcd)], height = 2, width = 7)


    # set posion button
    b_1.place(x=100, y=20)
    b_2.place(x=220, y=20)
    b_3.place(x=340, y=20)
    b_4.place(x=460, y=20)
    b_5.place(x=580, y=20)
    b_6.place(x=700, y=20)
    b_7.place(x=820, y=20)
    b_8.place(x=940, y=20)
    b_9.place(x=1060, y=20)







