import tkinter as tk
from tkinter import messagebox
import random
from datetime import date, timedelta

# ============================================
# VARIABLES GLOBALES (guardan los datos entre ventanas)
# ============================================

nombre_paciente = ""
direccion_paciente = ""
edad_paciente = ""

fiebre = ""
tos = ""
dolor = ""
diagnostico = ""

q = r = s = t = sistolica = diastolica = imc = 0
alertas = []
prioridad = ""
especialidad = ""
fecha_cita = None
hora_cita = ""


# ============================================
# VENTANA 1: DATOS DEL PACIENTE
# ============================================

def pantalla_datos():
    ventana = tk.Tk()
    ventana.title("Datos del paciente")
    ventana.geometry("400x350")
    ventana.resizable(False, False)
    ventana.config(bg="#cfe8f3")

    tk.Label(ventana, text="DATOS DEL PACIENTE", font=("Arial", 14, "bold"),
             bg="#cfe8f3", fg="#0b3d5c").pack(pady=15)

    tk.Label(ventana, text="Nombre completo:", bg="#cfe8f3").pack()
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.pack(pady=5)

    tk.Label(ventana, text="Dirección:", bg="#cfe8f3").pack()
    entry_direccion = tk.Entry(ventana, width=30)
    entry_direccion.pack(pady=5)

    tk.Label(ventana, text="Edad:", bg="#cfe8f3").pack()
    entry_edad = tk.Entry(ventana, width=10)
    entry_edad.pack(pady=5)

    def siguiente():
        global nombre_paciente, direccion_paciente, edad_paciente

        nombre_paciente = entry_nombre.get()
        direccion_paciente = entry_direccion.get()
        edad_paciente = entry_edad.get()

        if nombre_paciente.strip() == "" or direccion_paciente.strip() == "" or edad_paciente.strip() == "":
            messagebox.showerror("Error", "Debes llenar todos los campos")
            return

        if not edad_paciente.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número")
            return

        ventana.destroy()
        pantalla_diagnostico()

    tk.Button(ventana, text="Siguiente", bg="#0b3d5c", fg="white",
              command=siguiente).pack(pady=25)

    ventana.mainloop()


# ============================================
# VENTANA 2: DIAGNÓSTICO
# ============================================

def pantalla_diagnostico():
    ventana = tk.Tk()
    ventana.title("Sistema de diagnóstico")
    ventana.geometry("400x400")
    ventana.resizable(False, False)
    ventana.config(bg="#fff3cd")

    tk.Label(ventana, text="SISTEMA DE DIAGNÓSTICO", font=("Arial", 14, "bold"),
             bg="#fff3cd", fg="#7a5c00").pack(pady=15)

    fiebre_var = tk.StringVar(value="n")
    tos_var = tk.StringVar(value="n")
    dolor_var = tk.StringVar(value="n")

    def crear_pregunta(texto, variable):
        tk.Label(ventana, text=texto, bg="#fff3cd").pack(pady=(10, 0))
        fila = tk.Frame(ventana, bg="#fff3cd")
        fila.pack()
        tk.Radiobutton(fila, text="Sí", variable=variable, value="s", bg="#fff3cd").pack(side="left")
        tk.Radiobutton(fila, text="No", variable=variable, value="n", bg="#fff3cd").pack(side="left")

    crear_pregunta("¿Tiene fiebre?", fiebre_var)
    crear_pregunta("¿Tiene tos?", tos_var)
    crear_pregunta("¿Tiene dolor de garganta?", dolor_var)

    def siguiente():
        global fiebre, tos, dolor, diagnostico

        fiebre = fiebre_var.get()
        tos = tos_var.get()
        dolor = dolor_var.get()

        if fiebre == "s" and tos == "s":
            diagnostico = "Posible infección respiratoria"
        elif tos == "s" and dolor == "s":
            diagnostico = "Posible irritación respiratoria"
        elif fiebre == "s":
            diagnostico = "Se recomienda valoración profesional"
        else:
            diagnostico = "No se identificó un patrón"

        ventana.destroy()
        pantalla_signos_vitales()

    tk.Button(ventana, text="Siguiente", bg="#7a5c00", fg="white",
              command=siguiente).pack(pady=25)

    ventana.mainloop()


# ============================================
# VENTANA 3: SIGNOS VITALES
# ============================================

def pantalla_signos_vitales():
    ventana = tk.Tk()
    ventana.title("Signos vitales")
    ventana.geometry("400x450")
    ventana.resizable(False, False)
    ventana.config(bg="#e2d9f3")

    tk.Label(ventana, text="SIGNOS VITALES", font=("Arial", 14, "bold"),
             bg="#e2d9f3", fg="#3b1e66").pack(pady=15)

    def crear_campo(texto):
        tk.Label(ventana, text=texto, bg="#e2d9f3").pack(pady=(8, 0))
        entrada = tk.Entry(ventana, width=15)
        entrada.pack()
        return entrada

    entry_q = crear_campo("Frecuencia cardiaca (lpm):")
    entry_r = crear_campo("Oxigenación / SpO2 (%):")
    entry_s = crear_campo("Peso (kg):")
    entry_t = crear_campo("Talla (m):")

    tk.Label(ventana, text="Presión arterial (sistólica / diastólica):", bg="#e2d9f3").pack(pady=(8, 0))
    fila_pa = tk.Frame(ventana, bg="#e2d9f3")
    fila_pa.pack()
    entry_pa_sist = tk.Entry(fila_pa, width=6)
    entry_pa_sist.pack(side="left")
    tk.Label(fila_pa, text="/", bg="#e2d9f3").pack(side="left")
    entry_pa_dias = tk.Entry(fila_pa, width=6)
    entry_pa_dias.pack(side="left")

    def generar_reporte():
        global q, r, s, t, sistolica, diastolica, imc
        global alertas, prioridad, especialidad, fecha_cita, hora_cita

        try:
            q = float(entry_q.get())
            r = float(entry_r.get())
            s = float(entry_s.get())
            t = float(entry_t.get())
            sistolica = float(entry_pa_sist.get())
            diastolica = float(entry_pa_dias.get())
        except ValueError:
            messagebox.showerror("Error", "Todos los signos vitales deben ser números")
            return

        imc = s / (t ** 2)
        alertas = []

        if q < 60 or q > 100:
            alertas.append("Frecuencia cardiaca fuera de rango normal")

        if r < 90:
            alertas.append("Oxigenación crítica")
        elif r < 95:
            alertas.append("Oxigenación por debajo de lo normal")

        if imc < 18.5 or imc > 24.9:
            alertas.append("Índice de masa corporal fuera de rango normal")

        if sistolica > 140 or diastolica > 90:
            alertas.append("Presión arterial elevada")
        elif sistolica < 90 or diastolica < 60:
            alertas.append("Presión arterial baja")

        riesgo_alto = (r < 90) or (sistolica > 140 or diastolica > 90) or (q > 120 or q < 50)
        riesgo_medio = len(alertas) > 0 and not riesgo_alto

        if riesgo_alto:
            prioridad = "Alta"
        elif riesgo_medio or diagnostico == "Posible infección respiratoria":
            prioridad = "Media"
        else:
            prioridad = "Normal"

        if diagnostico == "Posible infección respiratoria":
            especialidad = "Neumología"
        elif diagnostico == "Posible irritación respiratoria":
            especialidad = "Otorrinolaringología"
        elif diagnostico == "Se recomienda valoración profesional":
            especialidad = "Medicina General"
        else:
            especialidad = "Medicina General"

        hoy = date.today()
        hora_cita = f"{random.randint(7, 17):02d}:{random.choice(['00', '15', '30', '45'])}"

        if prioridad in ("Media", "Alta"):
            fecha_cita = hoy
        else:
            dias_adelante = random.randint(2, 15)
            fecha_cita = hoy + timedelta(days=dias_adelante)

        ventana.destroy()
        pantalla_reporte()

    tk.Button(ventana, text="Generar Reporte", bg="#3b1e66", fg="white",
              command=generar_reporte).pack(pady=25)

    ventana.mainloop()


# ============================================
# VENTANA 4: REPORTE FINAL
# ============================================

def pantalla_reporte():
    ventana = tk.Tk()
    ventana.title("Reporte de atención")
    ventana.geometry("450x520")
    ventana.resizable(False, False)
    ventana.config(bg="#d9f2e3")

    tk.Label(ventana, text="REPORTE DE ATENCIÓN", font=("Arial", 14, "bold"),
             bg="#d9f2e3", fg="#155724").pack(pady=15)

    texto = tk.Text(ventana, width=50, height=22, bg="white", fg="#155724")
    texto.pack(padx=10, pady=5)

    lineas = []
    lineas.append(f"Nombre del paciente : {nombre_paciente}")
    lineas.append(f"Edad                : {edad_paciente}")
    lineas.append(f"Dirección           : {direccion_paciente}")
    lineas.append("")
    lineas.append("Signos vitales:")
    lineas.append(f"  Frecuencia cardiaca : {q} lpm")
    lineas.append(f"  Oxigenación (SpO2)  : {r} %")
    lineas.append(f"  Peso                : {s} kg")
    lineas.append(f"  Talla               : {t} m")
    lineas.append(f"  IMC                 : {imc:.2f}")
    lineas.append(f"  Presión arterial    : {sistolica}/{diastolica} mmHg")
    lineas.append("")

    if alertas:
        lineas.append("Alertas detectadas:")
        for a in alertas:
            lineas.append(f"  - {a}")
    else:
        lineas.append("Alertas detectadas: Ninguna")

    lineas.append("")
    lineas.append(f"Diagnóstico         : {diagnostico}")
    lineas.append(f"Prioridad           : {prioridad}")
    lineas.append(f"Remitido a          : {especialidad}")
    lineas.append(f"Fecha de la cita    : {fecha_cita.strftime('%d/%m/%Y')}")
    lineas.append(f"Hora de la cita     : {hora_cita}")

    texto.insert(tk.END, "\n".join(lineas))
    texto.config(state="disabled")

    tk.Button(ventana, text="Salir", bg="#155724", fg="white",
              command=ventana.destroy).pack(pady=15)

    ventana.mainloop()


# ============================================
# INICIO DEL PROGRAMA
# ============================================

pantalla_datos()
