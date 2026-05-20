# =====================================================================
# 1. ABSTRACCIÓN: 
# =====================================================================
class VehiculoBase:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

# =====================================================================
# 2. CLASE: El molde maestro que define la estructura del automóvil.
# =====================================================================
class Automovil(VehiculoBase):
    
    # =================================================================
    # 3. CONSTRUCTOR: Inicializa físicamente el objeto en memoria.
    # =================================================================
    def __init__(self, marca: str, modelo: str, bateria_inicial: int):
        super().__init__(marca, modelo)
        
        # =============================================================
        # 4. ENCAPSULAMIENTO: Atributo privado (__bateria).
        # =============================================================
        self.__bateria = max(0, min(100, bateria_inicial)) 

    # 5. ATRIBUTOS (Lectura controlada mediante métodos)
    def obtener_nombre(self) -> str:
        return f"{self.marca} {self.modelo}"
    
    def obtener_bateria(self) -> int:
        return self.__bateria

    # =================================================================
    # 6. MÉTODO: El comportamiento operativo que altera el estado interno.
    # =================================================================
    def conducir(self, kilometros: int) -> str:
        gasto = kilometros * 2
        if self.__bateria >= gasto:
            self.__bateria -= gasto  # Modificación segura del estado encapsulado
            return f"🚗 {self.obtener_nombre()} recorrió {kilometros} km. Batería restante: {self.__bateria}%"
        return f"❌ {self.obtener_nombre()} no tiene suficiente batería para recorrer {kilometros} km. Requiere {gasto}%."


# =====================================================================
# 7. HERENCIA: 'Tesla' "es un" 'Automovil'. Hereda todo de forma automática.
# =====================================================================
class Tesla(Automovil):
    def __init__(self, modelo: str, bateria_inicial: int, autopilot_version: float):
        super().__init__("Tesla", modelo, bateria_inicial)
        self.autopilot = autopilot_version

    # =================================================================
    # 8. POLIMORFISMO: El método 'conducir' se comporta de forma 
    # diferente y especializada en un Tesla (gasta menos energía).
    # =================================================================
    def conducir(self, kilometros: int) -> str:
        gasto = kilometros * 1  # El Tesla es más eficiente por su tecnología
        if self.obtener_bateria() >= gasto:
            # Para alterar la batería encapsulada usamos una vía indirecta simulada
            # (En un sistema real usaríamos un método setter público)
            self._Automovil__bateria -= gasto 
            return f"⚡ Tesla {self.modelo} en modo Autopilot v{self.autopilot} recorrió {kilometros} km. Batería: {self.obtener_bateria()}%"
        return f"❌ Tesla {self.modelo} necesita recargar para este viaje."


# =====================================================================
# INTERFAZ DE USUARIO INTERACTIVA EN CONSOLA
# =====================================================================
def iniciar_simulacion():
    print("=== BIENVENIDO AL SISTEMA DE GESTIÓN DE VEHÍCULOS ===")
    
    # Creación física de los 8. OBJETOS en memoria
    nissan = Automovil("Nissan", "Leaf", 60)
    tesla = Tesla("Model 3", 50, 12.0)
    
    # Lista para ejecutar Polimorfismo en lote
    garaje = [nissan, tesla]
    
    while True:
        print("\n--- VEHÍCULOS DISPONIBLES EN TU GARAJE ---")
        for i, vehiculo in enumerate(garaje):
            print(f"[{i + 1}] {vehiculo.obtener_nombre()} (Batería: {vehiculo.obtener_bateria()}%)")
        print("[3] Salir de la simulación")
        
        try:
            opcion = int(input("\nSelecciona un vehículo para conducir (1-3): "))
            if opcion == 3:
                print("Simulación finalizada de forma segura. ¡Buen viaje!")
                break
                
            if opcion in [1, 2]:
                vehiculo_seleccionado = garaje[opcion - 1]
                km = int(input(f"¿Cuántos kilómetros deseas conducir el {vehiculo_seleccionado.obtener_nombre()}?: "))
                
                # Aquí se ve el POLIMORFISMO en acción: 
                # Ejecutas exactamente la misma instrucción '.conducir()', pero 
                # la consola te responderá diferente según el auto elegido.
                print("\nResultado:")
                print(vehiculo_seleccionado.conducir(km))
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    iniciar_simulacion()
