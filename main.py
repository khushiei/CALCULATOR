from tkinter import *

def compute(value):
    entry.config(state="normal")
    l = len(entry.get())
    exp = entry.get()
    if value == "AC":
        entry.delete(0,END)
    elif value == "C":
        if l>0:
            entry.delete(l-1,END)
    elif value in "0123456789":
        entry.insert(END,value)
    elif value == "=":
        if exp:
            while exp and exp[-1] in "%*+-/^X":
                exp = exp[:-1]
            exp = exp.replace("^", "**")

            try:
                result = eval(exp)
                entry.delete(0, END)
                entry.insert(END, result)
            except:
                entry.delete(0, END)
                entry.insert(END, "Error")
    else:
        if exp[-1] in "%*+-/^":
            entry.delete(l-1,END)
            entry.insert(END,value)
        else:
            entry.insert(END,value) 
    entry.config(state='readonly')

window = Tk()
window.config(background="#fad1d9")
window.title("Calculator")
icon = PhotoImage(file="star.png")
window.iconphoto(True,icon)

frame = Frame(window)
frame.grid(row=1,column=1)

entry = Entry(frame, width=20, font=("Arial", 20), bd=5, relief=RIDGE, justify=RIGHT,fg="#848e59",state="readonly")
entry.grid(row=0, column=0, columnspan=4, pady=10)


btns = [['AC','C','%','/'],
        ['7','8','9','*'],
        ['4','5','6','-'],
        ['1','2','3','+'],
        ['^','0','.','=']]

for i in range(len(btns)):
    for j in range(len(btns[i])):
        Button(frame,text=btns[i][j],width=10,height=3,fg="#fad1d9",bg="#848e59",activebackground="#848e59",activeforeground="#fad1d9",command=lambda v=btns[i][j]: compute(v)).grid(row=i+1,column=j)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()