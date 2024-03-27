from tkinter import *
from tkinter import ttk

# Colors
color1 = "#3b3b3b"
color2 = "#feffff"
color3 = "#38576b"
color4 = "#ECEFF1"
color5 = "#FFAB40"



# Frames
window = Tk()
window.title("Calculator")
window.geometry("235x310")
window.config(bg=color1)

top_frame = Frame(window, width=235, height=50, bg=color3)
top_frame.grid(row =0, column=0)

body_frame = Frame(window, width=235, height=268)
body_frame.grid(row =1, column=0)

#Variable for all values

all_values = ''

# Function to enter values
def enter_values(event):

    global all_values

    all_values += str(event)

    
    value_texts.set(all_values)

# Function to calculate
def calculate():
    global all_values
    resultado = eval(all_values)
    value_texts.set(str(resultado))

# Function to clear the screen
def clear_screen():
    global all_values
    all_values=""
    value_texts.set("")


    

# Label
value_texts = StringVar()
app_label = Label(top_frame, textvariable = value_texts, text="123456789",width=16, height=2, padx="7", relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=color3, fg=color2)
app_label.place(x=0, y=0)

# Buttons

b_1 = Button(body_frame, command= clear_screen, text="C", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(body_frame, command = lambda: enter_values('%'), text="%", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(body_frame, command = lambda: enter_values('/'),text="/", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(body_frame, command = lambda: enter_values('7'),text="7", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(body_frame, command = lambda: enter_values('8'),text="8", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(body_frame, command = lambda: enter_values('9'),text="9", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(body_frame, command = lambda: enter_values('*'),text="*", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(body_frame, command = lambda: enter_values('4'),text="4", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(body_frame, command = lambda: enter_values('5'),text="5", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(body_frame, command = lambda: enter_values('6'),text="6", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(body_frame, command = lambda: enter_values('-'),text="-", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(body_frame, command = lambda: enter_values('1'),text="1", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(body_frame, command = lambda: enter_values('2'),text="2", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(body_frame, command = lambda: enter_values('3'),text="3", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(body_frame, command = lambda: enter_values('+'),text="+", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(body_frame, command = lambda: enter_values('0'),text="0", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(body_frame, command = lambda: enter_values('.'),text=".", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(body_frame, command = calculate,text="=", width=5, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)



window.mainloop()
