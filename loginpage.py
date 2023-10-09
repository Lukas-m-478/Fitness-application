#import hashing and sql libraries

import hashlib
import sqlite3

#import library to switch between files

from subprocess import call

#import gui libraries

import customtkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import font

# create window
window = customtkinter.CTk()
window.geometry("615x355")
window.title("FitPro")

#set colour of window

customtkinter.set_appearance_mode("green")
customtkinter.set_default_color_theme("dark-blue")

#create font
title_font = customtkinter.CTkFont(family="Helvetica", size = 20, weight="bold")
header_font = customtkinter.CTkFont(family="Helvetica", size = 18,weight="bold" )

#use "register" and "delete account" entries as variables for registerinfo and delete_account functions
username = StringVar()
password = StringVar()
deleteaccount_username = StringVar()


#add username and hashed password to database
def registerinfo():
    username_info = username.get()
    password_info = password.get()
    usernamelength = len(username_info)
    passwordlength = len(password_info)
    if (username_info != "") and (password_info != ""):
        if username_info != password_info:
            if (usernamelength >= 5) and (passwordlength >= 5):
                username_info = username_info.lower()
                h = hashlib.sha256()
                h.update(password_info.encode("utf-8"))
                try:
                    hashed_password = h.hexdigest()
                    conn = sqlite3.connect("information.db")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username_info, hashed_password))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(title="Success", message="Account has been created")
                except sqlite3.IntegrityError:
                    messagebox.showerror(title="Error", message="User already exists")
            else:
                messagebox.showerror(title="Error", message="Username and password must be at least 5 characters long")
        else:
            messagebox.showerror(title="Error", message="Username and password cannot be identical")  
    else:
        messagebox.showerror(title="Error", message="Username or password cannot be empty")              
    newusername_entry.delete(0, END)
    newpassword_entry.delete(0, END)


#use "login" entries as variables for login function
username_by_user = StringVar()
password_by_user = StringVar()

def login_correct():
    messagebox.showinfo(title="Login Success", message="You successfully logged in")
    call(["python","homepage.py"])
    window.destroy()

def login_wrong():
    messagebox.showerror(title="Error", message="Invalid password")

def user_not_found():
    messagebox.showerror(title="Error", message="User has not been found")

#compare user input with username and hashed password database

def login():
    username1 = username_by_user.get()
    password1 = password_by_user.get()
    username1 = username1.lower()
    h = hashlib.sha256()
    h.update(password1.encode("utf-8"))
    input_password = h.hexdigest()
    conn = sqlite3.connect("information.db")
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username=?", (username1,))
    data = cur.fetchone()
    conn.close()
    
    if data is not None:
        if input_password == data[0]:
            login_correct()
        else:
            login_wrong()
    else:
        user_not_found()
  
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
#go to "deleteaccount" page

def delete_acccountbutton():
    call(["python","deleteaccount.py"])
    window.destroy()
    

#create widgets for login

login_label = customtkinter.CTkLabel(master = window, text="Login", font =title_font)
username_label = customtkinter.CTkLabel(master = window, text="Username", font =header_font)
username_entry = customtkinter.CTkEntry(master = window, textvariable = username_by_user)
password_entry = customtkinter.CTkEntry(master = window,show="*", textvariable = password_by_user)
password_label = customtkinter.CTkLabel(master = window, text="Password", font =header_font)
login_button = customtkinter.CTkButton(master = window, text="Login", command = login)



#create widgets for register

register_label = customtkinter.CTkLabel(master = window, text="Register", font =title_font)
newusername_label = customtkinter.CTkLabel(master = window, text="New Username", font =header_font)
newusername_entry = customtkinter.CTkEntry(master = window,textvariable = username)
newpassword_entry = customtkinter.CTkEntry(master = window,textvariable = password)
newpassword_label = customtkinter.CTkLabel(master = window,text="New Password", font =header_font)
register_button = customtkinter.CTkButton(master = window, text="register", command = registerinfo)
delete_button = customtkinter.CTkButton(master = window, text = "delete", command = delete_acccountbutton)
deleteaccount_label = customtkinter.CTkLabel(master = window, text = "Delete Account?", font =header_font)

#place widgets manually for login

login_label.place(x = 110, y =50)
username_label.place(x =10, y =100)
username_entry.place(x = 110, y = 100)
password_entry.place(x = 110, y = 160)
password_label.place(x = 10, y = 160 )
login_button.place(x = 110, y = 210)


#place widgets manually for register

register_label.place(x = 450, y = 50)
newusername_label.place(x = 300, y = 100)
newusername_entry.place(x = 450, y = 100)
newpassword_entry.place(x = 450, y = 160) 
newpassword_label.place(x = 300, y =160) 
register_button.place(x = 450, y = 210)
delete_button.place(x = 300, y=305 )
deleteaccount_label.place(x=300, y=265)

#run window

window.mainloop()



