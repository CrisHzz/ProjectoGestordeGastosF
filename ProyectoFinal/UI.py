import tkinter as tk
from DesarolloLogico import Perfil, IngresoCatalogado, Egreso, balance, Ingreso, EgresoCatalogado 

def seleccionar_perfil(profile):
    if profile == "jubilado":
        perfil = Perfil(jubilado=True)
    elif profile == "estudiante":
        perfil = Perfil(estudiante=True)
    else:
        perfil = Perfil(trabajador=True)
    print(f"Perfil seleccionado: {perfil.__dict__}")

root = tk.Tk()
root.configure(bg='light blue')

welcome_label = tk.Label(root, text="¡Bienvenido usuario a este gestor de gastos!", bg='light blue')
welcome_label.pack()

jubilado_button = tk.Button(root, text="Jubilado", command=lambda: seleccionar_perfil("jubilado"))
jubilado_button.pack()

estudiante_button = tk.Button(root, text="Estudiante", command=lambda: seleccionar_perfil("estudiante"))
estudiante_button.pack()

trabajador_button = tk.Button(root, text="Trabajador", command=lambda: seleccionar_perfil("trabajador"))
trabajador_button.pack()

root.mainloop()
