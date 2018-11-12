#SelectWindow.py 19Sep2018
"""
Program Level Menu control
 From PoolWindow
"""
from tkinter import *

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class SelectWindow(Frame):
    def File_Open_tbd(self):
        print("File_Open_menu to be determined")

    def File_Save_tbd(self):
        print("File_Save_menu to be determined")

        
    # Define settings upon initialization. Here you can specify
    def __init__(self,
                 master=None,
                 title=None,
                 pgmExit=exit,
                 games=[],          # text, proc pairs
                 actions=[],
                 ):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.title = title
        self.master = master
        self.pgmExit = pgmExit
        self.games = games
        self.actions = actions
        
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

        
    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget 
        if self.title is not None:
            self.master.title(self.title)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # create the file object)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.File_Open_tbd)
        filemenu.add_command(label="Save", command=self.File_Save_tbd)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.pgmExit)
        menubar.add_cascade(label="File", menu=filemenu)

                                # Trace control
        tracemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Trace", menu=tracemenu)


#######################################################################
#          Self Test
#######################################################################
if __name__ == "__main__":
        
        
    # root window created. Here, that would be the only window, but
    # you can later have windows within windows.
    mw = Tk()
    def user_exit():
        print("user_exit")
        exit()
        
        
    mw.geometry("400x300")
    
    #creation of an instance
    app = SelectWindow(mw,
                    title="SelectWindow Testing",
                    pgmExit=user_exit,
                    )
    
    
    #mainloop 
    mw.mainloop()  

