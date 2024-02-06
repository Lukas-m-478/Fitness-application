import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
from tkinter import font
import os
import sqlite3

import subprocess
from subprocess import call

#class for changing fonts of labels
class CheckBox(ctk.CTkCheckBox):
    def __init__(self, master, text,variable,onvalue,offvalue,**kwargs):
        super().__init__(master, text=text,variable=variable,onvalue=onvalue,offvalue=offvalue)
        self.place(**kwargs)

class Font(ctk.CTkFont):
    def __init__(self, family, size, weight):
        super().__init__(family=family, size=size, weight=weight)

class ComboBox(ctk.CTkComboBox):
    def __init__(self,master,values, **kwargs):
        super().__init__(master,values=values)
        self.place(**kwargs)

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
        self.geometry("700x710")
        self.resizable(False, False)
        
        self.title_font = Font("Helvetica", 30, "bold")
        self.question_font = Font("Helvetica", 18,"bold")
        self.explanation_font = Font("Helvetica",18,"bold")

        #store values of entry boxes from q1 and q2
        self.q1 = StringVar()
        self.q2 = StringVar()

        self.dumbells_box = BooleanVar(value=False)
        self.pullupbar_box = BooleanVar(value=False)
        self.barbell_box = BooleanVar(value=False)
        self.bench_box = BooleanVar(value=False)
        self.legextension_box = BooleanVar(value=False)
        self.legcurl_box = BooleanVar(value=False)
        self.ezbar_box = BooleanVar(value=False)
        self.cables_box = BooleanVar(value=False)
        self.dipstation_box = BooleanVar(value=False)
        self.legpress_box = BooleanVar(value=False)
        self.pecfly_box = BooleanVar(value=False)
        self.skippingrope_box = BooleanVar(value=False)
        self.monday_box = BooleanVar(value=False)
        self.tuesday_box = BooleanVar(value=False)
        self.wednesday_box = BooleanVar(value=False)
        self.thursday_box = BooleanVar(value=False)
        self.friday_box = BooleanVar(value=False)
        self.saturday_box = BooleanVar(value=False)
        self.sunday_box = BooleanVar(value=False)

        #create widgets
        self.createfitnessplan_label = Label(self,"Create your own fitness plan",font=self.title_font,x=180,y=10)
        self.goback_button = Button(self,"Return to homepage", self.goback,x=10,y=15)
        self.heading = Label(self,"Answer these questions and we will create a plan for you:",font = self.explanation_font,x=10,y=60)
        self.question1 = Label(self,"1. What is your current weight?",font=self.question_font,x=10,y=110)
        self.question2 = Label(self,"2. What is your weight goal?",font=self.question_font,x=10,y=180)
        self.question3 = Label(self,"3. How many days a week are you free to exercise? If answer is not 7, \ntick the days:",font=self.question_font,x=10,y=250)
        self.question4 = Label(self,"4. How much physical activity do you do in a week?",font=self.question_font,x=10,y=320)
        self.question5 = Label(self,"5. Do you have any allergies?",font=self.question_font,x=10,y=390)
        self.question6 = Label(self,"6. Do you have access to the gym?",font=self.question_font,x=10,y=460)
        self.question7 = Label(self,"(If answer to question 6 was yes) \n7. Tick the boxes of the equipment that you have access to:",font=self.question_font,x=10,y=520)
        self.submit_button = Button(self,"Submit",self.get_info,x=210,y=665)
        self.q1_entry = Entry(self,"",self.q1,x=50,y=140)
        self.q2_entry = Entry(self,"",self.q2,x=50,y=210)
        self.q3_combobox = ComboBox(self,values = ["1","2","3","4","5","6","7"],x=50,y=280)
        self.q4_combobox = ComboBox(self,values = ["low","moderate","vigorous"],x=50,y=350)
        self.q5_combobox = ComboBox(self,values = ["yes","no","I don't know"],x=50,y=420)
        self.q6_combobox = ComboBox(self,values = ["yes","no"],x=50,y=490)
        self.dumbells_checkbox = CheckBox(self, "Dumbells", self.dumbells_box, True,False,x=40,y=570)
        self.pullupbar_checkbox = CheckBox(self, "Pull up bar", self.pullupbar_box, True,False,x=150,y=570)
        self.barbell_checkbox = CheckBox(self, "Barbell", self.barbell_box, True,False,x=250,y=570)
        self.bench_checkbox = CheckBox(self, "Bench", self.bench_box, True,False,x=350,y=570)
        self.legextension_checkbox = CheckBox(self, "Leg extension\nmachine", self.legextension_box, True,False,x=450,y=565)
        self.legcurl_checkbox = CheckBox(self, "Leg curl\nmachine", self.legcurl_box, True,False,x=580,y=570)
        self.ezbar_checkbox = CheckBox(self, "EZ bar", self.ezbar_box, True,False,x=110,y=625)
        self.cables_checkbox = CheckBox(self, "Cables", self.cables_box, True,False,x=455,y=620)
        self.dipstation_checkbox = CheckBox(self, "Dip\nstation", self.dipstation_box, True,False,x=352,y=620)
        self.legpress_checkbox = CheckBox(self, "Leg press\n machine", self.legpress_box, True,False,x=10,y=620)
        self.pecfly_checkbox = CheckBox(self, "Pec fly\nmachine", self.pecfly_box, True,False,x=580,y=620)
        self.skippingrope_checkbox = CheckBox(self, "Skipping rope", self.skippingrope_box, True,False,x=210,y=620)
        self.monday_checkbox = CheckBox(self, "Monday", self.monday_box, True,False,x=405,y=280)
        self.tuesday_checkbox = CheckBox(self, "Tuesday", self.tuesday_box, True,False,x=490,y=280)
        self.wednesday_checkbox = CheckBox(self, "Wednesday", self.wednesday_box, True,False,x=580,y=280)
        self.thursday_checkbox = CheckBox(self, "Thursday", self.thursday_box, True,False,x=490,y=310)
        self.friday_checkbox = CheckBox(self, "Friday", self.friday_box, True,False,x=580,y=310)
        self.saturday_checkbox = CheckBox(self, "Saturday", self.saturday_box, True,False,x=490,y=340)
        self.sunday_checkbox = CheckBox(self, "Sunday", self.sunday_box, True,False,x=580,y=340)
        

    def goback(self):    
        call(["python","homepage.py"])
        self.close_everything()

    #method will collect all information from user and store as variable
    def get_info(self):
        #collect user primary key
        with open("user_account_key.txt","r") as f:
                line = f.readline()
                parts = line.split(',') 
                self.number = parts[0].strip('(')
        #This will check if the user has reached the maximum number of plans
        conn = sqlite3.connect("information.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM user_personal_info WHERE user_fk = ?", (self.number,))
        rows = cur.fetchall()
        number_of_plans = len(rows)
        if number_of_plans < 3:

            self.current_weight = self.q1.get()
            self.weight_goal = self.q2.get()
            self.q3 = self.q3_combobox.get()
            self.q4 = self.q4_combobox.get()
            self.q5 = self.q5_combobox.get()
            self.q6 = self.q6_combobox.get()

            self.dumbells = self.dumbells_box.get()
            self.pull_up_bar = self.pullupbar_box.get()
            self.barbell = self.barbell_box.get()
            self.bench = self.bench_box.get() 
            self.leg_extension = self.legextension_box.get()
            self.leg_curl = self.legcurl_box.get() 
            self.ez_bar = self.ezbar_box.get()
            self.cables = self.cables_box.get()
            self.dip_station = self.dipstation_box.get()
            self.leg_press = self.legpress_box.get()
            self.pec_fly = self.pecfly_box.get()
            self.skipping_rope = self.skippingrope_box.get()
            self.monday = self.monday_box.get() 
            self.tuesday = self.tuesday_box.get() 
            self.wednesday = self.wednesday_box.get() 
            self.thursday = self.thursday_box.get()  
            self.friday = self.friday_box.get() 
            self.saturday = self.saturday_box.get() 
            self.sunday = self.sunday_box.get()

            q3_boolean_values = [self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.saturday,self.sunday]
            q7_boolean_values = [self.dumbells_box, self.pullupbar_box,self.barbell_box,self.bench_box,self.legextension_box,self.legcurl_box]

            x=0
            for day in q3_boolean_values:
                if day == True:
                    x+=1
            if (str(x) == self.q3) or (self.q3 == "7"):

                if (self.current_weight != "") and (self.weight_goal != ""):
                    try:
                        self.current_weight = float(self.current_weight)
                        self.weight_goal = float(self.weight_goal)
                        #go to insert information
                        self.insert_info()
                    except ValueError:
                        messagebox.showerror(title="Error", message="Questions 1 and 2 must be numbers")
                        self.q1_entry.delete(0,END)
                        self.q2_entry.delete(0,END)

                else:
                    messagebox.showerror(title="Error", message="Weight or height cannot be empty")
                    self.q1_entry.delete(0,END)
                    self.q2_entry.delete(0,END)
            else:
                messagebox.showerror(title ="Error",message = "Number of boxes ticked in question 3 must be the same as the number of days specified")
        else:
            messagebox.showerror(title="Error",message = "There is only a maximum of 3 fitness plans that can be created")

    #method will insert information into the tables
    def insert_info(self):
        if os.path.isfile("information.db"):
            conn = sqlite3.connect("information.db")
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO user_personal_info (user_fk,current_weight,weight_goal,exercise_days_count,physical_activity,allergies,gym_access) VALUES (?,?,?,?,?,?,?)",
                        (self.number,self.current_weight,self.weight_goal,self.q3,self.q4,self.q5,self.q6))

            cur.execute("INSERT INTO workout_plan_details (user_fk) VALUES (?)", (self.number,))
            cur.execute("INSERT INTO nutrition_plan_details (user_fk) VALUES (?)", (self.number,))
            conn.commit()
            conn.close()
            if self.q3 != "7":
                conn = sqlite3.connect("information.db")
                cur = conn.cursor()
                cur.execute(
                "INSERT INTO exercise_days (user_fk,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (?,?,?,?,?,?,?,?)",
                        (self.number,self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.saturday,self.sunday))
                conn.commit()  
                conn.close()
            else:
                conn = sqlite3.connect("information.db")
                cur = conn.cursor()
                cur.execute(
                "INSERT INTO exercise_days (user_fk,monday,tuesday,wednesday,thursday,friday,saturday,sunday) VALUES (?,?,?,?,?,?,?,?)",
                        (self.number,True,True,True,True,True,True,True))
                conn.commit()  
                conn.close()

            if self.q6 == "yes":
                conn = sqlite3.connect("information.db")
                cur = conn.cursor()
                cur.execute(
                "INSERT INTO equipment_access (user_fk,dumbells,pull_up_bar,barbell,bench,leg_extensions_machine,leg_curl_machine,ez_bar,cables,dip_station,leg_press_machine,pec_fly_machine,skipping_rope) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (self.number,self.dumbells,self.pull_up_bar,self.barbell,self.bench,self.leg_extension,self.leg_curl,self.ez_bar,self.cables,self.dip_station,self.leg_press,self.pec_fly,self.skipping_rope))
                conn.commit()  
                conn.close()
            else:
                conn = sqlite3.connect("information.db")
                cur = conn.cursor()
                cur.execute(
                "INSERT INTO equipment_access (user_fk,dumbells,pull_up_bar,barbell,bench,leg_extensions_machine,leg_curl_machine,ez_bar,cables,dip_station,leg_press_machine,pec_fly_machine,skipping_rope) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (self.number,False,False,False,False,False,False,False,False,False,False,False,False))
                conn.commit()  
                conn.close()
            call(["python","create_fitness_plan.py"])
            self.close_everything()
        else:
            messagebox.showerror(title = "Error",message="Database does not exist")
            self.q1_entry.delete(0,END)
            self.q2_entry.delete(0,END)

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

