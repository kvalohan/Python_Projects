try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
#
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x400+400+250")

label = tkinter.Label(mainWindow, text="Hello World!")
label.pack(side="top")

LeftFrame = tkinter.Frame(mainWindow)
LeftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(LeftFrame, relief='raise', borderwidth=1)
canvas.pack(side='left', anchor='n')
# canvas.pack(side='top', fill=tkinter.Y, expand=True)
# canvas.pack(side='left', fill=tkinter.BOTH, expand=True)
RightFrame = tkinter.Frame(mainWindow)
RightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(RightFrame, text='button1')
button2 = tkinter.Button(RightFrame, text='button2')
button3 = tkinter.Button(RightFrame, text='button3')

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()