from tkinter import *
from PIL import ImageTk , Image ,ImageDraw
from datetime import *
import time
from math import *
import tkinter.messagebox as msg
import mysql.connector
from verify_email import verify_email
from twilio.rest import Client
import smtplib
import random


class login_page:
    def __init__(self,root3):
        self.root3=root3
        self.root3.title("Login Page")
        w=root3.winfo_screenwidth()
        h=root3.winfo_screenheight()
        self.root3.geometry("{}x{}+0+0".format(w,h))
        self.root3.iconbitmap('icon.ico')

        #----------set uppper first image-----------
        img=Image.open(r"img\up1.jpg")
        img=img.resize((w//2,130),Image.ANTIALIAS)
        self.p1=ImageTk.PhotoImage(img)
        self.img_l1=Label(self.root3,image=self.p1)
        self.img_l1.place(x=0,y=0,width=w/3,height=130)
         
         #----------set upper second image-----------
        img=Image.open(r"img\up2.jpg")
        img=img.resize((w//2,130),Image.ANTIALIAS)
        self.p2=ImageTk.PhotoImage(img)
        self.img_l2=Label(self.root3,image=self.p2)
        self.img_l2.place(x=w/3,y=0,width=w/3,height=130)

        #-------------set upper third image------------
        img=Image.open(r"img\up3.jpg")
        img=img.resize((w//2,130),Image.ANTIALIAS)
        self.p3=ImageTk.PhotoImage(img)
        self.img_l3=Label(self.root3,image=self.p3)
        self.img_l3.place(x=2*w/3-1,y=0,width=w/3,height=130)
        
        #---------------set background image--------------
        img=Image.open(r"img\back.jpeg")
        img=img.resize((w,h-130),Image.ANTIALIAS)
        self.p4=ImageTk.PhotoImage(img)
        self.bgimg_l3=Label(self.root3,image=self.p4)
        self.bgimg_l3.place(x=0,y=130,width=w,height=h-130)

        # -------------Title----------
        self.title_lb2=Label(self.bgimg_l3,text="AUTOMATIC FACE RECOGNITION ATTENDANCE SYSTEM",bg='#caedf6',fg='red',font=("algerian",35,'bold'))
        self.title_lb2.place(x=0,y=0,width=w,height=45)

        #-----------login frame--------------
        self.login_frame=Frame(self.bgimg_l3,bg="#caedf6")
        self.login_frame.place(x=495,y=160,width=500,height=300)

        # -------------write login here--------------
        self.login_here=Label(self.login_frame,text="LOGIN HERE",fg='#ff0066',bg='#caedf6',font=("times new roman",23,"bold"))
        self.login_here.place(x=150,y=15,width=200,height=42)
        
        # -----------for email------------ -
        self.email_lb=Label(self.login_frame,text="EMAIL ADDRESS",fg='black',bg='#caedf6',font=("times new roman",12,'bold'))
        self.email_lb.place(x=149,y=80)
        self.email=StringVar()
        self.email_entry=Entry(self.login_frame,textvariable=self.email,bg='white',font=("times new roman",15))
        self.email_entry.place(x=151,y=100,width=230,height=25)
        self.email_entry.focus()

        # ----------------for password----------
        self.pass_lb=Label(self.login_frame,text="PASSWORD",fg='black',bg='#caedf6',font=("times new roman",12,'bold'))
        self.pass_lb.place(x=149,y=145)
        self.password=StringVar()
        self.pass_entry=Entry(self.login_frame,textvariable=self.password,bg='white',font=("times new roman",15))
        self.pass_entry.place(x=151,y=165,width=230,height=25)
        self.pass_entry.focus()

        #---------------forgot button-------------
        self.forgot_button=Button(self.login_frame,text="Forgot Password?",command=self.forgot_window,fg='red',bg='#caedf6',bd=0,font=("times new roman",12,'bold'),cursor="hand2")
        self.forgot_button.place(x=259,y=195,width=135,height=22)



        #-------------login Button-----------------
        self.login_button=Button(self.login_frame,text="Login",command=self.login,fg='white',bg='green',font=("times new roman",15,'bold'),cursor="hand2")
        self.login_button.place(x=151,y=230,width=100,height=35)

        #-------------register Button--------------
        self.login_button=Button(self.login_frame,text="Register",command=self.register_page,fg='white',bg='#0075FA',font=("times new roman",15,'bold'),cursor="hand2")
        self.login_button.place(x=280,y=230,width=100,height=35)


        #-------------clock label-------------
        self.clock_label=Label(self.bgimg_l3,bg="grey")
        self.clock_label.place(x=395,y=180,width=220,height=260)
        
        self.clock_run() 

    def forgot_window(self):
        self.root2=Toplevel()
        self.root2.title("Forgot Password")
        self.root2.geometry("425x270+618+320")
        self.root2.resizable(0,0)
        

        #forgot screen label
        self.forgot_lb=Label(self.root2,bg='#caedf6')
        self.forgot_lb.place(x=0,y=0,width=425,height=270)

        #title
        self.forgot_title=Label(self.forgot_lb,text="FORGOT PASSWORD",bg='#caedf6',fg='red',font=("algerian",15,'bold'))
        self.forgot_title.place(x=2,y=2,width=420,height=25)

        #email label
        self.forgot_email_lb=Label(self.forgot_lb,text="EMAIL ID",fg='black',bg='#caedf6',font=("times new roman",12,'bold'))
        self.forgot_email_lb.place(x=3,y=40,width=75,height=18)
        self.forgot_email=StringVar()
        self.forgot_email_entry=Entry(self.forgot_lb,textvariable=self.forgot_email,bg='white',font=("times new roman",15))
        self.forgot_email_entry.place(x=3,y=59,width=180,height=25)
        self.forgot_email_entry.focus()

        #verify button
        self.forgot_verify_button=Button(self.forgot_lb,text="Verify",command=self.verifyemail,bg='#caedf6',bd=0,fg='red',font=('times new roman',11,'bold'),cursor="hand2")
        self.forgot_verify_button.place(x=183,y=59,width=55,height=20)

        #otp label
        self.forgot_otp_lb=Label(self.forgot_lb,text="OTP",fg='black',bg='#caedf6',font=("times new roman",12,'bold'))
        self.forgot_otp_lb.place(x=240,y=40,width=30,height=18)
        self.forgot_otp=StringVar()
        self.forgot_otp_entry=Entry(self.forgot_lb,textvariable=self.forgot_otp,bg='white',font=("times new roman",15))
        self.forgot_otp_entry.place(x=240,y=59,width=100,height=25)
        self.forgot_otp_entry.focus()

        #resend button
        self.forgot_resend_button=Button(self.forgot_lb,bd=0,bg='#caedf6',fg='#004D0E',font=('times new roman',11,"bold"),cursor="hand2")
        self.forgot_resend_button.place(x=343,y=58,width=60,height=25)

        #New passwor label
        self.new_pass_lb=Label(self.forgot_lb,text="NEW PASSWORD",fg='black',bg='#caedf6',font=("times new roman",12,'bold'))
        self.new_pass_lb.place(x=3,y=115,width=130,height=18)
        self.new_pass=StringVar()
        self.new_pass_entry=Entry(self.forgot_lb,textvariable=self.new_pass,bg='white',font=("times new roman",15))
        self.new_pass_entry.place(x=3,y=133,width=180,height=25)
        self.new_pass_entry.focus()

        #confirm label
        self.conf_pass_lb=Label(self.forgot_lb,text="CONFIRM PASSWORD",fg='black',bg='#caedf6',font=("times new roman",12,'bold'))
        self.conf_pass_lb.place(x=240,y=115,width=172,height=18)
        self.conf_pass=StringVar()
        self.conf_pass_entry=Entry(self.forgot_lb,textvariable=self.conf_pass,bg='white',font=("times new roman",15))
        self.conf_pass_entry.place(x=240,y=133,width=180,height=25)
        self.conf_pass_entry.focus()

        #reset button
        self.reset_button=Button(self.forgot_lb,text="Reset",command=self.reset,fg='white',bg='green',font=("times new roman",15,'bold'),cursor="hand2")
        self.reset_button.place(x=163,y=190,width=100,height=35)

        self.root2.mainloop()
    
    def resend(self,event):
        self.update()
        self.send_otp()   

    def update(self):
        self.sec=180
        def count():
            if self.sec>0:
                global sec
                self.sec -= 1
                self.forgot_resend_button.config(text=str(self.sec)+" Sec",state="disabled",disabledforeground='red',cursor='arrow')
                self.forgot_resend_button.after(1000, count) 
            else:
                self.forgot_resend_button.config(text='Resend',state="active",cursor='hand2',activeforeground='#004D0E',activebackground='#caedf6')    
                self.forgot_resend_button.bind("<Button-1>", self.resend)
        count() 

    def send_otp(self):
        self.generate_otp=random.randint(1000,9999)
        #-----------for mobile otp--------
        #self.sid="xxxxxxxxxxxxx"
        #self.token="xxxxxxxxxxxxx" 
        #self.client=Client(self.sid,self.token)
        #self.body=f"Your verification Code is : {self.generate_otp}"
        

        #-----------for email otp-----------
        self.my_email="xxxxxxxxxxx@gmail.com"
        self.app_pass='xxxxxxxxxxxxx'
        self.receiver_email=self.forgot_email.get()
        self.subject="Facial Attendance Verification OTP"
        self.full_msg=f"Your Verification OTP is : {self.generate_otp}\n\n\n\nPlease do not share it with anyone for security reasons. Thank you for using Facial Attendance Software offered by SDCET MUZAFFARNAGAR.\n\n\n\n                   This is a system generated email please do not reply on it"
        self.message="Subject:{}\nTo:{}\n\n\n{}".format(self.subject,self.email_id.get(),self.full_msg)
        try:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login(self.my_email,self.app_pass)
            s.sendmail(self.my_email,self.receiver_email,self.message)
            s.quit()

            #self.client.messages.create(from_="+12513877838" ,body=self.body,to="+91"+f"{self.mobile.get()}")
            msg.showinfo("Success",'OTP Sent Successfully\n Please Check Your Email',parent=self.forgot_lb)
        except Exception:
            msg.showerror("Error","Unable to send email",parent=self.forgot_lb)  

    def verifyemail(self):
        conn=mysql.connector.connect(host='localhost',user="root",password='xxxxx',database='register')
        cur_sor=conn.cursor()
        query=('select * from register_table where email=%s')
        value=(self.forgot_email.get(),)
        cur_sor.execute(query,value)
        row=cur_sor.fetchone()
        if self.forgot_email.get()=='':
            msg.showerror('Error',"Please Enter Email Id",parent=self.forgot_lb)

        elif row==None:
                msg.showerror('Error',"Email id doesn't exist",parent=self.forgot_lb)
        
        else:
            result=verify_email(self.forgot_email.get())
            if result==True: 
                self.forgot_verify_button.config(text="Verified",state="disabled",disabledforeground='green',cursor='arrow') 
                
                self.update()
                self.send_otp()
            else:
                msg.showerror("Error","Invalid Email id, Please Try Again",parent=self.forgot_lb)
        conn.commit()
        conn.close()         

    def reset(self):
        if self.forgot_email.get()=="" or self.forgot_otp.get()=='' or self.new_pass.get()=="" or self.conf_pass.get()=='':
            msg.showerror("Error", "All Fields are required",parent=self.forgot_lb)
        elif self.new_pass.get()!=self.conf_pass.get():
            msg.showerror("Error","Passwords must be same",parent=self.forgot_lb)
            
        else:
            conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxxxx',database='register')
            cur_sor=conn.cursor()
            query=('select * from register_table where email=%s')
            value=(self.forgot_email.get(),)
            cur_sor.execute(query,value)
            row=cur_sor.fetchone()
            query=("update register_table set password=%s where email=%s")
            value=(self.new_pass.get(),self.forgot_email.get())
            cur_sor.execute(query,value)
            msg.showinfo("Success","Your Password has been reset, Please login",parent=self.forgot_lb)
            self.root2.destroy()


            conn.commit()
            conn.close()

    
        


    def login(self):
        if self.email.get()=='' or self.password.get()=='':
            msg.showerror('Error',"All field required")
        else:
            conn=mysql.connector.connect(host='localhost',user="root",password='xxxxx',database='register')
            cur_sor=conn.cursor()
            cur_sor.execute('select * from register_table where email=%s and password=%s',(self.email.get(),self.password.get()))
            row=cur_sor.fetchone() 
            if row==None:
                msg.showerror("Error","Invalid Email or Password")
            else:
                msg.showinfo("success","Login Successfully")
                self.dashboard()
                
                


        

    def dashboard(self):
        from dashboard import Main_Dashboard     
        self.new_window=Toplevel(self.root3)
        self.app=Main_Dashboard(self.new_window)

    #---------connect register page------------
    def register_page(self):
        self.root3.destroy()
        from register import register_page
            
            
        
            

    def clock_drawing(self,hh,mm,ss):

        #--------set clock on image-----------
        pic=Image.new("RGB",(220,260),(0,0,0)) #create image
        draw=ImageDraw.Draw(pic)
        watch=Image.open(r"D:\PROJECT\img\clock.png")
        watch=watch.resize((200,200),Image.ANTIALIAS)
        pic.paste(watch,(10,40))

        # Draw hour line
        draw.line((110,140,110+45*sin(radians(hh)),140-45*cos(radians(hh))),fill='#ff0066',width=3) #len=45

        # Draw Min line
        draw.line((110,140,110+55*sin(radians(mm)),140-55*cos(radians(mm))),fill='blue',width=3)    #len=35

        # Draw sec line
        draw.line((110,140,110+62*sin(radians(ss)),140-62*cos(radians(ss))),fill='green',width=3)    #len=45

        # Draw clock center
        draw.ellipse((105,135,115,145),fill='red')

        pic.save(r"img\new_clock.png")

    def clock_run(self):

        # ------Access current Time from system----------
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        #-------- calculate the angle of time---------
        hh=float((h+m/60.0)/12)*360
        mm=float(m/60)*360
        ss=float(s/60)*360
        

        self.clock_drawing(hh,mm,ss)   #function calling

        self.img=ImageTk.PhotoImage(file=r"D:\PROJECT\img\new_clock.png")   
        self.clock_label.config(image=self.img)  
        self.clock_label.after(100,self.clock_run)    #refersh label after 100 msec   
        







root3=Tk()
obj=login_page(root3)
root3.mainloop()
