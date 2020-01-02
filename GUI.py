import tkinter as tk

master = tk.Tk()
tk.Label(master, text="Number 1").grid(row=0, column=1)
tk.Label(master, text="Number 2").grid(row=1, column=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=0)
e2.grid(row=1, column=0)

def tinhToan():
    ketqua = int(e1.get()) + int(e2.get())
    tk.Label(master, text = ketqua).grid(row = 2, column = 1)

tk.Button(master, text="Add",command = tinhToan).grid(row=2,column=0)



master.mainloop()
