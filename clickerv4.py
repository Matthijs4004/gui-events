# Clicker v4
import tkinter as tk
from tkinter import IntVar
from tkinter.constants import NUMERIC
from typing import Literal
# 1 knop zorgt er voor dat het nummer in de label met 1 omhoog gaat
# 1 knop zorgt er voor dat het nummer in de label met 1 omlaag gaat.
# Als het nummer 0 is moet de achtergrond grijs zijn.
# Als het nummer kleiner dan 0 is moet de achtergrond rood zijn.
# Als het nummer groter dan 0 is moet de achtergrond groen zijn.
LastPressed = True
e = 0

def Pressed():
    if LastPressed == True:
        window.bind("<space>", UpTwo)
        window.bind("<Double-Button-1>", UpTwo)
    elif LastPressed == False:
        window.bind("<space>", DownTwo)
        window.bind("<Double-Button-1>", DownTwo)

def Background():
    if number.get() > 0:
        window["bg"] = "green"
    elif number.get() < 0:
        window["bg"] = "red"
    else:
        window["bg"] = "grey"

def Hover(e):
    window["bg"] = "yellow"

def HoverLeave(e):
    Background()

def Up(e):
    global number,LastPressed
    number.set(number.get() + 1)
    Label.configure(textvariable=number)
    Background()
    LastPressed = True
    Pressed()

def UpTwo(e):
    global number,LastPressed
    number.set(number.get() * 3)
    Label.configure(textvariable=number)
    Background()
    LastPressed = False

def DownTwo(e):
    global number,LastPressed
    number.set(number.get() / 3)
    Label.configure(textvariable=number)
    Background()
    LastPressed = True

def Down(e):
    global number,LastPressed
    number.set(number.get() - 1)
    Label.configure(textvariable=number)
    Background()
    LastPressed = False
    Pressed()

window = tk.Tk()
window.title("Clicker v4")
window.geometry("250x200")
window["bg"] = "grey"
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)
number = IntVar(value=0)
buttonUp = tk.Button(bg="white", width=20, text="Up", bd=0, command= lambda: Up(e))
Label = tk.Label(bg="white",width=20, textvariable=number)
buttonDown = tk.Button(bg="white",width=20, text="Down", bd=0, command= lambda: Down(e))
Label.bind("<Enter>", Hover)
Label.bind("<Leave>", HoverLeave)
window.bind("<Up>", Up)
window.bind("<Down>", Down)
buttonUp.place(y=45,x=50)
Label.place(y=100,x=50)
buttonDown.place(y=150,x=50)



window.mainloop()