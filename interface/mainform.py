# mainform with tab
import tkinter as tk                    
from tkinter import ttk
from tkinter import IntVar
import webbrowser
from Tab_1 import tab_1
from Tab_2 import tab_2
from Tab_3 import tab_3
  
root = tk.Tk()
root.title("Phần mềm phân tích điểm thi đại học")
tabControl = ttk.Notebook(root)

# window center screen
window_height = 600
window_width = 1100

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2)-20)

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# TAB 1 ( biểu đồ điểm)
tab_1(tabControl=tabControl)

# TAB 2( chọn trường đại học theo điểm)
tab_2(tabControl=tabControl)

#TAB 3 (So sánh các ngành học giữa các trường)
tab_3(tabControl=tabControl)

root.mainloop()