# ============================================================
# SISTEMA BÁSICO DE DIAGNÓSTICO DE EQUIPOS DE CÓMPUTO
# ============================================================
# Objetivo:
# Recibir información del usuario y del equipo,
# analizar diferentes condiciones y generar
# automáticamente un diagnóstico.
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTAR LIBRERÍAS
# ------------------------------------------------------------

# datetime permite obtener la fecha y hora actuales.
from datetime import datetime

# random permite generar un número aleatorio.
import random


# ------------------------------------------------------------
# 2. GENERAR NÚMERO DE REPORTE
# ------------------------------------------------------------

# Generamos un número aleatorio entre 10000 y 99999.
numero = random.randint(10000, 99999)

# Creamos el identificador del reporte.
numero_reporte = "REP-" + str(numero)


# ------------------------------------------------------------
# 3. OBTENER FECHA Y HORA
# ------------------------------------------------------------

# datetime.now() obtiene la fecha y hora actuales.
fecha_hora = datetime.now()

# Convertimos la fecha a un formato fácil de leer.
fecha = fecha_hora.strftime("%d/%m/%Y")

# Convertimos la hora a formato HH:MM.
hora = fecha_hora.strftime("%H:%M")


# ------------------------------------------------------------
# 4. DATOS DEL USUARIO
# ------------------------------------------------------------

print("\n==========================================")
print(" SISTEMA DE DIAGNÓSTICO DE EQUIPOS")
print("==========================================")

print("\nDATOS DEL USUARIO")

nombre = input("Nombre del usuario: ")

direccion = input("Dirección: ")


# ------------------------------------------------------------
# 5. DATOS DEL EQUIPO
# ------------------------------------------------------------

print("\nDATOS DEL EQUIPO")

print("\nSeleccione el tipo de equipo:")

print("1. Computadora de escritorio")
print("2. Laptop")
print("3. All in One")
print("4. Servidor")
print("5. Otro")

tipo_opcion = input("Seleccione una opción: ")


# ------------------------------------------------------------
# 6. CONVERTIR LA OPCIÓN EN UN TIPO DE EQUIPO
# ------------------------------------------------------------

if tipo_opcion == "1":
    tipo_equipo = "Computadora de escritorio"

elif tipo_opcion == "2":
    tipo_equipo = "Laptop"

elif tipo_opcion == "3":
    tipo_equipo = "All in One"

elif tipo_opcion == "4":
    tipo_equipo = "Servidor"

elif tipo_opcion == "5":
    tipo_equipo = input("Especifique el tipo de equipo: ")

else:
    tipo_equipo = "Tipo de equipo no especificado"


# ------------------------------------------------------------
# 7. RECIBIR INFORMACIÓN DEL EQUIPO
# ------------------------------------------------------------
# El paciente (usuario) debe contestar TODAS las preguntas,
# sin importar lo que haya respondido antes.

print("\n==========================================")
print(" DIAGNÓSTICO")
print("==========================================")

print("\nResponda utilizando S para Sí o N para No.")

# Pregunta 1: electricidad
electricidad = input("¿Tiene electricidad? (s/n): ").lower()

while electricidad not in ["s", "n"]:
    print("Respuesta no válida.")
    electricidad = input("Ingrese solamente s o n: ").lower()


# Pregunta 2: enciende
enciende = input("¿El equipo enciende? (s/n): ").lower()

while enciende not in ["s", "n"]:
    print("Respuesta no válida.")
    enciende = input("Ingrese solamente s o n: ").lower()


# Pregunta 3: imagen
imagen = input("¿Muestra imagen? (s/n): ").lower()

while imagen not in ["s", "n"]:
    print("Respuesta no válida.")
    imagen = input("Ingrese solamente s o n: ").lower()


# Pregunta 4: sistema operativo
sistema = input("¿Inicia el sistema operativo? (s/n): ").lower()

while sistema not in ["s", "n"]:
    print("Respuesta no válida.")
    sistema = input("Ingrese solamente s o n: ").lower()


# Pregunta 5: rendimiento
rendimiento = input("¿El equipo funciona con lentitud? (s/n): ").lower()

while rendimiento not in ["s", "n"]:
    print("Respuesta no válida.")
    rendimiento = input("Ingrese solamente s o n: ").lower()


# ------------------------------------------------------------
# 8. DECIDIR EL DIAGNÓSTICO
# ------------------------------------------------------------
# Ya que se contestaron todas las preguntas, ahora sí
# revisamos las respuestas en orden de importancia.

if electricidad == "n":

    diagnostico = "Revisar alimentación eléctrica."

    recomendacion = "Verificar cable, contacto eléctrico, regulador o fuente de alimentación."

    nivel = "ALTA"

elif enciende == "n":

    diagnostico = "El equipo recibe electricidad pero no enciende."

    recomendacion = "Revisar fuente de poder, batería, botón de encendido o tarjeta madre."

    nivel = "ALTA"

elif imagen == "n":

    diagnostico = "El equipo enciende pero no muestra imagen."

    recomendacion = "Revisar monitor, cable de video, memoria RAM o tarjeta gráfica."

    nivel = "MEDIA"

elif sistema == "n":

    diagnostico = "El equipo muestra imagen pero no inicia el sistema operativo."

    recomendacion = "Revisar disco, sistema operativo, memoria RAM o configuración de arranque."

    nivel = "MEDIA"

elif rendimiento == "s":

    diagnostico = "El equipo funciona pero presenta bajo rendimiento."

    recomendacion = "Revisar memoria RAM, almacenamiento, programas en ejecución y malware."

    nivel = "BAJA"

else:

    diagnostico = "Funcionamiento básico correcto."

    recomendacion = "No se detectaron problemas básicos."

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


# guardamos cuantos reportes van en un archivo de texto
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


# ------------------------------------------------------------
# 11. MOSTRAR REPORTE
# ------------------------------------------------------------

print("\n\n==========================================")
print("           REPORTE DE SERVICIO")
print("==========================================")

print("Número de reporte :", numero_reporte)

print("Fecha             :", fecha)

print("Hora              :", hora)

print("------------------------------------------")

print("USUARIO")

print("Nombre            :", nombre)

print("Dirección         :", direccion)

print("------------------------------------------")

print("EQUIPO")

print("Tipo de equipo    :", tipo_equipo)

print("------------------------------------------")

print("DIAGNÓSTICO")

print("Resultado          :", diagnostico)

print("Nivel              :", nivel)

print("Recomendación      :", recomendacion)

print("Comentario         :", mensaje_nivel)

print("------------------------------------------")

print("ESTADISTICAS")

print("Total de reportes hechos:", total_reportes)

print("Es su primer reporte?   :", primera_vez)

print("==========================================")

print("Fin del reporte.")
