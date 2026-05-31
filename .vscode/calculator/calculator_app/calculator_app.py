import tkinter as tk
import math

# main window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("350x500")
root.configure(bg="#1e1e2f")

expression = ""

# display function
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

def delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def square_root():
    global expression
    try:
        result = math.sqrt(float(expression))
        input_text.set(result)
        expression = str(result)
    except:
        input_text.set("Error")
        expression = ""

# display
input_text = tk.StringVar()

display = tk.Entry(root,
                   textvariable=input_text,
                   font=("Arial", 28),
                   bd=10,
                   relief="ridge",
                   justify="right",
                   bg="#2d2d44",
                   fg="white")

display.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=20)

# button style
btn_color = "#3a3a5a"
op_color = "#ff9500"

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

buttons = [
('7','8','9','/'),
('4','5','6','*'),
('1','2','3','-'),
('0','.','=','+')
]

for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e1e2f")
    row_frame.pack(expand=True, fill="both")
    
    for btn in row:
        if btn == "=":
            tk.Button(row_frame,text=btn,font=("Arial",18),
                      bg=op_color,fg="white",
                      command=equal,width=5,height=2).pack(side="left",expand=True,fill="both",padx=5,pady=5)
        else:
            tk.Button(row_frame,text=btn,font=("Arial",18),
                      bg=btn_color,fg="white",
                      command=lambda b=btn: press(b),
                      width=5,height=2).pack(side="left",expand=True,fill="both",padx=5,pady=5)

# extra feature buttons
extra = tk.Frame(root, bg="#1e1e2f")
extra.pack(fill="both")

tk.Button(extra,text="Clear",font=("Arial",14),bg="#ff4d4d",fg="white",
          command=clear).pack(side="left",expand=True,fill="both",padx=5,pady=5)

tk.Button(extra,text="Delete",font=("Arial",14),bg="#ffaa00",fg="white",
          command=delete).pack(side="left",expand=True,fill="both",padx=5,pady=5)

tk.Button(extra,text="√",font=("Arial",14),bg="#4CAF50",fg="white",
          command=square_root).pack(side="left",expand=True,fill="both",padx=5,pady=5)

root.mainloop()