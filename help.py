from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



mydata=[]
class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\hdesk1.png")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)


        dev_label=Label(f_lbl,text="For any enquiries, contact us at:",font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=620,y=580)
        dev_label=Label(f_lbl,text="helpdesk@jam.com",font=("times new roman",18,"bold"),bg="white")
        dev_label.place(x=690,y=620)



        Back_Button=Button(f_lbl,text="Back",command=self.root.destroy,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        Back_Button.place(x=700,y=680)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()