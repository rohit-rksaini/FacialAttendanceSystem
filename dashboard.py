from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk






class Main_Dashboard:
    def __init__(self,root8):
        self.root8 = root8
        w = self.root8.winfo_screenwidth()
        h = self.root8.winfo_screenheight()
        self.root8.geometry(f'{w}x{h}+0+0')
        self.root8.title("Face Recognition System")
        self.root8.iconbitmap('icon.ico')
        
        ### first image
        img = Image.open('img/BestFacialRecognition.jpg')
        img = img.resize((w//3,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root8,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=w//3,height=130)
        ##### second image
        img1 = Image.open('img/facialrecognition.png')
        img1 = img1.resize((w//3,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root8,image=self.photoimg1)
        f_lbl.place(x=w//3,y=0,width=w//3,height=130)
        ####### thried image
        img2 = Image.open('img/images.jpg')
        img2 = img2.resize((w//3,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root8,image=self.photoimg2)
        f_lbl.place(x=2*w//3,y=0,width=w//3,height=130)

        ######## BG image
        img3 = Image.open('img/dash.png')
        img3 = img3.resize((w,h-220),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_i = Label(self.root8,image=self.photoimg3)
        bg_i.place(x=0,y=130,width=w,height=h-130)

        title_lbl = ttk.Label(bg_i,text='Main Dashboard',anchor='center',font=('algerian',35,'bold'),background='#EBFCF9',foreground='red')
        title_lbl.place(x=0,y=0,width=w)

        ##### Student Registration 
        
            
        
        img4 = Image.open('img/clg.jpg')
        img4 = img4.resize((240,180),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_i,image=self.photoimg4,cursor='hand2',command=self.Student_reg)
        b1.place(x=130,y=80,width=240,height=180)
        b1_1 = Button(bg_i,text='Student Registration',cursor='hand2',font=('time new roman',12,'bold'),bg='darkblue',fg='white',command=self.Student_reg)
        b1_1.place(x=130,y=250,width=240,height=40)
        
        ##### Start Attendance 
        

        img5 = Image.open('img/smart-attendance.jpg')
        img5 = img5.resize((240,180),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_i,image=self.photoimg5,cursor='hand2',command=self.Student_Att)
        b1.place(x=560,y=80,width=240,height=180)
        b1_1 = Button(bg_i,text='Start Attendance',cursor='hand2',font=('time new roman',12,'bold'),bg='darkblue',fg='white',command=self.Student_Att)
        b1_1.place(x=560,y=250,width=240,height=40)
        
        ##### Attendance Record 
        

        img6 = Image.open('img/face_detector1.jpg')
        img6 = img6.resize((240,180),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_i,image=self.photoimg6,cursor='hand2',command=self.Student_Rec)
        b1.place(x=990,y=80,width=240,height=180)
        b1_1 = Button(bg_i,text='Attendance Record',cursor='hand2',font=('time new roman',12,'bold'),bg='darkblue',fg='white',command=self.Student_Rec)
        b1_1.place(x=990,y=250,width=240,height=40)
        
        ##### Help 
        

        img7 = Image.open('img/help.jpg')
        img7 = img7.resize((240,180),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_i,image=self.photoimg7,cursor='hand2',command=self.Student_help)
        b1.place(x=990,y=330,width=240,height=180)
        b1_1 = Button(bg_i,text='Help',cursor='hand2',font=('time new roman',12,'bold'),bg='darkblue',fg='white',command=self.Student_help)
        b1_1.place(x=990,y=510,width=240,height=40)
        
        ##### Train Data 
        

        img11 = Image.open('img/record.jpg')
        img11 = img11.resize((240,180),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_i,image=self.photoimg11,cursor='hand2',command=self.Train_Data)
        b1.place(x=130,y=330,width=240,height=180)
        b1_1 = Button(bg_i,text='Train Data',cursor='hand2',font=('time new roman',12,'bold'),bg='darkblue',fg='white',command=self.Train_Data)
        b1_1.place(x=130,y=510,width=240,height=40)
        
        
        ##### Developers 
        

        img9 = Image.open('img/student.jpg')
        img9 = img9.resize((240,180),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_i,image=self.photoimg9,cursor='hand2',command=self.Deve)
        b1.place(x=560,y=330,width=240,height=180)
        b1_1 = Button(bg_i,text='Developers',cursor='hand2',font=('time new roman',12,'bold'),bg='darkblue',fg='white',command=self.Deve)
        b1_1.place(x=560,y=510,width=240,height=40)

    def Student_reg(self):
        from student_reg import Registation
        self.new_window=Toplevel(self.root8)
        
        self.app=Registation(self.new_window)
        
    def Student_Att(self):
        from attendance import Attendance
        self.new_window=Toplevel(self.root8)
        
        self.app=Attendance(self.new_window)

    def Student_Rec(self):
        from attendance_record import Attendance_Record
        self.new_window=Toplevel(self.root8)
        
        self.app=Attendance_Record(self.new_window)

    def Student_help(self):
        from chatbot import ChatBot
        self.new_window=Toplevel(self.root8)
        self.app=ChatBot(self.new_window)
       

    def Train_Data(self):
        from train import Train 
        self.new_window=Toplevel(self.root8)
        
        self.app=Train(self.new_window)

    def Deve(self):
        from developer import Developer
        self.new_window=Toplevel(self.root8)
        self.app=Developer(self.new_window)
        
        

if __name__ == '__main__': 
    root8 = Tk()
    obj = Main_Dashboard(root8)
    root8.mainloop()

          