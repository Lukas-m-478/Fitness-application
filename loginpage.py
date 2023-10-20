#import hashing and sql libraries
import hashlib
import sqlite3

#import regular expressions to check if password has at least one capital letter and at least one special character
#I learned how to use re from https://www.youtube.com/watch?v=Dkiz0z3bMg0
import re

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
window.geometry("790x440")
window.title("FitPro")

#set colour of window
customtkinter.set_appearance_mode("green")
customtkinter.set_default_color_theme("dark-blue")

#create font
title_font = customtkinter.CTkFont(family="Helvetica", size = 20, weight="bold")
header_font = customtkinter.CTkFont(family="Helvetica", size = 18,weight="bold" )
requirements_font = customtkinter.CTkFont(family="Helvetica", size = 10,weight="bold",  )

#use "register" and "delete account" entries as variables for registerinfo and delete_account functions
username = StringVar()
password = StringVar()
deleteaccount_username = StringVar()
confirm_password_input = StringVar()

#add username and hashed password to database if they match requirements
def registerinfo():
    username_info = username.get()
    password_info = password.get()
    confirm_password = confirm_password_input.get()
    usernamelength = len(username_info)
    passwordlength = len(password_info)
    if username_info != "":
        if password_info != "":
            if usernamelength < 15:
                if passwordlength < 15:   
                    if username_info != password_info:
                        if usernamelength >= 5:
                            if passwordlength >= 5:
                                username_info = username_info.lower()
                                h = hashlib.sha256()
                                h.update(password_info.encode("utf-8"))
                                try:
                                    hashed_password = h.hexdigest()
                                    if (re.search(r'[!@#$%^&*()]', password_info)) and (re.search(r'[A-Z]', password_info)):
                                        if password_info == confirm_password:
                                            conn = sqlite3.connect("information.db")
                                            cur = conn.cursor()
                                            cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username_info, hashed_password))
                                            conn.commit()
                                            conn.close()
                                            messagebox.showinfo(title="Success", message="Account has been created")
                                            enter()
                                        else:
                                            messagebox.showerror(title="error",message="New Password must be identical to Confirm Password")
                                    else:
                                        messagebox.showerror(title="Error", message="Password must contain at least one capital letter and at least one special character")
                                except sqlite3.IntegrityError:
                                    messagebox.showerror(title="Error", message="User already exists")
                            else:
                                messagebox.showerror(title="Error",message="Password must be at least 5 characters long")
                        else:
                            messagebox.showerror(title="Error", message="Username must be at least 5 characters long")
                    else:
                        messagebox.showerror(title="Error", message="Username and password cannot be identical")
                else:
                    messagebox.showerror("error", message="Password is too long")
            else:
                messagebox.showerror("error", message="Username is too long")  
        else:
            messagebox.showerror(title="Error", message="Password cannot be empty")  
    else:
        messagebox.showerror(title="Error", message="Username cannot be empty")              
   
    newpassword_entry.delete(0, END)
    confirm_password_entry.delete(0,END)


#use "login" entries as variables for login function
username_by_user = StringVar()
password_by_user = StringVar()

#use "login" entries as variables for login function
username_by_user = StringVar()
password_by_user = StringVar()

#goes to homepage if credentials are correct
def login_correct():
    messagebox.showinfo(title="Login Success", message="You successfully logged in")
    call(["python","homepage.py"])
    window.destroy()

def enter():
    call(["python","homepage.py"])
    window.destroy()

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
    
    #checks if account(username) exists, then checks if password matches
    if data is not None:
        if input_password == data[0]:
            login_correct()
        else:
            messagebox.showerror(title="Error", message="Invalid password")
    else:
        messagebox.showerror(title="Error", message="User has not been found")
  
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
credentialslengths_label = customtkinter.CTkLabel(master=window, text = "1. Password and username must be at least 5 characters long\n and under 15 characters in length", font = requirements_font)
passwordrequirements_label = customtkinter.CTkLabel(master=window, text = "2. Password must have at least one capital letter\n and special character", font = requirements_font)
notidentical_label = customtkinter.CTkLabel(master=window, text = "3. password and username must not be identical", font = requirements_font)
delete_button = customtkinter.CTkButton(master = window, text = "delete", command = delete_acccountbutton)
deleteaccount_label = customtkinter.CTkLabel(master = window, text = "Delete Account?", font =header_font)

#create widgets for register
register_label = customtkinter.CTkLabel(master = window, text="Register", font =title_font)
newusername_label = customtkinter.CTkLabel(master = window, text="New Username", font =header_font)
newusername_entry = customtkinter.CTkEntry(master = window,textvariable = username)
newpassword_entry = customtkinter.CTkEntry(master = window,show = "*",textvariable = password)
newpassword_label = customtkinter.CTkLabel(master = window,text="New Password", font =header_font)
register_button = customtkinter.CTkButton(master = window, text="register", command = registerinfo)
confirm_password_label = customtkinter.CTkLabel(master = window,text="Confirm Password", font =header_font)
confirm_password_entry = customtkinter.CTkEntry(master= window, show="*", textvariable=confirm_password_input)

#place widgets manually for login
login_label.place(x = 170, y =50)
username_label.place(x =70, y =100)
username_entry.place(x = 170, y = 100)
password_entry.place(x = 170, y = 160)
password_label.place(x = 70, y = 160 )
login_button.place(x = 170, y = 210)
delete_button.place(x = 170, y=305 )
deleteaccount_label.place(x=170, y=265)

#place widgets manually for register
register_label.place(x = 590, y = 50)
newusername_label.place(x = 450, y = 100)
newusername_entry.place(x = 590, y = 100)
newpassword_entry.place(x = 590, y = 160) 
newpassword_label.place(x = 450, y =160) 
register_button.place(x = 590, y = 270)
credentialslengths_label.place(x=450,y=320)
passwordrequirements_label.place(x=450, y=360)
notidentical_label.place(x=450,y=390)
confirm_password_label.place(x=410, y = 220)
confirm_password_entry.place(x=590,y=220)

#run window
window.mainloop()
