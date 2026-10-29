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
from src.update_menu import update_menu
from src.menu_operations.save_data import save_data

window, canvas = create_window()

create_menu_option(canvas, 380, "Wczytaj warstwę", lambda: load_data_and_remember_outcome(), lambda: update_menu(canvas))
create_menu_option(canvas, 400, "Wyświetl warstwę", lambda: show_layer())
create_menu_option(canvas, 420, "Wyświetl informacje o warstwie", lambda: show_layer_info())
create_menu_option(canvas, 440, "Zapisz warstwę", lambda: save_data())
create_menu_option(canvas, 460, "Zamknij program", lambda: close_program(window))

window.mainloop()
