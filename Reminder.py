from tkinter import *
import os
from datetime import *
from time import sleep

def play1(p):
    os.system("echo \""+p+"\" > reminderraw.txt")
    os.system("festival --tts reminderraw.txt")

def play():
    os.system("echo \""+inp+"\" > reminderraw.txt")
    os.system("festival --tts reminderraw.txt")

inp = input('Enter massage : ')
tm = input('Enter time [hh:mm:ss]: ')
c_t1 = datetime.strptime(tm,"%H:%M:%S")
c_t1 = c_t1 - datetime(1900,1,1)
sec2 = c_t1.total_seconds()
now = datetime.now()
crtm = now.strftime("%H:%M:%S")
crtm = datetime.strptime(crtm,"%H:%M:%S")
crtm = crtm - datetime(1900,1,1)
sec1 = crtm.total_seconds()
play1('Your reminder is set')
sleep(sec2-sec1)
window = Tk()
window.title("Reminder")
window.geometry('1000x100')
lbl = Label(window, text=inp, font=("Arial Bold", 15))
lbl.grid(column=0, row=0)
play1('Be attention reminder is opening')
btn = Button(window, text='play',bg='green',fg='white',command=play)
btn.grid(column=0, row=1)
btn = Button(window, text='stop',bg='red',fg='white',command=exit)
btn.grid(column=0, row=2)
window.mainloop()