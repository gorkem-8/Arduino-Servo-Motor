from tkinter import *
import serial
import time
arduino = serial.Serial(port='COM5',baudrate=115200,timeout=.1)

gui = Tk()
gui.title("BackSpaceX LAB-2")
gui.geometry("500x170")

def send(position):
    position=str(position)
    print(position)
    arduino.write(bytes('BS'+position+'X','utf-8'))
    time.sleep(0.05)

def release():
    print("release")
    arduino.write(bytes('released','utf-8'))
    time.sleep(0.05)

def slidersend(a):
    a = slider.get()
    a = str(a)
    print(a)
    arduino.write(bytes('BS'+a+'X','utf-8'))
    time.sleep(0.05)
        

    
    

var = IntVar()
button1 = Radiobutton(gui,text="0",variable = var,value=0,command=lambda:send(var.get()))
button2 = Radiobutton(gui,text="45",variable = var,value=45,command=lambda:send(var.get()))
button3 = Radiobutton(gui,text="90",variable = var,value=90,command=lambda:send(var.get()))
button4 = Radiobutton(gui,text="135",variable = var,value=135,command=lambda:send(var.get()))
button5 = Radiobutton(gui,text="180",variable = var,value=180,command=lambda:send(var.get()))
button1.pack()
button1.place(x=50,y=30)
button2.pack()
button2.place(x=100,y=30)
button3.pack()
button3.place(x=150,y=30)
button4.pack()
button4.place(x=200,y=30)
button5.pack()
button5.place(x=250,y=30)
buttonrelease = Button(gui,text="RELEASE MOTOR",command=lambda:release())
buttonrelease.pack()
buttonrelease.place(x=320,y=30)

slider = Scale(gui,from_=0, to=180, orient =HORIZONTAL, length=400)
slider.bind("<ButtonRelease-1>",slidersend)
slider.pack()
slider.place(x=50,y=80)


gui.mainloop()
