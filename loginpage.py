#import hashing and sql libraries

import hashlib
import sqlite3

#connects to database

conn = sqlite3.connect("logindetails.db")

cur = conn.cursor()

#import library to switch between windows

from subprocess import call

#import gui library

import tkinter as tk
from tkinter import messagebox
from tkinter import *


# create window

window = tk.Tk()
window.geometry("600x340")
window.title("FitPro")

window.configure(bg="aqua")

#uses register entries as variables
username = StringVar()
password = StringVar()
deleteaccount_username = StringVar()


#adds username and hashed password to database
def registerinfo():
    username_info = username.get()
    password_info = password.get()
    usernamelength = len(username_info)
    passwordlength = len(password_info)
    if (usernamelength >= 5) and (passwordlength >= 5):
        username_info = username_info.lower()
        h = hashlib.sha256()
        h.update(password_info.encode("utf-8"))
        hashed_password = h.hexdigest()
        cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username_info, hashed_password))
        conn.commit()
    else:
        messagebox.showerror(title="Error", message="Username and password must be 5 characters long")
    newusername_entry.delete(0, END)
    newpassword_entry.delete(0, END)


#uses login entries as variables
username_by_user = StringVar()
password_by_user = StringVar()

def login_correct():
    messagebox.showinfo(title="Login Success", message="You successfully logged in")
    call(["python","homepage.py"])
    window.destroy()

def login_wrong():
    messagebox.showerror(title="Error", message="Invalid password")

def user_not_found():
    messagebox.showerror(title="Error", message="Invalid username")

#compares user input with username and hashed password database

def login():
    username1 = username_by_user.get()
    password1 = password_by_user.get()
    username1 = username1.lower()
    h = hashlib.sha256()
    h.update(password1.encode("utf-8"))
    input_password = h.hexdigest()
    cur.execute("SELECT password FROM users WHERE username=?", (username1,))
    data = cur.fetchone()
    print(data)
    print(input_password)
    
    if data is not None:
        if input_password == data[0]:
            login_correct()
        else:
            login_wrong()
    else:
        user_not_found()
  
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
# deletes an account

def delete_acccount():
    delete_username = deleteaccount_username.get()
    delete_username = delete_username.lower()
    cur.execute("DELETE FROM users WHERE username = ?",(delete_username,))
    conn.commit()
    deleteaccount_entry.delete(0, END)
    deleteaccount_entry.delete(0, END)
    

#create widgets for login

login_label = tk.Label( text="Login page", bg = "aqua", font="Arial")
username_label = tk.Label( text="Username", bg = "aqua", font="Arial")
username_entry = tk.Entry(textvariable = username_by_user)
password_entry = tk.Entry( show="*", textvariable = password_by_user)
password_label = tk.Label( text="Password", bg = "aqua", font="Arial")
login_button = tk.Button(text="Login", command = login)



#create widgets for register

register_label = tk.Label( text="Register", bg = "aqua", font="Arial")
newusername_label = tk.Label( text="New Username", bg = "aqua", font="Arial")
newusername_entry = tk.Entry(textvariable = username)
newpassword_entry = tk.Entry(textvariable = password)
newpassword_label = tk.Label( text="New Password", bg = "aqua", font="Arial")
register_button = tk.Button(text="register", command = registerinfo)
delete_button = tk.Button(text = "delete account", command = delete_acccount)
deleteaccount_entry = tk.Entry(textvariable= deleteaccount_username)
deleteaccount_label = tk.Label(text = "Delete Account",bg= "aqua", font="Arial")

#place widgets manually for login

login_label.place(x = 110, y =50)
username_label.place(x =10, y =100)
username_entry.place(x = 110, y = 106)
password_entry.place(x = 110, y = 166)
password_label.place(x = 10, y = 160 )
login_button.place(x = 110, y = 210)


#place widgets manually for register

register_label.place(x = 450, y = 50)
newusername_label.place(x = 300, y = 100 )
newusername_entry.place(x = 450, y = 106)
newpassword_entry.place(x = 450, y = 166) 
newpassword_label.place(x = 300, y =160) 
register_button.place(x = 450, y = 210)
delete_button.place(x = 300, y=300 )
deleteaccount_entry.place(x=315, y=270)
deleteaccount_label.place(x=180, y=265)

#run window

window.mainloop()







