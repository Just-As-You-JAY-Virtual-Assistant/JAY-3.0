import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from static_impulses import jay
from init import starter, GUIEngine as GE

JAY = ttk.Window()
JAY.title("JUST AS YOU - JAY")
JAY.geometry("600x190")
JAY.resizable(width=False, height=False)
style = ttk.Style("darkly")

login_frame = ttk.Frame(JAY)
login_frame.pack(side="left", anchor="n", padx=10, pady=10)

def clear_username(event):
   username_var.set("")
   username_entry.unbind('<Button-1>', clear_username)

username_var = ttk.StringVar()
username_entry = ttk.Entry(login_frame, textvariable=username_var, width= 70)
username_entry.grid(row=1, column=0, padx=3, pady=5, ipady=5, columnspan=2)
username_entry.bind('<Button-1>', clear_username)
username_var.set("Enter your username")


def clear_password(event):
   password_var.set("")
   password_entry.unbind('<Button-1>', clear_password)

password_var = ttk.StringVar()
password_entry = ttk.Entry(login_frame, textvariable=password_var, width= 70, show="*")
password_entry.grid(row=3, column=0, padx=3, pady=5, ipady=5, columnspan=2)
password_entry.bind('<Button-1>', clear_password)
password_var.set("Password")

def auth():
    if username_var.get().isalnum() == False:
        print(username_var.get().isalnum())
        jay("your username can only be alphanumeric")
        if len(password_var.get()) <= 7:
            jay("and your password must be atleast 8 characters long")
    elif len(password_var.get()) <= 7:
        jay("your password must be atleast 8 characters long")
    else:
        if starter(username_var.get(), password_var.get()):
            root_frame.pack(side="left", anchor="n", padx=10, pady=10)
            JAY.title("SESSION - " + username_var.get().title())
            login_frame.pack_forget()
        else:
            password_var.set("")
    


auth_btn = ttk.Button(login_frame, text="AUTHENTICATE", width=44, bootstyle = (SUCCESS, OUTLINE) ,command=auth)
auth_btn.grid(row=4, column=0, sticky="w", padx=3, pady=20, ipady=5)

exit_btn = ttk.Button(login_frame, text="CANCEL", width=19, bootstyle = (DANGER, SOLID) ,command=JAY.destroy)
exit_btn.grid(row=4, column=1, sticky="E", padx=3, pady=20, ipady=5)



root_frame = ttk.Frame(JAY)
# root_frame.pack(side="left", anchor="n", padx=10, pady=10)

cmd_var = ttk.StringVar()
cmdEntry = ttk.Entry(root_frame, textvariable=cmd_var, width= 70)
cmdEntry.grid(row=1, column=0, padx=3, pady=5, ipady=5, columnspan=2)
   
auth_btn = ttk.Button(root_frame, text="SEND COMMAND", width=44, bootstyle = (SUCCESS, OUTLINE) ,command=lambda: GE(cmd_var.get()))
auth_btn.grid(row=4, column=0, sticky="w", padx=3, pady=20, ipady=5)

auth_btn.bind('<Return>', auth)
JAY.mainloop()