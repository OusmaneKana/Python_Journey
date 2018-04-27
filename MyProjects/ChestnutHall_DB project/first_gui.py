''' First GUI with python'''
'''This one can't compile with python3 most problably because the tkMessageBox module is not supported in python3'''

import tkinter
import tkMessageBox

top = tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
