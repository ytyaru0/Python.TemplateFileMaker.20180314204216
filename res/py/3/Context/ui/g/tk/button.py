#from tkinter import *
import tkinter
win = tkinter.Tk()
btn = tkinter.Button(win, text="Hello Tkinter !!")
btn.pack() # ボタン配置
btn.bind('<1>', lambda e: print(e)) # イベント設定
win.mainloop()
