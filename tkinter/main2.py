from tkinter import *
from datetime import date
root = Tk()
root.title("My First Tkinter Window")
root.geometry("300x400")
root.configure(bg = 'pink')
def welcome():
    n = entry1.get()
    dt = date.today()
    greet = "Hello" +n + "\n welcome" + "\n Todays Date is: " + str(dt)
    text1.delete("1.0", END)
    text1.insert(END,greet)

Label1 = Label(root,text = "enter your name", bg = 'blue', fg = 'teal')
Label1.pack(pady=10)
entry1= Entry()
entry1.pack(pady = 10)
button1 = Button(root,text = "begin",bg = 'teal',fg = 'blue',command = welcome)
button1.pack(pady=10)
text1 = Text(root, bg= 'grey', fg = 'blue', width = 50, height = 10)
text1.pack(pady = 10)
root.mainloop()