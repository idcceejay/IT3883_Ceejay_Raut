# Program Name: Assignment_3.py
# Course: IT3883/Section 01
# Student Name: Ceejay Raut
# Assignment Number: Lab3
# Due Date:10/10/2026
# Purpose: GUI application to convert Miles per Gallon into Kilometers per Liter
#Your GUI should behave like most online conversion tools where the result is updated with each number the user types. 
#The user should not need to click on a button to compute the final total. 
#Your program should also not crash in the event of the user typing a letter or leaving a box blank. 
# Resources: Claude (debugging hints, comment cleanup), Turbo AI (learning), GitHub (code snippets for arguments and parameters)

import tkinter as tk #The GUI library that will be used to create the window and widgets

window = tk.Tk()
window.title("MPG Converter") #Displays the title of the window


tk.Label(window, text="Enter Miles per Gallon:").grid(row=0, column=0) #is the dimension of the label that will display the value of mpg
miles_entry = tk.Entry(window) #takes the value of mpg from the user and stores it in a variable
miles_entry.grid(row=0, column=1) #Is the dimension of the entry box that will take the value of mpg from the user and store it in a variable

tk.Label(window, text="Kilometers per Liter:").grid(row=1, column=0) #is the dimension of the label that will display the value of km/l
result_var = tk.StringVar() #Creates a variable that will store the value of km/l
tk.Label(window, textvariable=result_var).grid(row=1, column=1) # Is the dimension of the result box that will display the value of km/l

def update(*args): #defines the function that will update the value of km/l with each number the user types
    try: #Makes sure that the program does not crash if the user types a letter or leaves the box blank
        mpg = float(miles_entry.get()) #Converts the value of mpg to a float
        km_per_l = mpg * 0.425143707 #Converts the value of mpg to km/l
        result_var.set(f"{km_per_l}") #Cuts the value of km/l to 2 decimal places
    except ValueError:
        result_var.set("Invalid input") #Displays "Invalid input" if the user types a letter or leaves the box blank

miles_entry.bind('<KeyRelease>', update) # Makes the program update the result with each number the user types

window.mainloop() # Is the main loop that keeps the window open and responsive to user input

#1 mpg = 0.425143707 km/l