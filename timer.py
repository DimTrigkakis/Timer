import Tkinter
from Tkinter import *
import time
import os

top  = Tkinter.Tk()
top.resizable(width=False,height=False)
top.minsize(width=300,height=80)

var = StringVar()
var.set("--")
T = Label(top,textvariable=var)
T.pack()

start = 0
finaltime = 0
def updateLoop():
	global start, finaltime
	a = round(finaltime-(time.time()-start))
	print a
	var.set(a)
	if (abs(a - 0) < 1.0):
		print "END OF TIMES"
		a = 300
		b = 200
		os.system('espeak "You should now take a break!"')
		top.destroy()
		exit()
	top.after(1000,updateLoop)
	

L = Listbox(top)

def playPress():
	global start, finaltime
	t = L.curselection()
	start = time.time()
	finaltime = (t[0]+1)*60*30
	print finaltime	
	top.after(1000,updateLoop)

B = Button(top,text="Start",command = playPress)
B.pack()

L = Listbox(top)
L.insert(1,"0:30")
L.insert(2,"1:00")
L.insert(3,"1:30")
L.insert(4,"2:00")
L.insert(5,"2:30")
L.insert(6,"3:00")

L.pack()

top.mainloop()
