import time
import pygame
from tkinter import *
from tkinter import messagebox
import sys
import os
import requests
import json
from tkinter import ttk
from datetime import *
import logging
import threading
import asyncio






# These are the variables
today = str(date.today())
path = 'C:\scripts\KTimer\ktimer\\ran.txt'
webhook_on = 'http://192.168.2.6:8123/api/webhook/turn_on_rene'
webhook_off = 'http://192.168.2.6:8123/api/webhook/turn_off_rene'
name = 'Kaylee'
t = '10'


# Create a top gui
top = Tk()
top.geometry("600x600")
# Button defined

async def main():
    print ('asyncio worked')
    await asyncio.sleep(1)

def helloCallBack():
      print("Button Pressed")
      with open(path, "r") as f:
            s = f.read()
      if today == s:
            msg = messagebox.showinfo("Sorry " + name , " Your 2:00 is up for today.")
            r = requests.post(webhook_off, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            msg = messagebox.showinfo(name + " " , " Your 2:00 has ended.")
            print("Turned Off Intenet")
      else:
      #     Your file is going to ruin and will adjust file
      # add code here
            msg = messagebox.showinfo(name + " Your 2:00 is starting now.")
            print("Your File arleady worked")
            data = {'name': 'Rene'}
            r = requests.post(webhook_on, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print("Turned On Intenet")
            # time.sleep(150)  # Sleep for 3 seconds
            for x in range(10):
              P['value'] += 1
              top.update_idletasks()
              asyncio.run(main())
              L.config(text=P['value'])

              # for _ in tqdm(range(10)):
              #       sleep(18)

            r = requests.post(webhook_off, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            msg = messagebox.showinfo("Kaylee", "Your 2:00 has ended.")
            print("Turned Off Intenet")

            #end code here
            print("Running file and updating ran file")
            ran_file = open(path, "r+")
            ran_file.write(today)

def close():
    r = requests.post(webhook_off, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    top.destroy()


B = Button(top, text = "Start", command = helloCallBack)
B.place(x = 50,y = 50)
C = Button(top, text = "Quit", command = close)
C.place(x = 100, y = 50)
P = ttk.Progressbar(top, orient=HORIZONTAL, length=200, mode='determinate')
P.place (x= 50, y=25)
L = Label(top, text="")
L.place (x=50, y=15)

top.mainloop()




