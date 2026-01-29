"""
Blazius R. Nimrichter, Copyright (c) 2026
28 January, 2026
CSC 309 SFSU Spring 2026
Project 1 Due 4 February, 2026 23:59 PST

Last Modified: 28 January, 2026

Description: This program will ask the user for their name, it will subsequently print the name they input as well as
the current date and time.

Inputs: Keyboard input from user
Outputs: prints out a string to the display

Dependencies: imports the Python time module
Assumptions: developed and tested using PyCharm
"""
import datetime #

user_name = input("Enter your name: ") #variable for user to input their name
date = datetime.datetime.today() #variable created to be able to print the date and time
print("Welcome ",user_name,", it is currently ", date, sep="") #prints the user's input name, as well as the date and the time
