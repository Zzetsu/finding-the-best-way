from tkinter import *
from tkinter.ttk import Button, Style, Label, Entry

class MyWidget(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="linen")   
        self.parent = parent
        self.window()
    
    def window(self):
        self.parent.title("Project")
        self.pack(fill=BOTH, expand=True)
     

        self.columnconfigure(1, weight=1)
        self.columnconfigure(4, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(6, pad=7)
        
        
        lbl = Label(self, text="Оптимальное решение", font="Arial 14")
        lbl.grid(sticky=W, pady=4, padx=5)
        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)
        
        lbl1 = Label(self, text="A", width=6)
        lbl1.grid(row=1, column=2, pady=5)           
        entry1 = Entry(self)
        entry1.grid(row=1, column=3, columnspan=2, padx=5)
        
        sbtn = Button(self, text="Поиск")
        sbtn.grid(row=5, column=2)
 
        cbtn = Button(self, text="Закрыть", command=exit)
        cbtn.grid(row=6, column=4, pady=4)
        
        hbtn = Button(self, text="Помощь")
        hbtn.grid(row=6, column=0, padx=5)
 
        obtn = Button(self, text="Добавить")
        obtn.grid(row=5, column=4)        

def main():
    root = Tk()
    root.geometry("600x300")
    app = MyWidget(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()
