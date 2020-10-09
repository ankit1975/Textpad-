from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from tkinter import colorchooser
from tkinter import messagebox
root=Tk()
root.resizable(False,False)
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
    def exit(self):
        answer=messagebox.askquestion("Exit","Are you sure want to exit !!!")
        if answer=="yes":
            self.m.quit()
        else:
            return
        
    def new(self):
        self.text.delete(1.0,END)
        self.currentopenfile=="nofile"
    def copy(self):
        self.text.clipboard_append(self.text.selection_get())
    def cut(self):
        self.copy()
        self.text.delete("sel.first","sel.last")
    def paste(self):
        self.text.insert(INSERT,self.text.clipboard_get())
    def search(self):
        self.root1=Toplevel()
        self.root1.title="search any word"
        self.root1.geometry("200x200+120+150")
        self.entry=Entry(self.root1)
        def searchme():
            result=self.entry.get()
            print(self.text.search(result,1.0,stopindex=END))

        self.button=Button(self.root1,text="search",command=searchme)
        self.entry.pack()
        self.button.pack()

    #def leftclick(self):
        #self.text=Toplevel()
    def __init__(self,master):
        self.m=master
        master.title("Textpad")
        master.geometry("500x500+50+50")
        master.protocol("WM_DELETE_WINDOW",self.on_closing)
        #master.configure(background="black")
        self.f=Font(size=13)
        self.ff=Font(family="Times New Roman",size=18,weight="bold",underline=0)
        self.text=Text(self.m,font=self.f,undo=True,wrap=WORD,background="#204456",foreground="white")
        self.label=Label(self.m,text="*** Welcome To Textpad *** ",bg="#1ae2f4",font=self.ff)
        self.label.pack(fill=X)

        self.frame=Frame(self.m)
        self.frame.pack(side=RIGHT,fill=Y)
        self.scrollbar=Scrollbar(self.frame,command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(fill=Y,side=RIGHT)
        self.text.pack(fill=BOTH,expand=1)
        self.mainmenu=Menu()
        master.config(menu=self.mainmenu)
        self.filemenu=Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="File",menu=self.filemenu)
        self.editmenu=Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="Edit",menu=self.editmenu)
        self.editmenu.add_command(label="cut",command=self.cut)
        self.editmenu.add_command(label="copy",command=self.copy)
        self.editmenu.add_command(label="paste",command=self.paste)
        self.viewmenu=Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="View",menu=self.viewmenu)
        self.viewmenu.add_command(label="theme",command=self.dark)
        self.filemenu.add_command(label="new",command=self.new)
        self.filemenu.add_command(label="open",command=self.open)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="save",command=self.save)
        self.filemenu.add_command(label="saveas",command=self.saveas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="exit",command=self.exit)
        self.toolsmenu=Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="Tools",menu=self.toolsmenu)
        self.toolsmenu.add_command(label="undo",command=self.text.edit_undo)
        self.toolsmenu.add_command(label="redo",command=self.text.edit_redo)
        self.searchmenu=Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="Search",menu=self.searchmenu)
        self.searchmenu.add_command(label="search",command=self.search)

        #self.m.bind('<Button-1>',leftclick)
    def on_closing(self):
        answer=messagebox.askyesnocancel("exit","want to save ?")
        if answer:
            saveasreturn=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
            if saveasreturn is None:
                return
            s=self.text.get(1.0,END)  
            self.currentopenfile=saveasreturn.name
            saveasreturn.write(s) 
            saveasreturn.close()
        elif answer==False:
            self.m.destroy()
editor=text_editor(root)
root.mainloop()
