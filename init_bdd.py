import tkinter as tkt
from tkinter import messagebox
import os
from base_datos import crear_tablas, RUTA_DB
def inicializar_base_datos():
    if not os.path.exists(RUTA_DB):
        crear_tablas()
        root = root()
        root.withdraw()
        messagebox.showinfo("Base de Datos", "✅Se creó con exito la base de datos de sqlite")
    else:
        root = tkt.Tk()
        root.withdraw()
        messagebox.showinfo("Base de datos", "❗📄 La base de datos ya existía")
        root.destroy()
        

if __name__ == "__main__":
    inicializar_base_datos()