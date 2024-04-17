from tkinter import *
from tkinter import ttk
from typing import Counter
from PIL import ImageTk , Image
import tkinter.messagebox as msg
import mysql.connector
from verify_email import verify_email
import time
from twilio.rest import Client
import smtplib
import random

class register_page:
    def __init__(self,root1):
        self.root1=root1
        w=root1.winfo_screenwidth()
        h=root1.winfo_screenheight()
        self.root1.geometry("{}x{}+0+0".format(w,h))
        self.root1.iconbitmap('icon.ico')
        self.root1.title("Register Page")
    
        

        #----------set uppper first image----------
        img=Image.open(r"img\2up1.jpeg")
        img=img.resize((w//2,130),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img)
        self.img_l1=Label(self.root1,image=self.img1)
        self.img_l1.place(x=0,y=0,width=w/3,height=130)
         
         #---------set upper second image----------
        img=Image.open(r"img\up2.jpg")
        img=img.resize((w//2,130),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img)
        self.img_l2=Label(self.root1,image=self.img2)
        self.img_l2.place(x=w/3,y=0,width=w/3,height=130)

        #---------set upper third image------------
        img=Image.open(r"img\2up3.jpg")
        img=img.resize((w//2,130),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(img)
        self.img_l3=Label(self.root1,image=self.img3)
        self.img_l3.place(x=2*w/3-1,y=0,width=w/3,height=130)
        
        #----------set background image-------------
        img=Image.open(r"img\dash.png")
        img=img.resize((w,h-50),Image.ANTIALIAS)    
        self.img4=ImageTk.PhotoImage(img)
        self.bgimg_l3=Label(self.root1,image=self.img4)
        self.bgimg_l3.place(x=0,y=130,width=w,height=h-130)

        # -------------Title------------
        self.title_lb=Label(self.bgimg_l3,text="CREATE NEW ACCOUNT",bg='#caedf6',fg='red',font=("algerian",35,'bold'))
        self.title_lb.place(x=0,y=0,width=w,height=45)

        #---------make back label------------
        self.register_label=Label(self.bgimg_l3,bg='white')
        self.register_label.place(x=200,y=80,width=(w-400),height=(h-160-130))

        #------------left frame-------------
        self.left_frame=Frame(self.register_label,bg='white')
        self.left_frame.place(x=0,y=0,width=370,height=(h-160-135))

        #------------add photo on left frame---------
        img=Image.open(r"img\ai.jpg")
        img=img.resize((370,467),Image.ANTIALIAS)    
        self.frame_photo=ImageTk.PhotoImage(img)
        self.photo_lb=Label(self.left_frame,image=self.frame_photo)
        self.photo_lb.place(x=0,y=0)


        #---------right frame-----------
        self.right_frame=Frame(self.register_label,bg='#EBFCF9')
        self.right_frame.place(x=371,y=0,width=(w-400-376),height=(h-160-135))

        #---------design right frame----------
        self.heading=Label(self.right_frame,text="REGISTER HERE",bg='#EBFCF9',fg='green',font=('algerian',25,'bold'))
        self.heading.place(x=165,y=15,width=260,height=30)

        #-------first name label------------
        self.fname=Label(self.right_frame,text="FIRST NAME*",bg='#EBFCF9',fg='black',font=('times new roman',11,"bold"))
        self.fname.place(x=80,y=60,width=104,height=20)

        self.fname=StringVar()
        self.fname_entry=Entry(self.right_frame,bg='white',textvariable=self.fname,font=('arial',12))
        self.fname_entry.place(x=80,y=80,width=160,height=25)
        self.fname_entry.focus()

        #-------last name label----------
        self.lname=Label(self.right_frame,text="LAST NAME",bg='#EBFCF9',fg='black',font=('times new roman',11,"bold"))
        self.lname.place(x=350,y=60,width=95,height=20)
        
        self.lname=StringVar()
        self.lname_entry=Entry(self.right_frame,bg='white',textvariable=self.lname,font=('arial',12))
        self.lname_entry.place(x=350,y=80,width=160,height=25)
        self.lname_entry.focus()

        #---------Designation label----------
        self.desig_label=Label(self.right_frame,text="DESIGNATION*",bg='#EBFCF9',fg='black',font=('times new roman',11,"bold"))
        self.desig_label.place(x=80,y=125,width=114,height=20)

        self.designation=StringVar()
        self.desig_combo=ttk.Combobox(self.right_frame,textvariable=self.designation,state='readonly',font=('arial',11))
        self.desig_combo['values']=('Select','Director',"Principal",'HOD','Teacher','Other')
        self.desig_combo.current(0)
        self.desig_combo.place(x=80,y=145,width=160,height=25)
        

        #--------- Department label--------
        self.department_label=Label(self.right_frame,text="DEPARTMENT*",bg='#EBFCF9',fg='black',font=('times new roman',11,"bold"))
        self.department_label.place(x=350,y=125,width=114,height=20)

        self.department=StringVar()
        self.department_combo=ttk.Combobox(self.right_frame,textvariable=self.department,state='readonly',font=('arial',11))
        self.department_combo['values']=('Select','CSE',"IT",'CIVIL','ME','EE','EC','Other')
        
        self.department_combo.place(x=350,y=145,width=160,height=25)
        self.department_combo.current(0)

        if self.designation.get()=='Director' or self.designation.get()=='Principal' or self.designation.get()=='other':
            self.department_combo.config(state='disabled')

        #---------mobile no. label----------
        self.mobile=Label(self.right_frame,text="MOBILE NO.*",bg='#EBFCF9',fg='black',font=('times new roman',11,"bold"))
        self.mobile.place(x=80,y=190,width=104,height=20)

        self.mobile=StringVar()
        self.mobile_entry=Entry(self.right_frame,bg='white',textvariable=self.mobile,font=('arial',12))
        self.mobile_entry.place(x=80,y=210,width=160,height=25)
        self.mobile_entry.focus()

        #------------whatsapp no. label------------
        self.whatsapp=Label(self.right_frame,text="WHATSAPP NO.*",bg='#EBFCF9',fg='black',font=('times new roman',11,"bold"))
        self.whatsapp.place(x=350,y=190,width=124,height=20)

        self.whatsapp=StringVar()
        self.whatsapp_entry=Entry(self.right_frame,bg='white',textvariable=self.whatsapp,font=('arial',12))
        self.whatsapp_entry.place(x=350,y=210,width=160,height=25)
        self.whatsapp_entry.focus()
        
        #------------email id label------------
        self.email=Label(self.right_frame,text="EMAIL ID*",bg='#EBFCF9',fg='black',font=('times new roman',11,"bold"))
        self.email.place(x=80,y=255,width=79,height=20)

        self.email=StringVar()
        self.email_entry=Entry(self.right_frame,bg='white',textvariable=self.email,font=('arial',12))
        self.email_entry.place(x=80,y=275,width=160,height=25)
        self.email_entry.focus()

        #------------verify button-----------
        self.verify_button=Button(self.right_frame,text="Verify",command=self.verify,bg='#EBFCF9',bd=0,fg='red',font=('times new roman',11,'bold'),cursor="hand2")
        self.verify_button.place(x=243,y=275,width=55,height=20)
    
        #-----------otp label------------
        self.otp=Label(self.right_frame,text="OTP*",bg='#EBFCF9',fg='black',font=('times new roman',11,"bold"))
        self.otp.place(x=350,y=255,width=36,height=20)

        self.otp=StringVar()
        self.otp_entry=Entry(self.right_frame,bg='white',textvariable=self.otp,font=('arial',12))
        self.otp_entry.place(x=350,y=275,width=100,height=25)
        self.otp_entry.focus()

        #---------resend button----------------
        self.resend_button=Label(self.right_frame,bd=0,bg='#EBFCF9',fg='#004D0E',font=('times new roman',11,"bold"),cursor="hand2")
        self.resend_button.place(x=457,y=275,width=60,height=25)

        #-------------password label-------------
        self.password=Label(self.right_frame,text="PASSWORD*",bg='#EBFCF9',fg='black',font=('times new roman',11,"bold"))
        self.password.place(x=80,y=320,width=90,height=20)

        self.pass_word=StringVar()
        self.password_entry=Entry(self.right_frame,bg='white',textvariable=self.pass_word,font=('arial',12))
        self.password_entry.place(x=80,y=340,width=160,height=25)
        self.password_entry.focus()

        #----------confirm password label-----------
        self.confirm_pass=Label(self.right_frame,text="CONFIRM PASSWORD*",bg='#EBFCF9',fg='black',font=('Vrinda',10,'bold'))
        self.confirm_pass.place(x=350,y=320,width=145,height=20)

        self.con_pass=StringVar()
        self.confirm_pass_entry=Entry(self.right_frame,bg='white',textvariable=self.con_pass,font=('arial',12))
        self.confirm_pass_entry.place(x=350,y=340,width=160,height=25)
        self.confirm_pass_entry.focus()

        #------------submit button-------------
        self.submit_button=Button(self.right_frame,text="SUBMIT",command=self.submit,bg='#248f24',fg='#EBFCF9',font=('times new roman',15),cursor="hand2")
        self.submit_button.place(x=243,y=390,width=100,height=30)

        #--------already registered label---------
        self.already_lb=Label(self.right_frame,text='Already registered?',bg='#EBFCF9',fg='black',font=('times new roman',11,'bold'))
        self.already_lb.place(x=210,y=425,width=130,height=20)

        #------------login button--------------
        self.login_btn=Button(self.right_frame,text="Login",command=self.login_page,bg='#EBFCF9',fg='red',bd=0,font=('times new roman',11,'bold'),cursor="hand2")
        self.login_btn.place(x=340,y=425,width=45,height=20)

        self.click=0

    def resend(self,event):
        self.update()
        self.send_otp()
        
    def update(self):
        self.sec=180     
        def count():
            if self.sec>0:
                global sec
                self.sec -= 1
                self.resend_button.config(text=str(self.sec)+" Sec",state="disabled",disabledforeground='red',cursor='arrow')
                self.resend_button.after(1000, count) 
            else:
                self.resend_button.configure(text='Resend',state="active",cursor='hand2',activeforeground='#004D0E',activebackground='#EBFCF9')
                self.resend_button.bind("<Button-1>", self.resend)
        count()
        
    

    def send_otp(self):
        self.generate_otp=random.randint(1000,9999)
        #-----------for mobile otp--------
        #self.sid="xxxxxxx"
        #self.token="xxxxxxxxxx" 
        #self.client=Client(self.sid,self.token)
        #self.body=f"Your verification Code is : {self.generate_otp}"
        

        #-----------for email otp-----------
        self.my_email="xxxxxxxxxxx@gmail.com"
        self.app_pass='xxxxxxxxxx'
        self.receiver_email=self.email.get()
        self.subject="Facial Attendance Verification OTP"
        self.full_msg=f"Your Verification OTP is : {self.generate_otp}\n\n\n\nPlease do not share it with anyone for security reasons. Thank you for using Facial Attendance Software offered by SDCET MUZAFFARNAGAR.\n\n\n\n              This is a system generated email please do not reply on it"
        self.message="Subject:{}\nTo:{}\n\n\n{}".format(self.subject,self.email_id.get(),self.full_msg)
        try:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login(self.my_email,self.app_pass)
            s.sendmail(self.my_email,self.receiver_email,self.message)
            s.quit()

            #self.client.messages.create(from_="+12513877838" ,body=self.body,to="+91"+f"{self.mobile.get()}")
            msg.showinfo("Success",'OTP Sent Successfully\n Please Check Your Email',parent=self.right_frame)
        except Exception:
            msg.showerror("Error","Unable to send email",parent=self.right_frame)
        
        



    def verify(self):
        global click
        if self.email.get()=='':
            msg.showerror('Error',"Please Enter Email Id",parent=self.right_frame) 
        else:
            self.result=verify_email(self.email.get())
            if self.result==True:
                self.click=1
                conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxxxx',database='register')
                cur_sor=conn.cursor()
                query=('select * from register_table where email=%s')
                value=(self.email.get(),)
                cur_sor.execute(query,value)
                row=cur_sor.fetchone()
                if row!=None:
                    msg.showerror('Error',"User already exist,Try another email id",parent=self.right_frame)
                else:
                    self.verify_button.config(text="Verified",state="disabled",disabledforeground='green',cursor='arrow') 
                    self.update()
                    self.send_otp()
                
            else:
                msg.showerror("Error","Invalid Email id, Please Try Again",parent=self.right_frame)  
            
              
                   

    #-----------for submit button----------
    def submit(self):
        
        if self.fname.get()=="" or self.designation.get()=="Select" or self.department.get()=='Select' or self.mobile.get()=="" or self.whatsapp.get()=="" or self.email.get()=='' or self.pass_word.get()=="" or self.con_pass.get()=="" or self.otp.get()=='': 
            msg.showerror('Error',"All fields are required",parent=self.right_frame)
        elif self.click==0:
            msg.showerror("Error","Please Verify Your Email")
        elif self.otp.get()!=str(self.generate_otp):
            msg.showerror("Error","Invalid OTP Please Try Again")
        elif self.pass_word.get()!=self.con_pass.get():
            msg.showerror("Error","passwords must be same",parent=self.right_frame)
        
        else:
            conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxx',database='register')
            cur_sor=conn.cursor()
            query=('select * from register_table where email=%s')
            value=(self.email.get(),)
            cur_sor.execute(query,value)
            row=cur_sor.fetchone()
            if row!=None:
                msg.showerror('Error',"User already exist,Try another email id",parent=self.right_frame)
            else:
                cur_sor.execute("insert into register_table values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.fname.get(),self.lname.get(),self.designation.get(),self.department.get(),self.mobile.get(),self.whatsapp.get(),self.email.get(),self.pass_word.get()))
                msg.showinfo("Success","Register Successfully  Please Login",parent=self.right_frame)
                self.root1.destroy()
                import login
                
                
            conn.commit()
            conn.close()
        
            
        


    #-------connect login page---------
    def login_page(self):
            self.root1.destroy()
            from login import login_page
            



root1=Tk()
obj=register_page(root1)
root1.mainloop()