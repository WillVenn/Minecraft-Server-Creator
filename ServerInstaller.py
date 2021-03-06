#!/usr/bin/env python3.4
#----------------------------------------

import sys
from tkinter import *
import os
import subprocess
import urllib
#----------------------------------------

#Functions:
def jarDownload():
	##subprocess.call(['python2.7', 'Downloader.py'])
	subprocess.call(['sh', 'Extra/xtermDownload.sh'])
	print ("Downloading server packages...")

def perm():
	subprocess.call(['sh', 'Extra/perm.sh'])
	##os.popen("perm.sh")
	print ("Changed permission of launch.sh")

def start():
	##subprocess.call(['sh', 'launch.sh'])
	subprocess.call(['sh', 'Extra/command.sh'])
	print ("Server started...")

def about():
	pass
	##subprocess.call(['python', 'Extra/About.py'])
	##print ("About screen launched")


def RAM_ONE():
	print ("Generating launch scripts for 512mb RAM")
	RAM_ONE = open("launch.sh", "w+")
	RAM_ONE.write("java -Xmx512M -Xms512M -jar minecraft_server.1.8.jar nogui")
	print ("Generated 512mb server launch scripts")
	subprocess.call(['python', 'Extra/ram1done.py'])
	RAM_ONE.close()

def RAM_TWO():
	print ("Generating launch scripts for 1GB RAM")
	RAM_ONE = open("launch.sh", "w+")
	RAM_ONE.write("java -Xmx1024M -Xms1024M -jar minecraft_server.1.8.jar nogui")
	print ("Generated 1GB server launch scripts")
	subprocess.call(['python', 'Extra/ram2done.py'])
	RAM_ONE.close()

def RAM_THREE():
	print ("Generating launch scripts for 2GB RAM")
	RAM_ONE = open("launch.sh", "w+")
	RAM_ONE.write("java -Xmx2048M -Xms2048M -jar minecraft_server.1.8.jar nogui")
	print ("Generated 2GB server launch scripts")
	subprocess.call(['python', 'Extra/ram3done.py'])
	RAM_ONE.close()

def RAM_FOUR():
	print ("Generating launch scripts for 3GB RAM")
	RAM_ONE = open("launch.sh", "w+")
	RAM_ONE.write("java -Xmx3072M  -Xms3072M -jar minecraft_server.1.8.jar nogui")
	print ("Generated 3GB server launch scripts")
	subprocess.call(['python', 'Extra/ram4done.py'])
	RAM_ONE.close()

def RAM_FIVE():
	print ("Generating launch scripts for 4GB RAM")
	RAM_ONE = open("launch.sh", "w+")
	RAM_ONE.write("java -Xmx4096M  -Xms4096M -jar minecraft_server.1.8.jar nogui")
	print ("Generated 4GB server launch scripts")
	subprocess.call(['python', 'Extra/ram5done.py'])
	RAM_ONE.close()

def RAM_SIX():
	print ("Generating launch scripts for 5GB RAM")
	RAM_ONE = open("launch.sh", "w+")
	RAM_ONE.write("java -Xmx5120M  -Xms5120M -jar minecraft_server.1.8.jar nogui")
	print ("Generated 5GB server launch scripts")
	subprocess.call(['python', 'Extra/ram6done.py'])
	RAM_ONE.close()



#----------------------------------------

root = Tk() #Creates the window called 'Root'
root.geometry("800x600+250+450") #Sets the size of the window and the position
root.title("Minecraft Server Installer") #Sets the title of the root window
#----------------------------------------

#Menubar
menubar = Menu(root)
menubar.add_command(label="About", command=about)
menubar.add_command(label="Quit", command=root.quit)
root.config(menu=menubar)
#----------------------------------------

#Labels
label_welcome = Label(text="Welcome to Will's Vanilla Minecraft server installer").pack()
label_warning = Label(text="MAKE SURE YOU HAVE JAVA AND JKD OR OPENJDK INSTALLED", fg="red").pack()
breakline_label = Label(text="__________________________________________________________________________________________________________").pack()
#----------------------------------------

#Buttons
button_download = Button(text="1.) Download server packages", command=jarDownload).pack()
#----------------------------------------

#Images
photo = PhotoImage(file="Images/Minecraftlogo.gif")
logo = Label(root, image=photo)
logo.photo = photo
logo.pack()
#----------------------------------------

#----------------------------------------
#RAM selection
breakline_label2 = Label(text="__________________________________________________________________________________________________________").pack()

label_chooseram = Label(text="2.) Once the server files have been downloaded choose how much RAM you have/would like to allocate for the server").pack()

button_512 = Button(text="512MB", bd=2, command=RAM_ONE).pack()
button_1024 = Button(text="1GB", bd=2, command=RAM_TWO).pack()
button_2048 = Button(text="2GB", bd=2, command=RAM_THREE).pack()
button_3072 = Button(text="3GB", bd=2, command=RAM_FOUR).pack()
button_4096 = Button(text="4GB", bd=2, command=RAM_FIVE).pack()
button_5120= Button(text="5GB", bd=2, command=RAM_SIX).pack()
label_more = Label(text="Support for more RAM soon!").pack()
#----------------------------------------
breakline_label3 = Label(text="__________________________________________________________________________________________________________").pack()
#Permssion stuffs
label_chmod = Label(text="2.) Now we must make it exactuable...").pack()
button_chmod = Button(text="Run permission script", bd=2, command=perm).pack()
#---------------------------------------
breakline_label4 = Label(text="__________________________________________________________________________________________________________").pack()
#Server starting shizzle
label_Start = Label(text="Congratulations!").pack()
button_Start = Button(text="Press me to start your newly installed Vanilla Minecraft server!", bd=3, command=start).pack()

root.mainloop()
