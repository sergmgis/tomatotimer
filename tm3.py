# -*- coding: utf-8 -*-
"""
    Make alert after sets minutes or in set time. After times value you can set message to displaying.
"""


from tkinter import *
import time
import datetime


def setTme(e):
    global tmSec
    global doit
    global mesSt
    doit = True
    
    st = min_entry.get()
    a  = st.split(' ',1)
    if a[0].isdigit() :
        tmSec = int(a[0])*60
        if len(a) > 1 and len(a[1].strip()):
            mesSt = a[1].strip()
        tk0.destroy()
    else :
        b = a[0].split(':',1)
        if b[0].isdigit() and b[1].isdigit():
            if len(a) > 1 and len(a[1].strip()):
                mesSt = a[1].strip()
            tmSec = (int(b[0]) - datetime.datetime.now().hour)*3600 + (int(b[1]) - datetime.datetime.now().minute)*60 - datetime.datetime.now().second
            if tmSec < 0:
                tmSec = 0
            tk0.destroy()
        
    return
    
def cancel(e):
    global doit
    doit = False
    tk0.destroy()
    
def cancelTk(e):
    tk.destroy()    


doit = False
mesSt = "GO!"
tk0 = Tk()
tk0.title(u'Минуты или точное время')
frm = Frame(tk0)
frm.pack()
min_entry = Entry(frm, width=10, font="Courier 40")
min_entry.grid(row=0, column=0)
min_entry.focus()
# exit_button = Button(frm, text="Ok", width=30,height=2,command=setTme)
# exit_button.grid(row=1, column=0)
tk0.bind_all('<Return>',setTme)
tk0.bind_all('<Escape>',cancel)
tk0.mainloop()

if not doit:
    sys.exit(0)

# exit()
print(time.strftime("%H:%M:%S",time.localtime(time.time())))
print(tmSec)
time.sleep(tmSec)
print(time.strftime("%H:%M:%S",time.localtime(time.time())))

tk = Tk()
tk.title(u'GO!')
f = Frame()
f.pack()
time_var = StringVar()
time_label = Label(f, textvariable=time_var, font="Courier 60", bg="Black", fg="#00B000")
time_label.pack()
time_var.set(mesSt)
tk.bind_all('<Escape>',cancelTk)
tk.bind_all('<Return>',cancelTk)
tk.mainloop()

