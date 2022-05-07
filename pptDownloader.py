from selenium import webdriver
import time
from tkinter import *
from datetime import datetime
import mysql.connector
import subprocess

root=Tk()
root.title("BigBlueButton PPT downloader")
root.geometry('600x350')
root.configure(background='grey')


labelUrl=Label(root,text='Enter URL')
labelUrl.place(x=150,y=50)

urlEntry=Entry(root)
urlEntry.place(x=300,y=50)


labelName=Label(root,text='Enter PPT name')
labelName.place(x=150,y=100)

NameEntry=Entry(root)
NameEntry.place(x=300,y=100)



def pptDownload():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ca1")
    
    now=datetime.now()
    mycursor = mydb.cursor()

    sql = "INSERT INTO pptDT (pptUrl,PPTname,pptDate) VALUES (%s,%s,%s)"
    val = (urlEntry.get(),NameEntry.get(),now )
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    mycursor.close()

    browser1=webdriver.Chrome()
    url1=urlEntry.get()

    for i in range(1,1000):
        mainurl=url1+str(i)
        browser1.get(mainurl)
        browser1.maximize_window()
        picname= NameEntry.get()+str(i)+".png"
        browser1.save_screenshot(picname)
        




btn=Button(root,text='Start Downloading',command=pptDownload)
btn.place(x=200,y=150)


btn=Button(root,text='Show History',command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\pptHist.py"]))
btn.place(x=250,y=250)

root.mainloop()