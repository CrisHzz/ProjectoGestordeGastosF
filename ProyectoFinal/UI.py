import tkinter as tk
from tkinter import ttk

from DesarolloLogico import Perfil, IngresoCatalogado, Egreso, balance, Ingreso, EgresoCatalogado,Movimiento

def guardar_ingreso(monto,dia,mes,año,divisa ,descripcion):

    ingreso_catalogado = IngresoCatalogado(monto, dia, mes, año, divisa, descripcion)
    ingreso_catalogado.guardar_ingreso(divisa)

def guardar_egreso(monto, dia, mes, año, divisa, categoria):
    egreso = EgresoCatalogado(monto, dia, mes, año, divisa, categoria)
    egreso.guardar(divisa)


def seleccionar_ingreso_egreso(opcion):
    limpiar_ventana()
    if opcion == "Ingreso":
        ingreso_label = tk.Label(root, text="Por favor ingrese los detalles del ingreso", bg='#98FB98', font=("RomanD", 25), anchor='center')
        ingreso_label.pack(fill='both', expand=True)

        monto_label = tk.Label(root, text="Monto:")
        monto_label.pack()
        monto_entry = tk.Entry(root)
        monto_entry.pack()

        dia_label = tk.Label(root, text="Día:")
        dia_label.pack()
        dia_entry = tk.Entry(root)
        dia_entry.pack()

        mes_label = tk.Label(root, text="Mes:")
        mes_label.pack()
        mes_entry = tk.Entry(root)
        mes_entry.pack()

        año_label = tk.Label(root, text="Año:")
        año_label.pack()
        año_entry = tk.Entry(root)
        año_entry.pack()

        divisa_label = tk.Label(root, text="Divisa:")
        divisa_label.pack()
        divisa_entry = tk.Entry(root)
        divisa_entry.pack()


        descripcion_label = tk.Label(root, text="Descripción:")
        descripcion_label.pack()
        descripcion_entry = tk.Entry(root)
        descripcion_entry.pack()

        categoria_label = tk.Label(root, text="Categoría:")
        categoria_label.pack()
        categoria_entry = tk.Entry(root)
        categoria_entry.pack()


        guardar_button = ttk.Button(root, text="Guardar", command=lambda: guardar_ingreso(monto_entry.get(), dia_entry.get(), descripcion_entry.get()))
        guardar_button.pack()

    else:
        egreso_label = tk.Label(root, text="Por favor ingrese los detalles del egreso", bg='#98FB98', font=("RomanD", 25), anchor='center')
        egreso_label.pack(fill='both', expand=True)

        monto_label = tk.Label(root, text="Monto:")
        monto_label.pack()
        monto_entry = tk.Entry(root)
        monto_entry.pack()

        dia_label = tk.Label(root, text="Día:")
        dia_label.pack()
        dia_entry = tk.Entry(root)
        dia_entry.pack()

        mes_label = tk.Label(root, text="Mes:")
        mes_label.pack()
        mes_entry = tk.Entry(root)
        mes_entry.pack()

        año_label = tk.Label(root, text="Año:")
        año_label.pack()
        año_entry = tk.Entry(root)
        año_entry.pack()

        divisa_label = tk.Label(root, text="Divisa:")
        divisa_label.pack()
        divisa_entry = tk.Entry(root)
        divisa_entry.pack()

        descripcion_label = tk.Label(root, text="Descripción:")
        descripcion_label.pack()
        descripcion_entry = tk.Entry(root)
        descripcion_entry.pack()

        categoria_label = tk.Label(root, text="Categoría:")
        categoria_label.pack()
        categoria_entry = tk.Entry(root)
        categoria_entry.pack()
        guardar_button = ttk.Button(root, text="Guardar", command=lambda:guardar_egreso(monto_entry.get(), dia_entry.get(), categoria_entry.get()))
        guardar_button.pack()

    root.mainloop()

def mostrar_opciones_ingreso_egreso():
    limpiar_ventana()
    ingreso_egreso_label = tk.Label(root, text="¿Desea ingresar un ingreso o un egreso?", bg='#98FB98', font=("RomanD", 25), anchor='center')
    ingreso_egreso_label.pack(fill='both', expand=True)

    button_frame = tk.Frame(root)
    button_frame.pack()

    ingreso_button = ttk.Button(button_frame, text="Ingreso", command=lambda: seleccionar_ingreso_egreso("Ingreso"))
    ingreso_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

    egreso_button = ttk.Button(button_frame, text="Egreso", command=lambda: seleccionar_ingreso_egreso("Egreso"))
    egreso_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=10)

    root.mainloop()




def mostrar_opciones_divisa():
    limpiar_ventana()
    divisa_label = tk.Label(root, text="Por favor seleccione la divisa", bg='#98FB98', font=("RomanD", 25), anchor='center')
    divisa_label.pack(fill='both', expand=True)

    button_frame = tk.Frame(root)
    button_frame.pack()

    usd_button = ttk.Button(button_frame, text="USD", command=lambda: seleccionar_divisa("USD"))
    usd_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

    cop_button = ttk.Button(button_frame, text="COP", command=lambda: seleccionar_divisa("COP"))
    cop_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=10)

    root.mainloop()

def seleccionar_perfil(profile):
    if profile == "jubilado":
        perfil = Perfil(jubilado=True)
    elif profile == "estudiante":
        perfil = Perfil(estudiante=True)
    else:
        perfil = Perfil(trabajador=True)
    print(f"Perfil seleccionado: {perfil.__dict__}")
    mostrar_opciones_divisa()

def seleccionar_divisa(divisa):
    if divisa == "USD":
        divisa = "USD"
    else:
        divisa = "COP"
    print(f"Divisa seleccionada: {divisa}")
    mostrar_opciones_ingreso_egreso()

def limpiar_ventana():
    for widget in root.winfo_children():
        widget.destroy()

root = tk.Tk()
root.configure(bg='white')

welcome_label = tk.Label(root, text="¡Bienvenido usuario a este gestor de gastos!\n \n \n Porfavor seleccione el perfil para su cuenta", bg='#98FB98', font=("RomanD", 25), anchor='center')
welcome_label.pack(fill='both', expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

jubilado_button = ttk.Button(button_frame, text="Jubilado", command=lambda: seleccionar_perfil("jubilado"))
jubilado_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

estudiante_button = ttk.Button(button_frame, text="Estudiante", command=lambda: seleccionar_perfil("estudiante"))
estudiante_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=10)

trabajador_button = ttk.Button(button_frame, text="Trabajador", command=lambda: seleccionar_perfil("trabajador"))
trabajador_button.grid(row=0, column=2, padx=10, pady=10, ipadx=20, ipady=10)

root.mainloop()


