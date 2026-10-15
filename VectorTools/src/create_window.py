import tkinter as tk
from pathlib import Path

def create_window():
    window = tk.Tk()
    window.title("VectorTools")
    window.resizable(False, False)

    canvas = tk.Canvas(
        window,
        width=650,
        height=550,
        highlightthickness=0
    )

    canvas.pack()

    current_dir = Path(__file__).resolve().parent

    image_path = current_dir / "img" / "ekran.png"

    background_screen = tk.PhotoImage(file=str(image_path))


    canvas.create_image(
        0,
        0,
        image=background_screen,
        anchor="nw"
    )

    canvas.background_image = background_screen

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

    def quit_program(event=None):
        window.destroy()

    label = tk.Label(window, text="Press esc to exit", font=('Helvetica', 10, 'bold'), fg="gray",bg="white")
    canvas.create_window(
        55,
        495,
        window=label,
        anchor="center"
    )
    window.bind('<Escape>', quit_program)

    return (window, canvas)