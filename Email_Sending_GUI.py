from tkinter import *
import smtplib as s
from tkinter import messagebox

# main screen
window=Tk()
window.title("Email_Sender_By_Prajapati_Omkar...!")
window.geometry("600x400")

#Function
def send():

    try:
        to=Entry1_.get()
        subject=Entry2_.get()
        body=text1.get(1.0, "end-1c")
        if to=="" or subject=="" or body=="":
            messagebox.showinfo("Field Error","All Field Compulsary")
        else:
            server=s.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login("","") #<--Here you have to put Email_Id and Password of your Email_Id under the "Double Quote"
            finalmess='subject:{}\n\n{}'.format(subject,body)
            server.sendmail("prajapatiomkar070@gmail.com",to,finalmess)
            print("Mail...Send Succesfully..!")
            server.quit()
    except Exception as e:
        print("Error",e)

def rest():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    text1.delete("1.0",'end')

def close():
    window.destroy()

#Graphics
canvas1 = Label(window,text="Email Sending Application..",bg="grey",height=1,width=85,border=3,relief="solid").place(x=0,y=0)
lable1=Label(window,text="To: ",width=7).place(x=0,y=40,anchor=W)
lable2=Label(window,text="Subject: ",width=7).place(x=0,y=80,anchor=W)

#Storage_Area
Entry1_=StringVar()
Entry2_=StringVar()


#Entry
entry1 = Entry(window,width=50,textvariable=Entry1_)
entry1.place(x=60,y=40,anchor=W)

entry2 = Entry(window,width=50,textvariable=Entry2_)
entry2.place(x=60,y=80,anchor=W)

text1=Text(window,bg="white",width=74,height=19)
text1.place(x=0,y=100)

#Button
send_butt=Button(window,text="Send",width=8,height=3,relief=GROOVE,command=send).place(x=370,y=30)
clear_butt=Button(window,text="Clear",width=8,height=3,relief=GROOVE,command=rest).place(x=440,y=30)
close_but=Button(window,text="Exit",width=8,height=3,relief=GROOVE,command=close).place(x=510,y=30)

window.mainloop()

