from tkinter import *

master = Tk()
#####MPG
b = Canvas(master, width=200, height=100)


Label(master, text="Miles").grid(row=0)
Label(master, text="Gallons").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop( )










b.pack()
mainloop()