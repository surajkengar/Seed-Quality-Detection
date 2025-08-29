import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1
#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="#2C3539")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Seed Quality")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('s1.jpg')
image2 = image2.resize((1350, 700), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
canvas = tk.Canvas(root, width=900, height=50,bg="#48D1CC")
canvas.pack()

text = "Welcome to Seed Quality Detection using Deep Learning"
x = canvas.create_text(0, 25, text=text, anchor="w", font=('times',25,'bold underline'), fill="#0000A5")

def scroll():
    canvas.move(x, -1, 0)  # Move text to the left
    if canvas.bbox(x)[0] < -canvas.winfo_width():
        canvas.move(x, canvas.winfo_width(), 0)  # Reset text position
    root.after(20, scroll)  # Schedule next scroll after 50 milliseconds

scroll()



def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])

    
def window():
  root.destroy()


button1 = tk.Button(root, text="Sign-In",bd=5, command=log, width=12, height=1,font=('times', 20, ' bold '), bg="blue", fg="white")
button1.place(x=1140, y=0)

button2 = tk.Button(root, text="Sign-Up",bd=5, command=reg,width=12, height=1,font=('times', 20, ' bold '), bg="green", fg="white")
button2.place(x=1140, y=60)

button3 = tk.Button(root, text="Logout",bd=5, command=window,width=12, height=1,font=('times', 20, ' bold '), bg="brown", fg="white")
button3.place(x=1140, y=120)

root.mainloop()