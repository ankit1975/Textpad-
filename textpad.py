from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
root=Tk()
root.config(background="red")
class text_editor:
    currentopenfile="nofile"
    def open(self):
        openreturn=filedialog.askopenfile(initialdir="/",title="select file to open",filetypes=(("text files","*.txt"),("all files","*.*")))
        if openreturn!=None:
            self.text.delete(1.0,END)
            for line in openreturn:
                self.text.insert(INSERT,line)
            self.currentopenfile
            openreturn.close()

    def saveas(self):
        saveasreturn=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if saveasreturn is None:
            return
        s=self.text.get(1.0,END)  
        saveasreturn.write(s) 
        saveasreturn.close()

    """def save(self):
        print("save")"""
        
    def __init__(self,master):
        master.title("Textpad")
        master.geometry("500x500+50+50")
        #master.configure(background="black")
        self.f=Font(size=16)
        self.text=Text(foreground="blue",font=self.f)
        self.text.pack(fill=BOTH,expand=1)
        self.mainmenu=Menu()
        master.config(menu=self.mainmenu)
        self.filemenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="file",menu=self.filemenu)
        self.editmenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="edit",menu=self.editmenu)
        self.filemenu.add_command(label="open",command=self.open)
        self.filemenu.add_command(label="saveas",command=self.saveas)
        #self.filemenu.add_command(label="save",command=self.save)

editor=text_editor(root)
root.mainloop()