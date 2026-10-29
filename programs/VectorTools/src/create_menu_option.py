import tkinter as tk
from collections.abc import Callable 

def create_menu_option(
        canvas: tk.Canvas,
        height: int,
        text: str,
        *operations: Callable
):
    text_id = canvas.create_text(
        110,
        height,
        text=text,
        font=("Arial", 11, "bold"),
        fill="black",
        
    )

    canvas.tag_bind(
        text_id,
        "<Button-1>",
        lambda event: [operation() for operation in operations]
    )

    canvas.tag_bind(
        text_id,
        "<Enter>",
        lambda event: (canvas.itemconfig(
            text_id,
            fill="#F00524"),
            canvas.config(cursor="hand2"),
            
                

        )

    )

    canvas.tag_bind(
        text_id,
        "<Leave>",
        lambda event: (canvas.itemconfig(
            text_id,
            fill="black"),
            canvas.config(cursor="")
           
        )
    )

