from selenium import webdriver
import time
from tkinter import *
import threading
import mysql.connector
from datetime import datetime
import subprocess


root=Tk()
root.title("Articles View Increaser")
root.geometry('600x350')
bg = PhotoImage(file = "viewsbg2.png")
# Show image using label
label1 = Label( root, image = bg)
label1.pack()

labelUrl=Label(root,text='Enter URL')
labelUrl.place(x=150,y=50)

urlEntry=Entry(root)
urlEntry.place(x=300,y=50)

viewsLabel=Label(root,text='Enter views needed')
viewsLabel.place(x=150,y=100)


numOfViewsEntry=Entry(root)
numOfViewsEntry.place(x=300,y=100)


waitLabel=Label(root,text='Enter wait seconds')
waitLabel.place(x=150,y=150)

waitSeconds=Entry(root)
waitSeconds.place(x=300,y=150)
def getViews1():
    command=threading.Thread(target=getViews).start()

def getViews():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ca1")
    
  
    now=datetime.now()
    mycursor = mydb.cursor()

    sql = "INSERT INTO articleT (ArticleUrl, views, waitTime, ArticleDate) VALUES (%s, %s,%s,%s)"
    val = (urlEntry.get(),numOfViewsEntry.get(),waitSeconds.get(),now )
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    mycursor.close()


    browser1=webdriver.Chrome()
    a=int(float(numOfViewsEntry.get()))
    for i in range(a):
        browser1.get(""+urlEntry.get())
        time.sleep(int(waitSeconds.get()))
        statusLabel=Label(root,text=f"Page viewed {i+1} times.")
        statusLabel.place(x=220,y=320)
  

                    


btn=Button(root,text='Start',command=getViews1)
btn.place(x=250,y=220)





btn=Button(root,text='Show History',command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\articleHist.py"]))
btn.place(x=250,y=320)


root.mainloop()