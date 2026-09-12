import random
from datetime import date, timedelta

# ============================================
# SISTEMA EXPERTO DE DIAGNÓSTICO
# ============================================

print("SISTEMA DE DIAGNÓSTICO")

# ============================================
# DATOS DEL PACIENTE
# ============================================

print("\nDATOS DEL PACIENTE")

nombre_paciente = input("Nombre completo del paciente: ")
direccion_paciente = input("Dirección del paciente: ")
edad_paciente = input("Edad del paciente: ")

fiebre = input("¿Tiene fiebre? (s/n): ")
tos = input("¿Tiene tos? (s/n): ")
dolor = input("¿Tiene dolor de garganta? (s/n): ")

if fiebre == "s" and tos == "s":

    diagnostico = "Posible infección respiratoria"

elif tos == "s" and dolor == "s":

    diagnostico = "Posible irritación respiratoria"

elif fiebre == "s":

    diagnostico = "Se recomienda valoración profesional"

else:

    diagnostico = "No se identificó un patrón"

print("\nResultado:")
print(diagnostico)


#Implementación de mejores decisiones para un mejor resultado.


# ============================================
# SIGNOS VITALES
# ============================================
# q  = frecuencia cardiaca (lpm)
# r  = oxigenación / SpO2 (%)
# s  = peso (kg)
# t  = talla (m)
# pa = presión arterial (formato sistólica/diastólica, ej. 120/80)

print("\nSIGNOS VITALES")

q = float(input("Frecuencia cardiaca (lpm): "))
r = float(input("Oxigenación / SpO2 (%): "))
s = float(input("Peso (kg): "))
t = float(input("Talla (m): "))
while True:
    pa = input("Presión arterial (sistólica/diastólica, ej. 120/80): ")
    partes_pa = pa.split("/")
    if len(partes_pa) == 2 and partes_pa[0].strip().isdigit() and partes_pa[1].strip().isdigit():
        sistolica = float(partes_pa[0])
        diastolica = float(partes_pa[1])
        break
    else:
        print("Formato inválido. Debes escribirlo como sistólica/diastólica, ejemplo: 120/80")

imc = s / (t ** 2)

# ------------------------------------------------
# COMPARACIÓN DE SIGNOS VITALES CONTRA RANGOS NORMALES
# ------------------------------------------------

alertas = []

# Frecuencia cardiaca normal: 60 - 100 lpm
if q < 60 or q > 100:
    alertas.append("Frecuencia cardiaca fuera de rango normal")

# Oxigenación normal: 95% - 100%
if r < 90:
    alertas.append("Oxigenación crítica")
elif r < 95:
    alertas.append("Oxigenación por debajo de lo normal")

# IMC normal: 18.5 - 24.9
if imc < 18.5 or imc > 24.9:
    alertas.append("Índice de masa corporal fuera de rango normal")

# Presión arterial normal: 90/60 - 120/80
if sistolica > 140 or diastolica > 90:
    alertas.append("Presión arterial elevada")
elif sistolica < 90 or diastolica < 60:
    alertas.append("Presión arterial baja")

# ============================================
# DETERMINAR PRIORIDAD Y ESPECIALIDAD DE REMISIÓN
# ============================================

# Prioridad según signos vitales críticos
riesgo_alto = (r < 90) or (sistolica > 140 or diastolica > 90) or (q > 120 or q < 50)
riesgo_medio = len(alertas) > 0 and not riesgo_alto

if riesgo_alto:
    prioridad = "Alta"
elif riesgo_medio or diagnostico == "Posible infección respiratoria":
    prioridad = "Media"
else:
    prioridad = "Normal"

# Especialidad de remisión según el diagnóstico
if diagnostico == "Posible infección respiratoria":
    especialidad = "Neumología"
elif diagnostico == "Posible irritación respiratoria":
    especialidad = "Otorrinolaringología"
elif diagnostico == "Se recomienda valoración profesional":
    especialidad = "Medicina General"
else:
    especialidad = "Medicina General"

# ============================================
# ASIGNACIÓN DE CITA (ALEATORIA)
# ============================================

hoy = date.today()
hora_cita = f"{random.randint(7, 17):02d}:{random.choice(['00', '15', '30', '45'])}"

if prioridad in ("Media", "Alta"):
    # Cita para el mismo día
    fecha_cita = hoy
else:
    # Cita normal: se asigna aleatoriamente para otro día (entre 2 y 15 días después)
    dias_adelante = random.randint(2, 15)
    fecha_cita = hoy + timedelta(days=dias_adelante)

# ============================================
# REPORTE FINAL
# ============================================

print("\n" + "=" * 45)
print("REPORTE DE ATENCIÓN")
print("=" * 45)
print(f"Nombre del paciente : {nombre_paciente}")
print(f"Edad                : {edad_paciente}")
print(f"Dirección           : {direccion_paciente}")
print("\nSignos vitales:")
print(f"  Frecuencia cardiaca : {q} lpm")
print(f"  Oxigenación (SpO2)  : {r} %")
print(f"  Peso                : {s} kg")
print(f"  Talla               : {t} m")
print(f"  IMC                 : {imc:.2f}")
print(f"  Presión arterial    : {pa} mmHg")

if alertas:
    print("\nAlertas detectadas:")
    for a in alertas:
        print(f"  - {a}")
else:
    print("\nAlertas detectadas: Ninguna")

print(f"\nDiagnóstico         : {diagnostico}")
print(f"Prioridad           : {prioridad}")
print(f"Remitido a          : {especialidad}")
print(f"Fecha de la cita    : {fecha_cita.strftime('%d/%m/%Y')}")
print(f"Hora de la cita     : {hora_cita}")
print("=" * 45)
