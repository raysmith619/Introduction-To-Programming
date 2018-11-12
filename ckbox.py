
from tkinter import *    

class App:
    def __init__(self, root):
        self.start = 0
        self.root = root
        self.sb = Scrollbar(orient="vertical")
        text = Text(root, width=40, height=20, yscrollcommand=self.sb.set)
        self.sb.config(command=text.yview)
        self.sb.pack(side="right",fill="y")
        text.pack(side="top", fill="both", expand=True)
        self.chkbuttons = [Checkbutton(text="checkbutton %s" % i,padx=0,pady=0,bd=0)
                          for i in range(30)]                        
        for cb in self.chkbuttons:
            text.window_create("end", window=cb)
            text.insert("end", "\n")
            cb.bind("<Button-1>", self.selectstart)
            cb.bind("<Shift-Button-1>", self.selectrange)

    def selectstart(self, event):
        self.start = self.chkbuttons.index(event.widget)

    def selectrange(self, event):
        start = self.start
        end = self.chkbuttons.index(event.widget)
        sl = slice(min(start, end)+1, max(start, end))
        for cb in self.chkbuttons[sl]:
            cb.toggle()
        self.start = end

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()