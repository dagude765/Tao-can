from tkinter import *
import os
import fnmatch

root=Tk()

root.title('查找带有指定后缀的文件路径')

def showpath():
    t1=Toplevel()
    t1.title('文件列表')
    lb=Listbox(t1)
    lb['width']=80#设置表宽
    sl=Scrollbar(t1)
    sl.pack(side=RIGHT,fill=Y)
    lb['yscrollcommand']=sl.set
    name='*'+var1.get()
    for root,dirs,files in os.walk(var0.get()):
        for filename in fnmatch.filter(files,name):
            #print(os.path.join(root,filename))
            #Label(t1,text=os.path.join(root,filename)).pack()
            lb.insert(END,os.path.join(root,filename))
    lb.pack(side=LEFT)
    sl['command']=lb.yview

label0=Label(root,text='查找目录')
label0.grid(row=0,column=0,padx=15,pady=2,sticky='e')

label1=Label(root,text='查找后缀')
label1.grid(row=1,column=0,padx=15,pady=2,sticky='e')

var0=StringVar()
tk0=Entry(root,textvariable=var0)
tk0.grid(row=0,column=1,padx=15,pady=2)

var1=StringVar()
tk1=Entry(root,textvariable=var1)
tk1.grid(row=1,column=1,padx=15,pady=2)

btn=Button(root,text='查找',width=10,command=showpath)
btn.grid(row=1,column=2,padx=15,pady=2)

root.mainloop()
