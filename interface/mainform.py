# mainform with tab
import tkinter as tk
from tkinter import Image, Label, image_names, ttk
from tkinter import IntVar
from PIL import Image,ImageTk
import webbrowser
from Tab_1 import tab_1
from Tab_2 import tab_2
from Tab_3 import tab_3

root = tk.Tk()
root.title("Phần mềm phân tích điểm thi đại học 2020")
# icon
root.iconbitmap('pheni.ico')

tabControl = ttk.Notebook(root)


# window center screen
window_height = 650
window_width = 1250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2)-20)

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))



s = ttk.Style()
s.configure('new.TFrame', background='#CCCCFF')
# TAB 1 ( biểu đồ điểm)
tab_1(tabControl=tabControl)

# TAB 2( chọn trường đại học theo điểm)
# s.configure('new.TFrame2', background='#00FF00')
tab_2(tabControl=tabControl)

#TAB 3 (So sánh các ngành học giữa các trường)
# s.configure('new.TFrame3', background='#9999CC')
tab_3(tabControl=tabControl)

root.mainloop()
