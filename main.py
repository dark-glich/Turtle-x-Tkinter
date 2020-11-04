import turtle
from tkinter import *
root = Tk()
root.title("Menu")
root.configure(bg='white')

def clean():
    button_1["state"] = NORMAL
    button_2["state"] = NORMAL
    button_3["state"] = NORMAL
    button_4["state"] = NORMAL
    button_5["state"] = NORMAL
    turtle.clear()
    cleaning = True
    while cleaning:
        turtle.reset()
    

def spiral():
    button_1["state"] = DISABLED
    button_2["state"] = DISABLED
    button_3["state"] = DISABLED
    button_4["state"] = DISABLED
    button_5["state"] = DISABLED
    
    x = -200
    y = 250
    turtle.reset()
    cleaning = False
    turtle.pen(pencolor="red", pensize=2)  
    
    turtle.delay(1)
    turtle.penup()
    turtle.goto(0, x)
    turtle.pendown()
    turtle.circle(y)

    for i in range (24):
        if i % 2 == 0:
            turtle.pen(pencolor="orange", pensize=2)
        else:
            turtle.pen(pencolor="red", pensize=2)    
        turtle.penup()
        turtle.goto(0, x+10)
        turtle.pendown()
        turtle.circle(y-10)
        x = x+10
        y = y-10
    button_1["state"] = NORMAL
    button_2["state"] = NORMAL
    button_3["state"] = NORMAL
    button_4["state"] = NORMAL
    button_5["state"] = NORMAL
    turtle.clear()

def diamond ():
    button_1["state"] = DISABLED
    button_2["state"] = DISABLED
    button_3["state"] = DISABLED
    button_4["state"] = DISABLED
    button_5["state"] = DISABLED
    turtle.reset()
    cleaning = False
    a = 300
    b = -300
    for i in range(31):
        turtle.penup()
        turtle.goto(0, -300)
        turtle.pendown()
        turtle.goto(a,00)
        turtle.goto(00, a)
        turtle.goto(b, 00)
        turtle.goto(0, -300)
        a = a - 10
        b = b + 10
    button_1["state"] = NORMAL
    button_2["state"] = NORMAL
    button_3["state"] = NORMAL
    button_4["state"] = NORMAL
    button_5["state"] = NORMAL

def rainbow():
    button_1["state"] = DISABLED
    button_2["state"] = DISABLED
    button_3["state"] = DISABLED
    button_4["state"] = DISABLED
    button_5["state"] = DISABLED
    cleaning = False
    turtle.reset()
    e = 350
    f = 330
    colors = ["#c61aff", "#6600cc", "DodgerBlue", "#99ff33", "yellow", "orange", "red"]
    for i in range(7):
        if i == 0:
            turtle.left(90)
            turtle.pen(pencolor= "violet",pensize=50)
        else:
            turtle.left(180)
        turtle.pen(pencolor= colors[i], pensize=50)
        
        turtle.penup()
        turtle.goto(e, -400)
        turtle.delay(2)
        turtle.pendown()
        turtle.circle(f, 180)
        e = e+50
        f = f+50
        if i == 6:
            turtle.penup()
            turtle.goto(e, -1000)
            turtle.pendown()
    button_1["state"] = NORMAL
    button_2["state"] = NORMAL
    button_3["state"] = NORMAL
    button_4["state"] = NORMAL
    button_5["state"] = NORMAL
def semicircle():
    button_1["state"] = DISABLED
    button_2["state"] = DISABLED
    button_3["state"] = DISABLED
    button_4["state"] = DISABLED
    button_5["state"] = DISABLED
    turtle.reset()
    cleaning = False
    m = 15
    for i in range(24):
        turtle.pen(pensize=2)
        turtle.delay(1)
        turtle.left(m)
        turtle.circle(200)
        turtle.home()
        m = m + 15
    button_1["state"] = NORMAL
    button_2["state"] = NORMAL
    button_3["state"] = NORMAL
    button_4["state"] = NORMAL
    button_5["state"] = NORMAL

def semi():
    button_1["state"] = DISABLED
    button_2["state"] = DISABLED
    button_3["state"] = DISABLED
    button_4["state"] = DISABLED
    button_5["state"] = DISABLED
    turtle.reset()
    cleaning = False
    m = 5
    for i in range(72):
        turtle.delay(1)
        turtle.left(m)
        turtle.circle(200, 180)
        turtle.home()
        m = m + 5
    button_1["state"] = NORMAL
    button_2["state"] = NORMAL
    button_3["state"] = NORMAL
    button_4["state"] = NORMAL
    button_5["state"] = NORMAL

# creating buttons
intro_label= Label(root, text= "Welcome", font=("arial", 80, "bold"), fg="#ff6600", bg="white")
intro_label.grid(row= 0,column=0, columnspan=200)

main_frame = LabelFrame(root, text = "choose any One Drawing", padx= 50, font=("arial", 40, "bold"), fg="#ff471a", bg="white")
main_frame.grid(row=1, column=0, padx=5 ,pady=5 , ipadx=25, ipady= 140)

blank_label=Label(main_frame, text="", bg="white")
blank_label.grid(row=0, column=0)

label_1 = Label(main_frame, text= "Circle Pattern: ", font=("helvetica", 20, "italic"), fg= "#33334d", bg="white")
button_1 = Button(main_frame, text="Create" , command= spiral, state=NORMAL, relief="ridge", bg="white") 
label_1.grid(row=1, column=0, padx=100)
button_1.grid(row=1, column=1)

label_2 = Label(main_frame, text= "   Triangle Pattern : ", font=("helvetica", 20, "italic"), fg= "#33334d", bg="white")
button_2 = Button(main_frame, text="Create" , command= diamond, state=NORMAL, relief="ridge", bg="white") 
label_2.grid(row=2, column=0)
button_2.grid(row=2, column=1)

label_3 = Label(main_frame, text= "Rainbow: ", font=("helvetica", 20, "italic"), fg= "#33334d", bg="white")
button_3 = Button(main_frame, text="Create" , command= rainbow, state=NORMAL, relief="ridge", bg="white") 
label_3.grid(row=3, column=0)
button_3.grid(row=3, column=1)

label_4 = Label(main_frame, text= "Round pattern: ", font=("helvetica", 20, "italic"), fg= "#33334d", bg="white")
button_4 = Button(main_frame, text="Create" , command= semicircle, state=NORMAL, relief="ridge", bg="white") 
label_4.grid(row=4, column=0)
button_4.grid(row=4, column=1)

label_5 = Label(main_frame, text= "SemiCircle Design : ", font=("helvetica", 20, "italic"), fg= "#33334d", bg="white")
button_5 = Button(main_frame, text="Create" , command= semi, state=NORMAL, relief="ridge", bg="white") 
label_5.grid(row=5, column=0)
button_5.grid(row=5, column=1)

blank_label=Label(main_frame, text="", bg="white")
blank_label.grid(row=6, column=0)
blank_label=Label(main_frame, text="", bg="white")
blank_label.grid(row=7, column=0)

clear_label=Label(main_frame, text="Clear : ", font=("helvetica", 60, "bold"), fg= "black", bg="white")
clear_label.grid(row=8, column=0)
clear_button = Button(main_frame, text= "Clear", relief="groove", command=clean, bg="white")
clear_button.grid(row=8, column=1, ipadx=100, ipady= 25)
root.mainloop()

