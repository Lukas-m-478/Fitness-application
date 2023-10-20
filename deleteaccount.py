#import libraries
import customtkinter
import sqlite3
from subprocess import call
from tkinter import messagebox
from tkinter import *
import hashlib

#create window
window = customtkinter.CTk()
window.geometry("350x300")
window.title("FitPro")

#function to return to home page
def back():
    call(["python","loginpage.py"])
    window.destroy()


#create font
title_font = customtkinter.CTkFont(family="Helvetica", size = 20, weight="bold")
header_font = customtkinter.CTkFont(family="Helvetica", size = 18,weight="bold" )
intructions_font = customtkinter.CTkFont(family="Helvetica", size = 12,weight="bold" )

#use entries as variables
deleteaccount_username = StringVar()
deleteaccount_password = StringVar()

#delete account if username and password matches
def delete_acccount():
    delete_username = deleteaccount_username.get()
    delete_username = delete_username.lower()
    delete_password = deleteaccount_password.get()
    conn = sqlite3.connect("information.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?",(delete_username,))
    password_hash = cur.fetchone()
    if password_hash is not None:
        h = hashlib.sha256()
        h.update(delete_password.encode("utf-8"))
        delete_password = h.hexdigest()
        if delete_password == password_hash[2]:
            msg_box = messagebox.askquestion(title="Alert!",message = "Are you sure you want to delete the account?")
            if msg_box == "yes":
                cur.execute("DELETE FROM users WHERE username = ?",(delete_username,))
                conn.commit()
                conn.close()
                messagebox.showinfo(title = "Success", message = "Account has been deleted")
        else:
            messagebox.showerror(title= "Error", message = "Invalid password")
    else:
        messagebox.showerror(title="Error", message="No account has been found")
   
    username_entry.delete(0, END)
    password_entry.delete(0, END)


#create widgets
delete_button = customtkinter.CTkButton(master = window, text = "delete", command = delete_acccount)
username_entry = customtkinter.CTkEntry(master = window, textvariable= deleteaccount_username)
password_entry = customtkinter.CTkEntry(master = window, textvariable = deleteaccount_password, show="*")
deleteaccount_label = customtkinter.CTkLabel(master = window, text = "Delete Account", font = title_font)
username_label = customtkinter.CTkLabel(master=window,text="Username", font = header_font)
password_label = customtkinter.CTkLabel(master=window,text="Password", font = header_font)
return_button = customtkinter.CTkButton(master = window, text="Return to login page",command = back)
instructions_label = customtkinter.CTkLabel(master = window, text = "Enter username and password of\n the account that you wish to delete", font = intructions_font)

#place widgets
delete_button.place(x = 140, y=200)
username_entry.place(x=140, y=120)
password_entry.place(x=140,y=160)
deleteaccount_label.place(x=130, y=80)
username_label.place(x=30,y=120)
password_label.place(x=30,y=160)
return_button.place(x=130,y=20)
instructions_label.place(x=70,y=250)

#run window
window.mainloop()
