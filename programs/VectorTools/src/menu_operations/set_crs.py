import geopandas as gpd
import tkinter as tk
from tkinter import filedialog
from src.data_service import get_layer, set_layer

def set_crs():
    layer = get_layer()

    if layer is not None:
        new_layer = layer.to_crs("EPSG:2180")

        set_layer(new_layer)

        print("set crs")
    else:
        print("error")

   
  

