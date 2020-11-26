from tkinter import *
import os
import time
import tkinter.messagebox as tmsg
# Import Success

root = Tk()

root.title('Simple TaskManager')

# Defining To Use On DEF
def cll():
	os.system('cls')

# Defining 
def killntpad():
	os.system('taskkill /PID notepad.exe')
	root.title('NOTEPAD Killed')
	cll()
	answer.set('NOTEPAD KILLED')
def killcmd():
	os.system('taskkill /PID cmd.exe')
	root.title('CMD Killed')
	cll()
	answer.set('CMD KILLED')
def killbandicut():
	os.system('taskkill /PID bdcut.exe')
	root.title('BANDICUT Killed')
	cll()
	answer.set('BANDICUT KILLED')
def killbandicam():
	os.system('taskkill /PID bdcam.exe')
	root.title('BANDICAM Killed')
	cll()
	answer.set('BANDICAM KILLED')
def killchrome():
	os.system('taskkill /PID chrome.exe')
	root.title('CHROME Killed')
	cll()
	answer.set('CHROME KILLED')
def killscrrecorder():
	os.system('taskkill /PID ScnRec.exe')
	root.title('ScreenRecorder Killed')
	cll()
	answer.set('SCREEN RECORDER KILLED')
def killsublime():
	os.system('taskkill /PID sublime_text.exe')
	root.title('SUBLIME TEXT Killed')
	cll()
	answer.set('SUBLIME KILLED')
def killvlc():
	os.system('taskkill /PID vlc.exe')
	root.title('VLC Killed')
	cll()
	answer.set('VLC KILLED')
def killopera():
	os.system('taskkill /PID opera.exe')
	root.title('OPERA Killed')
	cll()
	answer.set('OPERA KILLED')
def killexplorer():
	b = tmsg.askquestion('Warning','Are You Sure To Restart Your Explorer ?')
	if(b == "yes"):
		os.system('kill explorer.exe')
		root.title('Restarting Explorer In Few Minutes')
		answer.set('RESTARTING EXPLORER In Few Minutes')
	else:
		root.title('Restart Explorer Cancelled')
		answer.set('RESTART EXPLORER CANCELLED')
def killcomputer():
	a = tmsg.askquestion('Warning','Are You Sure To ShutDown Your PC ?')
	if(a == "yes"):
		os.system("shutdown /s /t 1")
		root.title('Shutting Down..')
		answer.set('SHUTTING DOWN')
	else:
		root.title('Computer ShutDown Cancelled')
		answer.set('COMPUTER SHUTDOWN CANCELLED')
def killrestart():
	c = tmsg.askquestion('Warning','Are You Sure To Restart Your PC ?')
	if(c == "yes"):
		os.system('shutdown /r/ /t 1')
		root.title('Restarting..')
		answer.set('Restarting..')
	else:
		root.title('Restart Cancelled')
		answer.set('RESTART CANCELLED..')
def killline():
	os.system('taskkill /PID Line.exe')
	os.system('taskkill /PID LineUpdater.exe')
	os.system('taskkill /PID LineLauncher.exe')
	os.system('cls')
	root.title('Line Killed')
	answer.set('LINE KILLED')
def killiexplore():
	os.system('taskkill /PID iexplore.exe')
	os.system('cls')
	root.title('Internet Explorer Killed')
	answer.set('INTERNET EXPLORER KILLED')
def killqbasic():
	os.system('taskkill /PID qb64.exe')
	os.system('cls')
	root.title('QBASIC KILLED')
	answer.set('QBASIC KILLED')
def killpaint():
	os.system('taskkill /PID mspaint.exe')
	os.system('cls')
	root.title('PAINT KILLED')
	answer.set('Paint KILLED')
def killdefender():
	os.system('taskkill /PID mspaint.exe')
	os.system('cls')
	root.title('DEFENDER KILLED')
	answer.set('DEFENDER KILLED')
def killmanager():
	os.system('taskkill /PID Taskmgr.exe')
	os.system('cls')
	root.title('TaskManager KILLED')
	answer.set('TaskManager KILLED')
def killshotcut():
	os.system('taskkill /PID shotcut.exe')
	os.system('cls')
	root.title('ShotCut KILLED')
	answer.set('ShotCut KILLED')
def killpython():
	os.system('taskkill /PID python.exe')
	os.system('cls')
	root.title('Python KILLED')
	answer.set('Python KILLED')
def killidle():
	os.system('taskkill /PID pythonw.exe')
	os.system('cls')
	root.title('Python IDLE KILLED')
	answer.set('Python IDLE KILLED')

# Making Frames
f1 = Frame(borderwidth = 10, bg = "black")
f2 = Frame(borderwidth = 10, bg = "black")
f3 = Frame(borderwidth = 10, bg = "black")
f4 = Frame(borderwidth = 10, bg = "black")
f5 = Frame(borderwidth = 10, bg = "black")
f6 = Frame(borderwidth = 10, bg = "black")
f7 = Frame(borderwidth = 10, bg = "black")


# Making Buttons
Button(f1,text = "Kill Notepad",command = killntpad, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f1,text = "Kill CMD",command = killcmd, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f1,text = "Kill Bandicut",command = killbandicut, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)

Button(f2,text = "Kill Bandicam",command = killbandicam, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f2,text = "Kill Chrome",command = killchrome, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f2,text = "Kill ScreenRecorder",command = killscrrecorder, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)

Button(f3,text = "Kill Sublime Text",command = killsublime, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f3,text = "Kill VLC Media Player",command = killvlc, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f3,text = "Kill Opera Browser",command = killopera, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)

Button(f5, text = "Kill Line APP",command = killline, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f5, text = "Kill Internet Explorer",command = killiexplore, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f5, text = "Kill QBASIC",command = killqbasic, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)

Button(f6, text = "Kill Paint",command = killpaint, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f6, text = "Kill WIN DEFENDER",command = killdefender, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f6, text = "Kill TaskManager",command = killmanager, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)

Button(f7, text = "Kill Python IDLE",command = killidle, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f7, text = "Kill ShotCut",command = killshotcut, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f7, text = "Exit & Kill Python",command = killpython, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)

Button(f4,text = "Restart File Explorer",command = killexplorer, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f4,text = "ShutDown Computer",command = killcomputer, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)
Button(f4,text = "Restart Computer",command = killrestart, bg = "black", fg = "white",font = "comicsansms 11 italic",width = 18).pack(side = LEFT)

f1.pack()
f2.pack()
f3.pack()
f5.pack()
f6.pack()
f7.pack()
f4.pack()

answer = StringVar()
Label(textvariable = answer,justify = "center",padx = 10,pady = 10,font = "comicsansms 14",bg = "black",fg = "white").pack()

root.config(bg = "black")
root.mainloop()