import tkinter as tk

root=tk.Tk()
root.title("button based gui")
root.geometry("400x200")

def greet():
    label.config(text="hey KWL GOAT, button works!!!")

label=tk.Label(root,text="press the button below",font=("Segoe UI",14))
label.pack(pady=10)

button=tk.Button(root,text="click me",command=greet)
button.pack()

tk.mainloop()