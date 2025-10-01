from tkinter import *
from tkinter import messagebox

def greet_user():
    """Function to display a greeting message with the entered username."""
    username = txt.get()
    messagebox.showinfo("Welcome to my world", "Hello " + username)

def main():
    # Create main window
    window = Tk()
    window.title("Welcome to my world")
    window.geometry("300x300")

    # Labels
    lbl = Label(window, text="Hello World", font=("Arial", 14))
    lbl.grid(column=0, row=0)

    lbl2 = Label(window, text="Please Enter your name")
    lbl2.grid(column=0, row=1)

    # Input Field
    global txt
    txt = Entry(window, width=10)
    txt.grid(column=1, row=1)

    # Button
    btn = Button(window, text="Click me", bg="red", fg="pink", command=greet_user)
    btn.grid(column=2, row=1)

    window.mainloop()

if __name__ == "__main__":
    main()
