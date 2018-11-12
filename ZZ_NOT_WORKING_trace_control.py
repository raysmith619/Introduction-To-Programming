# trace_control.py 25Sep2018

from tkinter import *    

class TraceControl:
    def __init__(self, root, strace=None, change_call=None):
        """ Trace flag dictionary
        :root: - root window
        :strace: Reference to SlTrace object
        :change_call: - call with change flag, value
        """
        if strace is None:
            strace = SlTrace
        self.strace = strace
        self.change_call = change_call
        
        self.start = 0
        self.root = root
        self.sb = Scrollbar(orient="vertical")
        text = Text(root, width=40, height=20, yscrollcommand=self.sb.set)
        self.sb.config(command=text.yview)
        self.sb.pack(side="right",fill="y")
        text.pack(side="top", fill="both", expand=True)
        self.chkbutton_d = {}             # Dictionary hashed on widget
        for flag in sorted(strace.getTraceFlags()):
            level = strace.getLevel(flag)
            var = BooleanVar()
            var.set(level)
            cb = Checkbutton(text=flag, padx=0, pady=0, bd=0, variable = var)
            self.chkbutton_d[cb] = (cb, flag, var)
            text.window_create("end", window=cb)
            text.insert("end", "\n")
            cb.bind("<Button-1>", self.select_button)
        self.list_ckbuttons()
        
    def select_button(self, event):
        cb, flag, var = self.chkbutton_d[event.widget]
        val = var.get()
        print("flag=%s var=%s val=%s" %(flag, var, val))
        self.strace.setLevel(flag, val)
            
        if self.change_call is not None:
            self.change_call(flag, val, cklist=self)

    def get_ckbuttons(self):
        return self.chkbutton_d

    def list_ckbuttons(self):
        ckb_d = self.get_ckbuttons()
        for ckb_key in ckb_d:
            cb, flag, var = ckb_d[ckb_key]
            print("flag=%s var=%s val=%d" % (flag, var, var.get()))

if __name__ == '__main__':
    from select_trace import SlTrace
    
    def report_change(flag, val, cklist=None):
        print("changed: %s = %d" % (flag, val))
        new_val = SlTrace.getLevel(flag)
        print("New val: %s = %d" % (flag, new_val))
        if cklist is not None:
            cklist.list_ckbuttons()
    
    root = Tk()

    SlTrace.setProps()
    SlTrace.setFlags("flag1=1,flag2=0,flag3=1,flag4=0, flag5=1, flag6=1")
    app = TraceControl(root, change_call=report_change)
        
        
    root.mainloop()