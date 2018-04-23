from tkinter import *

master = Tk()
#####Start Show info
b = Canvas(master, width=200, height=100)
def callback():
    w = Label(master, text="Joe Kapple")
    f = Label(master, text="123 Main St.")
    i = Label(master, text="Funky Town, FL 80786")
    w.pack()
    f.pack()
    i.pack()

b = Button(master, text="Show Info", command=callback)

b.pack()

### Start EXit

def callback():
    master.destroy()

b = Button(master, text="Exit", command=callback)

b.pack()





mainloop()