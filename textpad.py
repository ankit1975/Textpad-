from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from tkinter import colorchooser
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
            self.currentopenfile=openreturn.name
            openreturn.close()

    def saveas(self):
        saveasreturn=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if saveasreturn is None:
            return
        s=self.text.get(1.0,END)  
        self.currentopenfile=saveasreturn.name
        saveasreturn.write(s) 
        saveasreturn.close()

    def save(self): 
        if self.currentopenfile=="nofile":
            self.saveas()
        else:
            saveasreturn=open(self.currentopenfile,"w")
            saveasreturn.write(self.text.get(1.0,END))
            saveasreturn.close()

    def dark(self):
        self.r=colorchooser.askcolor()
        self.text.config(background=self.r[1])   
    def __init__(self,master):
        master.title("Textpad")
        master.geometry("500x500+50+50")
        #master.configure(background="black")
        self.f=Font(size=10)
        self.text=Text(foreground="black",font=self.f)
        self.text.pack(fill=BOTH,expand=1)
        self.mainmenu=Menu()
        master.config(menu=self.mainmenu)
        self.filemenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="file",menu=self.filemenu)
        self.editmenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="edit",menu=self.editmenu)
        self.viewmenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="view",menu=self.viewmenu)
        self.viewmenu.add_command(label="theme",command=self.dark)
        self.filemenu.add_command(label="open",command=self.open)
        self.filemenu.add_command(label="saveas",command=self.saveas)
        self.filemenu.add_command(label="save",command=self.save)

editor=text_editor(root)
root.mainloop()
