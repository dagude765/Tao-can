from tkinter import *
from PIL import ImageTk,Image
root=Tk()

root.title('fenlei')


root.geometry('1280x720')
mbar=Frame(root,relief=RAISED,borderwidth=2)#Frame在上面
mbar.pack(fill=X)

mbar2=Frame(root)
mbar2.pack()

#image=img=lab=None
def showpeach():
    print("haha")
    #img.set(ImageTk.PhotoImage(file='G:\\Python33\\22.jpg'))#如何在这个图里显示呢，由于函数在内部调用图片，而Frame在外部
    #Label(root,text="abc",image=img).pack()
    global image,img,lb#回答上个问题，加入global即可
    #t1=Toplevel(height=800,width=400)
    #t1.title('haha')
    image=Image.open('G:\\Python33\\program\\tkinter\\practice6\\peach.jpg')
    img=ImageTk.PhotoImage(image)
    lb=Label(mbar2,image=img)
    lb.grid(row=0,column=0)

def showpear():
    global image,img,lb#回答上个问题，加入global即可
    image=Image.open('G:\\Python33\\program\\tkinter\\practice6\\pear.jpg')
    img=ImageTk.PhotoImage(image)
    lb=Label(mbar2,image=img)
    lb.grid(row=0,column=0)

def showorange():
    global image,img,lb#回答上个问题，加入global即可
    image=Image.open('G:\\Python33\\program\\tkinter\\practice6\\orange.jpg')
    img=ImageTk.PhotoImage(image)
    lb=Label(mbar2,image=img)
    lb.grid(row=0,column=0)

#menu
cascade=Menubutton(mbar,text='organism')
cascade.pack(side=LEFT, padx="2m")

cascade_menu=Menu(cascade)#cascade_menu自己命名

cascade_menu_choices = Menu(cascade_menu)#cascade_menu_choices自己命名


cascade_menu_choices_mul = Menu(cascade_menu_choices)

cascade_menu_choices_mul.add_command(label='peach',command=showpeach)
cascade_menu_choices_mul.add_command(label='orange',command=showorange)
cascade_menu_choices_mul.add_command(label='pear',command=showpear)

for item in['vegetables','flowers','trees','grass']:
    cascade_menu_choices.add_command(label=item)
cascade_menu_choices.add_cascade(label='fruits',menu=cascade_menu_choices_mul)
    
cascade_menu.add_command(label='animals')
cascade_menu.add_cascade(label='plants',menu=cascade_menu_choices)

cascade['menu']=cascade_menu
'''
def popup(event):
    cascade_menu.post(event.x_root,event.y_root)
cascade.bind('<Button-3>',popup)
'''

root.mainloop()
