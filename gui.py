from tkinter import * 
from PIL import* 
root =Tk()
root.title("GUI")
root.iconbitmap("./components/editor.ico")
screen_width =root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
print(screen_height, screen_width)
ls="#d8d9f2"
win="#7D0A0A"
root.geometry(f"{screen_width}x{screen_height}")

upload=PhotoImage(file="./components/Upload.png")



f1=Frame(root,bg=ls,width=500)
f1.pack(side=RIGHT,fill=Y)
f2=Frame(root,bg="#007F73",height=750)
f2.pack(side=TOP,fill=X)
f3=Frame(root,bg="#57A845",height=450)
f3.pack(side=BOTTOM,fill=X)


b1 = Button(f2, image=upload) 
b1.pack()
b2 = Button(f2, image=rm_bg, border=0,bg=bin) 
b2.grid(row=0,column=0,padx=0)
b1.pack()
root.mainloop()