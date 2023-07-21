from time import strftime 
from tkinter import *

import time
import datetime
from pygame import mixer

root=Tk()
root.title('UME Alarm-clock')

def setalarm():
    alarmtime=f"{hrs.get()}:{min.get()}:{sec.get()}"
    print (alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime)

def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root,font=('arial',20,'bold'),text="wake up! wake up",bg="blue",fg="pink").grid(row=8,columnspan=4)
            print("wake up!")
            mixer.init()
            mixer.music.load(r"C:\Users\Sravan\Downloads\mixkit-retro-game-emergency-alarm-1000.wav")
            mixer.music.play()
            break


hrs=StringVar()
min=StringVar()
sec=StringVar()

greet=Label(root,font=('arial',20,'bold'),text="take a nap").grid(row=1,columnspan=4)

hrbtn=Entry(root,textvariable=hrs,width=5,font =('arial', 20, 'bold'))
hrbtn.grid(row=2,column=1)

minbtn=Entry(root,textvariable=min,
width=5,font = ('arial', 20, 'bold')).grid(row=2,column=2)

secbtn=Entry(root,textvariable=sec,
width=5,font = ('arial', 20, 'bold')).grid(row=2,column=3)

setbtn=Button(root,text="set alarm",command=setalarm,bg="DodgerBlue2",
fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3)

timeleft=Label(root,font=('arial',20,'bold'))
timeleft.grid()

mainloop()