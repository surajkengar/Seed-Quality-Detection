import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="#ADDFFF")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("800x550+200+50")
root.title("Sign-In")


lbl = tk.Label(root, text="Seed Quality Detection", font=('times', 25,' bold '), height=1, width=40,bg="#ADDFFF",fg="#0000FF")
lbl.place(x=0, y=3)

username = tk.StringVar()
password = tk.StringVar()
        



def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            root.destroy()

            from subprocess import call
            call(['python','GUI_Master_old.py'])

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')



title=tk.Label(root, text="Login Here", font=("times", 30, "bold"),bd=5,bg="#ADDFFF",fg="#000000")
title.place(x=250,y=80,width=250)
        
Login_frame=tk.Frame(root,bg="#ADDFFF")
Login_frame.place(x=100,y=150)
        

        
lbluser=tk.Label(Login_frame,text="Username:",compound=LEFT,font=("Times new roman", 20, "bold"),bg="#ADDFFF").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password:",compound=LEFT,font=("Times new roman", 20, "bold"),bg="#ADDFFF").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Submit",bd=5,command=login,width=15,font=("Times new roman", 14, "bold"),bg="#0000FF",fg="#FFFFFF")
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Sign-Up",bd=5, command=registration,width=15,font=("Times new roman", 14, "bold"),bg="#008000",fg="#FFFFFF")
btn_reg.grid(row=3,column=0,pady=10)
        
       

root.mainloop()