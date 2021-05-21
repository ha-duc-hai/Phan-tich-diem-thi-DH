import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from PIL import Image,ImageTk
A = [5, 7, 9 ]
 
root= tk.Tk()
root.title('Phân tích Điểm Thi Đại Học💯💯')
root.geometry("800x630")
root.iconbitmap('kk.ico')
  
load=Image.open("background.png")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=1,y=0)

canvas1 = tk.Canvas(root, width = 800, height = 300)
filename = PhotoImage(file = "background.png")
image = canvas1.create_image(800, 0, anchor=NE, image=filename)
canvas1.pack()

label1 = tk.Label(root, text='Phân tích điểm thi Đại Học')
label1.config(font=('Arial', 20))

  
def create_charts():

    
    global bar1
    global pie2
    # x1 = float(entry1.get())
    # x2 = float(entry2.get())
    # x3 = float(entry3.get())
    x1 = A[0]
    x2 = A[1]
    x3 = A[2]


    figure1 = Figure(figsize=(4,3), dpi=100)
    subplot1 = figure1.add_subplot(111)
    xAxis = [float(x1),float(x2),float(x3)]
    yAxis = [float(x1),float(x2),float(x3)]
    subplot1.bar(xAxis,yAxis, color = 'lightsteelblue')
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

    figure2 = Figure(figsize=(4,3), dpi=100)
    subplot2 = figure2.add_subplot(111)
    labels2 = 'Label1', 'Label2', 'Label3'
    pieSizes = [float(x1),float(x2),float(x3)]
    my_colors2 = ['lightblue','lightsteelblue','silver']
    explode2 = (0, 0.1, 0)
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) 
    subplot2.axis('equal')
    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().pack()

def clear_charts():
    bar1.get_tk_widget().pack_forget()
    pie2.get_tk_widget().pack_forget()

button1 = tk.Button (root, text=' Create Charts ',command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 180, window=button1)

button2 = tk.Button (root, text='  Clear Charts  ', command=clear_charts, bg='lightskyblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 220, window=button2)

button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(400, 260, window=button3)

root.mainloop()
