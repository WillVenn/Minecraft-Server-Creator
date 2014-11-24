#!/usr/bin/env python3.4

from tkinter import *

root = Tk()
root.title("Download finished!")
label_1 = Label(text="Server files have been downloaded in your current working directory").pack()

photo = PhotoImage(file="Images/downloadicon.jpg")
logo = Label(root, image=photo)
logo.photo = photo
logo.pack()

root.mainloop()
