# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:03:58 2021

@author: vincent
"""

import serial
from decimal import Decimal
from datetime import datetime
import csv 
import tkinter as tk

# create a serial connection
ser = serial.Serial(port = "COM15", baudrate=19200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

# function to read data
def readData():    
    buffer = ""
    while True:
        oneByte = ser.read(1)
        if oneByte == b"\r":    #method should returns bytes
            return buffer
        else:
            try:
                buffer += oneByte.decode("ascii")
            except:
                return ""

# function called when the button is hit
# write the data in a csv file
def btn1(): 
    # csv file name with the time
    fileName = "values_"+datetime.now().strftime("%m-%d-%Y-%H-%M-%S")+".csv" 
    # create the file
    with open(fileName, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        # write the column titles
        spamwriter.writerow(["timestamp" ,"pressure", "temperature", "volFlow", "standFlow"])
        # get the number of iteration chosen
        numberIteration = e1.get()
        for i in range(int(numberIteration)):
            val = readData()
            liste = val.split(" ") # spliting the line at each space
            liste = [s for s in liste if s]
    
            try:
                pressure=Decimal(liste[0])
                temperature=Decimal(liste[1])
                volFlow=Decimal(liste[2])
                massFlow=Decimal(liste[3])                
                
                # write on each line the values read
                spamwriter.writerow([datetime.now(),pressure, temperature, volFlow, massFlow])
                
                #print("Presion: "+str(pressure) + " temp:" + str(temperature)
                 #     +"Flow (vol): "+ str(volFlow) + "Flow (mass): "+str(massFlow))
            except:
                continue

# not used yet
def btn3():           
    ser.close()
 
# close the serial connection when closing the program
def on_closing():
    ser.close()
    myWindow.destroy()

# create the window (Tkinter object)and add a title
myWindow = tk.Tk()
myWindow.winfo_toplevel().title("Flow meter recorder")

# choose the window size
canvas1 = tk.Canvas(myWindow, width = 300, height = 100)

# create a button to start recording, bind to function btn1
but1 = tk.Button(myWindow, text ='Start record',command=btn1).pack(side='bottom', padx=5, pady=5)
#but3 = tk.Button(myWindow, text ='Stop connection',command=btn3).pack(side='bottom', padx=5, pady=5)
# create a field to enter the number of steps
label2 = tk.Label(myWindow, text="Number of iterations").pack(side='top',padx=5, pady=5)
e1 = tk.Entry(myWindow)
canvas1.create_window(150, 30, window=e1)
canvas1.pack()

# call the function to close the serial connection when closing the window
myWindow.protocol("WM_DELETE_WINDOW", on_closing)

# open the window
myWindow.mainloop()
