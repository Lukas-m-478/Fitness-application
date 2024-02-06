#Plans are managed in a way that they are ordered by instances. 
#So if a user was to create 3 plans, (which is the maximum) 
#plan1 would be the first plan that was created by the user 
#and plan2 would be the second plan created by the user, etc

import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
from tkinter import font
import sqlite3

import subprocess
from subprocess import call

#class for changing font of labels
class Font(ctk.CTkFont):
    def __init__(self, family, size, weight):
        super().__init__(family=family, size=size, weight=weight)

class Entry(ctk.CTkEntry):
    def __init__(self, master, show, textvariable, **kwargs):             
        super().__init__(master, show=show , textvariable=textvariable)
        self.place(**kwargs)

class Label(ctk.CTkLabel):
    def __init__(self, master, text,font=None, **kwargs):
        super().__init__(master, text=text, font=font)
        self.place(**kwargs)

class Button(ctk.CTkButton):
    def __init__(self, master, text, command, **kwargs):
        super().__init__(master, text=text, command=command)
        self.place(**kwargs)

class window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("FitPro")
        self.geometry("500x300")
        self.resizable(False, False)
        self.back_button = Button(self, "Go back to homepage", self.goback, x=10, y=10)

        self.title_font = Font("Helvetica", 20, "bold")
        self.header_font = Font("Helvetica", 12, "bold")

        self.deleteplan_var = StringVar()

        self.selectplan_label = Label(self,"Select a plan to open:",self.title_font,x=200,y=15)
        self.deleteplan_label = Label(self,"Enter name of\n plan to delete:",self.header_font,x=45,y=180)
        self.plan1_button = Button(self, "Empty plan", self.display_plan_1, x=20, y=100)
        self.plan2_button = Button(self, "Empty plan", self.display_plan_2, x=180, y=100)
        self.plan3_button = Button(self, "Empty plan", self.display_plan_3, x=340, y=100)
        self.deleteplan_button = Button(self, "Delete plan", self.delete_plan, x=180, y=220)
        self.deleteplan_entry = Entry(self, "",self.deleteplan_var, x=180,y=180)

        self.update_button_text()

    #method will check if plan 1 exists then go to display_plan to display it
    def display_plan_1(self):
        with open(r"C:\NEA - (Main)\user_account_key.txt") as f:
            line = f.readline()
            parts = line.split(',') 
            key = parts[0].strip('(')  

        conn = sqlite3.connect("information.db")
        cur = conn.cursor()
        #find all instances of the user's fitness plans
        cur.execute("SELECT * FROM plan_identification WHERE user_fk = ?", (key,))
        row = cur.fetchall()
        conn.close()
        #Collect plan key from first row if it exists, if not an error message box will appear
        try:
            first_row = row[0]
            plan_key = first_row[0]
            with open("user_plan_key.txt","w") as file:
                        file.write(str(plan_key))
            call(["python","display_plan.py"])
            self.close_everything()  
        except:
            messagebox.showerror(title = "error", message = "plan does not exist")

    #method will check if plan 2 exists then go to display_plan to display it
    def display_plan_2(self):
        with open(r"user_account_key.txt") as f:
            line = f.readline()
            parts = line.split(',') 
            key = parts[0].strip('(')  

        conn = sqlite3.connect("information.db")
        cur = conn.cursor()
        #find all instances of the user's fitness plans
        cur.execute("SELECT * FROM plan_identification WHERE user_fk = ?", (key,))
        row = cur.fetchall()
        conn.close()
        #Collect plan key from second row if it exists, if not an error message box will appear
        try:
            second_row = row[1]
            plan_key = second_row[0]
            with open("user_plan_key.txt","w") as file:
                        file.write(str(plan_key))
            call(["python","display_plan.py"])
            self.close_everything() 
        except IndexError:
            messagebox.showerror(title = "error",message= "Plan does not exist")

    #method will check if plan 3 exists then go to display_plan to display it
    def display_plan_3(self):
        with open(r"user_account_key.txt") as f:
            line = f.readline()
            parts = line.split(',') 
            key = parts[0].strip('(')  

        conn = sqlite3.connect("information.db")
        cur = conn.cursor()
        #find all instances of the user's fitness plans
        cur.execute("SELECT * FROM plan_identification WHERE user_fk = ?", (key,))
        row = cur.fetchall()
        conn.close()
        #Collect plan key from third row if it exists, if not an error message box will appear
        try:
            third_row = row[2]
            plan_key = third_row[0]
            with open("user_plan_key.txt","w") as file:
                        file.write(str(plan_key))
            call(["python","display_plan.py"])
            self.close_everything() 
        except IndexError:
            messagebox.showerror(title = "Error", message = "Plan does not exist")

    #check if plan exists and then delete it
    def delete_plan(self):
        plan_name = self.deleteplan_var.get()
        if plan_name != "":
            conn = sqlite3.connect("information.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM plan_identification WHERE plan_name = ?", (plan_name,))
            row = cur.fetchone()
            if row is not None:
                cur.execute("DELETE FROM plan_identification WHERE plan_name = ?", (plan_name,))
                conn.commit()
                conn.close()
                self.update_button_text_after_delete()
            else:
                messagebox.showerror(title = "Error", message = "Plan does not exist")
        else:
            messagebox.showerror(title = "Error", message = "Entry box must not be empty")
        self.deleteplan_entry.delete(0,END)
    
    #update text of the buttons every time the window runs by using the primary key from users table
    def update_button_text(self):
        with open(r"user_account_key.txt") as f:
            line = f.readline()
            parts = line.split(',') 
            key = parts[0].strip('(') 
        conn = sqlite3.connect("information.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM plan_identification WHERE user_fk = ?", (key,))
        row = cur.fetchall()
        #There is a maximum of three instances for a user's plan so it checks each row to see if the plan exists
        #and if it does exist, the plan name is taken and given to the button
        try:
            first_row = row[0]
            plan_name = first_row[2]
            self.plan1_button.configure(text=plan_name)
        except:
            pass

        try:
            second_row = row[1]
            plan_name2 = second_row[2]
            self.plan2_button.configure(text=plan_name2)
        except:
            pass

        try:
            third_row = row[2]
            plan_name3 = third_row[2]
            self.plan3_button.configure(text=plan_name3)
        except:
            pass

    #This method automatically changes the text of the buttons after a plan is deleted by the user
    def update_button_text_after_delete(self):
        with open(r"C:\NEA - (Main)\user_account_key.txt") as f:
            line = f.readline()
            parts = line.split(',') 
            key = parts[0].strip('(') 
        conn = sqlite3.connect("information.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM plan_identification WHERE user_fk = ?", (key,))
        rows = cur.fetchall()
        #If the user deleted a plan, and there are two plans left, button texts are changed in accordance
        if len(rows) == 2:
            first_row = rows[0]
            first_plan = first_row[2]
            second_row = rows[1] 
            second_plan = second_row[2]
            self.plan1_button.configure(text=first_plan)
            self.plan2_button.configure(text=second_plan)  
            self.plan3_button.configure(text="Empty plan")
        #If the user deleted a plan, and there is one plan left, button texts are changed in accordance
        elif len(rows) == 1:
            first_row = rows[0]
            first_plan = first_row[2]
            self.plan1_button.configure(text=first_plan)
            self.plan2_button.configure(text="Empty plan")  
            self.plan3_button.configure(text="Empty plan")
        #If the user deleted a plan, and there are zero plans left, all button texts are changed to Empty plan
        else:
            self.plan1_button.configure(text="Empty plan")
            self.plan2_button.configure(text="Empty plan")  
            self.plan3_button.configure(text="Empty plan")
        messagebox.showinfo(title = "Success",message="Plan has been deleted")

    #go back to homepage
    def goback(self):
        call(["python","homepage.py"])
        self.close_everything()

    #method to delete every widget before closing window
    def close_everything(self):
        children = self.winfo_children()
        for widget in children:
            widget.destroy()
        self.quit()

#run window
if __name__ == "__main__":
    app = window()
    app.mainloop()
