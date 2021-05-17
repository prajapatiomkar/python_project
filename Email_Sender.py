# The Code Written by Prajapati omkar on 09-05-2021.

## --------------------------------- Email Sending Application in Python Using Tkinter,SMTP modules -------------------------------------------------------##

# Module Section.

from tkinter import *
import smtplib as s
from tkinter import messagebox
window = Tk()
window.title("EMAIL SENDER...!")
window.geometry("500x400")

# Function
def m_send():

    try:
        s_e = sender_e1.get()
        s_p = sender_p1.get()
        r_e = receiver_e2.get()
        sub = subject_e.get()
        body = text_a.get(1.0, "end-1c")

        if s_e == "" or s_p == "" or r_e == "":
            messagebox.showinfo("Field Error", "All Field Are Compulsary")
        else:
            e_server = s.SMTP("smtp.gmail.com", 587)
            e_server.starttls()
            e_server.login(s_e, s_p)
            finall_m = "subject:{}\n\n{}".format(sub, body)
            e_server.sendmail(s_e, r_e, finall_m)

            print("Mail Successfully Sended...!")

            e_server.quit()
    except Exception as e:
        print("Error", e)

def clear():
    sender_e1.delete(0, "end")
    sender_p1.delete(0, "end")
    receiver_e2.delete(0, "end")
    subject_e.delete(0, "end")
    text_a.delete("1.0", "end")

def exit():
    window.destroy()

# Frame

frame1 = Frame(window, bg="white", relief=SOLID, border=2)
frame1.pack()

heading = Label(frame1, bg="black", foreground="white", text="Email Sender",
                width=80, font=("Helvetica", 20, "bold"), bd=1, relief=SOLID)
heading.pack(padx=1, pady=1)

canvas = Canvas(window, bg="black", width=200, height=200)
canvas.pack(fill="both", expand=True)

# Entry Storage Area
sender_e1 = StringVar()
sender_p1 = StringVar()
receiver_e2 = StringVar()
subject_e = StringVar()

# User Input Section

sender_e1 = Entry(canvas, relief=SUNKEN, bg="black",
                  foreground="white", width=30)
sender_e1.place(x=170, y=50)

sender_p1 = Entry(canvas, relief=SUNKEN, bg="black",
                  foreground="white", show="*", width=30)
sender_p1.place(x=170, y=80)

receiver_e2 = Entry(canvas, relief=SUNKEN, bg="black",
                    foreground="white", width=30)
receiver_e2.place(x=170, y=110)

subject_e = Entry(canvas, relief=SUNKEN, bg="black", foreground="white",
                  width=32, font=("Microsoft YaHei Light", 12, ""))
subject_e.place(x=170, y=140)


# Text Area
sender_email = Label(canvas, text="Sender_Email", relief=SUNKEN, width=16,
                     bg="black", foreground="white", font=("Helvetica", 9, "bold"))
sender_email.place(x=30, y=50)

sender_passwd = Label(canvas, text="Sender_Password", relief=SUNKEN,
                      width=16, bg="black", foreground="white", font=("Helvetica", 9, "bold"))
sender_passwd.place(x=30, y=80)

receiver_email = Label(canvas, text="Receiver_Email", relief=SUNKEN,
                       width=16, bg="black", foreground="white", font=("Helvetica", 9, "bold"))
receiver_email.place(x=30, y=110)

user_subject = Label(canvas, text="Subject", relief=SUNKEN, width=16,
                     bg="black", foreground="white", font=("Helvetica", 9, "bold"))
user_subject.place(x=30, y=140)

# Button Section
send_Butt = Button(canvas, text="Send", width=11, height=2, bg="black",
                   foreground="white", font=("Helvetica", 9, "bold"), command=m_send)
send_Butt.place(x=370, y=50)
clear_Butt = Button(canvas, text="Clear", width=4, bg="black",
                    foreground="white", font=("Helvetica", 9, "bold"), command=clear)
clear_Butt.place(x=370, y=100)
exit_Butt = Button(canvas, text="Exit", width=4, bg="black",
                   foreground="white", font=("Helvetica", 9, "bold"), command=exit)
exit_Butt.place(x=420, y=100)

# Message section

text_a = Text(canvas, bg="black", foreground="white", font=(
    "Lucida Console", 11, ""), width=48, height=10)
text_a.place(x=30, y=180)

window.mainloop()