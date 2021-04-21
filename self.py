import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import pickle
 
#on app open load previous pickle file data (this loads all my previous settings)
def loaddata():
    with open('sender2_ini.pkl', 'rb') as f:
        Mydata = pickle.load(f)
        return Mydata
 
Mydata = loaddata()
 
class MainApp(tk.Tk):
 
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Userpage')
 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
 
        self.frames = {}
        for F in (Userpage, Setup):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
 
            # put all of the pages in the same location; the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame("Userpage")
 
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
 
    def capture_asset(self):
        print("get the name of button pressed and store global variable for later use")
 
class Userpage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#b22222")
        self.controller = controller
        Mydata = loaddata()
        data1 = tk.StringVar(value=Mydata[0])
        data2 = tk.StringVar(value=Mydata[1])
 
        button1 = tk.Button(self, textvariable =data1, width=8)
        button1.grid(row=2, column=1, padx =5, pady =5)
        button2 = tk.Button(self, textvariable = data2, width=8)
        button2.grid(row=2, column=2, padx =5, pady =5)
        button3 = tk.Button(self, text="Setup", command=lambda: controller.show_frame("Setup"))
        button3.grid(row=6, column=3)
 
class Setup(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=500, background="bisque")
        self.controller = controller
        self.Mydata = loaddata()
 
        data1 = tk.Entry(self, textvariable = tk.StringVar(value=self.Mydata[0]))
        data1.grid(row=4, column=0)
        data2 = tk.Entry(self, textvariable = tk.StringVar(value=self.Mydata[1]))
        data2.grid(row=4, column=1)
 
        def setup_update():
            Mydata = [data1.get(), data2.get()]
            with open('sender2_ini.pkl', 'wb') as f:
                pickle.dump(Mydata, f)
 
        SaveButton = tk.Button(self, text='Save', width=25, command = setup_update)
        SaveButton.grid(row=5, column=0)
 
        senderbutton = tk.Button(self, text="Back to Userpage", command=lambda: controller.show_frame("Userpage"))
        senderbutton.grid(row=8, column=0)
 
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()