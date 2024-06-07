import tkinter as tk
from tkinter import messagebox

custom_font = ("Helvetica", 28)

def show_message1():
    messagebox.showinfo("SignIn", "Sign-up completed")

def show_message2():
    messagebox.showinfo("Login", "Login completed")

def login():
    username = entry_name_login.get()
    password = entry_password_login.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password")

def switch_to_login():
    root.withdraw()
    login_window.deiconify()

root = tk.Tk()
root.title("Signup")

label_name = tk.Label(root, text="Username", font=custom_font)
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")

label_email = tk.Label(root, text="Email", font=custom_font)
label_email.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5, sticky="w")

label_password = tk.Label(root, text="Password", font=custom_font)
label_password.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(root)
entry_password.grid(row=2, column=1, padx=10, pady=5, sticky="w")

button_signup = tk.Button(root, text="Sign Up", command=show_message1, font=custom_font)
button_signup.grid(row=3, column=0, columnspan=2, pady=10)

button_login = tk.Button(root, text="Already have an account", command=switch_to_login, font=custom_font)
button_login.grid(row=4, column=0, columnspan=2, pady=10)

login_window = tk.Toplevel(root)
login_window.title("Login")

label_name_login = tk.Label(login_window, text="Username", font=custom_font)
label_name_login.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name_login = tk.Entry(login_window)
entry_name_login.grid(row=0, column=1, padx=10, pady=5, sticky="w")

label_password_login = tk.Label(login_window, text="Password", font=custom_font)
label_password_login.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password_login = tk.Entry(login_window)
entry_password_login.grid(row=1, column=1, padx=10, pady=5, sticky="w")

button_login = tk.Button(login_window, text="Login", command=login, font=custom_font)
button_login.grid(row=2, column=0, columnspan=2, pady=10)

login_window.withdraw()

root.mainloop()
