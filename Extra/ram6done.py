#!/usr/bin/env python3.4

from tkinter import *
#----------------------------------

root = Tk()
root.title("Completed")

Label_1 = Label(text="Generated 5120mb server launch scripts").pack()

Button_Quit = Button(text="Quit", command=root.quit).pack()

root.mainloop()
