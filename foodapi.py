#I used this video to learn how to use API's with python, requests and json: https://www.youtube.com/watch?v=bKCORrHbutQ&t=14s
#I found this website online to fetch food information from: https://world.openfoodfacts.org/
#I used these for documentation: https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v2/ , https://openfoodfacts.github.io/openfoodfacts-server/api/tutorial-off-api/
#API says that one barcode scan equals one API call
#100 calls a minute
#This API has access to 3,043,802 products from the world, as of right now, meaning not every product is on there

#import requests for HTTP requests
import requests

#import GUI needed

import customtkinter as ctk
from tkinter import messagebox
from tkinter import *
from tkinter import font
import customtkinter as ctk

#import subprocess for switching between python scripts

import subprocess
from subprocess import call

#I used https://www.youtube.com/watch?v=eaxPK9VIkFM to learn how to use classes with tkinter
#I learned **kwargs (keywordarguments) from https://www.youtube.com/watch?v=GdSJAZDsCZA

#classes for creating different widgets that will be used
class Entry(ctk.CTkEntry):
    def __init__(self, master, show, textvariable, **kwargs):             
        super().__init__(master, show=show , textvariable=textvariable)
        self.place(**kwargs)

class Label(ctk.CTkLabel):
    def __init__(self, master, text,font=None, **kwargs):
        super().__init__(master, text=text, font=("Helvetica", 16,))
        self.place(**kwargs)

class Button(ctk.CTkButton):
    def __init__(self, master, text, command, **kwargs):
        super().__init__(master, text=text, command=command)
        self.place(**kwargs)

#class for window to run
class window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Food nutrition information")
        self.geometry("820x1000")
        self.resizable(False, False)

        # Create and add widgets with custom placement
        self.title_label = Label(self, "Enter product code here:", x=100, y=50, font=("Helvetica", 16))
        self.button = Button(self, "Find information", self.getfoodinfo, x=100, y=150)
        self.button = Button(self, "Go back to homepage", self.goback, x=10,y=10)
        # text variable
        self.productcode = StringVar()
        # variable for getfoodinfo function
        global entry
        entry = Entry(self, "", self.productcode, x=100, y=100)

    #method will fetch data from API
    def getfoodinfo(self):
        product_input = self.productcode.get()
        url = f"https://world.openfoodfacts.org/api/v0/product/{product_input}.json"
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get('status', '') == 1:
                    product_info = data.get('product', {})

                    #learned winfo_children() from https://www.youtube.com/watch?v=A6m7TmjuNzw
                    #previous labels get deleted and new labels get added dynamically
                    for widget in self.winfo_children():
                        if isinstance(widget, Label) and widget != self.title_label:
                            widget.destroy()

                    #I used the https://openfoodfacts.github.io/openfoodfacts-server/api/tutorial-off-api/ documentation to learn the format of the API, and to know to use dictionaries
                    #Display data as labels

                    product_name_label = Label(self, f"Product name: {product_info.get('product_name', 'N/A')}",font=("Helvetica", 16))
                    product_name_label.place(x=100,y=200)

                    brand_label = Label(self, f"Brand: {product_info.get('brands', 'N/A')}", font=("Helvetica", 16))
                    brand_label.place(x=100,y=230)

                    categories_label = Label(self, f"Categories: {', '.join(product_info.get('categories_tags', ['N/A'])).split(' ')[2]}",font=("Helvetica", 16))
                    categories_label.place(x=100,y=260)

                    allergens_label = Label(self, f"Allergens: {', '.join(product_info.get('allergens_tags', ['N/A']))}",font=("Helvetica", 16))
                    allergens_label.place(x=100,y=290)

                    nutrition_info_label = Label(self, "Nutrition Information:", font=("Helvetica", 16))
                    nutrition_info_label.place(x=100,y=320)

                    nutrition_info = product_info.get('nutriments', {})
                    energy_label = Label(self, f"Energy: {nutrition_info.get('energy-kcal_100g', 'N/A')} kcal/100g",font=("Helvetica", 16))
                    energy_label.place(x=100,y=350)

                    fat_label = Label(self, f"Fat: {nutrition_info.get('fat_100g', 'N/A')} g/100g", font=("Helvetica", 16))
                    fat_label.place(x=100,y=380)

                    carbohydrates_label = Label(self,f"Carbohydrates: {nutrition_info.get('carbohydrates_100g', 'N/A')} g/100g",font=("Helvetica", 16))
                    carbohydrates_label.place(x=100,y=410)

                    proteins_label = Label(self, f"Proteins: {nutrition_info.get('proteins_100g', 'N/A')} g/100g",font=("Helvetica", 16))
                    proteins_label.place(x=100,y=440)

                else:
                    messagebox.showerror(title = "error", message = "Product not found.")
            except requests.exceptions.JSONDecodeError as e:
                messagebox.showerror(title = "Error", message = f"Error decoding JSON: {e}\n{response.content}")
        else:
            messagebox.showerror(title = "Error", message = f"Error: {response.status_code}\n{response.content}")
        entry.delete(0, END)

#go back to homepage
    def goback(self):
        call(["python","homepage.py"])
        self.destroy()

#run window
if __name__ == "__main__":
    app = window()
    app.mainloop()




