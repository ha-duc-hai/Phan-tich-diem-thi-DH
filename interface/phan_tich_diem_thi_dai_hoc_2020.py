from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Phần mềm phân tích điểm thi đại học 2020")
# icon
root.iconbitmap('pheni.ico')

load=Image.open("background.jpg")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=1,y=0)

# window center screen
window_height = 650
window_width = 1250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2)-20)

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# back_ground
def image(smp):
    img = PhotoImage(file="red2.png")
    img = img.subsample(smp, smp)
    return img
 
def nextPage():
    root.destroy()
    import mainform
 

# button
but = Button(
    root,
    bd=0,
    relief="groove",
    compound=CENTER,
    bg="white",
    fg="yellow",
    activeforeground="pink",
    activebackground="white",
    font="arial 30",
    text="ENTER",
    pady=0,
    command=lambda:nextPage()
    # width=300
    )
 
img = image(2) # 1=normal, 2=small, 3=smallest
but.config(image=img)
but.place(x = 500, y = 270)


root.mainloop()