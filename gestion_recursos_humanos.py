class Empleado:
    """Clase base con las tarifas oficiales."""
    TARIFAS = {"Gerente": 100.0, "Supervisor": 80.0, "Operario": 50.0}

    def __init__(self, nombre: str, cargo: str, antiguedad: int, tipo: str):
        self.nombre = nombre
        self.cargo = cargo.capitalize()
        self.antiguedad = antiguedad  # Años en la empresa
        self.tipo = tipo

    def calcular_salario_final(self, factor: int) -> float:
        pass

    def __str__(self) -> str:
        return f"[{self.tipo}] {self.nombre:<20} | Antigüedad: {self.antiguedad} años"


class EmpleadoPlanta(Empleado):
    """Empleados con contrato fijo de 40 horas semanales."""
    def __init__(self, nombre: str, cargo: str, antiguedad: int):
        super().__init__(nombre, cargo, antiguedad, "Planta")
        self.horas_semanales = 40

    def calcular_salario_final(self, semanas_trabajadas: int) -> float:
        tarifa_hora = self.TARIFAS.get(self.cargo, 50.0)
        salario_semanal = tarifa_hora * self.horas_semanales
        return salario_semanal * semanas_trabajadas


class EmpleadoPorHora(Empleado):
    """Empleados con jornadas flexibles por horas."""
    def __init__(self, nombre: str, cargo: str, antiguedad: int):
        super().__init__(nombre, cargo, antiguedad, "Por Hora")

    def calcular_salario_final(self, horas_totales: int) -> float:
        tarifa_hora = self.TARIFAS.get(self.cargo, 50.0)
        return tarifa_hora * horas_totales


# ==============================================================================
# LISTA INICIAL Y DICCIONARIO DE HISTORIAL DE PAGOS
# ==============================================================================
empleados = [
    EmpleadoPlanta("Carlos Mendoza", "Gerente", 8),
    EmpleadoPlanta("Jorge Rivas", "Supervisor", 12),
    EmpleadoPlanta("Luis Torres", "Operario", 12),
    EmpleadoPlanta("Elena Rostova", "Operario", 3),
    EmpleadoPlanta("Pedro Infante", "Supervisor", 5),
    
    EmpleadoPorHora("Ana Gómez", "Supervisor", 4),
    EmpleadoPorHora("María López", "Operario", 2),
    EmpleadoPorHora("Juan Pérez", "Gerente", 1),
    EmpleadoPorHora("Sofía Castro", "Operario", 6),
    EmpleadoPorHora("Lucas Silva", "Operario", 2)
]

historial_salarios = {}

# ==============================================================================
# MENÚ INTERACTIVO
# ==============================================================================
def menu():
    cargos_orden = ["Gerente", "Supervisor", "Operario"]

    while True:
        print("\n" + "="*50)
        print("SISTEMA DE GESTIÓN DE EMPLEADOS.")
        print("="*50)
        print("1. 👔 MOSTRAR ESCALA DE EMPLEADOS")
        print("2. 💰 CALCULAR SALARIO DE EMPLEABILIDAD")
        print("3. 📄 GENERAR BOLETA DE PAGO")
        print("4. 📊 MOSTRAR EMPLEADO CON MAYOR SALARIO")
        print("5. ⏳ MOSTRAR EMPLEADOS CON MAYOR TIEMPO LABORAL")
        print("6. ➕ AÑADIR NUEVO EMPLEADO")
        print("7. ❌ ELIMINAR EMPLEADO DE LA EMPRESA")
        print("8. 🚪 SALIR DEL PROGRAMA")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            print("\n==================================================")
            print("       ESTRUCTURA JERÁRQUICA DE LA EMPRESA        ")
            print("==================================================")
            for cargo in cargos_orden:
                print(f"\n🔹 SECCIÓN: {cargo.upper()}S")
                print("-" * 40)
                
                print("  [CONTRATO DE PLANTA]")
                empleados_planta = [e for e in empleados if e.cargo == cargo and isinstance(e, EmpleadoPlanta)]
                if empleados_planta:
                    for emp in empleados_planta:
                        print(f"   • {emp.nombre:<20} | Antigüedad: {emp.antiguedad} años")
                else:
                    print("   (No hay empleados de Planta en este cargo)")
                
                print("\n  [CONTRATO POR HORA]")
                empleados_hora = [e for e in empleados if e.cargo == cargo and isinstance(e, EmpleadoPorHora)]
                if empleados_hora:
                    for emp in empleados_hora:
                        print(f"   • {emp.nombre:<20} | Antigüedad: {emp.antiguedad} años")
                else:
                    print("   (No hay empleados Por Hora en este cargo)")
                print("-" * 40)

        elif opcion == "2":
            print("\n--- SECCIÓN DE CÁLCULO DE SALARIOS ---")
            print("1. Calcular Empleado de Planta")
            print("2. Calcular Empleado Por Hora")
            sub_opcion = input("Seleccione el tipo de cálculo (1 o 2): ").strip()

            if sub_opcion == "1":
                plantas = [e for e in empleados if isinstance(e, EmpleadoPlanta)]
                if not plantas:
                    print("No hay empleados de planta registrados.")
                    continue
        
                print("\nSeleccione el empleado de Planta a calcular:")
                for idx, emp in enumerate(plantas, 1):
                    print(f"{idx}. {emp.nombre} ({emp.cargo})")
                try:
                    seleccion = int(input("Número de empleado: ")) - 1
                    if 0 <= seleccion < len(plantas):
                        emp_elegido = plantas[seleccion]
                        semanas = int(input(f"¿Cuántas semanas trabajó {emp_elegido.nombre} en el mes?: "))
                        
                        salario = emp_elegido.calcular_salario_final(semanas)
                        historial_salarios[emp_elegido.nombre] = {
                            "cargo": emp_elegido.cargo,
                            "tipo": emp_elegido.tipo,
                            "detalle": f"{semanas} semanas trabajadas",
                            "monto": salario
                        }
                        print(f"✔️ Salario de {emp_elegido.nombre} calculado y guardado.")
                    else:
                        print("❌ Número fuera de rango.")
                except ValueError:
                    print("❌ Entrada inválida. Use números enteros.")

            elif sub_opcion == "2":
                por_horas = [e for e in empleados if isinstance(e, EmpleadoPorHora)]
                if not por_horas:
                    print("No hay empleados por hora registrados.")
                    continue

                print("\nSeleccione el empleado Por Hora a calcular:")
                for idx, emp in enumerate(por_horas, 1):
                    print(f"{idx}. {emp.nombre} ({emp.cargo})")
                try:
                    seleccion = int(input("Número de empleado: ")) - 1
                    if 0 <= seleccion < len(por_horas):
                        emp_elegido = por_horas[seleccion]
                        horas = int(input(f"¿Cuántas horas totales trabajó {emp_elegido.nombre} en el mes?: "))
                        
                        salario = emp_elegido.calcular_salario_final(horas)
                        historial_salarios[emp_elegido.nombre] = {
                            "cargo": emp_elegido.cargo,
                            "tipo": emp_elegido.tipo,
                            "detalle": f"{horas} horas trabajadas",
                            "monto": salario
                        }
                        print(f"✔️ Salario de {emp_elegido.nombre} calculado y guardado.")
                    else:
                        print("❌ Número fuera de rango.")
                except ValueError:
                    print("❌ Entrada inválida. Use números enteros.")
            else:
                print("❌ Opción incorrecta.")
                
        elif opcion == "3":
            print("\n--- REPORTE DE BOLETAS DE PAGO GENERADAS ---")
            print("1. Ver boleta de un empleado de Planta")
            print("2. Ver boleta de un empleado Por Hora")
            sub_boleta = input("Seleccione una opción (1 o 2): ").strip()

            if sub_boleta == "1":
                plantas_calculados = [e for e in empleados if isinstance(e, EmpleadoPlanta) and e.nombre in historial_salarios]
                if not plantas_calculados:
                    print("⚠️ No se han calculado salarios para empleados de Planta aún.")
                    continue
                print("\nSeleccione el empleado para ver su boleta:")
                for idx, emp in enumerate(plantas_calculados, 1):
                    print(f"{idx}. {emp.nombre}")
                try:
                    sel = int(input("Número: ")) - 1
                    if 0 <= sel < len(plantas_calculados):
                        emp_sel = plantas_calculados[sel]
                        datos = historial_salarios[emp_sel.nombre]
                        print("\n" + "═"*45)
                        print(f"       📄 BOLETA DE PAGO - EMPRESA S.A.")
                        print("═"*45)
                        print(f" Empleado:    {emp_sel.nombre}")
                        print(f" Cargo:       {datos['cargo']}")
                        print(f" Contrato:    {datos['tipo']}")
                        print(f" Registro:    {datos['detalle']}")
                        print(f" Total Neto:  ${datos['monto']:.2f}")
                        print("═"*45)
                    else:
                        print("❌ Número fuera de rango.")
                except ValueError:
                    print("❌ Entrada inválida.")

            elif sub_boleta == "2":
                horas_calculados = [e for e in empleados if isinstance(e, EmpleadoPorHora) and e.nombre in historial_salarios]
                if not horas_calculados:
                    print("⚠️ No se han calculado salarios para empleados Por Hora aún.")
                    continue
                print("\nSeleccione el empleado para ver su boleta:")
                for idx, emp in enumerate(horas_calculados, 1):
                    print(f"{idx}. {emp.nombre}")
                try:
                    sel = int(input("Número: ")) - 1
                    if 0 <= sel < len(horas_calculados):
                        emp_sel = horas_calculados[sel]
                        datos = historial_salarios[emp_sel.nombre]
                        print("\n" + "═"*45)
                        print(f"       📄 BOLETA DE PAGO - EMPRESA S.A.")
                        print("═"*45)
                        print(f" Empleado:    {emp_sel.nombre}")
                        print(f" Cargo:       {datos['cargo']}")
                        print(f" Contrato:    {datos['tipo']}")
                        print(f" Registro:    {datos['detalle']}")
                        print(f" Total Neto:  ${datos['monto']:.2f}")
                        print("═"*45)
                    else:
                        print("❌ Número fuera de rango.")
                except ValueError:
                    print("❌ Entrada inválida.")
            else:
                print("❌ Opción inválida.")
        
        elif opcion == "4":
            if not empleados:
                print("❌ No hay empleados en la lista.")
                continue
            print("\n" + "="*55)
            print(" 📊 INFORME: MAYOR SALARIO GENERADO (Mensual Estándar)")
            print("="*55)
            
            salarios_simulados = []
            for emp in empleados:
                sal = emp.calcular_salario_final(4) if isinstance(emp, EmpleadoPlanta) else emp.calcular_salario_final(160)
                salarios_simulados.append((sal, emp))
            
            # Buscamos el salario máximo analizando únicamente los números
            max_valor_salario = max(sal for sal, emp in salarios_simulados)
            
            # Filtramos e imprimimos comparando solo los números para evitar colisiones
            for sal, emp in salarios_simulados:
                if sal == max_valor_salario:
                    print(f" • Empleado:    {emp.nombre}")
                    print(f"   Cargo:       {emp.cargo}")
                    print(f"   Contrato:    {emp.tipo}")
                    print(f"   Salario:     ${sal:.2f}")
                    print("-" * 45)

        elif opcion == "5":
            if not empleados:
                print("❌ No hay empleados en la lista.")
                continue
            max_antiguedad = max(e.antiguedad for e in empleados)
            print("\n" + "=" * 55)
            print(f" 📊 INFORME: EMPLEADOS CON MAYOR ANTIGÜEDAD")
            print("=" * 55)
            for emp in empleados:
                if emp.antiguedad == max_antiguedad:
                    print(f" • Empleado:    {emp.nombre}")
                    print(f"   Cargo:       {emp.cargo}")
                    print(f"   Contrato:    {emp.tipo}")
                    print(f"   Antigüedad:  {emp.antiguedad} años de trabajo")
                    print("-" * 45)

        elif opcion == "6":
            print("\n--- AGREGAR NUEVO EMPLEADO ---")
            nombre = input("Nombre completo: ").strip()
            cargo = input("Cargo (Gerente, Supervisor, Operario): ").strip().capitalize()
            if cargo not in cargos_orden:
                print("❌ Cargo no válido. Operación cancelada.")
                continue
            try:
                antiguedad = int(input("Años de antigüedad: "))
            except ValueError:
                print("❌ La antigüedad debe ser un número entero. Cancelado.")
                continue
            
            tipo_emp = input("Tipo de empleado (1: Planta / 2: Por Hora): ").strip()
            if tipo_emp == "1":
                empleados.append(EmpleadoPlanta(nombre, cargo, antiguedad))
                print(f"✔️ {nombre} agregado con éxito a Planta.")
            elif tipo_emp == "2":
                empleados.append(EmpleadoPorHora(nombre, cargo, antiguedad))
                print(f"✔️ {nombre} agregado con éxito Por Hora.")
            else:
                print("❌ Opción inválida. Cancelado.")

        elif opcion == "7":
            print("\n--- ELIMINAR EMPLEADO ---")
            for i, emp in enumerate(empleados, 1):
                print(f"{i}. {emp.nombre} ({emp.cargo}) - {emp.tipo}")
            try:
                indice = int(input("Seleccione el número del empleado a eliminar: ")) - 1
                if 0 <= indice < len(empleados):
                    eliminado = empleados.pop(indice)
                    historial_salarios.pop(eliminado.nombre, None)
                    print(f"❌ {eliminado.nombre} ha sido removido del sistema.")
                else:
                    print("❌ Número fuera de rango.")
            except ValueError:
                print("❌ Entrada inválida.")

        elif opcion == "8":
            print("\nCerrando el sistema de gestión. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()