import tkinter as tk
root=tk.Tk()
root.title("first gui window")
root.geometry("500x500")

label=tk.Label(root,text="KWL's a GOAT",font=("Segoe UI",14))
label.pack(pady=50)

root.mainloop()