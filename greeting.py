#!/usr/bin/env python3
import datetime
import time
import webbrowser

# Declare variables
webPages = ("https://www.businessinsider.com/","https://www.nytimes.com/","https://www.google.com/search?q=weather")
# Declare variables dependent on classes
thisDay = datetime.date.today()
thisTime = datetime.datetime.now()

# Function returns current date in long format
def thisDate(): # no args
    months = ("January","February","March","April","May","June","July","August","September","October","November","December") # tuple of all months
    return str(months[thisDay.month - 1])+" "+str(thisDay.day)+", "+str(thisDay.year) # returns formatted date Month Day, Year

# Function returns time of day in Hour:Minute format
def timeOfDay(): # no args
    hour = thisTime.hour
    minute = thisTime.minute
    return str(hour) + ":" + str(minute)

# Function returns current day of week
def dayOfWeek(): # no args
    return ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")[thisDay.weekday()] # returns current day from tuple of days indexed by thisDay.weekday()

# Function saves date and time to file
def saveInput(input, filename): # def funct and args
    input_str = (str(input)) # input object to string
    with open(filename, "a") as f: # open file in append mode
        for i in input_str: # iterate over string characters
            f.write(i) # write chars to file
        f.write("\n") # write newline to file

# Function prints information to console/terminal
def displayContent(): # no args
    print("\n\n\n    Hello Logan\n\n    Today is " + dayOfWeek() + "\n    " + str(thisDate()) + "\n\n    The Time is " + timeOfDay() + "\n\n") # print Hello, dayOfWeek, thisDate, time of day

# Function opens web pages in default browser
def openBrowser(url=webPages): # web pages passed through url arg - defaulted object is webPages
    for i in url: # iterate over url list/tuple
        time.sleep(1) # wait one second each iteration
        webbrowser.open_new(i) # open url stored at specific index using default browser
#
# Execute functions
saveInput(thisTime,'day_time.csv') # calls saveInput() to record thisTime to day_time.csv
displayContent() # calls displayContent()
openBrowser() # calls openBrowser
saveInput(str(thisTime)+"| "+input("    Notes: "),'user_input.csv') # calls saveInput() to record time and user input
print("\n")

# TO-DO
# 2 Create Tkinter GUI for application
# 5 Save weather to csv file
# 6 Print weather to console

# Completed
# 1 Organize into functions and classes
# 4 Save date and time to csv file
# 3 Create input form which saves to csv file

# Notes:
# thisDay and thisTime are assigned at the beginning of the program. Subsequent calls do not update the variable.