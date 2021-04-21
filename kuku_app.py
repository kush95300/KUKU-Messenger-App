from os import error
import tkinter as tk
from tkinter import PhotoImage, StringVar, ttk, messagebox, simpledialog
import tkinter
from tkinter import font
from tkinter.constants import DISABLED, GROOVE, RAISED, RIDGE, SUNKEN, TOP, Y
from PIL import Image, ImageTk
import threading
import socket

global IP 
global Port 
global con, addr


  

LARGEFONT =("raleway", 40)
LARGEFONT2 =("raleway", 30)
#IMG = "kuku_logo.png"
IMG = "kukulogo2.png"
server=False
msg_list = ["Your","all","messages","will","show","here"]
         
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        gm = "1050x600"

        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry(gm)
        self.maxsize(1205,600)
        self.minsize(700,500)
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2,Page3):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)  
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = Image.open(IMG)
        logo = logo.resize((400,350))
        logo = ImageTk.PhotoImage(logo)
        logo_label = ttk.Label(self,image=logo,padding=Y)
        logo_label.image = logo
        logo_label.grid(column=2,row=0)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="KUKU Messanger APP", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 1, column = 2, padx = 10, pady = 30)

        
  
        button1 = tkinter.Button(self, text="Start using TCP",background="Black",fg="white",font="raleway 20 italic",activebackground="grey",cursor="circle",bd=3
        ,relief=RAISED,command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = tkinter.Button(self,text="Start using UDP",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3
        ,highlightbackground="blue",highlightcolor="yellow",command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 3, column = 3, padx = 10, pady = 10)
        button3 = tkinter.Button(self,text="         Exit        ",fg="black",font="raleway 25 italic",cursor="pirate",activebackground="grey",bd=3
        ,highlightbackground="blue",highlightcolor="yellow",command = lambda: exit())
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 2, padx = 10, pady = 10)

     
  
# second window frame page1
class Page1(tk.Frame): 
    
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        logo = Image.open(IMG)
        logo = logo.resize((280,150))
        logo = ImageTk.PhotoImage(logo)
        logo_label = ttk.Label(self,image=logo,padding=Y)
        logo_label.image = logo
        logo_label.grid(column=1,row=0,padx = 10, pady = 30)


        # label of frame Layout 2
        label = ttk.Label(self, text ="KUKU Messanger APP",justify="center", font = LARGEFONT2)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column= 2,columnspan = 2 , padx = 10, pady = 30)

        t1 = tkinter.Label(self,text="Enter IP (eg - 192.169.43.111) :",font="raleway 15 bold")
        t1.grid(row=1,column=1,pady=25)
        E1 = tkinter.Entry(self,cursor="pencil",width=50,bd=4,font="releway 15 italic",state="normal",highlightbackground="grey",
        highlightcolor="grey")
        E1.grid(column=2,row=1,pady=25)
        
        t1 = tkinter.Label(self,text="Enter Port (eg - 9001) :",font="raleway 15 bold")
        t1.grid(row=2,column=1,pady=25)
        E2 = tkinter.Entry(self,cursor="pencil",width=50,bd=4,font="releway 15 italic",state="normal",highlightbackground="grey",
        highlightcolor="grey")
        E2.grid(column=2,row=2,pady=25)

        c = tkinter.Canvas(self,width=500,height=80)
        c.grid(column=0,columnspan=5,row=3)
        # button to show frame 2 with text
        # layout2
        button1 = tkinter.Button(self, text ="<< Back",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3
        ,highlightbackground="blue",highlightcolor="yellow",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 4, column = 0, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = tkinter.Button(self, text ="Start Server",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3
        ,highlightbackground="blue",highlightcolor="yellow",command = lambda : startserver())
        def startserver():
            server = True
            IP = E1.get()
            Port = E2.get()
            print(IP,str(Port))
            controller.show_frame(Page2)
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 4, column = 4, padx = 10, pady = 10)

        button3 = tkinter.Button(self, text ="Join other's Server",justify="center",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3
        ,highlightbackground="blue",highlightcolor="yellow",
                            command = lambda : joinserver())

        def joinserver():
            server = True
            IP = E1.get()
            Port = E2.get()
            print(IP,Port)
            receive_thread=threading.Thread(target = 
            client(IP,Port) )           
            controller.show_frame(Page2)
    
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 4, column= 1, columnspan=3, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Chat Inbox", font="raleway 35 italic")
        c=tkinter.Canvas(self,width=1200,height=300,)
        E1 = tkinter.Entry(self,cursor="pencil",width=80,bd=4,font="releway 15 italic",state="normal",highlightbackground="grey",highlightcolor="grey")
        send = tkinter.Button(self, text ="Send Message",background="white",font="raleway 15 italic",cursor="circle",activebackground="grey",bd=3,highlightbackground="blue",highlightcolor="yellow",command=lambda: change(msg = E1.get()))
        buttonT = tkinter.Button(self, text ="Save Message",justify="right",background="white",font="raleway 15 italic",cursor="circle",activebackground="grey",bd=3,highlightbackground="blue",highlightcolor="yellow", command = lambda: save())
        buttonL = tkinter.Button(self, text ="Browse Messages",justify="left",background="white",font="raleway 15 italic",cursor="circle",activebackground="grey",bd=3,highlightbackground="blue",highlightcolor="yellow",command = lambda : controller.show_frame(Page3))
        button1 = tkinter.Button(self, text ="<< Back",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3,highlightbackground="blue",highlightcolor="yellow",command = lambda : controller.show_frame(Page1))
        button2 = tkinter.Button(self, text ="Menu",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3,highlightbackground="blue",highlightcolor="yellow",command = lambda : controller.show_frame(StartPage))
        button3 = tkinter.Button(self, text ="Exit",justify="center",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3,highlightbackground="blue",highlightcolor="yellow",command = lambda: exit())
     

        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column= 0,columnspan = 5 , padx = 10, pady = 30)       
        c.grid(column=0,columnspan=5,row=2)
        E1.grid(column=0,columnspan=4,row=3,padx=10,pady=20)
        send.grid(column=4,row=3,padx=10)
        buttonL.grid(row = 1, column = 0, padx = 10, pady = 10)
        buttonT.grid(row = 1, column= 3,columnspan=2, padx = 10, pady = 10)
        button1.grid(row = 4, column = 0, padx = 10, pady = 10)
        button2.grid(row = 4, column = 1,columnspan=3, padx = 10, pady = 10)
        button3.grid(row = 4, column= 4, padx = 10, pady = 10)
    
        
        
        ss = tkinter.Label(c,text=msg_list[len(msg_list)-6],justify="left",font="raleway 25 italic")
        ss.grid(row=0)
        s1 = tkinter.Label(c,text=msg_list[len(msg_list)-5],justify="left", font="raleway 25 italic")
        s1.grid(row=1)
        s2 = tkinter.Label(c,text=msg_list[len(msg_list)-4],justify="left", font="raleway 25 italic")
        s2.grid(row=2)
        s3 = tkinter.Label(c,text=msg_list[len(msg_list)-3],justify="left", font="raleway 25 italic")
        s3.grid(row=3)
        s4 = tkinter.Label(c,text=msg_list[len(msg_list)-2],justify="left", font="raleway 25 italic")
        s4.grid(row=4)
        s5 = tkinter.Label(c,text=msg_list[len(msg_list)-1],justify="left", font="raleway 25 italic")
        s5.grid(row=5)

        
        #msg = tk.StringVar() 

        def change(msg):
            msg_list.append(msg)
            print(msg_list)    
            s5.config(text=msg_list[-1])
            s4.config(text=msg_list[-2])
            s3.config(text=msg_list[-3])
            s2.config(text=msg_list[-4])
            s1.config(text=msg_list[-5])
            ss.config(text=msg_list[-6])
        

        def save():
            db = simpledialog.askstring("input string", "please input your added text")
            db=db+".txt"
            try:
                f=open(db,"xt")
            except error:
                f=open(db,"at")
            f.write(str(self.msg_list))
            f.close()
            messagebox.showinfo("File Saved",db + " is successfully saved.")

class Page3(tk.Frame):
    msg_list = ["Your","all","messages","will","show","here"]
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Message Inbox", font="raleway 40 italic")
        c=tkinter.Canvas(self,width=1200,height=300,)
        button1 = tkinter.Button(self, text ="<< Back",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3,highlightbackground="blue",highlightcolor="yellow",command = lambda : print("old"))
        button2 = tkinter.Button(self, text ="Back to messenger",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3,highlightbackground="blue",highlightcolor="yellow",command = lambda : controller.show_frame(Page2))
        button3 = tkinter.Button(self, text ="Next >>",justify="center",background="Black",fg="white",font="raleway 20 italic",cursor="circle",activebackground="grey",bd=3,highlightbackground="blue",highlightcolor="yellow",command = lambda: print("new"))
     

        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column= 0,columnspan = 5 , padx = 10, pady = 30)       
        c.grid(column=0,columnspan=5,row=2)
        button1.grid(row = 4, column = 0, padx = 10, pady = 10)
        button2.grid(row = 4, column = 1,columnspan=3, padx = 10, pady = 10)
        button3.grid(row = 4, column= 4, padx = 10, pady = 10)
        
    
        
        
        ss = tkinter.Label(c,text=self.msg_list[len(self.msg_list)-6],justify="left",font="raleway 25 italic")
        ss.grid(row=0)
        s1 = tkinter.Label(c,text=self.msg_list[len(self.msg_list)-5],justify="left", font="raleway 25 italic")
        s1.grid(row=1)
        s2 = tkinter.Label(c,text=self.msg_list[len(self.msg_list)-4],justify="left", font="raleway 25 italic")
        s2.grid(row=2)
        s3 = tkinter.Label(c,text=self.msg_list[len(self.msg_list)-3],justify="left", font="raleway 25 italic")
        s3.grid(row=3)
        s4 = tkinter.Label(c,text=self.msg_list[len(self.msg_list)-2],justify="left", font="raleway 25 italic")
        s4.grid(row=4)
        s5 = tkinter.Label(c,text=self.msg_list[len(self.msg_list)-1],justify="left", font="raleway 25 italic")
        s5.grid(row=5)

        
        #msg = tk.StringVar() 

        def change(msg,s):
            self.msg_list.append(msg)
            print(self.msg_list)    
            s5.config(text=self.msg_list[-1])
            s4.config(text=self.msg_list[-2])
            s3.config(text=self.msg_list[-3])
            s2.config(text=self.msg_list[-4])
            s1.config(text=self.msg_list[-5])
            ss.config(text=self.msg_list[-6])
        

        def save():
            db = simpledialog.askstring("input string", "please input your added text")
            db=db+".txt"
            try:
                f=open(db,"xt")
            except error:
                f=open(db,"at")
            f.write(str(self.msg_list))
            f.close()
            messagebox.showinfo("File Saved",db + " is successfully saved.")
            

# functions

def client(IP,PORT):
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip=IP
    port=int(PORT)
    s.connect((ip,port))
    print("\n\t\t\t\t\tWELCOME\n")
    print("connected successfully...")
    receive_thread=threading.Thread(target = lambda: crecv(ip,s))
    send_thread=threading.Thread(target = lambda: csend(ip,s))

def csend(ip,s):
    while True:
        data=input("\n\t\t\t\t\t\t<<<: ")
        data=data.encode()
        s.send(data)


def crecv(ip,s):
    while True:
        data=s.recv(1024)
        data=data.decode()
        print("\n\t"+ip+":>>> "+data)

    

    



# Driver Code
app = tkinterApp()
icon = Image.open(IMG)
icon = icon.resize((300,250))
pic = ImageTk.PhotoImage(icon)
app.iconphoto(False,pic)
app.title("KUKU Messenger App")
app.mainloop()