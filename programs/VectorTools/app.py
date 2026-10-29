import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.create_window import create_window
from src.create_menu_option import create_menu_option
from src.menu_operations.close_program import close_program
from src.menu_operations.load_data_and_remember_outcome import load_data_and_remember_outcome
from src.data_service import get_layer
from src.menu_operations.show_layer import show_layer
from src.menu_operations.show_layer_info import show_layer_info



def update_menu():
    canvas.delete("layer status")

    if get_layer is not None:
        canvas.create_text(
            180,
            380,
            text="FILE UPLOADED SUCCESSFULLY",
            fill="green",
            tags="layer_status"
        )



window, canvas = create_window()

create_menu_option(canvas, 380, "Close Program", lambda: close_program(window))
create_menu_option(canvas, 400, "Wyświetl warstwę", lambda: show_layer())
create_menu_option(canvas, 435, "Wyświetl informacje o warstwie", lambda: show_layer_info())

window.mainloop()
