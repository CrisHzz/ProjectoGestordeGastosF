import tkinter as tk
from tkinter import ttk
from datetime import date
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

hoy = date.today()

from DesarolloLogico import Perfil, IngresoCatalogado, Egreso, balance, Ingreso, EgresoCatalogado,Movimiento

def guardar_ingreso(monto,categoria, divisa):

    ingreso_catalogado = IngresoCatalogado(monto, hoy.day, hoy.month, hoy.year, divisa, categoria)
    ingreso_catalogado.guardar_ingreso(divisa)

def guardar_egreso(monto, categoria, divisa):
    egreso = EgresoCatalogado(monto, hoy.day, hoy.month, hoy.year, divisa, categoria)
    egreso.guardar(divisa)

def movimientos():
    with open('balance.csv', 'r') as file:
        suma1 = 0
        suma2 = 0
        for line in file:
            linea = line.split(',')
            if int(linea[0]) >= 0:
                suma1 += int(linea[0])
            else:
                suma2 += int(linea[0])
    return [suma1, suma2*-1]

def mostrar_grafica_circular():
    etiquetas = ['Ingresos', 'Egresos']
    valores = movimientos()
    etiquetas[0] += ":"+str(valores[0])
    etiquetas[1] += ":"+str(valores[1])

    figura = Figure(figsize=(5, 5), dpi=100)
    grafica_circular = figura.add_subplot(111)

    grafica_circular.pie(valores, labels=etiquetas, autopct='%1.1f%%')

    lienzo = FigureCanvasTkAgg(figura, master=root)
    lienzo.draw()


    lienzo.get_tk_widget().pack()

def funciones_combinadas(monto, categoria, divisa,count):
    if count == 1:
        guardar_ingreso(monto, categoria, divisa)
    else:
        guardar_egreso(monto, categoria, divisa)
    mostrar_opciones_ingreso_egreso()

def seleccionar_categoria(monto,divisa,count):
    limpiar_ventana()
    ingreso_label = tk.Label(root,text="Por favor seleccione una de las categoria",bg='#98FB98',font=("RomanD", 25),anchor='center')
    ingreso_label.pack(fill='both', expand=True)
    categoria_label1 = tk.Label(root, text="1.Salud")
    categoria_label1.pack()
    categoria_label2 = tk.Label(root, text="2.Vivienda")
    categoria_label2.pack()
    categoria_label3 = tk.Label(root, text="3.Educación")
    categoria_label3.pack()
    categoria_label4 = tk.Label(root, text="4.Alimentación")
    categoria_label4.pack()
    categoria_label5 = tk.Label(root, text="5.Transporte")
    categoria_label5.pack()
    categoria_label6 = tk.Label(root, text="6.Alquiler")
    categoria_label6.pack()
    categoria_label7 = tk.Label(root, text="7.hipoteca")
    categoria_label7.pack()
    categoria_label8 = tk.Label(root, text="8.ahorros")
    categoria_label8.pack()
    categoria_label9 = tk.Label(root, text="9.Alimentación")
    categoria_label9.pack()
    categoria_label10 = tk.Label(root, text="10.otros")
    categoria_label10.pack()
    categoria_label = tk.Label(root, text="Categoría:")
    categoria_label.pack()
    categoria_entry = tk.Entry(root)
    categoria_entry.pack()

    guardar_button = ttk.Button(root, text="Guardar",command=lambda: funciones_combinadas(monto, categoria_entry.get(), divisa, count))
    guardar_button.pack()

    root.mainloop()

def seleccionar_ingreso_egreso(opcion):
    limpiar_ventana()
    if opcion == "Ingreso":
        ingreso_label = tk.Label(root, text="Por favor ingrese los detalles del ingreso", bg='#98FB98', font=("RomanD", 25), anchor='center')
        ingreso_label.pack(fill='both', expand=True)

        monto_label = tk.Label(root, text="Monto:")
        monto_label.pack()
        monto_entry = tk.Entry(root)
        monto_entry.pack()

        guardar_button = ttk.Button(root, text="Guardar", command=lambda: seleccionar_categoria(monto_entry.get(),divisa,count=1))
        guardar_button.pack()

    else:
        egreso_label = tk.Label(root, text="Por favor ingrese los detalles del egreso", bg='#98FB98', font=("RomanD", 25), anchor='center')
        egreso_label.pack(fill='both', expand=True)

        monto_label = tk.Label(root, text="Monto:")
        monto_label.pack()
        monto_entry = tk.Entry(root)
        monto_entry.pack()

        guardar_button = ttk.Button(root, text="Guardar", command=lambda:seleccionar_categoria(monto_entry.get(), divisa,count=0))
        guardar_button.pack()

    root.mainloop()

def mostrar_opciones_ingreso_egreso():
    limpiar_ventana()
    mostrar_grafica_circular()
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

def seleccionar_divisa(divisas):
    global divisa
    if divisas == "USD":
        divisa = "USD"
    else:
        divisa = "COP"
    print(f"Divisa seleccionada: {divisas}")
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


