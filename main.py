from datetime import datetime
import re

class HistorialMantenimientos:  # Lista circular
    def __init__(self):
        self.cabeza = None
        self.final = None
        self.actual = None
        self.contador = 0

    def agregar_mantenimiento(self, fecha, descripcion, costo):
        nuevo_mantenimiento = Mantenimiento(fecha, descripcion, costo)

        if not self.cabeza:
            self.cabeza = nuevo_mantenimiento
            self.final = nuevo_mantenimiento
            nuevo_mantenimiento.siguiente = nuevo_mantenimiento
            self.actual = nuevo_mantenimiento
        else:
            nuevo_mantenimiento.siguiente = self.cabeza
            self.final.siguiente = nuevo_mantenimiento
            self.final = nuevo_mantenimiento

        self.contador += 1

    def mostrar_historial(self):
        if not self.cabeza:
            print("No hay mantenimientos registrados.")
            return

        actual = self.cabeza
        while True:
            print(actual.mostrar_datos())
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def calcular_costo_total(self):
        if not self.cabeza:
            return 0

        total = 0
        actual = self.cabeza
        while True:
            total += actual.costo
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        return total

    def eliminar_mantenimiento(self, fecha):
        if not self.cabeza:
            print("No hay mantenimientos registrados.")
            return False

        actual = self.cabeza
        previo = self.final

        while True:
            if actual.fecha == fecha:
                if actual == self.cabeza:  # Si es el primero
                    self.cabeza = self.cabeza.siguiente
                    self.final.siguiente = self.cabeza
                elif actual == self.final:  # Si es el último
                    self.final = previo
                    self.final.siguiente = self.cabeza
                else:  # Caso intermedio
                    previo.siguiente = actual.siguiente

                self.contador -= 1

                if self.contador == 0:
                    self.cabeza = self.final = None

                print(f"Mantenimiento del {fecha} eliminado.")
                return True

            previo = actual
            actual = actual.siguiente

            if actual == self.cabeza:
                break

        print("Mantenimiento no encontrado.")
        return False

    
from datetime import datetime
import re

class Vehiculo:
    def __init__(self, placa, modelo, fecha_produccion, kilometraje, historial_de_mantenimientos):
        self._placa = None
        self._fecha_produccion = None
        self._kilometraje = None

        self.placa = placa  
        self.modelo = modelo
        self.fecha_produccion = fecha_produccion  
        self.kilometraje = kilometraje  
        self.historial_de_mantenimientos = historial_de_mantenimientos
        self.siguiente = None

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, value):
        if re.fullmatch(r"^[A-Z0-9]{7}$", value): 
            self._placa = value
        else:
            raise ValueError("La placa debe tener exactamente 7 caracteres alfanuméricos.")

    @property
    def fecha_produccion(self):
        return self._fecha_produccion

    @fecha_produccion.setter
    def fecha_produccion(self, value):
        anio_actual = datetime.now().year
        if isinstance(value, int) and 1900 <= value <= anio_actual:
            self._fecha_produccion = value
        else:
            raise ValueError(f"El año de producción debe ser un número entre 1900 y {anio_actual}.")

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._kilometraje = value
        else:
            raise ValueError("El kilometraje debe ser un número positivo.")

    def mostrar_datos(self):
        return f"Placa: {self.placa}, Modelo: {self.modelo}, Año: {self.fecha_produccion}, Kilometraje: {self.kilometraje}"


class Mantenimiento: #Nodo de mantenimientos
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo
        self.siguiente = None
    def mostrar_datos(self):
        return f"Fecha: {self.fecha}, Descripción: {self.descripcion}, Costo: Q.{self.costo}"

class FlotaVehiculos:  # Lista enlazada
    def __init__(self):
        self.cabeza = None  # Primer vehículo de la lista

    def agregar_vehiculo(self, placa, modelo, fecha_produccion, kilometraje):
        nuevo_vehiculo = Vehiculo(placa, modelo, fecha_produccion, kilometraje, HistorialMantenimientos())

        if not self.cabeza:
            self.cabeza = nuevo_vehiculo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_vehiculo  # Agregar al final de la lista

    def mostrar_vehiculos(self):
        if not self.cabeza:
            print("No hay vehículos registrados.")
            return

        actual = self.cabeza
        while actual:
            print(actual.mostrar_datos())
            actual = actual.siguiente

    def buscar_vehiculo(self, placa):
        actual = self.cabeza
        while actual:
            if actual.placa == placa:
                return actual  # Retorna el objeto vehículo si lo encuentra
            actual = actual.siguiente
        return None  # Si no lo encuentra

    def eliminar_vehiculo(self, placa):
        if not self.cabeza:
            print("No hay vehículos en la flota.")
            return False

        if self.cabeza.placa == placa:
            self.cabeza = self.cabeza.siguiente  # Elimina el primer nodo si coincide
            return True

        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.placa == placa:
                actual.siguiente = actual.siguiente.siguiente  # Salta el nodo eliminado
                return True
            actual = actual.siguiente
        
        print("Vehículo no encontrado.")
        return False

    
def menu():
    flota = FlotaVehiculos()
    while True:
        import os
        os.system('cls')

        print("\n=== MENÚ PRINCIPAL ===")
        print("[1] Gestión de Vehículos")
        print("[2] Gestión de Mantenimientos")
        print("[3] Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                os.system('cls')
                print("\n=== GESTIÓN DE VEHÍCULOS ===")
                print("[1] Registrar vehículo")
                print("[2] Mostrar vehículos")
                print("[3] Buscar vehículo")
                print("[4] Regresar")
                opcion_v = input("Seleccione una opción: ")
                
                if opcion_v == "1":
                    placa = input("Placa (7 caracteres alfanuméricos): ")
                    modelo = input("Modelo: ")
                    anio = int(input("Año de producción: "))
                    km = float(input("Kilometraje: "))
                    flota.agregar_vehiculo(placa, modelo, anio, km)
                    print("Vehículo registrado correctamente.")
                    input()
                elif opcion_v == "2":
                    print(flota.mostrar_vehiculos())
                    input()
                elif opcion_v == "3":
                    placa = input("Ingrese la placa: ")
                    vehiculo = flota.buscar_vehiculo(placa)
                    if vehiculo:
                        print(vehiculo.mostrar_datos())
                    else:
                        print("Vehículo no encontrado.")

                    input()
                elif opcion_v == "4":
                    break
                else:
                    print("Opción no válida.")

        elif opcion == "2":
            while True:
                os.system('cls')
                print("\n=== GESTIÓN DE MANTENIMIENTOS ===")
                print("[1] Agregar mantenimiento")
                print("[2] Ver historial")
                print("[3] Calcular costo total")
                print("[4] Regresar")
                opcion_m = input("Seleccione una opción: ")

                if opcion_m == "1":
                    placa = input("Ingrese la placa del vehículo: ")
                    vehiculo = flota.buscar_vehiculo(placa)
                    if vehiculo:
                        fecha = input("Fecha (DD-MM-YYYY): ")
                        descripcion = input("Descripción: ")
                        costo = float(input("Costo: Q."))
                        vehiculo.historial_de_mantenimientos.agregar_mantenimiento(fecha, descripcion, costo)
                        print("Mantenimiento agregado.")
                        
                    else:
                        print("Vehículo no encontrado.")

                    input()

                elif opcion_m == "2":
                    placa = input("Ingrese la placa del vehículo: ")
                    vehiculo = flota.buscar_vehiculo(placa)
                    if vehiculo:
                        print(vehiculo.historial_de_mantenimientos.mostrar_historial())
                    else:
                        print("Vehículo no encontrado.")

                    input()

                elif opcion_m == "3":
                    placa = input("Ingrese la placa del vehículo: ")
                    vehiculo = flota.buscar_vehiculo(placa)
                    if vehiculo:
                        print(f"Costo total de mantenimientos: Q.{vehiculo.historial_de_mantenimientos.calcular_costo_total()}")
                    else:
                        print("Vehículo no encontrado.")

                    input()
                elif opcion_m == "4":
                    break
                else:
                    print("Opción no válida.")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
