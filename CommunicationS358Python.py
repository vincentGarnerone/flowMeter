# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:03:58 2021

@author: vince
"""

import serial
from decimal import Decimal
from datetime import datetime
import csv


ser = serial.Serial(port = "COM15", baudrate=19200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

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

nom_fichier = "valeurs_"+datetime.now().strftime("%m-%d-%Y-%H-%M-%S")+".csv"
with open(nom_fichier, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerow(["timestamp" ,"pressure", "temperature", "volFlow", "massFlow"])
    for i in range(100):
        val = readData()
        liste = val.split(" ")
        liste = [s for s in liste if s]

        try:
            pressure=Decimal(liste[0])
            temperature=Decimal(liste[1])
            volFlow=Decimal(liste[2])
            massFlow=Decimal(liste[3])
            
            spamwriter.writerow([datetime.now(),pressure, temperature, volFlow, massFlow])
            
            print("Presion: "+str(pressure) + " temp:" + str(temperature)
                  +"Flow (vol): "+ str(volFlow) + "Flow (mass): "+str(massFlow))
        except:
            continue
ser.close()
