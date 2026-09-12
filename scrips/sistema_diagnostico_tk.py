# ============================================================
# SISTEMA DE DIAGNOSTICO DE EQUIPOS - CON INTERFAZ GRAFICA
# ============================================================

import tkinter as tk
from datetime import datetime
import random

ventana = tk.Tk()
ventana.title("Sistema de diagnostico de equipos")
ventana.geometry("450x680")
ventana.configure(bg="#dceefb")

# esto hace que el usuario no pueda cambiar el tamaño de la ventana
ventana.resizable(False, False)


# ------------------------------------------------------------
# DATOS DEL USUARIO
# ------------------------------------------------------------

tk.Label(ventana, text="Nombre del usuario:", bg="#dceefb").pack()
entrada_nombre = tk.Entry(ventana, width=40)
entrada_nombre.pack()

tk.Label(ventana, text="Direccion:", bg="#dceefb").pack()
entrada_direccion = tk.Entry(ventana, width=40)
entrada_direccion.pack()


# ------------------------------------------------------------
# TIPO DE EQUIPO
# ------------------------------------------------------------

tk.Label(ventana, text="\nTipo de equipo:", bg="#dceefb").pack()

tipo_equipo_var = tk.StringVar()
tipo_equipo_var.set("Computadora de escritorio")

opciones_equipo = ["Computadora de escritorio", "Laptop", "All in One", "Servidor", "Otro"]

menu_tipo = tk.OptionMenu(ventana, tipo_equipo_var, *opciones_equipo)
menu_tipo.pack()


# ------------------------------------------------------------
# PREGUNTAS SI / NO
# ------------------------------------------------------------

electricidad_var = tk.StringVar()
electricidad_var.set("s")

enciende_var = tk.StringVar()
enciende_var.set("s")

imagen_var = tk.StringVar()
imagen_var.set("s")

sistema_var = tk.StringVar()
sistema_var.set("s")

rendimiento_var = tk.StringVar()
rendimiento_var.set("n")


def crear_pregunta(texto, variable):

    tk.Label(ventana, text=texto, bg="#dceefb").pack()

    fila = tk.Frame(ventana, bg="#dceefb")
    fila.pack()

    tk.Radiobutton(fila, text="Si", variable=variable, value="s", bg="#dceefb").pack(side="left")
    tk.Radiobutton(fila, text="No", variable=variable, value="n", bg="#dceefb").pack(side="left")


crear_pregunta("\n¿Tiene electricidad?", electricidad_var)
crear_pregunta("¿El equipo enciende?", enciende_var)
crear_pregunta("¿Muestra imagen?", imagen_var)
crear_pregunta("¿Inicia el sistema operativo?", sistema_var)
crear_pregunta("¿El equipo funciona con lentitud?", rendimiento_var)


# ------------------------------------------------------------
# CUADRO DONDE SE MUESTRA EL REPORTE
# ------------------------------------------------------------

texto_reporte = tk.Text(ventana, width=50, height=15, bg="white", fg="#003366")


# ------------------------------------------------------------
# FUNCION QUE GENERA EL DIAGNOSTICO
# ------------------------------------------------------------

def generar_diagnostico():

    nombre = entrada_nombre.get()
    direccion = entrada_direccion.get()
    tipo_equipo = tipo_equipo_var.get()

    electricidad = electricidad_var.get()
    enciende = enciende_var.get()
    imagen = imagen_var.get()
    sistema = sistema_var.get()
    rendimiento = rendimiento_var.get()

    if nombre == "":
        texto_reporte.delete("1.0", tk.END)
        texto_reporte.insert(tk.END, "Debe escribir el nombre del usuario.")
        texto_reporte.pack()
        return

    # numero de reporte
    numero = random.randint(10000, 99999)
    numero_reporte = "REP-" + str(numero)

    # fecha y hora
    fecha_hora = datetime.now()
    fecha = fecha_hora.strftime("%d/%m/%Y")
    hora = fecha_hora.strftime("%H:%M")

    # decidir el diagnostico
    if electricidad == "n":
        diagnostico = "Revisar alimentacion electrica."
        recomendacion = "Verificar cable, contacto electrico, regulador o fuente de alimentacion."
        nivel = "ALTA"

    elif enciende == "n":
        diagnostico = "El equipo recibe electricidad pero no enciende."
        recomendacion = "Revisar fuente de poder, bateria, boton de encendido o tarjeta madre."
        nivel = "ALTA"

    elif imagen == "n":
        diagnostico = "El equipo enciende pero no muestra imagen."
        recomendacion = "Revisar monitor, cable de video, memoria RAM o tarjeta grafica."
        nivel = "MEDIA"

    elif sistema == "n":
        diagnostico = "El equipo muestra imagen pero no inicia el sistema operativo."
        recomendacion = "Revisar disco, sistema operativo, memoria RAM o configuracion de arranque."
        nivel = "MEDIA"

    elif rendimiento == "s":
        diagnostico = "El equipo funciona pero presenta bajo rendimiento."
        recomendacion = "Revisar memoria RAM, almacenamiento, programas en ejecucion y malware."
        nivel = "BAJA"

    else:
        diagnostico = "Funcionamiento basico correcto."
        recomendacion = "No se detectaron problemas basicos."
        nivel = "NORMAL"

    # mensaje extra segun el nivel
    if nivel == "ALTA":
        mensaje_nivel = "Es urgente, hay que revisarlo pronto"
    elif nivel == "MEDIA":
        mensaje_nivel = "No es tan urgente pero hay que revisarlo"
    elif nivel == "BAJA":
        mensaje_nivel = "No es urgente, es preventivo"
    else:
        mensaje_nivel = "El equipo esta bien"

    # estadisticas guardadas en un archivo de texto
    nombre_lower = nombre.lower()

    try:
        archivo = open("reportes.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
    except:
        lineas = []

    total_reportes = len(lineas) + 1

    primera_vez = "si"

    for linea in lineas:
        if nombre_lower in linea:
            primera_vez = "no"

    archivo = open("reportes.txt", "a")
    archivo.write(nombre_lower + "\n")
    archivo.close()

    # armar el texto del reporte
    reporte = ""
    reporte = reporte + "REPORTE DE SERVICIO\n"
    reporte = reporte + "==========================================\n"
    reporte = reporte + "Numero de reporte : " + numero_reporte + "\n"
    reporte = reporte + "Fecha             : " + fecha + "\n"
    reporte = reporte + "Hora              : " + hora + "\n"
    reporte = reporte + "------------------------------------------\n"
    reporte = reporte + "USUARIO\n"
    reporte = reporte + "Nombre    : " + nombre + "\n"
    reporte = reporte + "Direccion : " + direccion + "\n"
    reporte = reporte + "------------------------------------------\n"
    reporte = reporte + "EQUIPO\n"
    reporte = reporte + "Tipo de equipo : " + tipo_equipo + "\n"
    reporte = reporte + "------------------------------------------\n"
    reporte = reporte + "DIAGNOSTICO\n"
    reporte = reporte + "Resultado     : " + diagnostico + "\n"
    reporte = reporte + "Nivel         : " + nivel + "\n"
    reporte = reporte + "Recomendacion : " + recomendacion + "\n"
    reporte = reporte + "Comentario    : " + mensaje_nivel + "\n"
    reporte = reporte + "------------------------------------------\n"
    reporte = reporte + "ESTADISTICAS\n"
    reporte = reporte + "Total de reportes hechos : " + str(total_reportes) + "\n"
    reporte = reporte + "Es su primer reporte?    : " + primera_vez + "\n"
    reporte = reporte + "==========================================\n"

    texto_reporte.delete("1.0", tk.END)
    texto_reporte.insert(tk.END, reporte)
    texto_reporte.pack()


# ------------------------------------------------------------
# BOTON PARA GENERAR EL REPORTE
# ------------------------------------------------------------

boton = tk.Button(
    ventana,
    text="Generar diagnostico",
    command=generar_diagnostico,
    bg="#3399ff",
    fg="white"
)
boton.pack(pady=10)

texto_reporte.pack()

ventana.mainloop()
