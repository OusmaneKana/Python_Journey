from tkinter import *
# from tkinter import ttk

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

parent, caption = "",""
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")

content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)
Submit_btn = Button(parent)
Submit_btn.pack()

master.mainloop()


