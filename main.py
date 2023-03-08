import tkinter as tk 
import random
#hexvalue indexex
hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]


def randum_number():
    return  random.randint(0, len(hex) - 1)

def hex_genrator():  
    hexvalue = "#" 

    for i in range(6):
        hexvalue += str(hex[randum_number()])
        print(hexvalue) 
        
    root.config(bg=hexvalue)
    frame_labale.config(text="HEX VALUE: " + str(hexvalue),fg=hexvalue)     


def clicked():
    hex_genrator()


root = tk.Tk()
root.title("color picker")
root.geometry("800x600")
root.resizable(False,False)
root.configure(bg="#000")



#header 

root_labale =  tk.Label(root,text="COLOR PICKER",bg="#000",fg="#fff",font=("Arial",45,"bold"))
root_labale.place(x=175 , y=10)

root_frame = tk.Frame(root,width=600,height=250,bg="#fff")
root_frame.place(x=100 , y=180)

frame_labale =  tk.Label(root_frame,text="HEX VALUE: ",bg="#fff",fg="#000",font=("Arial",30,"bold"))
frame_labale.place(x=65 , y=90)

button = tk.Button(root_frame, text="CLICK HERE", bd=2, fg="black", bg="white",font=("Arial",10,"bold"),command=clicked)
button.config(relief="groove", highlightthickness=2, highlightcolor="black", highlightbackground="black")
button.place(x=250 ,y=200)

root.mainloop()

