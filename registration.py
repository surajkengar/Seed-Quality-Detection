import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os



window = tk.Tk()
window.geometry("700x700")
window.title("REGISTRATION FORM")
window.configure(background="#00827F")

lbl = tk.Label(window, text="Seed Quality Detection", font=('times', 18,' bold '), height=1, width=40,bg="#00827F",fg="#EEEEEE")
lbl.place(x=50, y=0)


Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()
policeno = tk.IntVar()
value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM admin_registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO admin_registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.askquestion("askquestion", "Are you sure?")
            ms.askokcancel("askokcancel", "Want to continue?")
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            window.destroy()

#####################################################################################################################################################
def login():
     from subprocess import call
     call(["python", "login.py"])
 


l1 = tk.Label(window, text="Create Your Account!!", font=("Times new roman",18, "bold"), bg="#00827F", fg="#EEEEEE")
l1.place(x=210, y=40)



l2 = tk.Label(window, text="Enter Your Name:", width=16, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF")
l2.place(x=110, y=120)
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=330, y=120)
# that is for label 2 (full name)


l3 = tk.Label(window, text="Enter Your Address:", width=16, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF")
l3.place(x=110, y=160)
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=330, y=160)


l5 = tk.Label(window, text="Enter Your Mail-Id", width=16, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF")
l5.place(x=110, y=200)
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=330, y=200)
# that is for email address

l6 = tk.Label(window, text="Enter Your Phone-number:", width=20, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF")
l6.place(x=70, y=240)
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=330, y=240)
# phone number
l7 = tk.Label(window, text="Enter Your Gender:", width=16, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF")
l7.place(x=110, y=280)
# gender
tk.Radiobutton(window, text="Male", padx=5, width=5, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF", variable=var, value=1).place(x=330,
                                                                                                                y=280)
tk.Radiobutton(window, text="Female", padx=20, width=4, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF", variable=var, value=2).place(
    x=440, y=280)

l8 = tk.Label(window, text="Enter Your Age:", width=16, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF")
l8.place(x=110, y=320)
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=330, y=320)

l4 = tk.Label(window, text="Enter Your Username", width=18, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF")
l4.place(x=90, y=360)
t3 = tk.Entry(window, textvar=username, width=20, font=('', 15))
t3.place(x=330, y=360)


l9 = tk.Label(window, text="Enter Your Password:", width=18, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF")
l9.place(x=90, y=400)
t9 = tk.Entry(window, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=330, y=400)

l10 = tk.Label(window, text="Re-Confirm Password:", width=18, font=("Times new roman", 16, "bold"), bg="#00827F",fg="#FFFFFF")
l10.place(x=90, y=440)

t10 = tk.Entry(window, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=330, y=440)

btn = tk.Button(window, text="Submit", bg="#006A4E",font=("times",20),fg="#FFFFFF",bd=5, width=9, height=0, command = insert)
btn.place(x=250, y=500)


window.mainloop()