from tkinter import *
root= Tk()

root.title("选择题")
def showanswer0(event):
    if lb0.curselection()==('2',):
        var0.set('正确，蛇是会下蛋的')
    else:
        var0.set('错误，你有见过%s下蛋么'%lb0.get(lb0.curselection()))
    #print(lb0.curselection())

def showanswer1(event):
    if lb1.curselection()==('0','3'):
        var1.set('正确')
    else:
        var1.set('错误')
    #print(lb1.curselection())
        
label0=Label(root,text='下列哪个不是哺乳动物?')
label0.grid(row=0,column=0,padx=15,pady=2,sticky=('w','e'))

lb0=Listbox(root)
lb0.bind('<Double-Button-1>',showanswer0)
lb0.insert(END,'猪')
lb0.insert(END,'兔')
lb0.insert(END,'蛇')
lb0.insert(END,'牛')
lb0.grid(row=1,column=0,padx=15,pady=2,sticky=('w','e'))


var0=StringVar()
ans0=Label(root,textvariable=var0,fg='red')
ans0.grid(row=2,column=0,padx=15,pady=2,sticky='w')


label1=Label(root,text='多选题：下列哪个不是奥运会比赛项目')
label1.grid(row=3,column=0,padx=15,pady=2,sticky=('w','e'))

sl1=Scrollbar(root)
sl1.grid(row=4,column=1,sticky=('n','s'))
    
lb1=Listbox(root,selectmode=MULTIPLE)
lb1.bind('<Shift-Up>',showanswer1)
lb1.insert(END,'War3')
lb1.insert(END,'足球')
lb1.insert(END,'篮球')
lb1.insert(END,'武术')
lb1['yscrollcommand']=sl1.set
for i in range(100):
    lb1.insert(END,str(i))
lb1.grid(row=4,column=0,padx=15,pady=2,sticky=('w','e'))
sl1['command']=lb1.yview


var1=StringVar()
ans1=Label(root,textvariable=var1,fg='red')
ans1.grid(row=5,column=0,padx=15,pady=2,sticky='w')

root.mainloop()
