from tkinter import *
from tkinter.ttk import Button, Style, Label, Entry
from tkinter import messagebox as mb


class MyWidget(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="lightblue")   
        self.parent = parent
        self.window()
    
    def window(self):
        self.parent.title("Project")
        self.pack(fill=BOTH, expand=1)

        self.frame1 = Frame(self)
        self.frame1.pack(fill=X, side=LEFT)
        self.lbl1 = Label(self, text="Позиции", font="Arial 10", background="lightblue")
        self.lbl1.pack(side=TOP, fill=X, anchor=W)
        self.lbox = Listbox(self, selectmode=EXTENDED, font="Arial 14")
        self.lbox.pack(side=LEFT, padx=5, pady=2)
        self.lbox.bind('<Delete>', self.to_dlt)
        self.scroll = Scrollbar(self, command=self.lbox.yview)
        self.scroll.pack(side=LEFT, fill=Y, pady=2)
        self.lbox.config(yscrollcommand=self.scroll.set)

        self.frame2 = Frame(self)
        self.frame2.pack(fill=X, side=TOP)
        self.entry = Entry(self, font="Arial 10")
        self.entry.bind('<Return>', self.to_listbox)
        self.entry.pack(anchor=N)
        self.abtn = Button(self, text="Добавить", command=self.add)
        self.abtn.pack(fill=X, padx=5, pady=2)
        self.dbtn = Button(self, text="Удалить", command=self.dlt)
        self.dbtn.pack(fill=X, padx=5, pady=2)
        self.sbtn = Button(self, text="Сохранить", command=self.save)
        self.sbtn.pack(fill=X, padx=5, pady=2)
        self.pbtn = Button(self, text="Путь", command=self.way)
        self.pbtn.pack(fill=X, padx=5, pady=2)

        self.frame3 = Frame(self)
        self.frame3.pack(fill=X, side=BOTTOM)
        self.ebtn = Button(self, text=" Выход ", command=self.exit)
        self.ebtn.pack(fill=X, side=RIGHT, padx=10, pady=2)
        self.ibtn = Button(self, text="Помощь", command=self.info)
        self.ibtn.pack(fill=X, side=RIGHT, padx=5, pady=2)

    def add(self):
        self.lbox.insert(END, self.entry.get())
        self.entry.delete(0, END)
    
    def dlt(self):
        select = list(self.lbox.curselection())
        select.reverse()
        for i in select:
            self.lbox.delete(i)
    
    def save(self):
        f = open('Список.txt', 'w')
        f.writelines("\n".join(self.lbox.get(0, END)))
        f.close()

    def to_listbox(self, event):
        self.lbox.insert(END, self.entry.get())
        self.entry.delete(0, END)


    def to_dlt(self, event):
        select = list(self.lbox.curselection())
        select.reverse()
        for i in select:
            self.lbox.delete(i)

 
    def way(self):
        w = Toplevel()
        w.title("Оптимальное решение")
        w.geometry('300x300')
        w.canvas = Canvas(w)
        w.canvas.create_line(15, 25, 200, 25)
        w.canvas.create_oval(30, 30, 30, 30)
        w.canvas.pack(fill=BOTH, expand=1)

    def info(self):
        inf = mb.showinfo(title="Информация", message='Soon!')

    def exit(self):
        self.quit()

def main():
    root = Tk()
    root.geometry("600x300")
    app = MyWidget(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()
