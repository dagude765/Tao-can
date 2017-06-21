from tkinter import *

class app():
    #zidian
    num_info = {}
    #char_info = {}
    search_char = []
    
    def __init__(self):
        self.root = Tk()
        self.root.title('ascii码查询')

        self.load()

        self.frm_L=Frame(self.root)

        self.lb=Listbox(self.frm_L,width=20, height=10)
        self.lb.bind('<Double-Button-1>',self.get_char)
        for item in self.search_char:
            self.lb.insert(END,item)
        self.sl=Scrollbar(self.frm_L)
        self.sl.pack(side=RIGHT,fill=Y)
        #self.lb['yscrollcommand']=self.sl
        self.lb.pack(side=LEFT,fill=BOTH)
        self.sl['command']=self.lb.yview
        

        self.frm_L.pack(side=LEFT)

        self.frm_R=Frame(self.root)

        #self.var0=StringVar()
        #self.label=Label(self.root,textvariable=self.var0)
        #self.label.pack(side=RIGHT)
        self.tshow = Text(self.frm_R,width=15,height=6,font=('Verdana',15))
        self.tshow.insert('1.0','')
        self.tshow.pack()
        self.frm_R.pack(side=RIGHT)
        

    def get_char(self,event):
        tmp=self.lb.get(self.lb.curselection())
        #self.var0.set(tmp)
        #self.var0.set(self.num_info[tmp][2])
        self.tshow.delete('1.0','10.0')
        self.tshow.insert('1.0','八进制是：'+'\t'+self.num_info[tmp][0]+'\n')
        self.tshow.insert('1.0','十进制是：'+'\t'+self.num_info[tmp][1]+'\n')
        self.tshow.insert('1.0','十六进制是：'+'\t'+self.num_info[tmp][2]+'\n')
        self.tshow.insert('1.0','你查询的是：'+'\t'+tmp+'\n')


    def load(self):
        f=open(r'G:\Python33\program\tkinter\ascii.txt')
        lines=f.readlines()
        for line in lines:
            chunk = line.strip().split()
            self.search_char.append(chunk[3])
            self.num_info[chunk[3]]=[chunk[0],chunk[1],chunk[2]]


if __name__=='__main__':
    d=app()
    mainloop()

