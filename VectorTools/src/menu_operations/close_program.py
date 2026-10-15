from tkinter import *
def close_program(window):
    toplevel_window = Toplevel()
    toplevel_window.geometry("365x200")
    toplevel_window.title("Close program")
    toplevel_window.grab_set()

    label = Label(toplevel_window,
                text="Are you sure?",
                font=("Arial", 11),
                )
    label.pack(pady=25)

    btn_yes = Button(toplevel_window,
                     text="Yes",
                     font=("bold",20),
                     bg="#0055fe",
                     cursor="hand2",
                     command=window.destroy)
    btn_yes.place(x=90,y=100)

    btn_no = Button(toplevel_window,
                         text="No",
                         font=("bold",20),
                         bg="#0055fe",
                         cursor="hand2",
                         command=toplevel_window.destroy)
    btn_no.place(x=200,y=100)