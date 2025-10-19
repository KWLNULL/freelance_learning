import tkinter as tk

def input_update():
    name=entry.get()
    if name=="saumya kejriwal" or name=="KWL":
        label.config(text=f"welcome GOAT")
    else:
        label.config(text=f"welcome {name}")

root=tk.Tk()
root.title("input based gui")
root.geometry("400x250")

entry=tk.Entry(root,width=30)
entry.pack(pady=20)

label=tk.Label(root,text="",font=("Segoe UI",14))
label.pack(pady=10)

button=tk.Button(root,text="submit",command=input_update)
button.pack(pady=25)

tk.mainloop()