import tkinter as tk

def close_program():
    window.destroy()

window = tk.Tk()
window.title("VectorTools")
window.resizable(False, False)

canvas = tk.Canvas(
    window,
    width=650,
    height=548,
    highlightthickness=0
)

canvas.pack()

background_screen = tk.PhotoImage(
    file=r"C:\Users\nikit\Nikita-Osaula---Struktury-Danych\night2.png"
)

canvas.create_image(
    0,
    0,
    image =background_screen,
    anchor="nw"
)

canvas.create_text(
    510,
    50,
    text="VectorTools",
    font=("Arial",30,"bold"),
    fill="black"

)

canvas.create_text(
    120,
    360,
    text="Choose operation:",
    font=("Arial",15,"bold"),
    fill="black"

)

canvas.create_text(
    110,
    380,
    text="Close Program",
    font=("Arial", 11, "bold"),
    fill="black",
    tags="close"
)

canvas.tag_bind(
    "close",
    "<Button-1>",
    lambda event: close_program()
)


canvas.tag_bind(
    "close",
    "<Enter>",
    lambda event: canvas.itemconfig(
        "close",
        fill="#F00524",
        
    )
)


canvas.tag_bind(
    "close",
    "<Leave>",
    lambda event: canvas.itemconfig(
        "close",
        fill="black"
    )
)

window.mainloop()