from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image 
import os
from os import listdir
import cv2
import numpy as np
import tkinter.messagebox as msg



class Train():
    def __init__(self,root7):
        self.root7=root7
    

        self.root7.title('TRAIN DATA')
        w=root7.winfo_screenwidth()
        h=root7.winfo_screenheight()
        self.root7.geometry("{}x{}+0+0".format(w,h))
        self.root7.iconbitmap('icon.ico')
       

        
        


         ###### Images ########
        self.img=Image.open(r"img\photo1.jpg")
        #self.img=Image.open(r"img\photo1.jpg")
        self.img=self.img.resize((500,130),Image.ANTIALIAS)
        self.phot1=ImageTk.PhotoImage(self.img)
        self.img_l1=Label(root7,image=self.phot1)
        self.img_l1.place(x=0,y=0,width=w/3,height=130)

        self.img=Image.open(r"img\photo2.jpg")
        self.img=self.img.resize((500,130),Image.ANTIALIAS)
        self.phot2=ImageTk.PhotoImage(self.img)
        self.img_l2=Label(root7,image=self.phot2)
        self.img_l2.place(x=w/3,y=0,width=w/3+1,height=130)


        self.img=Image.open(r"img\photo3.jpg")
        self.img=self.img.resize((500,130),Image.ANTIALIAS)
        self.phot3=ImageTk.PhotoImage(self.img)
        self.img_l3=Label(root7,image=self.phot3)
        self.img_l3.place(x=2*w/3,y=0,width=w/3,height=130)

        
        self.main_frame=Frame(root7,bd=3,relief=RIDGE,bg='white')
        self.main_frame.place(x=0,y=170,width=w,height=560)
        self.main_frame.config(bg='black')



        ##### BG #######

        
        img=Image.open(r"img\AI photo.jpg")
        img=img.resize((w,h-130),Image.ANTIALIAS)
        self.phot4=ImageTk.PhotoImage(img)
        self.bgimg_l3=Label(self.root7,image=self.phot4)
        self.bgimg_l3.place(x=0,y=130,width=w,height=h-130)


        self.title_name=Label(self.bgimg_l3,text='TRAIN DATA',font=('algerian',35,'bold'),bg='#5E9CD6',fg='red')
        self.title_name.place(x=0,y=0,width=w,height=45)

       
        
        self.btn1=Button(self.bgimg_l3,text='TRAIN',command=self.train,font=('algerian',15,'bold'),fg='white',bg='green',cursor="hand2")
        self.btn1.place(x=580,y=220,width=220,height=40)

 

    def train(self):
        photo_folder=('photo')
        path=[os.path.join(photo_folder,photo) for photo in listdir(photo_folder)]
        faces,roll=[],[]

        for image in path:
            
            img=cv2.imread(image,cv2.IMREAD_GRAYSCALE)
            img_np=np.asarray(img,dtype=np.uint8)
            roll_number=(os.path.split(image)[1].split('.')[1])
            faces.append(img_np)
            roll.append(roll_number)
            cv2.imshow("Train Data",img_np)
            cv2.waitKey(1)==13
        roll=np.asarray(roll,dtype=np.int32)
        

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(np.asarray(faces),np.asarray(roll))
        clf.write('traindata.xml')
        cv2.destroyAllWindows()
        msg.showinfo("Success","Training Datasets Completed !!!",parent=self.root7)

if __name__ == '__main__':
    root7=Tk()
    obj=Train(root7)
    root7.mainloop() 