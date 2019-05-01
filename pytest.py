import tkinter
x = tkinter.Tk()
x.geometry("400x400")
x.title("CS Project")
x.configure(bg = "White")
def pushbutton():
    y = tkinter.Tk()
butt1 = tkinter.Button(x, text = "Button 1 ", command = pushbutton)
butt1.pack()


x.mainloop()
