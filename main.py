import ttkbootstrap as ttk
from init import *

JAY = ttk.Window()
JAY.title("JUST AS YOU - JAY")
JAY.geometry("600x230")
JAY.resizable(width=False, height=False)
style = ttk.Style("darkly")

login_frame = ttk.Frame(JAY)
login_frame.pack(side="left", anchor="n", padx=10, pady=10)

username_label = ttk.Label(login_frame, text="Username", font=25)
username_label.grid(row=0, column=0, padx=5, sticky="w")

username_var = ttk.StringVar()
username_entry = ttk.Entry(login_frame, textvariable=username_var, width= 70)
username_entry.grid(row=1, column=0, padx=5, pady=5, ipady=5)


password_label = ttk.Label(login_frame, text="Password", font=20)
password_label.grid(row=2, column=0, padx=5, sticky="w")

password_var = ttk.StringVar()
password_entry = ttk.Entry(login_frame, textvariable=password_var, width= 70, show="*")
password_entry.grid(row=3, column=0, padx=5, pady=5, ipady=5)

def auth():
    if starter(username_var.get(), password_var.get()):
        JAY.destroy()
        engine()
    else:
        pass
    


auth_btn = ttk.Button(login_frame, text="AUTHENTICATE", command=auth)
auth_btn.grid(row=4, column=0, sticky="w", padx=5, pady=13, ipady=8, ipadx=25)

JAY.mainloop()