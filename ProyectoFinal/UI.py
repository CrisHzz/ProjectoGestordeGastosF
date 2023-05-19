import tkinter as tk
from datetime import date
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

hoy = date.today()

from DesarolloLogico import Perfil, IngresoCatalogado,  EgresoCatalogado


def ver_habituales(count=0,count1=0):
    limpiar_ventana()
    with open('ingreso_habitual.csv', 'r') as file:
        for line in file:
            linea = line.split(',')
            if int(linea[0]) < 0 :
                label = tk.Label(root,text="egreso:"+str(linea[0][1:])+"  fecha:"+linea[1]+"/"+linea[2]+"/"+linea[3]+"  categoria: "+linea[4],width=50, height=2,bg="lightblue",font=("Arial", 12))
                label.grid(row=count, column=3,pady=0)
                count += 1
            else:
                label = tk.Label(root, text="ingresos:" + str(linea[0]) + "  fecha:" + linea[1] + "/" +linea[2] + "/" +linea[3] + "  categoria: " +linea[4],width=50, height=2,bg="lightblue",font=("Arial", 12))
                label.grid(row=count1, column=1, pady=0)
                count1 += 1
    volver_button = tk.Button(root, text="Regresar", width=15,height=4, font=("Arial", 13),command=lambda: mostrar_opciones_ingreso_egreso())
    volver_button.grid(row=10, column=2, padx=10, pady=20)
    root.mainloop()

def registrar_pago_habitual(categoria,cantidad,tipo):

    with open('ingreso_habitual.csv', 'a') as file:
        if tipo :
            if categoria :
                file.write(f'{cantidad},{hoy.day},{hoy.month},{hoy.year},{"Habitual Mes"}\n')
            else:
                file.write(f'{cantidad},{hoy.day},{hoy.month},{hoy.year},{"Habitual Semana"}\n')
        else:
            if categoria:
                file.write(f'{int(cantidad)*-1},{hoy.day},{hoy.month},{hoy.year},{"Habitual Mes"}\n')
            else:
                file.write(f'{int(cantidad)*-1},{hoy.day},{hoy.month},{hoy.year},{"Habitual Semana"}\n')
    mostrar_opciones_ingreso_egreso()

def crear_pago_habitual(tipo):
    limpiar_ventana()
    label = tk.Label(root,text="digite la cantidad y\n seleccione el tipo:",width=20, height=5, bg="lightblue",font=("Arial", 20))
    label.grid(row=0, column=2)

    monto_label = tk.Label(root, text="Monto:", width=25,font=("Arial", 13),bg="lightblue")
    monto_label.grid(row=2, column=2, pady=10)
    monto_entry = tk.Entry(root, width=25,font=("Arial", 13))
    monto_entry.grid(row=3, column=2, pady=10)

    agregar_button = tk.Button(root,text="ingreso",bg="lightblue",width=25, height=5,font=("Arial", 13),command=lambda: registrar_pago_habitual(tipo,monto_entry.get(),True))
    agregar_button.grid(row=4, column=2, padx=10,pady=10, ipadx=20, ipady=10)

    agregar_button = tk.Button(root,text="egreso",bg="lightblue",width=25, height=5,font=("Arial", 13),command=lambda: registrar_pago_habitual(tipo,monto_entry.get(),False))
    agregar_button.grid(row=5, column=2, padx=10,pady=10, ipadx=20, ipady=10)

    root.mainloop()

def agregar_pago_habitual():
    limpiar_ventana()
    label = tk.Label(root,text="seleccione la \nfrecuencia del pago:",width=30, height=5, bg="lightblue",font=("Arial", 20))
    label.grid(row=0, column=2)


    agregar_button1 = tk.Button(root,text="cada mes",bg="lightblue",width=25, height=5,font=("Arial", 13),command=lambda: crear_pago_habitual(True))
    agregar_button1.grid(row=2, column=2, padx=10,pady=10, ipadx=20, ipady=10)

    agregar_button2 = tk.Button(root,text="cada semana",bg="lightblue",width=25, height=5,font=("Arial", 13),command=lambda: crear_pago_habitual(False))
    agregar_button2.grid(row=4, column=2, padx=10,pady=10, ipadx=20, ipady=10)

    root.mainloop()

def pagos_habituales():
    limpiar_ventana()
    label = tk.Label(root,text="seleccione una\n opcion:",width=20, height=5, bg="lightblue",font=("Arial", 20))
    label.grid(row=0, column=2)

    agregar_button = tk.Button(root,text="agregar pago habitual",bg="lightblue",width=25, height=5,font=("Arial", 13),command=lambda: agregar_pago_habitual())
    agregar_button.grid(row=1, column=2, padx=10,pady=10,)

    agregar_button = tk.Button(root,text="ver pagos habituales",bg="lightblue",width=25, height=5,font=("Arial", 13),command=lambda: ver_habituales())
    agregar_button.grid(row=2, column=2, padx=10,pady=10,)

    root.mainloop()

def guardar_ingreso(monto,categoria, divisa):

    ingreso_catalogado = IngresoCatalogado(monto, hoy.day, hoy.month, hoy.year, divisa, categoria)
    ingreso_catalogado.guardar_ingreso(divisa)

def guardar_egreso(monto, categoria, divisa):
    egreso = EgresoCatalogado(monto, hoy.day, hoy.month, hoy.year, divisa, categoria)
    egreso.guardar(divisa)

def botones(monto,divisa,count):
    limpiar_ventana()
    root.configure(bg="lightblue")
    label = tk.Label(root, text="seleccione una\n categoria:",width=20,height=5,bg="lightblue",font=("Arial", 20))
    label.grid(row=0, column=2)
    salud_button = tk.Button(root, text="Salud",width=25,height=5,font=("Arial", 15),command=lambda: funciones_combinadas(monto, "Salud", divisa,count))
    vivienda_button = tk.Button(root, text="Vivivenda",width=25,height=5,font=("Arial", 15),command=lambda: funciones_combinadas(monto, "Vivienda", divisa,count))
    educacion_button = tk.Button(root, text="Educacion",width=25,height=5,font=("Arial", 15),command=lambda: funciones_combinadas(monto, "Educacion", divisa,count))
    alimentacion_button = tk.Button(root, text="Alimentacion",width=25,height=5,font=("Arial", 15),command=lambda: funciones_combinadas(monto, "Alimentacion", divisa,count))
    otros_button = tk.Button(root, text="Otros",width=25,height=5,font=("Arial", 15),command=lambda: funciones_combinadas(monto, "Otros", divisa,count))
    alquiler_button = tk.Button(root, text="Alquiler",width=25,height=5,font=("Arial", 15),command=lambda: funciones_combinadas(monto, "Alquiler",divisa, count))
    hipoteca_button = tk.Button(root, text="Hipoteca",width=25,height=5,font=("Arial", 15),command=lambda: funciones_combinadas(monto, "hipoteca", divisa,count))
    ahorros_button = tk.Button(root, text="Ahorros",width=25,height=5,font=("Arial", 15),command=lambda: funciones_combinadas(monto, "Ahorros", divisa,count))
    deudas_button = tk.Button(root, text="Deudas",width=25,height=5,font=("Arial", 15),command=lambda: funciones_combinadas(monto, "Deudas", divisa,count))
    salud_button.grid(row=1, column=1,padx=10, pady=20)
    vivienda_button.grid(row=1, column=2,padx=10, pady=20)
    educacion_button.grid(row=1, column=3,padx=10, pady=20)
    alimentacion_button.grid(row=2, column=1,padx=10, pady=20)
    otros_button.grid(row=2, column=2,padx=10, pady=20)
    alquiler_button.grid(row=2, column=3,padx=10, pady=20)
    hipoteca_button.grid(row=3, column=1,padx=10, pady=20)
    ahorros_button.grid(row=3, column=2,padx=10, pady=20)
    deudas_button.grid(row=3, column=3,padx=10, pady=20)
    root.mainloop()
def ver_movimientos(count=0,count1=0):
    limpiar_ventana()
    with open('balance.csv', 'r') as file:
        for line in file:
            linea = line.split(',')
            if int(linea[0]) < 0 :
                label = tk.Label(root,text="egreso:"+str(linea[0][1:])+"  fecha:"+linea[1]+"/"+linea[2]+"/"+linea[3]+"  categoria: "+linea[4],width=50, height=2,bg="lightblue",font=("Arial", 12))
                label.grid(row=count, column=3,pady=0)
                count += 1
            else:
                label = tk.Label(root, text="ingresos:" + str(linea[0]) + "  fecha:" + linea[1] + "/" +linea[2] + "/" +linea[3] + "  categoria: " +linea[4],width=50, height=2,bg="lightblue",font=("Arial", 12))
                label.grid(row=count1, column=1, pady=0)
                count1 += 1
    volver_button = tk.Button(root, text="Regresar", width=15,height=4, font=("Arial", 13),command=lambda: mostrar_opciones_ingreso_egreso())
    volver_button.grid(row=10, column=2, padx=10, pady=20)
    root.mainloop()
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
    grafica_circular.pie(valores, labels=etiquetas,autopct='%1.1f%%')
    lienzo = FigureCanvasTkAgg(figura, master=root)
    lienzo.draw()


    lienzo.get_tk_widget().pack()

def funciones_combinadas(monto, categoria, divisa,count):
    if count == 1:
        guardar_ingreso(monto, categoria, divisa)
    else:
        guardar_egreso(monto, categoria, divisa)
    mostrar_opciones_ingreso_egreso()

def seleccionar_ingreso_egreso(opcion):
    limpiar_ventana()
    if opcion == "Ingreso":
        ingreso_label = tk.Label(root, text="Por favor ingrese los\ndetalles del ingreso", bg='lightblue', font=("RomanD", 18), width=18)
        ingreso_label.grid(row=1, column=2)

        monto_label = tk.Label(root, text="Monto:",width=25,font=("Arial", 13),bg="lightblue")
        monto_label.grid(row=4, column=2,pady=10)
        monto_entry = tk.Entry(root,width=25,font=("Arial", 13))
        monto_entry.grid(row=5, column=2,pady=10)

        guardar_button = tk.Button(root, text="siguiente",width=25,height=5,font=("Arial", 13), command=lambda: botones(monto_entry.get(),divisa,count=1))
        guardar_button.grid(row=9, column=2, pady=10)

        volver_button = tk.Button(root, text="Regresar",width=25,height=5,font=("Arial", 13),command=lambda: mostrar_opciones_ingreso_egreso())
        volver_button.grid(row=10, column=2, pady=10)


    else:
        egreso_label = tk.Label(root,text="Por favor ingrese los\ndetalles del egreso",bg='lightblue',font=("RomanD", 18),width=18)
        egreso_label.grid(row=1, column=10,ipadx=20, ipady=10)

        monto_label = tk.Label(root, text="Monto:",width=25, font=("Arial", 13),bg="lightblue")
        monto_label.grid(row=4, column=10, pady=10)
        monto_entry = tk.Entry(root, width=25,font=("Arial", 13))
        monto_entry.grid(row=5, column=10, pady=10,ipadx=20, ipady=10)

        guardar_button = tk.Button(root, text="siguiente",width=25, height=5,font=("Arial", 13),command=lambda: botones(monto_entry.get(),divisa, count=0))
        guardar_button.grid(row=9, column=10, pady=10,ipadx=20, ipady=10)

        volver_button = tk.Button(root, text="Regresar",width=25, height=5,font=("Arial", 13),command=lambda: mostrar_opciones_ingreso_egreso())
        volver_button.grid(row=10, column=10, pady=10,ipadx=20, ipady=10)

    root.mainloop()

def mostrar_opciones_ingreso_egreso():
    limpiar_ventana()
    mostrar_grafica_circular()
    ingreso_egreso_label = tk.Label(root, text="¿Desea ingresar un ingreso o un egreso?", bg='lightblue', font=("RomanD", 25), anchor='center')
    ingreso_egreso_label.pack(fill='both', expand=True)

    button_frame = tk.Frame(root)
    button_frame.pack()

    ingreso_button = tk.Button(button_frame, text="Ingreso",bg="lightblue",width=25,height=5,font=("Arial", 13), command=lambda: seleccionar_ingreso_egreso("Ingreso"))
    ingreso_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

    egreso_button = tk.Button(button_frame, text="Egreso",bg="lightblue",width=25,height=5,font=("Arial", 13), command=lambda: seleccionar_ingreso_egreso("Egreso"))
    egreso_button.grid(row=0, column=2, padx=10, pady=10, ipadx=20, ipady=10)

    verMovimientos_button = tk.Button(button_frame, text="Ver movimientos",bg="lightblue",width=25,height=5,font=("Arial", 13),command=lambda: ver_movimientos())
    verMovimientos_button.grid(row=0, column=1, padx=10, pady=10,ipadx=20, ipady=10)

    habituales_button = tk.Button(button_frame,text="Pagos habituales",bg="lightblue",width=25, height=5,font=("Arial", 13),command=lambda: pagos_habituales())
    habituales_button.grid(row=0, column=1, padx=10,pady=10, ipadx=20, ipady=10)

    root.mainloop()




def mostrar_opciones_divisa():
    limpiar_ventana()
    divisa_label = tk.Label(root, text="Por favor seleccione la divisa", bg='lightblue', font=("RomanD", 25), anchor='center')
    divisa_label.pack(fill='both', expand=True)

    button_frame = tk.Frame(root)
    button_frame.pack()

    usd_button = tk.Button(button_frame, text="USD",width=25, height=5,font=("Arial", 13), command=lambda: seleccionar_divisa("USD"))
    usd_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

    cop_button = tk.Button(button_frame, text="COP",width=25, height=5,font=("Arial", 13), command=lambda: seleccionar_divisa("COP"))
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
root.configure(bg="lightblue")

welcome_label = tk.Label(root, text="¡Bienvenido usuario a este gestor de gastos!\n \n \n Porfavor seleccione el perfil para su cuenta", bg='lightblue', font=("RomanD", 25), anchor='center')
welcome_label.pack(fill='both', expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

jubilado_button = tk.Button(button_frame, text="Jubilado",width=25, height=5,font=("Arial", 13), command=lambda: seleccionar_perfil("jubilado"))
jubilado_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

estudiante_button = tk.Button(button_frame, text="Estudiante",width=25, height=5,font=("Arial", 13), command=lambda: seleccionar_perfil("estudiante"))
estudiante_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=10)

trabajador_button = tk.Button(button_frame, text="Trabajador",width=25, height=5,font=("Arial", 13), command=lambda: seleccionar_perfil("trabajador"))
trabajador_button.grid(row=0, column=2, padx=10, pady=10, ipadx=20, ipady=10)

root.mainloop()


