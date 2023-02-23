
#Libraries Import
from main import scanner
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
from tkinter import filedialog

#Window 
h_root=Tk()

#Interface Dimensions
h_root.geometry("1024x720")
h_root.minsize(300,100)
h_root.maxsize(1200,988)
h_root.config(bg='black')

#Interface Icon
h_root.iconbitmap('icon.ico')

#Interface Title
h_root.title("Hate Speech Detection Software")

#Background Image
image=Image.open("bg.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(h_root,image=photo)
label.place(x=0,y=0)

#Scanning Function
def scan():
    data=scanner(inputvalue.get())
    a=tmsg.showinfo("Scanned!!",data)

#File Open Function
def fileopen():
    textfile=filedialog.askopenfilename(initialdir="/C",title="Select a File",filetypes= (("txt files", "*.txt"),))
    textfile=open(textfile,'r')
    textdata=textfile.read()
    data1=scanner(textdata)
    b=tmsg.showinfo("Scanned!!",data1)
    textfile.close()

#Text Input Box
inputvalue=StringVar()
userentry=Entry(h_root,textvariable=inputvalue,borderwidth=4)
userentry.place(x=750,y=70)

#Buttons Frame
f1=Frame(h_root,bg="black",borderwidth=5,relief=SUNKEN)
f1.pack(side=RIGHT,anchor="ne",pady=120,padx=170)

#Buttons
b1=Button(f1,bg = "#8B0000",fg="white",text="   SCAN   ",command=scan,borderwidth=2,relief=RAISED)
b1.pack()

b2=Button(f1,text="Open File",bg = "#8B0000",fg="white",command=fileopen,borderwidth=2, relief=RAISED)
b2.pack(pady=2)


h_root.mainloop()
