import time
import random
from datetime import datetime


class AgenteClimatizacion:

    def __init__(self, archivo_log="clima_bitacora.txt"):
        self.temperatura = 0.0
        self.humedad = 0.0
        self.accion = ""
        self.archivo_log = archivo_log

#sensores

    def leer_sensores(self):
        """Simula lecturas del entorno y las guarda en los atributos."""
        self.temperatura = round(random.uniform(12.0, 38.0), 1)
        self.humedad = round(random.uniform(25.0, 95.0), 1)

    def sello_de_tiempo(self):
        """Marca de fecha y hora para cada lectura."""
        return datetime.now().strftime("%d-%m-%Y | %H:%M:%S")

#agente

    def evaluar_ambiente(self):
        """
        Combina proposiciones con conjunción (AND) para decidir la acción
        y guarda el resultado en self.accion.

        calor      = temperatura > 29
        frio       = temperatura < 17
        muy_humedo = humedad  > 75
        muy_seco   = humedad  < 35
        """
        calor = self.temperatura > 29
        frio = self.temperatura < 17
        muy_humedo = self.humedad > 75
        muy_seco = self.humedad < 35

        if calor and muy_humedo:
            self.accion = "A/C + Deshumidificador encendido"
        elif calor and muy_seco:
            self.accion = "A/C + Humidificador encendido"
        elif frio and muy_seco:
            self.accion = "Calefacción + Humidificador encendido"
        elif frio and muy_humedo:
            self.accion = "Calefacción + Deshumidificador encendido"
        elif calor:
            self.accion = "Ventilador encendido"
        elif frio:
            self.accion = "Calefacción encendido"
        elif muy_humedo:
            self.accion = "Deshumidificador encendido"
        elif muy_seco:
            self.accion = "Humidificador encendido"
        else:
            self.accion = "Todo estable, sistema apagado"
#bitacora
    def anotar_en_bitacora(self, hora):
        renglon = (
            f"[{hora}] Temp={self.temperatura}°C  "
            f"Hum={self.humedad}%  => {self.accion}\n"
        )
        with open(self.archivo_log, "a", encoding="utf-8") as bitacora:
            bitacora.write(renglon)

    def imprimir_estado(self, hora):
        print(f"Hora: {hora}")
        print(f"Temperatura: {self.temperatura}°C   Humedad: {self.humedad}%")
        print(f"Decisión: {self.accion}")
        print("-" * 45)

#ciclo

    def correr(self, segundos_espera=3):

        print("Agente de climatización activado")
        print(f"Guardando bitácora en: {self.archivo_log}")
        print("Presiona Ctrl + C para detener.\n")

        try:
            while True:
                self.leer_sensores()
                hora = self.sello_de_tiempo()
                self.evaluar_ambiente()

                self.imprimir_estado(hora)
                self.anotar_en_bitacora(hora)

                time.sleep(segundos_espera)

        except KeyboardInterrupt:
            print("\n Agente detenido manualmente por el usuario.")

#ejecucion

if __name__ == "__main__":
    agente = AgenteClimatizacion()
    agente.correr(segundos_espera=3)