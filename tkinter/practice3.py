from tkinter import *
import webbrowser 
from tkinter.ttk import *
root0=Tk()

root0.title('衢州网络游戏中心')

'''def showinfo():
    print(var0.get())
    print(var1.get())
    print(var2.get())
    print(int0.get())
'''

note=Notebook(root0)
tab1=Frame(note)
tab2=Frame(note)

note.add(tab1,text='普通用户登陆')
note.add(tab2,text='电信宽带用户登陆')

#tab1
def showinfo():
    f=open(r'G:\Python33\program\tkinter\user.txt','r')
    g=open(r'G:\Python33\program\tkinter\password.txt','r')
    user=(f.read()).split()
    password=(g.read()).split()
    f.close()
    g.close()
    print(var0.get())
    print(var2.get())    
    if (var1.get(),var2.get()) in zip(user,password):
        print("access")
    else:
        print("error")

def openweb(event):
    '''
    url='www.baidu.com'
    webbrowser.open_new(url)
    '''
    t1=Toplevel()
    t1.title('注册界面')
    
    lab0=Label(t1,text='注册账号')
    lab0.grid(row=0,column=0,padx=15,pady=2,sticky='e')

    lab1=Label(t1,text='注册密码')
    lab1.grid(row=1,column=0,padx=15,pady=2,sticky='e')

    lab2=Label(t1,text='确认密码')
    lab2.grid(row=2,column=0,padx=15,pady=2,sticky='e')

    zhucevar0=StringVar()
    ent0=Entry(t1,textvariable=zhucevar0)
    ent0.grid(row=0,column=1,padx=15,pady=2)

    zhucevar1=StringVar()
    ent1=Entry(t1,textvariable=zhucevar1)
    ent1.grid(row=1,column=1,padx=15,pady=2)

    zhucevar2=StringVar()
    ent2=Entry(t1,textvariable=zhucevar2)
    ent2.grid(row=2,column=1,padx=15,pady=2)

    def register():
        def callback(event):
            t1.destroy()
        if zhucevar2.get()==zhucevar1.get():
            f=open(r'G:\Python33\program\tkinter\user.txt','a')
            f.write(zhucevar0.get()+'\n')
            f.close()
            g=open(r'G:\Python33\program\tkinter\password.txt','a')
            g.write(zhucevar1.get()+'\n')
            g.close()
            lab3=Label(t1,text='注册成功')
            lab3.grid(row=4,column=1,padx=15,pady=2)
            lab3.bind('<Button-1>',callback)#单击label退出
        else:
            lab3=Label(t1,text='注册失败，密码不一致')
            lab3.grid(row=4,column=1,padx=15,pady=2)
            lab3.bind('<Button-1>',callback)#单击label退出

    bt0=Button(t1,text='注册',width=10,command=register)
    bt0.grid(row=3,column=1,padx=15,pady=2)
    
def openweb2(event):
    url='translate.google.cn'
    webbrowser.open_new(url)

def changepassword(event):
    g=open(r'G:\Python33\program\tkinter\password.txt','r')
    password=(g.read()).split()
    ind=user.index(var1.get())
    var2.set(password[ind])
  
label0=Label(tab1,text='服务区')
label0.grid(row=0,column=0,padx=15,pady=2,sticky='e')
#label0.pack()

label1=Label(tab1,text='账号')
label1.grid(row=1,column=0,padx=15,pady=2,sticky='e')
#label1.pack()

label2=Label(tab1,text='密码')
label2.grid(row=2,column=0,padx=15,pady=2,sticky='e')
#label2.pack()

var0=StringVar()
var0.set("衢州网络游戏中心")
#tk0=OptionMenu(tab1,var0,'衢州网络游戏中心','衢州网络游戏中心二站')
tk0=Combobox(tab1,textvariable=var0)
tk0['values']=['衢州网络游戏中心','衢州网络游戏中心二站']
tk0.grid(row=0,column=1,padx=15,pady=2)

'''
var1=StringVar()
tk1=Entry(tab1,textvariable=var1)
tk1.grid(row=1,column=1,padx=15,pady=2)
'''
var1=StringVar()
f=open(r'G:\Python33\program\tkinter\user.txt','r')
user=(f.read()).split()
#user=list(open(r'G:\Python33\program\tkinter\user.txt'))
var1.set(user[0])
#tk1=OptionMenu(*((tab1,var1)+tuple(user)))
tk1=Combobox(tab1,textvariable=var1)
tk1['values']=user
tk1.grid(row=1,column=1,padx=15,pady=2)
f.close()

var2=StringVar()
g=open(r'G:\Python33\program\tkinter\password.txt','r')
password=(g.read()).split()
var2.set(password[0])
tk1.bind('<<ComboboxSelected>>',changepassword)
tk2=Entry(tab1,textvariable=var2)
tk2.grid(row=2,column=1,padx=15,pady=2)
g.close()

int0=IntVar()
cbt=Checkbutton(tab1,variable=int0,text='记住密码')
cbt.grid(row=2,column=2,padx=15,pady=2,sticky='e')

btn=Button(tab1,text='登陆',width=10,command=showinfo)
btn.grid(row=3,column=1,padx=15,pady=2)

label3=Label(tab1,text='注册账号')

label3.bind('<Button-1>',openweb)
label3.grid(row=1,column=2,padx=15,pady=2,sticky='w')

label4=Label(tab1,text='忘记密码')#为什么不能设定前景色fg

label4.bind('<Button-1>',openweb2)
label4.grid(row=3,column=2,padx=15,pady=2,sticky='w')

#tab2

def openwin():
    t2=Toplevel(height = 800, width=400)
    t2.title('自动登录')
    Label(t2,text = 'loading.....').pack()

Button(tab2,text='点我登陆',command=openwin).pack()
#note.bind('<<NotebookTabChanged>>',openwin)



note.pack()
root0.mainloop()
