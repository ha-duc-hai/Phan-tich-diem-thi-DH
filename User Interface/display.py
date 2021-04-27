from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title('Phân tích Điểm Thi Đại Học💯💯')
root.geometry("800x630")
root.iconbitmap('icon.ico')

load=Image.open('background.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

name=Label(root,text="Tra số báo danh", fg="#FFFFFF")


root.mainloop()