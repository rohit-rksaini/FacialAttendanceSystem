from tkinter import *
from types import coroutine
from PIL import ImageTk , Image
import cv2
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime
import smtplib
class Attendance:
    def __init__(self,root4):
        self.root4=root4
        self.root4.title("Attendance")
        w=root4.winfo_screenwidth()
        h=root4.winfo_screenheight()
        self.root4.geometry("{}x{}+0+0".format(w,h))
        self.root4.iconbitmap('icon.ico')

        #----------set uppper first image-----------
        img=Image.open(r"img\3up1.jpg")
        img=img.resize((w//3,130),Image.ANTIALIAS)
        self.ph1=ImageTk.PhotoImage(img)
        self.img_l1=Label(self.root4,image=self.ph1)
        self.img_l1.place(x=0,y=0,width=w/3,height=130)
         
         #----------set upper second image-----------
        img=Image.open(r"img\3up2.jpeg")
        img=img.resize((w//3,130),Image.ANTIALIAS)
        self.ph2=ImageTk.PhotoImage(img)
        self.img_l2=Label(self.root4,image=self.ph2)
        self.img_l2.place(x=w/3,y=0,width=w/3,height=130)

        #-------------set upper third image------------
        img=Image.open(r"img\3up3.jpg")
        img=img.resize((w//3,130),Image.ANTIALIAS)
        self.ph3=ImageTk.PhotoImage(img)
        self.img_l3=Label(self.root4,image=self.ph3)
        self.img_l3.place(x=2*w/3-1,y=0,width=w/3,height=130)
        
        #---------------set background image--------------
        img=Image.open(r"img\back2.png")
        img=img.resize((w,h-130),Image.ANTIALIAS)
        self.ph4=ImageTk.PhotoImage(img)
        self.bgimg_l3=Label(self.root4,image=self.ph4)
        self.bgimg_l3.place(x=0,y=130,width=w,height=h-130)

        # -------------Title----------
        self.title_lb3=Label(self.bgimg_l3,text="FACE RECOGNITION ATTENDANCE",bg='#caedf6',fg='red',font=("algerian",35,'bold'))
        self.title_lb3.place(x=0,y=0,width=w,height=45)

        


        img=Image.open(r"img\face.jpg")
        img=img.resize((445,467),Image.ANTIALIAS)
        self.ph5=ImageTk.PhotoImage(img)
        self.start_lb=Label(self.bgimg_l3,image=self.ph5,bg="white")
        self.start_lb.place(x=455,y=80,width=450,height=470)

        self.start_button=Button(self.start_lb,text="Start Attendance",command=self.start_attendance,fg='white',bg='green',font=('times new roman',15,'bold'),cursor="hand2")
        self.start_button.place(x=149,y=415,width=150,height=30)
    
    def send_notification(self,r,d,t):
        conn=mysql.connector.connect(host='localhost',user="root",password='xxxxx',database='student_reg')
        cur_sor=conn.cursor()
        query=('select email from student where roll=%s')
        value=(r,)
        row1=cur_sor.execute(query,value)
        row1=cur_sor.fetchone()
        student_email=row1[0]
        query=('select p_email from student where roll=%s')
        value=(r,)
        row2=cur_sor.execute(query,value)
        row2=cur_sor.fetchone()
        parent_email=row2[0]

        query=('select name from student where roll=%s')
        value=(r,)
        row3=cur_sor.execute(query,value)
        row3=cur_sor.fetchone()

        query=('select fname from student where roll=%s')
        value=(r,)
        row4=cur_sor.execute(query,value)
        row4=cur_sor.fetchone()


        self.my_email="facial2attendance@gmail.com"
        self.app_pass='uinvzobswnkloiod'
        self.receiver_email=student_email
        self.subject="Your Attendace Record Successfully"
        self.full_msg=f"Dear {row3[0]}\n\nYour Attendance Record Successfuly Date: {d} and Time {t} in SD College Of Engineering And Technology\n\n\n\n Thank you for using Facial Attendance Software offered by SDCET MUZAFFARNAGAR.\n\n\n\n                This is a system generated email please do not reply on it"
        self.message="Subject:{}\nTo:{}\n\n\n{}".format(self.subject,self.receiver_email,self.full_msg)
       
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(self.my_email,self.app_pass)
        s.sendmail(self.my_email,self.receiver_email,self.message)
        s.quit()
        

        self.my_email="facial2attendance@gmail.com"
        self.app_pass='uinvzobswnkloiod'
        self.receiver_email=parent_email
        self.subject=f"{row3[0]} Today Persent In College"
        self.full_msg=f"Dear {row4[0]}\n\n{row3[0]} Come To Date: {d} and Time {t} in SD College Of Engineering And Technology\n\n\n\n Thank you for using Facial Attendance Software offered by SDCET MUZAFFARNAGAR. If You\n\n\n\n                This is a system generated email please do not reply on it"
        self.message="Subject:{}\nTo:{}\n\n\n{}".format(self.subject,self.receiver_email,self.full_msg)
       
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(self.my_email,self.app_pass)
        s.sendmail(self.my_email,self.receiver_email,self.message)
        s.quit()



    def add_attendance(self,n,r,b,c):
        try:
            s='Present'
            now=datetime.now()
            d=now.strftime("%d/%m/%Y")
            t=now.strftime("%H:%M:%S")
            conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxx',database='data')
            cur_sor=conn.cursor()
            cur_sor.execute('SELECT sr_no FROM attendance ORDER BY sr_no DESC LIMIT 1')   
            row=cur_sor.fetchone() 
            if row!=None:
                self.sr=int(row[0])+1
            else:
                self.sr=1
            query=('SELECT date FROM attendance WHERE sr_no=(SELECT MAX(sr_no) FROM attendance WHERE Roll=%s)')
            #query=('select exists(select date from attendance where Roll=%s)')
            #query=('select date from attendance where Roll=%s')
            value=(r,)
            cur_sor.execute(query,value)
            row=cur_sor.fetchone() 
            self.key=0
            if row==None or row[0]!=d:
                cur_sor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s,%s,%s)",(n,r,b,c,s,d,t,str(self.sr)))
                #cur_sor.execute('insert into attendance values(%s,%s,%s,%s,%s,%s,%s,%s)',(n,r,b,c,s,d,t,self.sr))
                self.key=1
                

                conn.commit()
            conn.close()

            if self.key==1:
                self.send_notification(r,d,t)

        except Exception as e:
            pass
        
    

        
    def start_attendance(self):
        
        def draw_rectangle(img,classifier,scale,min,color,text,clf):
            self.gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=classifier.detectMultiScale(self.gray,scale,min)   
            coordinate=[]
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                roll,predict=clf.predict(self.gray[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                

                conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxx',database='student_reg')
                cur_sor=conn.cursor()

                cur_sor.execute('Select roll from student where roll='+str(roll))
                r=cur_sor.fetchone()
                r='+'.join(r)
                
                cur_sor.execute('Select name from student where roll='+str(roll))
                n=cur_sor.fetchone()
                n='+'.join(n)
            
                # n=n[0]

                cur_sor.execute('Select branch from student where roll='+str(roll))
                b=cur_sor.fetchone()
                
                b=b[0]
                

                cur_sor.execute('Select course from student where roll='+str(roll))
                c=cur_sor.fetchone()

                c=c[0]

                conn.commit()
                conn.close()
               
                
                if confidence>85:
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(127,0,255),2)
                    cv2.putText(img,f"Roll No.:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(127,0,255),2)
                    cv2.putText(img,f"Branch:{b}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(127,0,255),2)
                    self.add_attendance(n,r,b,c)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Student",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),1)

                
                coordinate=[x,y,w,h]
            return coordinate

        def reconize(img,clf,faceCascade):
            cv2.putText(img,"For Stop Attendance  Press 'Enter' key ",(50,470),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
            coordinate=draw_rectangle(img,faceCascade,1.1,10,(255,25,255),'Face',clf)
            return img
            
        
            
               

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("traindata.xml")
        
        cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        
        
        while True:
            ret,img=cap.read()
            img=reconize(img,clf,faceCascade)
            
            cv2.namedWindow("Attendance",cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Attendance",550,440)
            cv2.moveWindow("Attendance",405,245)
            cv2.imshow("Attendance",img)
            
            
            if cv2.waitKey(1)==13:
                break
        
        cap.release()
        cv2.destroyAllWindows()
    
    
        
        
        
    
if __name__ == '__main__':
    root4=Tk()
    obj=Attendance(root4)
    root4.mainloop()