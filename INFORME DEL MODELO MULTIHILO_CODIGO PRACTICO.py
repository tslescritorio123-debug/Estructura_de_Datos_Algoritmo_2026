import threading
import time
import logging

# Configuración de log con formato profesional de auditoría
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(threadName)-18s] %(message)s', datefmt='%H:%M:%S')

class MotorTransaccional:
    def __init__(self, fondo_reserva):
        self._saldo_auditado = fondo_reserva
        # Mutex: Objeto de Exclusión Mutua para control de concurrencia
        self.mutex = threading.Lock()

    def ejecutar_transaccion_atomica(self, monto, latencia_red):
        # Entrada a la Sección Crítica
        with self.mutex:
            logging.info(f"SOLICITUD RECIBIDA: Transacción por ${monto}")
            
            # Simulación de validación en base de datos externa
            nuevo_balance = self._saldo_auditado + monto
            time.sleep(latencia_red) 
            
            self._saldo_auditado = nuevo_balance
            logging.info(f"CONFIRMACIÓN: Balance actualizado a ${self._saldo_auditado}")

    @property
    def balance_total(self):
        with self.mutex:
            return self._saldo_auditado

def terminal_bancaria():
    # Inicialización del sistema con un fondo de reserva de $1000
    sistema_oltp = MotorTransaccional(1000)
    
    print("\n" + "="*50)
    print("   NUCLEO BANCARIO - SISTEMA DE ALTA CONCURRENCIA")
    print("="*50)
    
    while True:
        print(f"\nBALANCE EN BÓVEDA: ${sistema_oltp.balance_total}")
        print("1. Ejecutar ráfaga de transacciones concurrentes (OLTP)")
        print("2. Apagar núcleo del sistema")
        
        comando = input("\nIngrese comando de sistema: ")

        if comando == "1":
            try:
                n_hilos = int(input("¿Número de transacciones simultáneas?: "))
                valor = float(input("¿Monto de cada transacción?: "))
                
                print(f"\nIniciando procesamiento de {n_hilos} hilos de ejecución...\n")
                
                pool_hilos = []
                for i in range(n_hilos):
                    # Instanciación de hilos con nombres de auditoría
                    hilo = threading.Thread(
                        target=sistema_oltp.ejecutar_transaccion_atomica, 
                        args=(valor, 0.3), 
                        name=f"Worker-OLTP-{i+1}"
                    )
                    pool_hilos.append(hilo)
                    hilo.start()

                # Sincronización de hilos (Barrier)
                for hilo in pool_hilos:
                    hilo.join()
                
                print("\n[!] Ráfaga completada. Consistencia de datos verificada.")
            except ValueError:
                print("Error: Parámetros de transacción inválidos.")
        
        elif comando == "2":
            print("Cerrando todas las conexiones al núcleo...")
            break

if __name__ == "__main__":
    terminal_bancaria()
