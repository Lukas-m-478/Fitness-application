#import libraries
from subprocess import call
import tkinter as tk
import customtkinter 
from tkinter import *
from tkinter import messagebox

#create window
customtkinter.set_appearance_mode("dark-blue")
window = customtkinter.CTk()
window.geometry("950x470")
window.title("FitPro")

#create font
title_font = customtkinter.CTkFont(family="Helvetica", size = 40, weight="bold")
header_font = customtkinter.CTkFont(family="Helvetica", size = 18,weight="bold" )
bmi_label_font = customtkinter.CTkFont(family="Helvetica", size = 22,weight="bold" )
convertfrom_cm_font = customtkinter.CTkFont(family="Helvetica", size = 12 ,weight="bold")
ethnicityexplanation_font = customtkinter.CTkFont(family="Helvetica", size = 15 ,weight="bold")

#use variables to retrieve values from entries
weight = StringVar()
height = StringVar()
cm = StringVar()
mm = StringVar()

#log out
def logout():
    msg_box = messagebox.askquestion(title = "Logout", message = "Are you sure you want to log out?")
    if msg_box == "yes":
        call(["python","loginpage.py"])
        window.destroy()

#go to "makefitnessplan" page
def create_plan():
    call(["python","makefitnessplan.py"])
    window.destroy()

#information for BMI calculator about ethnicity groups is used from https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/

#when "Calculate" button is pressed, check the value switches to see what units the user wants to use,
#and check if input is a number or if entries are not empty, or else an error message will pop up
def calculate_bmi():
    weight_input = weight_entry.get()
    height_input = height_entry.get()
    if (weight_input != "") and (height_input != ""):
        try:
            weight = float(weight_input)
            height = float(height_input)

            weightswitch_value = weight_switch.get()
            heightswitch_value = height_switch.get()
            if (weightswitch_value == 0) and (heightswitch_value == 0):
                calculate_bmi_kg_m()
            elif (weightswitch_value == 1) and (heightswitch_value == 1):
                calculate_bmi_lbs_inches()
            elif (weightswitch_value == 1) and (heightswitch_value == 0):
                calculate_bmi_lbs_m()
            elif (weightswitch_value == 0) and (heightswitch_value == 1):
                calculate_bmi_kg_inches()
        
        except ValueError:
            messagebox.showerror(title="Error", message="Weight and height must be numbers")
    else:
        messagebox.showerror(title="Error", message="Weight or height cannot be empty")        
    weight_entry.delete(0,END)
    height_entry.delete(0,END)

#convert inches to metres and calculate bmi
def calculate_bmi_kg_inches():
    kg = float(weight_entry.get())
    inches = float(height_entry.get())
    m = inches / 39.37
    m_squared = m * m
    bmi = kg/m_squared
    messagebox.showinfo(title = "Success", message = f"Your BMI is {(bmi)}")
    result(bmi)

#convert metres to inches and calculate bmi
def calculate_bmi_lbs_m():
    lbs = float(weight_entry.get())
    m = float(height_entry.get())
    inches = m * 39.37
    bmi = (lbs/(inches*inches)) * 703
    messagebox.showinfo(title = "Success", message = f"Your BMI is {(bmi)}")
    result(bmi)

#calculate bmi
def calculate_bmi_kg_m():
    kg = float(weight_entry.get())
    m = float(height_entry.get())
    m_squared = m*m
    bmi = kg/m_squared
    result(bmi)

#calculate bmi
def calculate_bmi_lbs_inches():
    lbs = float(weight_entry.get())
    inches = float(height_entry.get())
    bmi = (lbs/(inches*inches)) * 703
    messagebox.showinfo(title = "Success", message = f"Your BMI is {(bmi)}")
    result(bmi) 

#show result of BMI, also depending on ethicity option (e.g: underweight, overweight, healthy weight)
def result(bmi):
    selected_value = ethnicity_options.get()
    underweight_border = 18.5
    overweight_border = 24.9
    obese_border = 30

    if selected_value not in ["White", "Prefer not to say"]:
        overweight_border = 23
        obese_border = 27.5
    if underweight_border <= bmi <= overweight_border:
        weight_result = "a healthy weight"
    elif bmi < underweight_border:
        weight_result = "underweight"
    elif bmi > obese_border:
        weight_result = "obese"
    else:
        weight_result = "overweight"
    
    messagebox.showinfo(title = "Success", message = f"Your BMI is {(bmi)}, you are {(weight_result)}. \nTo ensure that you have the correct result, please make sure to check your units.")

#convert cm to m and display result
def convert_cm_to_m():
    input_cm = cm.get()
    if input_cm != "":
        try:
            input_cm = float(input_cm)

            m = float(input_cm)/100
            messagebox.showinfo(title="Success", message = f"{float(input_cm)} cm is {float(m)} m")
        except ValueError:
            messagebox.showerror(title = "Error", message = "cm must be a number")
    else:
        messagebox.showerror(title = "Error",message="cm to m cannot be empty")
    cm_to_m_entry.delete(0,END)

#convert mm to m and display result
def convert_mm_to_m():
    input_mm = mm.get()
    if input_mm != "":
        try:
            input_mm = float(input_mm)

            m = float(input_mm)/1000
            messagebox.showinfo(title="Success", message = f"{float(input_mm)} mm is {float(m)} m")
        except ValueError:
            messagebox.showerror(title = "Error", message = "mm must be a number")
    else:
        messagebox.showerror(title = "Error",message="mm to m cannot be empty")
    mm_to_m_entry.delete(0,END)


#create widgets
return_button = customtkinter.CTkButton(master = window, text="Log out", command = logout)
homepage_label = customtkinter.CTkLabel(master= window, text = "Homepage",font=title_font)
createplan_button = customtkinter.CTkButton(master=window,text = "Create fitness plan?", command = create_plan)
bmi_label = customtkinter.CTkLabel(master=window, text="Calculate your BMI here:",font = bmi_label_font)
weight_entry = customtkinter.CTkEntry(master=window,textvariable=weight)
height_entry = customtkinter.CTkEntry(master=window,textvariable=height)
weight_label = customtkinter.CTkLabel(master=window,text="Weight:",font = header_font)
height_label = customtkinter.CTkLabel(master=window,text="Height:",font = header_font)
calculate_button = customtkinter.CTkButton(master=window,text="Calculate", command= calculate_bmi)
weight_switch = customtkinter.CTkSwitch(master=window,text = "Weight in kg or lbs? \n(KG-LEFT, LBS-RIGHT)")
height_switch = customtkinter.CTkSwitch(master=window,text = "Height in metres or inches? \n(METRES-LEFT, INCHES-RIGHT)")
convertfrom_cm_label = customtkinter.CTkLabel(master=window,text="Do you only know your\n height in cm or mm?\n convert your height into\n metres here:",font = convertfrom_cm_font)
cm_to_m_label = customtkinter.CTkLabel(master=window,text = "cm to m:", font = header_font)
mm_to_m_label = customtkinter.CTkLabel(master=window,text = "mm to m:", font = header_font)
cm_to_m_entry = customtkinter.CTkEntry(master=window, textvariable=cm)
mm_to_m_entry = customtkinter.CTkEntry(master=window, textvariable=mm)
convert_mm_to_m_button = customtkinter.CTkButton(master=window,text="Convert",command = convert_mm_to_m)
convert_cm_to_m_button = customtkinter.CTkButton(master=window,text="Convert",command = convert_cm_to_m)
ethnicity_options = customtkinter.CTkComboBox(master=window, values = ["Prefer not to say","White","Mixed","Pakistani","Middle eastern","Indian","Chinese","Black caribbean","Black african","Bangladeshi","Other"])
ethnicity_label = customtkinter.CTkLabel(master=window,text = "What is your ethnicity?", font = header_font)
ethnicityexplanation_label = customtkinter.CTkLabel(master = window, text = "(We ask this because \nBMI results can vary for \ndifferent ethnic groups)", font = ethnicityexplanation_font)

#place widgets manually
return_button.place(x=20,y=20)
homepage_label.place(x=420,y=20)
createplan_button.place(x=20,y=50)
bmi_label.place(x=350,y=230)
weight_entry.place(x=430,y=310)
height_entry.place(x=430,y=270)
weight_label.place(x=350,y=310)
height_label.place(x=350,y=270)
calculate_button.place(x=430,y=350)
weight_switch.place(x=390,y=430)
height_switch.place(x=390,y=390)
convertfrom_cm_label.place(x=90,y=230)
cm_to_m_label.place(x=20,y=300)
mm_to_m_label.place(x=20,y=385)
cm_to_m_entry.place(x=120,y=300)
mm_to_m_entry.place(x=120,y=385)
convert_mm_to_m_button.place(x=120,y=420)
convert_cm_to_m_button.place(x=120,y=335)
ethnicity_options.place(x=700,y=270)
ethnicity_label.place(x=700,y=230)
ethnicityexplanation_label.place(x=700,y=340)

#run window
window.mainloop()
