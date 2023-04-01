from tkinter import *

def login():
    username = entry_username.get()
    password = entry_password.get()


    if username == "admin" and password == "123":
        message_label.config(text="Login successful")
        root.destroy() # close login window
        open_main_window() # open main window
    else:
        message_label.config(text="Incorrect username or password")

def open_main_window():
    main_window = Tk()
    main_window.title("Welcome Window")
    main_window.geometry("400x300") # set size of main window
    main_window.resizable(False, False) # disable resizing of main window

    # create label in main window
    label = Label(main_window, text="Welcome to the main window!")
    label.pack(expand=True, pady=50) # center label in main window

    main_window.mainloop()

# create login window
root = Tk()
root.title("Login Window")
root.geometry("300x200") # set size of login window
root.resizable(False, False) # disable resizing of login window

# create frame in login window
frame = Frame(root)
frame.pack(expand=True) # center frame in login window

# create label for username in frame
label_username = Label(frame, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)

# create entry widget for username in frame
entry_username = Entry(frame)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# create label for password in frame
label_password = Label(frame, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)

# create entry widget for password in frame
entry_password = Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# create login button in frame
button_login = Button(frame, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# create label for login message in frame
message_label = Label(frame, text="")
message_label.grid(row=3, column=0, columnspan=2)
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.mainloop()
