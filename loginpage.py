#import operating system to access text files

import os

#import library

import tkinter as tk
from tkinter import messagebox
from tkinter import *

# create window

window = tk.Tk()
window.geometry("600x300")
window.title("FitPro")

window.configure(bg="aqua")

#allows variables to be used outside of fuctions
global password
global username

#uses entries as variables
username = StringVar()
password = StringVar()

#adds login details to a new .txt file
def registerinfo():
    username_info = username.get()
    password_info = password.get()
    newest_password = password_info
    file = open(username_info + ".txt","w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    newusername_entry.delete(0,END)
    newpassword_entry.delete(0,END)

def delete_account():
    pass
    

global username_by_user
global password_by_user
username_by_user = StringVar()
password_by_user = StringVar()

def login_correct():
    messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    
def login_wrong():
    messagebox.showerror(title="Error", message="Invalid login.")

def user_not_found():
    messagebox.showerror(title="Error", message="User not found.")


def login():
    username1 = username_by_user.get()
    password1 = password_by_user.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    list_of_files = os.listdir()
    
    if (username1 + ".txt" in list_of_files) and (username1 != ""):
        file1 = open(username1 + ".txt", "r")
        check = file1.read().splitlines()
        if password1 in check:
            login_correct()
        else:
            login_wrong()
    else:
        user_not_found()



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


#run window


window.mainloop()







