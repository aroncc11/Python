import threading
import requests

# -------------------------------
# 1. Falla de Excepción
# -------------------------------
def fallo_excepcion():
    try:
        x = 10 / 0
    except ZeroDivisionError as e:
        print("[Excepción manejada] ->", e)


# -------------------------------
# 2. Falla de Lógica
# -------------------------------
def fallo_logica(base, altura):
    # Error lógico: debería ser (base * altura) / 2 para triángulo
    area = base * altura
    print("[Lógica] Área calculada incorrectamente:", area)


# -------------------------------
# 3. Falla de Concurrencia
# -------------------------------
contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100000):
        # Solución: usar lock para evitar condición de carrera
        with lock:
            contador += 1

def fallo_concurrencia():
    global contador
    hilos = [threading.Thread(target=incrementar) for _ in range(5)]
    for h in hilos: h.start()
    for h in hilos: h.join()
    print("[Concurrencia] Contador final:", contador)


# -------------------------------
# 4. Falla de Recursos
# -------------------------------
def fallo_recursos():
    try:
        lista = []
        for i in range(1000000):
            lista.append("dato" * 1000)  # Puede agotar RAM
            if i % 200000 == 0:
                print(f"[Recursos] Elementos almacenados: {i}")
    except MemoryError as e:
        print("[Recursos] Error de memoria:", e)


# -------------------------------
# 5. Falla de Comunicación
# -------------------------------
def fallo_comunicacion():
    try:
        requests.get("http://10.255.255.1", timeout=2)
    except requests.exceptions.RequestException as e:
        print("[Comunicación] Error detectado:", e)


# -------------------------------
# 6. Falla de Seguridad
# -------------------------------
def fallo_seguridad():
    entrada = "_import_('os').system('echo HACKED')"  # Nunca hacer esto en producción
    try:
        eval(entrada)
    except Exception as e:
        print("[Seguridad] Intento de ejecución maliciosa bloqueado:", e)


# -------------------------------
# Ejecución de pruebas
# -------------------------------
if __name__ == "__main__":
    print("=== Simulación de Fallas de Software ===")
    fallo_excepcion()
    fallo_logica(10, 5)
    fallo_concurrencia()
    fallo_recursos()
    fallo_comunicacion()
    fallo_seguridad()