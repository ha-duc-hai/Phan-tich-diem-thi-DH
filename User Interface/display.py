from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title('Phân tích Điểm Thi Đại Học💯💯')
root.geometry("800x630")
root.iconbitmap('kk.ico')

load=Image.open("background.png")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

name=Label(root,text="Tra số báo danh", fg="#FFFFFF",bd=0,bg="#03152D")
name.config(font=("Transformers Movie",30))
name.pack(pady=1)

box=Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)

button_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
#def ......()

#...._button=Button(button_frame,text="Tìm Số Báo Danh",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=....)
#....
clear_button=Button(button_frame,text="xóa số vừa nhập",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=clear)
clear_button.place(x=150,y=310)
box1=Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)



root.mainloop()