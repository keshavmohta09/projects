from tkinter import *
from datetime import *
from time import sleep
import os

typed_msg='Empty'
sec = 0

def msg_save():
    global typed_msg
    typed_msg = msg.get("1.0", "end-1c")
    print(typed_msg)

def play_msg():
    os.system("echo \""+typed_msg+"\" > reminderraw.txt")
    os.system("festival --tts reminderraw.txt")

def play1(p):
    os.system("echo \""+p+"\" > reminderraw.txt")
    os.system("festival --tts reminderraw.txt")

def tm_save():
    global sec
    days = day_btn.get()
    typed_tm = f'{hr_btn.get()}:{min_btn.get()}'
    print(typed_tm)
    c_t1 = datetime.strptime(typed_tm,"%H:%M")
    c_t1 = c_t1 - datetime(1900,1,1)
    t2 = datetime.now()
    c_t2 = t2.strftime("%H:%M:%S")
    c_t2 = datetime.strptime(c_t2,"%H:%M:%S")
    c_t2 = c_t2 - datetime(1900,1,1)
    sec_t1 = c_t1.total_seconds()
    sec_t2 = c_t2.total_seconds()
    if days!=0:
        sec_t1 = sec_t2 + (days*86400) - (sec_t2-sec_t1)   #total seconds in 24hrs = 86400
    elif sec_t1<sec_t2:
        play1('You entered wrong information.')
        exit()
    sec = sec_t1 - sec_t2


root = Tk()
root.title('It is a Reminder created by Keshav Mohta')
root.geometry('450x358')
root.minsize(450,358)
root.maxsize(470,358)

frm_top = Frame(root,borderwidth=8,bg='grey',relief=GROOVE)
frm_lft = Frame(root,borderwidth=8,bg='grey',relief=GROOVE)
frm_typ = Frame(root,borderwidth=8,bg='grey',relief=GROOVE)
frm_top.pack(side=TOP,fill='x')
frm_lft.pack(side=LEFT,fill='y')
frm_typ.pack(side=TOP,fill='x')

Label(frm_top,text='Welcome!',bg='grey',fg='white',font='Bold 15').pack()
Label(frm_typ,text='Type a massage......',bg='grey',fg='white',font='Bold 15').pack()
msg = Text(frm_typ,width=30,height=12,font='Bold 15')
msg.pack()
sv_msg = Button(frm_typ,text='    Save Massage     ',font='Bold 15',command=msg_save,bg='Blue',fg='white')
sv_msg.pack()

Label(frm_lft,text='Set reminder time',bg='grey',fg='white',font='Bold 15').pack()

Label(frm_lft,text='      Days       ',bg='dark grey',fg='white',font='Bold 15').pack()
day_btn = Scale(frm_lft, from_=0, to=30,font='Bold 15',orient=HORIZONTAL,length=170)
day_btn.pack()
Label(frm_lft,text='      Hours      ',bg='dark grey',fg='white',font='Bold 15').pack()
hr_btn = Scale(frm_lft, from_=0, to=23,font='Bold 15',orient=HORIZONTAL,length=170)
hr_btn.pack()
Label(frm_lft,text='     Minutes     ',bg='dark grey',fg='white',font='Bold 15').pack()
min_btn = Scale(frm_lft, from_=0, to=59,font='Bold 15',orient=HORIZONTAL,length=170)
min_btn.pack()
Button(frm_lft,bg='Blue',fg='White',text='   Save Time   ',font='Bold 15',command=tm_save).pack()
Button(frm_lft,bg='red',fg='white',text='     Start     ',font='Bold 15',command=root.destroy).pack()
root.mainloop()


sleep(sec)

window = Tk()
window.title("Reminder")
window.geometry('1000x100')
lbl = Label(window, text=typed_msg, font=("Arial Bold", 15))
lbl.pack()
play1('Be attention reminder is opening')
btn = Button(window, text='play',bg='green',fg='white',command=play_msg)
btn.pack()
btn = Button(window, text='stop',bg='red',fg='white',command=exit)
btn.pack()
window.mainloop()