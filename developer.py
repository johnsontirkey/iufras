from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


mydata=[]
class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Team Members", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)



        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=1000,y=0,width=500,height=600)

        #member1
        img_top1=Image.open(r"college_images\dev1.png")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #member2
        img_top2=Image.open(r"college_images\dev2.png")
        img_top2=img_top2.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=155,y=300,width=200,height=200)

        #member3
        img_top3=Image.open(r"college_images\dev3.png")
        img_top3=img_top3.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)

        f_lbl=Label(main_frame,image=self.photoimg_top3)
        f_lbl.place(x=0,y=0,width=200,height=200)


        # Members Info
        #member1
        dev_label=Label(main_frame,text="Hello my name is \n Anish",font=("times new roman",18,"bold"),bg="black",fg="white")
        dev_label.place(x=300,y=200)


        #member2
        dev_label=Label(main_frame,text="Hello my name is \n Miznah",font=("times new roman",18,"bold"),bg="black",fg="white")
        dev_label.place(x=160,y=500)



        #member3
        dev_label=Label(main_frame,text="Hello my name is \n Johnson",font=("times new roman",18,"bold"),bg="black",fg="white")
        dev_label.place(x=10,y=200)











if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()