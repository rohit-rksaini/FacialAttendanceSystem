from math import exp
from re import search
from tkinter import *
from types import resolve_bases
from PIL import ImageTk, Image 
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as msg
from mysql.connector.cursor import RE_SQL_ON_DUPLICATE
from verify_email import verify_email
import time
from twilio.rest import Client
import smtplib
import random
import cv2
from tkcalendar import DateEntry
import datetime
import os


class Registation():
    def __init__(self,root5):
        self.root5=root5
    

        self.root5.title('STUDENT__REGISTATION')
        w=root5.winfo_screenwidth()
        h=root5.winfo_screenheight()
        self.root5.geometry("{}x{}+0+0".format(w,h))
        self.root5.iconbitmap('icon.ico')
        self.root5.config(bg='white')

        ######## Title Frame #######

        self.title_name=Label(root5,text='STUDENT REGISTATION',font=('algerian',35,'bold'),bg='#5E9CD6',fg='red')
        self.title_name.place(x=0,y=130,width=w,height=45)

        
        

        ###### Images ########
        self.img=Image.open(r"img\reg1.jpg")
        self.img=self.img.resize((500,130),Image.ANTIALIAS)
        self.pho1=ImageTk.PhotoImage(self.img)
        self.img_l1=Label(root5,image=self.pho1)
        self.img_l1.place(x=0,y=0,width=w/3,height=130)
        

        self.img=Image.open(r"img\reg2.png")
        self.img=self.img.resize((500,130),Image.ANTIALIAS)
        self.pho2=ImageTk.PhotoImage(self.img)
        self.img_l2=Label(root5,image=self.pho2)
        self.img_l2.place(x=w/3,y=0,width=w/3,height=130)

        


        self.img=Image.open(r"img\reg3.jpg")
        self.img=self.img.resize((500,130),Image.ANTIALIAS)
        self.pho3=ImageTk.PhotoImage(self.img)
        self.img_l3=Label(root5,image=self.pho3)
        self.img_l3.place(x=2*w/3-1,y=0,width=w/3,height=130)

        ###### Frame set #########

        self.main_frame=Frame(root5,bd=3,relief=RIDGE,bg='#caedf6')
        self.main_frame.place(x=0,y=170,width=w/2,height=h-(130+110))

        self.main_frame1=Frame(root5,bd=3,relief=RAISED,bg='#5f905e')
        self.main_frame1.place(x=w/2,y=170,width=w/2,height=h-(130+110))

        self.main_frame2=Frame(self.main_frame1,bd=3,relief=RAISED,bg='blue')
        self.main_frame2.place(x=0,y=37,width=w/2-13,height=h-(130+150))
        
        ####### Scroll Box ##########

        self.scroll_x=Scrollbar(self.main_frame2,orient=HORIZONTAL)
        self.scroll_y=Scrollbar(self.main_frame2,orient=VERTICAL)
        self.table=ttk.Treeview(self.main_frame2,columns=('Student Name','Father Name','Roll Number','Email','MOB Number','Gender','DOB','Course Name','Branch','Sem','Parent Email','Address'),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)

        self.scroll_x.config(command=self.table.xview)
        self.scroll_y.config(command=self.table.yview)

        style = ttk.Style()
        style.configure("Treeview", font=('times new roman',14))
        style.configure("Treeview.Heading", font=('times new roman',14,'bold'))

        self.table.heading('Student Name',text='Student Name',anchor=CENTER)#,font=('times new roman',14,'bold'))
        self.table.heading('Father Name',text='Father Name',anchor=CENTER)
        self.table.heading('Roll Number',text='Roll Number',anchor=CENTER)
        self.table.heading('Email',text='Email',anchor=CENTER)
        self.table.heading('MOB Number',text='MOB Number',anchor=CENTER)
        self.table.heading('Gender',text='Gender',anchor=CENTER)
        self.table.heading('DOB',text='DOB',anchor=CENTER)
        self.table.heading('Course Name',text='Course Name',anchor=CENTER)
        self.table.heading('Branch',text='Branch',anchor=CENTER)
        self.table.heading('Sem',text='Sem',anchor=CENTER)
        self.table.heading('Parent Email',text='Year',anchor=CENTER)
        self.table.heading('Address',text='Address',anchor=CENTER)
        self.table['show']='headings'

        self.table.column('Student Name',width=150,anchor=CENTER)
        self.table.column('Father Name',width=150,anchor=CENTER)
        self.table.column('Roll Number',width=150,anchor=CENTER)
        self.table.column('Email',width=150,anchor=CENTER)
        self.table.column('MOB Number',width=150,anchor=CENTER)
        self.table.column("Gender",width=150,anchor=CENTER)
        self.table.column('DOB',width=150,anchor=CENTER)
        self.table.column('Course Name',width=150,anchor=CENTER)
        self.table.column('Branch',width=150,anchor=CENTER)
        self.table.column('Sem',width=150,anchor=CENTER)
        self.table.column('Parent Email',width=150,anchor=CENTER)
        self.table.column('Address',width=150,anchor=CENTER)
        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease>",self.cursor)
        self.data_fetch()
        
        
        


        self.sname=StringVar()
        self.father_name=StringVar()
        self.roll_no=StringVar()
        self.email_id=StringVar()
        self.OTP=StringVar()
        self.phone_no=StringVar()
        self.gender=StringVar()
        self.dob=StringVar()
        self.course_name=StringVar()
        self.branchs=StringVar()
        self.parent_email=StringVar()
        self.schdata=StringVar()
        self.sem=StringVar()
        



        ###### Labels F1 #############                                 #caedf6

        self.name=Label(self.main_frame,text='Student Name:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.name.place(x=3,y=15,width=120,height=20)

        self.name_entry=Entry(self.main_frame,font=('arial',15),textvariable=self.sname,relief=GROOVE,bg='white',width=40,highlightthickness=1)
        self.name_entry.place(x=140,y=13,width=170,height=28)


        self.fname=Label(self.main_frame,text='Father Name:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.fname.place(x=350,y=15,width=120,height=20)

        self.fname_entry=Entry(self.main_frame,font=('arial',15),textvariable=self.father_name,relief=GROOVE,bg='white',width=40,highlightthickness=1)
        self.fname_entry.place(x=487,y=13,width=170,height=28)

        
        self.rolln=Label(self.main_frame,text='Roll Number:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.rolln.place(x=5,y=70,width=110,height=20)

        self.rolln_entry=Entry(self.main_frame,font=('arial',15),textvariable=self.roll_no,relief=GROOVE,bg='white',width=40,highlightthickness=1)
        self.rolln_entry.place(x=140,y=68,width=170,height=28)

        
        self.course=Label(self.main_frame,text='Course Name:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.course.place(x=350,y=70,width=120,height=20)

        self.course_entry=ttk.Combobox(self.main_frame,value=('*Select your option','Diploma','B.Tech','M.Tech'),textvariable=self.course_name,font=('times new roman',15),width=42,state='readonly')
        self.course_entry.set('Select your option')
        self.course_entry.place(x=487,y=68,width=170,height=25)


        self.branch=Label(self.main_frame,text='Branch:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.branch.place(x=5,y=125,width=70,height=20)

        self.branch_entry=ttk.Combobox(self.main_frame,value=('*Select option','CSE','IT','ME','EE','CE','OTHER'),textvariable=self.branchs,font=('times new roman',15),width=14,state='readonly')
        self.branch_entry.set('Select option')
        self.branch_entry.place(x=140,y=123,width=170,height=25)


        self.semester=Label(self.main_frame,text='Semester:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.semester.place(x=350,y=125,width=80,height=20)

        self.sem_entry=ttk.Combobox(self.main_frame,value=('*Select option','1-Semester','2-Semester','3-Semester','4-Semester','5-Semester','6-Semester','7-Semester','8-Semester'),textvariable=self.sem,font=('times new roman',15),width=14,state='readonly')
        self.sem_entry.set('Select option')
        self.sem_entry.place(x=487,y=123,width=170,height=25)


        self.gen=Label(self.main_frame,text='Gender:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.gen.place(x=5,y=180,width=70,height=20)

        self.gen_entry=ttk.Combobox(self.main_frame,value=('*Select option',"Male","Female","Other"),textvariable=self.gender,font=('times new roman',15),width=14,state='readonly')
        self.gen_entry.set('Select option')
        self.gen_entry.place(x=140,y=178,width=170,height=28)

        self.DOB=Label(self.main_frame,text='Date of Birth:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.DOB.place(x=350,y=180,width=120,height=20)

        self.current_date=datetime.date.today()
        self.maxdate = self.current_date + datetime.timedelta(days=0)
        
        self.DOB_entry=DateEntry(self.main_frame, locale='en_US',maxdate=self.maxdate,textvariable=self.dob, date_pattern='dd/mm/y',font=('times new roman',14,'bold'))
        self.DOB_entry.place(x=487,y=178,width=170,height=28) 
        self.DOB_entry.delete(0,END)


        self.email=Label(self.main_frame,text='Email Id:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.email.place(x=5,y=236,width=75,height=20)

        self.email_entry=Entry(self.main_frame,font=('arial',15),textvariable=self.email_id,relief=GROOVE,bg='white',width=40,highlightthickness=1)
        self.email_entry.place(x=140,y=236,width=170,height=28)


        self.otp=Label(self.main_frame,text='OTP:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.otp.place(x=390,y=236)

        self.otp_entry=Entry(self.main_frame,font=('arial',15),textvariable=self.OTP,relief=GROOVE,bg='white',width=7,highlightthickness=1)
        self.otp_entry.place(x=487,y=236)


        self.phone=Label(self.main_frame,text='Mobile No.:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.phone.place(x=5,y=290,width=105,height=20)

        self.phone_entry=Entry(self.main_frame,font=('arial',15),textvariable=self.phone_no,relief=GROOVE,bg='white',width=40,highlightthickness=1)
        self.phone_entry.place(x=140,y=288,width=170,height=28)


        self.p_email=Label(self.main_frame,text='Parent Email:',font=('times new roman',14,'bold'),bg='#caedf6',fg='black')
        self.p_email.place(x=350,y=290,width=120,height=20)

        self.p_email_entry=Entry(self.main_frame,font=('arial',15),textvariable=self.parent_email,relief=GROOVE,bg='white',width=40,highlightthickness=1)
        self.p_email_entry.place(x=487,y=288,width=170,height=28)


        self.add=Label(self.main_frame,text='Address:',font=('times new roman',15,'bold'),bg='#caedf6',fg='black')
        self.add.place(x=5,y=360,width=75,height=20)


        self.add_entry=Text(self.main_frame,font=('arial',15),bg='white',highlightthickness=1 )
        self.add_entry.place(x=140,y=345,width=520,height=65)

        

        ###### Label F2 ########

        self.sch=Label(self.main_frame1,text='SEARCH BY:',font=('times new roman',12,'bold'),bg='#5f905e',fg='white')
        self.sch.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        

        self.sch=StringVar()
        self.sch_entry=ttk.Combobox(self.main_frame1,value=('*Select your option','Roll Number','Email'),textvariable=self.sch,font=('times new roman',15),width=15,state='readonly')
        self.sch_entry.set('Select your option')
        self.sch_entry.grid(row=0,column=1,padx=8,pady=5,sticky=W)

        ######## Button #######

        self.btn1=Button(self.main_frame,text='SUBMIT',command=self.submit,cursor='hand2',font=('arial',14,'bold'),fg="white",bg='green',width=11,highlightthickness=1)
        self.btn1.place(x=12,y=480)

        self.btn2=Button(self.main_frame,text='UPDATE',command=self.update_data,cursor='hand2',font=('arial',14,'bold'),fg="white",bg='green',width=11,highlightthickness=1)
        self.btn2.place(x=163,y=480)

        self.btn3=Button(self.main_frame,text='DELETE',command=self.delete,cursor='hand2',font=('arial',14,'bold'),fg="white",bg='green',width=11,highlightthickness=1)
        self.btn3.place(x=315,y=480)

        self.btn6=Button(self.main_frame,text='RESET',command=self.reset,cursor='hand2',font=('arial',14,'bold'),fg="white",bg='green',width=11,highlightthickness=1)
        self.btn6.place(x=467,y=480)


        self.btn4=Button(self.main_frame,text='TAKE PHOTO',command=self.take_photo,cursor='hand2',font=('arial',14,'bold'),fg="white",bg='#0075FA',width=20,highlightthickness=1)
        self.btn4.place(x=30,y=430)

        self.btn5=Button(self.main_frame,text='UPDATE PHOTO',command=self.take_photo,font=('arial',14,'bold'),cursor='hand2',fg="white",bg='#0075FA',width=20,highlightthickness=1)
        self.btn5.place(x=335,y=430)

        
        self.btn7=Button(self.main_frame1,text='SERACH',command=self.search,font=('arial',10,'bold'),cursor='hand2',fg='white',bg='red',width=7,highlightthickness=1)
        self.btn7.place(x=475,y=5,width=90)
        
        self.btn8=Button(self.main_frame1,text='SHOW ALL',command=self.data_fetch,font=('arial',10,'bold'),cursor='hand2',fg='white',bg='#0075FA',width=8,highlightthickness=1)
        self.btn8.place(x=575,y=5,width=90)

        self.btn9=Button(self.main_frame,text='Verify',command=self.verify,cursor='hand2',font=('arial',11,"bold"),bg='#caedf6',bd=0,width=6,highlightthickness=1)
        self.btn9.place(x=310,y=236)

        self.btn10=Button(self.main_frame,text='',font=('arial',11,"bold"),cursor='hand2',bg='#caedf6',bd=0,width=6,highlightthickness=1)
        self.btn10.place(x=590,y=236)



       ####### Entry #######
        
        self.sch_entry=Entry(self.main_frame1,font=('arial',15),textvariable=self.schdata,bg='white',width=15,highlightthickness=1)
        self.sch_entry.place(x=295,y=5)

        self.photo=0
        self.click=0
        self.dataclear=0
        self.timestop=0
        self.disablebutton=0

        

    def submit(self):
        global timestop
        if self.sname.get()=='' or self.father_name.get()=='' or self.roll_no.get()=='*Select option' or self.email_id.get()=='' or self.OTP=='' or self.phone_no.get()=='' or self.gender.get()=='' or self.dob.get()=='' or self.course_name.get()=='*Select your option' or self.branchs.get()=='*Select option' or self.parent_email.get()=='' or self.add_entry.get("1.0", "end-1c")=='':
             msg.showerror('Error',"All fields are required",parent=self.main_frame1)
        elif self.click==0:
            msg.showerror("Error","Please Verify Your Email",parent=self.main_frame1)
        elif self.OTP.get()!=str(self.generate_otp):
            msg.showerror("Error","Invalid OTP Please Try Again",parent=self.main_frame1)
        elif self.photo==0:
            msg.showerror('Error',"Please Add Sample Photo",parent=self.main_frame1)
        else:
            conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxx',database='student_reg')
            cur_sor=conn.cursor()
            
            query=('select * from student where roll=%s')
            value=(self.roll_no.get(),)
            cur_sor.execute(query,value)
            row=cur_sor.fetchone() 
            if row!=None:
                msg.showerror('Error',"Roll Number already exist !!",parent=self.main_frame1)
                
            else:
                cur_sor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.sname.get(),self.father_name.get(),self.roll_no.get(),self.email_id.get(),self.phone_no.get(),self.gender.get(),self.dob.get(),self.course_name.get(),self.branchs.get(),self.sem.get(),self.parent_email.get(),self.add_entry.get("1.0", "end-1c")))
                msg.showinfo("Success","Registration Completed",parent=self.main_frame1)
                self.dataclear=1
                self.timestop=1
                
                
            conn.commit()
            self.data_fetch()
            if self.dataclear==1:
                self.click=0
                self.reset()
            
            self.btn9.configure(text='verify',state="active",cursor='hand2',activeforeground='#004D0E',activebackground='#caedf6')
            self.btn9.bind("<Button-1>", self.verify)
            self.btn10.configure(text=" ",activeforeground='#004D0E',activebackground='#caedf6')
            

            conn.close()

    def data_fetch(self):
        conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxxx',database='student_reg')
        cur_sor=conn.cursor()
        cur_sor.execute("Select * from student")
        data=cur_sor.fetchall()
       
        if len(data)!=0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def cursor(self,event=' '):
        try:
            focus=self.table.focus()
            content=self.table.item(focus)
            data=content['values']

            self.sname.set(data[0])
            self.father_name.set(data[1]) 
            self.roll_no.set(data[2]) 
            self.email_id.set(data[3])
            self.phone_no.set(data[4]) 
            self.gender.set(data[5]) 
            self.dob.set(data[6]) 
            self.course_name.set(data[7]) 
            self.branchs.set(data[8])
            self.sem.set(data[9]) 
            self.parent_email.set(data[10])
            self.add_entry.insert(END,data[11])
            self.disablebutton=1
        except IndexError:
            pass
        
    
    def update_data(self):
        if self.sname.get()=='' or self.father_name.get()=='' or self.roll_no.get()=='*Select option' or self.email_id.get()=='' or self.OTP=='' or self.phone_no.get()=='' or self.gender.get()=='' or self.dob.get()=='' or self.course_name.get()=='*Select your option' or self.branchs.get()=='*Select option' or self.parent_email.get()=='' or self.add_entry.get("1.0", "end-1c")=='':
             msg.showerror('Error',"All fields are required",parent=self.main_frame1)
        elif self.click==0:
            msg.showerror("Error","Please Verify Your Email")
        elif self.OTP.get()!=str(self.generate_otp):
            msg.showerror("Error","Invalid OTP Please Try Again")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxx',database='student_reg')
                cur_sor=conn.cursor()
                cur_sor.execute("update student set name=%s,fname=%s,email=%s,mobile=%s,gender=%s,dob=%s,course=%s,branch=%s,sem=%s,year=%s,address=%s where roll=%s",(self.sname.get(),self.father_name.get(),self.email_id.get(),self.phone_no.get(),self.gender.get(),self.dob.get(),self.course_name.get(),self.branchs.get(),self.sem.get(),self.parent_email.get(),self.add_entry.get("1.0", "end-1c"),self.roll_no.get()))
                msg.showinfo("Success","Student Details Successfully  Updated",parent=self.main_frame1)
                self.dataclear=1
                self.timestop=1
                self.button_disable()
                conn.commit()
                self.data_fetch()
                if self.dataclear==1:
                    self.dataclear=0
                    self.click=0
                    self.reset()
                self.btn9.configure(text='verify',state="active",cursor='hand2',activeforeground='#004D0E',activebackground='#caedf6')
                self.btn9.bind("<Button-1>", self.verify)
                self.btn10.configure(text=" ",activeforeground='#004D0E',activebackground='#caedf6')
                conn.close()
            except Exception as e:
                msg.showerror('Error',f"Due to {str(e)}",parent=self.main_frame1)
    def delete(self):
        if self.roll_no.get()=='':
            msg.showerror('Error',"Please Select Student Data row",parent=self.main_frame1)
        else:
            try:
                delete=msg.askyesno("Delete","Do You Want to Delete This Student",parent=self.main_frame1)
                if delete>0:

                    p=r'photo'
                    for file in os.listdir(p):
                        roll=self.roll_no.get()
                        path=file.split('.')[1]
                        if roll==str(path):
                            os.remove(os.path.join(p,file)) 
                    conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxxx',database='student_reg')
                    cur_sor=conn.cursor()
                    query="delete from student where roll=%s"
                    rollno=(self.roll_no.get(),)
                    cur_sor.execute(query,rollno)
                else:
                    if not delete:
                        return
                conn.commit()
                
                conn.close()
                self.reset()
                self.btn9.configure(text='verify',state="active",cursor='hand2',activeforeground='#004D0E',activebackground='#caedf6')
                self.btn9.bind("<Button-1>", self.verify)
                self.btn10.configure(text=" ",activeforeground='#004D0E',activebackground='#caedf6')
                self.data_fetch()
                


                msg.showinfo("Success","Student Details Successfully  Deleted",parent=self.main_frame1)
                self.timestop=1
                self.button_disable()
            except Exception as e:
                msg.showerror('Error',f"Due to {str(e)}",parent=self.main_frame1)
    
    def reset(self):
        self.sname.set('')
        self.father_name.set('') 
        self.roll_no.set('') 
        self.email_id.set('')
        self.OTP.set("")
        self.phone_no.set('') 
        self.gender.set('Select option') 
        self.dob.set('') 
        self.course_name.set('Select your option') 
        self.branchs.set('Select option') 
        self.sem.set('')
        self.parent_email.set('') 
        self.add_entry.delete('1.0',END)
        self.btn9.configure(text='verify',state="active",cursor='hand2',activeforeground='#004D0E',activebackground='#caedf6')
        self.btn9.bind("<Button-1>", self.verify)
        self.timestop=1
        self.button_disable()
        
    def resend(self,event):
        self.update()
        self.send_otp()
        
    def update(self):
        global timestop
        self.sec=180     
        def count():
            if self.sec>0 and self.timestop==0:
                global sec
                self.sec -= 1
                self.btn10.config(text=str(self.sec)+" Sec",state="disabled",disabledforeground='red',cursor='arrow')
                self.btn10.after(1000, count) 
            else:
                self.btn10.configure(text='Resend',state="active",cursor='hand2',activeforeground='#004D0E',activebackground='#caedf6')
                self.btn10.bind("<Button-1>", self.resend)
        
        count()
    
    
        
    

    def send_otp(self):
        self.generate_otp=random.randint(1000,9999)
        #-----------for mobile otp--------
        #self.sid="xxxxxxxxxxxxxxxxxxxxxxxxxx"
        #self.token="xxxxxxxxxxxxxxxxxxxx" 
        #self.client=Client(self.sid,self.token)
        #self.body=f"Your verification Code is : {self.generate_otp}"
        

        #-----------for email otp-----------
        self.my_email="xxxxxxxxxxxx@gmail.com"
        self.app_pass='xxxxxxxxxx'
        self.receiver_email=self.email_id.get()
        self.subject="Facial Attendance Verification OTP"
        self.full_msg=f"Dear {self.sname.get()}\n\nYour Verification OTP is : {self.generate_otp}\n\n\n\nPlease do not share it with anyone for security reasons. Thank you for using Facial Attendance Software offered by SDCET MUZAFFARNAGAR.\n\n\n\n                This is a system generated email please do not reply on it"
        self.message="Subject:{}\nTo:{}\n\n\n{}".format(self.subject,self.email_id.get(),self.full_msg)
        try:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login(self.my_email,self.app_pass)
            s.sendmail(self.my_email,self.receiver_email,self.message)
            s.quit()

            #self.client.messages.create(from_="+12513877838" ,body=self.body,to="+91"+f"{self.mobile.get()}")
            msg.showinfo("Success",'OTP Sent Successfully\n Please Check Your Email',parent=self.main_frame1)
        except Exception:
            msg.showerror("Error","Unable to send email",parent=self.main_frame1)
        
        



    def verify(self):
        self.button_disable()
        self.disablebutton=0
        global click
        if self.email_id.get()=='':
            msg.showerror('Error',"Please Enter Email Id",parent=self.main_frame1)
        else:
            try:
                self.result=verify_email(self.email_id.get())
            
                if self.result==True:
                    self.click=1
                   
                    self.btn9.config(text="Verified",state="disabled",disabledforeground='green',cursor='arrow') 
                    self.update()
                    self.send_otp()
                
                else:
                    msg.showerror("Error","Invalid Email id, Please Try Again",parent=self.main_frame1)
            except Exception as e:
                msg.showerror('Error',f"Due to {str(e)}",parent=self.main_frame1)
    
    def take_photo(self):
        global photo
        if self.sname.get()=='' or self.father_name.get()=='' or self.roll_no.get()=='*Select option' or self.email_id.get()=='' or self.phone_no.get()=='' or self.gender.get()=='' or self.dob.get()=='' or self.course_name.get()=='*Select your option' or self.branchs.get()=='*Select option' or self.parent_email.get()=='' or self.add_entry.get("1.0", "end-1c")=='':
             msg.showerror('Error',"All fields are required",parent=self.main_frame1)
        elif self.click==0:
            msg.showerror("Error","Please Verify Your Email",parent=self.main_frame1)
        elif self.otp_entry.get()!=str(self.generate_otp):
            msg.showerror("Error","Invalid OTP Please Try Again",parent=self.main_frame1)
        else:
                face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    

                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                
                img_id=0 

                while cap.isOpened():
                    ret,frame=cap.read()
                    if face_cropped(frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        
                        path=f"photo/{self.sname.get()}.{self.roll_no.get()}.{str(img_id)}.jpg"
                        
                        cv2.imwrite(path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('Sample Photo',face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        
                        break

                cap.release()
                cv2.destroyAllWindows()
                msg.showinfo("Success",'Your Sample Photo Add Successfully !!!',parent=self.main_frame1)
                self.photo=1
            # except Exception as e:
            #     msg.showerror('Error',f"Due to {str(e)}",parent=self.main_frame1)            
    




    def search(self):
        if self.sch.get()=='Select your option':
            msg.showerror('Error',"Please Select Roll Number or Email",parent=self.main_frame1)
        elif self.schdata.get()=="":
            msg.showerror('Error',f"Please Enter {self.sch.get()}",parent=self.main_frame1)
        else:
            if self.sch.get()=='Roll Number':
                q=('select * from student where roll=%s')
            elif self.sch.get()=="Email":
                q=('select * from student where email=%s')  
            conn=mysql.connector.connect(host='localhost',user="root",password='xxxxxxxxxxxx',database='student_reg')
            cur_sor=conn.cursor()
            value=(self.schdata.get(),)
            cur_sor.execute((q),value)
            row=cur_sor.fetchall()
            
            if len(row)!=0:
                self.table.delete(*self.table.get_children())
                for i in row:
                    self.table.insert("",END,values=i)
                self.sch.set('Select your option')
                self.schdata.set("")
            else:
                msg.showerror('Error',"Student doesn't exist",parent=self.main_frame1) 

                conn.commit()
            conn.close()  
    def button_disable(self):
        if self.disablebutton==1:
            self.btn1["state"] = "disabled"
            self.btn4["state"] = "disabled"
            self.btn5["state"] = "normal"
        else:
            self.btn1["state"] = "normal"
            self.btn4["state"] = "normal"
            self.btn5["state"] = "disabled"          
        

if __name__ == '__main__':
    root5=Tk()   
    obj=Registation(root5)
    root5.mainloop()


