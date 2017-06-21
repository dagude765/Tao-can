from tkinter import *
from webbrowser import *
root=Tk()

root.title('衢州网络游戏中心')

'''def showinfo():
    print(var0.get())
    print(var1.get())
    print(var2.get())
    print(int0.get())
'''
def showinfo():
    user=[('xzt','100'),('xjg','010'),('wlz','001')]
    print(var0.get())
    print(var2.get())    
    if (var1.get(),var2.get()) in user:
        print("access")
    else:
        print("error")

def openweb(event):
    url='www.baidu.com'
    open_new(url)

def openweb2(event):
    url='translate.google.cn'
    open_new(url)
    
label0=Label(root,text='服务区')
label0.grid(row=0,column=0,padx=15,pady=2,sticky='e')
#label0.pack()

label1=Label(root,text='账号')
label1.grid(row=1,column=0,padx=15,pady=2,sticky='e')
#label1.pack()

label2=Label(root,text='密码')
label2.grid(row=2,column=0,padx=15,pady=2,sticky='e')
#label2.pack()

'''var0=StringVar()
tk0=Entry(root,textvariable=var0)
tk0.grid(row=0,column=1,padx=15,pady=2)'''
#tk0.pack()

var0=StringVar()
var0.set("衢州网络游戏中心")
tk0=OptionMenu(root,var0,'衢州网络游戏中心','衢州网络游戏中心二站')
tk0.grid(row=0,column=1,padx=15,pady=2)

var1=StringVar()
tk1=Entry(root,textvariable=var1)
tk1.grid(row=1,column=1,padx=15,pady=2)
#tk1.pack()

var2=StringVar()
tk2=Entry(root,textvariable=var2,show='*')
tk2.grid(row=2,column=1,padx=15,pady=2)
#tk2.pack()

int0=IntVar()
cbt=Checkbutton(root,variable=int0,text='记住密码')
cbt.grid(row=2,column=2,padx=15,pady=2,sticky='e')
#cbt.pack()

btn=Button(root,text='登陆',width=10,command=showinfo)
btn.grid(row=3,column=1,padx=15,pady=2)
#btn.pack()

label3=Label(root,text='注册账号',fg='blue')
label3.bind('<Button-1>',openweb)
label3.grid(row=1,column=2,padx=15,pady=2,sticky='w')

label4=Label(root,text='忘记密码',fg='blue')
label4.bind('<Button-1>',openweb2)
label4.grid(row=3,column=2,padx=15,pady=2,sticky='w')

root.mainloop()
