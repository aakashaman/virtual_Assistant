from tkinter import *
import threading
from PIL import Image,ImageTk
import subprocess



def seleniumWindow():
      top1=Toplevel(root)
      top1.title("Selenium Applications")
      top1.geometry("1200x700")
      top1.configure(background='yellow')

      global img
      path = r"C:\Users\ritik\Desktop\Virtual Assistant\bg2.png"
      img = ImageTk.PhotoImage(Image.open(path))
      panel = Label(top1, image=img)
      panel.pack()
      
      #ppt downloader
      btnbg1 = PhotoImage(file = "pptbg.png")
      # Show image using label
      label1 = Label( top1, image = btnbg1)
      btn1=Button(top1,image=btnbg1,borderwidth=0,command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\pptDownloader.py"])).place(x=120,y=175)

      #bigbluebutton poll clicker
      btnbg2 = PhotoImage(file = "bigbluebg.png")
      # Show image using label
      label2 = Label( top1, image = btnbg2)
      btn2=Button(top1,image=btnbg2,borderwidth=0,command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\bigbluePoll.py"])).place(x=480,y=175)

      ##article writer
      btnbg3 = PhotoImage(file = "articlebg.png")
      # Show image using label
      label3 = Label( top1, image = btnbg3)
      btn3=Button(top1,image=btnbg3,borderwidth=0,command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\article.py"])).place(x=840,y=175)


      top1.mainloop()





root = Tk()
root.title('Virtual Servant - Created by Aakash Kumar and Ritik Dubey')
root.geometry('1200x700')
root.configure(background='yellow')
bg = PhotoImage(file = "bg1.png")


# Show image using label
label1 = Label( root, image = bg)
label1.pack()

frame1=Frame(root,height=100,width=1200)
frame1.place(x=0,y=600)


btnbg1 = PhotoImage(file = "1.png")
# Show image using label
label2 = Label( root, image = btnbg1)
btn1=Button(frame1,image=btnbg1,borderwidth=0,command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\app.py"])).place(x=133,y=10)

btnbg2 = PhotoImage(file = "2.png")
# Show image using label
label3 = Label( root, image = btnbg1)
btn2=Button(frame1,image=btnbg2,borderwidth=0,command=lambda:subprocess.Popen(args=['python',r'C:\Users\ritik\Desktop\Virtual Assistant\PythonNotepad.py'])).place(x=346.6,y=10)

btnbg3 = PhotoImage(file = "3.png")
# Show image using label
label4 = Label( root, image = btnbg1)
btn3=Button(frame1,image=btnbg3,borderwidth=0,command=seleniumWindow).place(x=559.6,y=10)

btnbg4 = PhotoImage(file = "4.png")
# Show image using label
label5 = Label( root, image = btnbg1)
btn4=Button(frame1,image=btnbg4,borderwidth=0,command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\calc.py"])).place(x=772.9,y=10)

btnbg5 = PhotoImage(file = "5.png")
# Show image using label
label6 = Label( root, image = btnbg1)
btn5=Button(frame1,image=btnbg5,borderwidth=0,command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\snake.py"])).place(x=986.2,y=10)

# import subprocess
# Play = Button(root, text="PLay(Bot)", fg="blue", bg="cyan",command=lambda:subprocess.Popen(args=['python', r"C:\Users\ritik\Desktop\Virtual Assistant\bigblue poll.py"]))
# Play.place(x=100,y=100)

root.mainloop()