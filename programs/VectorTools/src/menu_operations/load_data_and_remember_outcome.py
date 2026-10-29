import geopandas as gpd
from tkinter import filedialog, messagebox

from src.data_service import set_layer

def load_data_and_remember_outcome():
    layer = load_data()
    set_layer(layer)

def load_data():
    path = filedialog.askopenfilename(
        title="Choose layer",

    )
    if not path:
        return None
    try:
        layer = gpd.read_file(path)
    except Exception:
        messagebox.showwarning(
            "Loading error",
            "Failed to load the selected file.\n"
            "Ensure that it is a valid GIS file."
        )
        return None
    return layer