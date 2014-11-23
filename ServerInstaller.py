#!/usr/bin/env python3.4
#----------------------------------------

import sys
from tkinter import *
import os
import subprocess
#----------------------------------------

#Functions:

#----------------------------------------

root = Tk() #Creates the window called 'Root'
root.geometry("800x600+250+450") #Sets the size of the 
window and the position
root.title("Minecraft Server Installer") #Sets the title 
of the root window
#----------------------------------------

#Labels
label_welcome = Label(text="Welcome to Will's Vanilla 
Minecraft server installer").pack()
label_warning = Label(text="MAKE SURE YOU HAVE JAVA AND 
JKD OR OPENJDK INSTALLED", fg="red").pack()

#----------------------------------------
























root.mainloop()
