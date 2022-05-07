import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("1250x250") 
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="1234",
  database="ca1"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM pptDT limit 0,100")
e=Label(my_w,width=10,text='srnum',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='PPT URL',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='PPT Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=2)
e=Label(my_w,width=10,text='Date for PPT',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=3)
i=1
for bigblue in my_conn: 
    for j in range(len(bigblue)):
        e = Entry(my_w, width=50, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, bigblue[j])
    i=i+1
my_w.mainloop()