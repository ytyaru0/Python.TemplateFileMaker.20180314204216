import tkinter

def callback(sv):
    print(sv.get())

win = tkinter.Tk()
sv = tkinter.StringVar()
sv.trace('w', lambda name, index, mode, sv=sv: callback(sv))
entry = tkinter.Entry(win, textvariable=sv)
entry.pack()
win.mainloop()

