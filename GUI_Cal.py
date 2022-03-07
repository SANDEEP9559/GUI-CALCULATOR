import tkinter
import tkinter as tk
window = tkinter.Tk()
window.title("Calculator")
window.configure(bg="white")
window.geometry("170x280")
window.resizable(0,0)
expression = ""
#Creating functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
def calculate():
    global expression
    result = ""
    #using try block
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "Syntax error / input error"
            expression = ""
    label_result.config(text=result)
#creating GUI

Lower_left = tk.Label(window,text="By:- Sandeep Kumar")#Created label and addes some text
Lower_left.place(relx = 0.0,rely=1.0,anchor="sw")#using place method we can set the position of label

label_result = tkinter.Label(window, text="",bg="white")
label_result.grid(row=0,column=0,columnspan=4,padx=10, pady=10)
#button_1
button_1 = tkinter.Button(window, text="1",bg="white",activebackground="orange",command=lambda: add("1"))
button_1.grid(row=1,column=0,padx=10, pady=10)
#button_2
button_2 = tkinter.Button(window, text="2",bg="white",activebackground="white",command=lambda: add("2"))
button_2.grid(row=1,column=1,padx=10, pady=10)
#button_3
button_3 = tkinter.Button(window, text="3",bg="white",activebackground="green",command=lambda: add("3"))
button_3.grid(row=1,column=2,padx=10, pady=10)
#button_divide
button_divide = tkinter.Button(window, text="/", command=lambda: add("/"))
button_divide.grid(row=1,column=3,padx=10, pady=10)
#button_4
button_4 = tkinter.Button(window, text="4",bg="white",activebackground="orange", command=lambda: add("4"))
button_4.grid(row=2,column=0,padx=10, pady=10)
#button_5
button_5 = tkinter.Button(window, text="5",bg="white",activebackground="white", command=lambda: add("5"))
button_5.grid(row=2,column=1,padx=10, pady=10)
#button_6
button_6 = tkinter.Button(window, text="6",bg="white",activebackground="green",command=lambda: add("6"))
button_6.grid(row=2,column=2,padx=10, pady=10)
#button_Multiply
button_Multiply = tkinter.Button(window, text="*", command=lambda: add("*"))
button_Multiply.grid(row=2,column=3,padx=10, pady=10)
#button_7
button_7 = tkinter.Button(window, text="7",bg="white",activebackground="orange", command=lambda: add("7"))
button_7.grid(row=3,column=0,padx=10, pady=10)
#button_8
button_8 = tkinter.Button(window, text="8", bg="white",activebackground="white",command=lambda: add("8"))
button_8.grid(row=3,column=1,padx=10, pady=10)
#button_9
button_9 = tkinter.Button(window, text="9",bg="white",activebackground="green", command=lambda: add("9"))
button_9.grid(row=3,column=2,padx=10, pady=10)
#button_subtract
button_subtract = tkinter.Button(window, text="-",command=lambda: add("-"))
button_subtract.grid(row=3,column=3,padx=10, pady=10)
#button_clear
button_clear = tkinter.Button(window, text="C", bg="white",activebackground="red",command=lambda: clear())
button_clear.grid(row=4,column=0,padx=10, pady=10)
#button_0
button_0 = tkinter.Button(window, text="0", bg="white",activebackground="yellow",command=lambda: add("0"))
button_0.grid(row=4,column=1,padx=10, pady=10)
#button_dot
button_dot = tkinter.Button(window, text=".",bg="white",activebackground="green", command=lambda: add("."))
button_dot.grid(row=4,column=2,padx=10, pady=10)
#button_add
button_add = tkinter.Button(window, text="+", command=lambda: add("+"))
button_add.grid(row=4,column=3,padx=10, pady=10)
#button_equals
button_equals = tkinter.Button(window, text="=",bg="white",activebackground="Green",width=20,command=lambda: calculate())
button_equals.grid(row=5,column=0,columnspan=4)
#outerloop of tkinter Tk()
window.mainloop()
