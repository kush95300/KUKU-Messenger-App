from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.maxsize(800,550)
#window.minsize(750,500)

mpage = Canvas(window,width=780,height=300, )
mpage.grid(columnspan=3)

# logo
logo = Image.open('kuku_logo.png')
logo = logo.resize((300,250))
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo,pady=20)
logo_label.image = logo
logo_label.grid(column=1,row=0)

# Title

title = Label(window,text="KUKU Messanger App", font="raleway 40 bold")
title.grid(columnspan=3,row=1)

# gap

mpage = Canvas(window,width=700,height=50,)
mpage.grid(columnspan=3)

def prints(s):
    if s==1:
        print("UDP")
        window.destroy()
        window2 = Tk()
        # buttons
        b1 = Button(window,text="Start using UDP",bg="Black",fg="white",font="raleway 20 italic",command=lambda:prints(1))
        b1.grid(column=0,row=3)
        b2 = Button(window,text="Start using TCP",bg="Black",fg="white",font="raleway 20 italic",command=lambda:prints(2))
        b2.grid(column=2,row=3)

    else:
        print("tcp")

# buttons
b1 = Button(window,text="Start using UDP",bg="Black",fg="white",font="raleway 20 italic",command=lambda:prints(1))
b1.grid(column=0,row=3)
b2 = Button(window,text="Start using TCP",bg="Black",fg="white",font="raleway 20 italic",command=lambda:prints(2))
b2.grid(column=2,row=3)

# gap

mpage = Canvas(window,width=700,height=20)
mpage.grid(columnspan=3)


#c=Canvas(bg="white",borderwidth=10,height=700,width=900)
#c.pack()
#f1=Frame(c,bg="white",borderwidth=5)
#f1.pack()
#s= Label(window,)
#heading = Label(f1,text="   KUKU Messenger   ",font="200",pady=10,background='grey')
#heading.pack()


window.mainloop()