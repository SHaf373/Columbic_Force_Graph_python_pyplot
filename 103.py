import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *

Columbic_constant=9e+10
def graphA():
    radius=radiusvalue.get() 
    charge1=charge1value.get()
    charge2=charge2value.get()
    radiuses=np.array(range(radius,20000,2))
    columbic_force=(Columbic_constant*charge1*charge2)/(radiuses**2)
    plt.plot(radiuses,columbic_force,label=("F = k (q1*q2)/r**2"))
    plt.title("RELATION BETWEEN COLUMBIC FORCE AND RADIUS")
    plt.xlabel("Radius (R) ",fontsize="medium",)
    plt.ylabel("Gravitaional Force (F = k (q1*q2)/r**2) ")

    plt.grid(alpha=.4,linestyle="--")
    plt.legend()
    plt.show()
	
def graphB():
    radius=radiusvalue.get() 
    charge1=charge1value.get()
    charge2=charge2value.get()
    chargeTwos = np.array(range(charge2,20000,2))
    columbic_force=(Columbic_constant*charge1*chargeTwos)/(radius**2)
    plt.plot(chargeTwos,columbic_force,label=("F = k (q1*q2)/r**2"))
    plt.title("RELATION BETWEEN COLUMBIC FORCE AND RADIUS")
    plt.xlabel("Radius (R) ",fontsize="medium",)
    plt.ylabel("Gravitaional Force (F = k (q1*q2)/r**2) ")

    plt.grid(alpha=.4,linestyle="--")
    plt.legend()
    plt.show()


def tkinter():
    global radiusvalue
    global charge1value
    global charge2value
    
    root = Tk()
    root.title('CALCULATING RELATIONS B/W COLUMBIC FORCE VS MASS/RADIUS')
    photo = PhotoImage(file = "10.png")
    w = Label(root, image=photo)
    w.pack()
    
    label1=Label(root,text='enter mass one here:')
    label1.pack()

    charge1value = IntVar()
    ent = Entry(root,textvariable=charge1value)
    ent.pack()
    ent.focus_set()

    label2=Label(root,text='enter mass 2 here:')
    label2.pack()

    charge2value = IntVar()
    ent2=Entry(root,textvariable=charge2value)
    ent2.pack()

    label3=Label(root,text='enter radius here:')
    label3.pack()

    radiusvalue = IntVar()
    ent3=Entry(root,textvariable=radiusvalue)
    ent3.pack()

    button = Button(root,bg="#FF5833",fg="#ecf0f1",font=("cala"),text="RELATION WITHRESPECT TO RADIUS",justify="center", command=graphA)
    w.place(relx=0.30,rely=-0.10)
    button.pack()

    button2 = Button(root,bg="#FF5833",fg="#ecf0f1",font=("cala"),text="RELATION WITHRESPECT TO CHARGE",justify="center", command=graphB)
    button2.pack()
    root.mainloop()

tkinter()

