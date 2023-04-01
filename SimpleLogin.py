from tkinter import *

root = Tk()
root.title("Login Window")

# Set the size of the window and center it
frame_width = 300
frame_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (frame_width/2))
y = int((screen_height/2) - (frame_height/2))
root.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x, y))

# Create a frame to hold the login widgets and center it
frame = Frame(root, width=250, height=150)
frame.pack_propagate(0) # Prevent the frame from shrinking
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Creating a label for username
label_username = Label(frame, text="Username:")
label_username.pack(pady=5)

# Creating an entry widget for username
entry_username = Entry(frame)
entry_username.pack(pady=5)

# Creating a label for password
label_password = Label(frame, text="Password:")
label_password.pack(pady=5)

# Creating an entry widget for password
entry_password = Entry(frame, show="*")
entry_password.pack(pady=5)

# Creating a button to login
button_login = Button(frame, text="Login")
button_login.pack(pady=5)

root.mainloop()
