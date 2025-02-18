from datetime import datetime
import re

class Vehiculo:  # Nodo
    def __init__(self, placa, modelo, fecha_produccion, kilometraje, historial_de_mantenimientos):
        self.placa = placa
        self.modelo = modelo
        self.fecha_produccion = fecha_produccion
        self.kilometraje = kilometraje
        self.historial_de_mantenimientos = historial_de_mantenimientos
        self.siguiente = None

    def mostrar_datos(self):
        return f"Placa: {self.placa}, Modelo: {self.modelo}, Año: {self.fecha_produccion}, Kilometraje: {self.kilometraje}, Historial de Mantenimientos: {self.historial_de_mantenimientos}"

class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo

def menu():

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("[1] Gestión de Vehículos")
        print("[2] Gestión de Mantenimientos")
        print("[3] Salir")

        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            while True:
                print("\n=== GESTIÓN DE VEHÍCULOS ===")
                print("[1] Registrar vehículo")
                print("[2] Mostrar vehículos")
                print("[3] Buscar vehículo")
                print("[4] Eliminar vehículo")
                print("[5] Regresar al menú principal")

                opcion_menu_vehiculos = input("Seleccione una opción (1-5): ")

                if opcion_menu_vehiculos == "1":
                    print("Ingrese los datos del vehículo")
                
                elif opcion_menu_vehiculos == "2":
                    print("Vehículos registrados en la flota:")
                
                elif opcion_menu_vehiculos == "3":
                    print("Ingrese la placa del vehículo que busca:")

                elif opcion_menu_vehiculos == "4":
                    print("Ingrese la placa del vehículo que desea eliminar:")

                elif opcion_menu_vehiculos == "5":
                    break  

                else:
                    print("Opción no válida, intente nuevamente.")

                input("\nPresione Enter para continuar...") 

        elif opcion == "2":
            while True:
                print("\n=== GESTIÓN DE MANTENIMIENTOS ===")
                print("[1] Agregar mantenimiento a un vehículo")
                print("[2] Historial de mantenimientos por vehículo")
                print("[3] Calcular costo de mantenimientos por vehículo")
                print("[4] Regresar al menú principal")

                opcion_menu_mantenimientos = input("Seleccione una opción (1-4): ")

                if opcion_menu_mantenimientos == "1":
                    print("Ingrese la placa del vehículo: ")
                
                elif opcion_menu_mantenimientos == "2":
                    print("Ingrese la placa del vehículo: ")

                elif opcion_menu_mantenimientos == "3":
                    print("Ingrese la placa del vehículo:")
                
                elif opcion_menu_mantenimientos == "4":
                    break  # Regresa al menú principal

                else:
                    print("Opción no válida, intente nuevamente.")

                input("\nPresione Enter para continuar...") 

        elif opcion == "3":
            print("Saliendo...")
            break 

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
