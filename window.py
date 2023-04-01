import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My Window")
window.geometry("600x500")

# Add a label to the window
label = tk.Label(window, text="Hello", font=("Arial", 24))
label.pack(pady=50)

# Start the main event loop
window.mainloop()
