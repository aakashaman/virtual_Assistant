from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from tkinter import *
import mysql.connector
from datetime import date, datetime
import subprocess
import mysql.connector

root=Tk()
root.title("Poll Clicker BigBlueButton")
root.geometry("600x350")
root.configure(background='yellow')

labelUrl=Label(root,text='Enter URL')
labelUrl.place(x=150,y=50)

urlEntry=Entry(root,width=30)
urlEntry.place(x=300,y=50)

def pollClk():
      mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234",
      database="ca1")

      now=datetime.now()
      mycursor = mydb.cursor()

      sql = "INSERT INTO bigblue (classUrl, classDate) VALUES (%s, %s)"
      val = (urlEntry.get(),now )
      mycursor.execute(sql, val)
      mydb.commit()
      mydb.close()
      mycursor.close()
      broswer1=webdriver.Chrome()
      url=urlEntry.get()
      broswer1.get(url)
      enterName=broswer1.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/input[4]").send_keys("TestingStudent")
      clkJoinBtn=broswer1.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/form/div/span/button").click()

      time.sleep(50)

      for i in range(1,100):
       try:
        clkAudioCrossBtn=broswer1.find_element_by_xpath("/html/body/div["+str(i)+"]/div/div/div[1]/div/div/span/button[2]/span[1]/i").click()
       
       except:
        time.sleep(0.1)




      for i in range(1000000000):
        try:
            for j in range(20):
               try:
                        broswer1.find_element_by_xpath("/html/body/div[1]/div/div["+str(j)+"]/div/span/div[2]/div[2]/button").click()
                                      # /html/body/div[1]/div/div[3]/div/span/div[2]/div[2]/button  b option
               except:
                time.sleep(0.1)
       
        except:
            time.sleep(0.1)
        


btn=Button(root,text='Start Class',command=pollClk)
btn.place(x=200,y=150)

btn=Button(root,text='Show History',command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\bigblueHist.py"]))
btn.place(x=320,y=150)

root.mainloop()

