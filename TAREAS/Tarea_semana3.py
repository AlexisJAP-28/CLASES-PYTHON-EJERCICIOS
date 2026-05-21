#==== LENGUAJE DE PROGRAMACIÓN =====
#==== TAREA PRÁCTICA - SEMANA 3 =====
# FECHA: Semana 3 (04/05/2026 - 17/05/2026)
# TEMA: Estructuras Condicionales y Bucles

# EJERCICIOS A RESOLVER:

# ----------------------------------------------------
# ===== EJERCICIO 1  ¿Es el protocolo seguro? =====
# ----------------------------------------------------
# Es el protocolo seguro? (condicionales)
# Dado el nombre de un protocolo guardado en una variable protocolo, indique si es seguro o
# inseguro. Seguros: HTTPS, SSH, SFTP. Inseguros: HTTP, Telnet, FTP. Si el protocolo no esta en
# ninguna de las listas, imprimir "Desconocido"

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización de condicionales if,else,or)
def ejercicio1():
    protocolo = "HTTPS"
    print("\nProtocolo Seguro o Inseguro?")
    if protocolo == "HTTPS" or protocolo == "SSH" or protocolo == "SFTP":
        print("El protocolo", protocolo, "es SEGURO")
    elif protocolo == "HTTP" or protocolo == "Telnet" or protocolo == "FTP":
        print("El protocolo", protocolo, "es INSEGURO")
    else:
        print("Desconocido")
# FINALIZACIÓN DEL EJERCICIO


# ----------------------------------------------------------------
# ===== EJERCICIO 2 - Identificar el servicio según el puerto=====
# ----------------------------------------------------------------
# Identificar el servicio segun el puerto (if / elif / else)
# Dado un numero de puerto en una variable puerto, imprimir el servicio asociado segun la siguiente
# tabla: 22 = SSH, 80 = HTTP, 443 = HTTPS, 3306 = MySQL, 3389 = RDP. Si no esta en la lista, imprimir
# Servicio desconocido

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización de condicionales if, elif, else)
def ejercicio2():
    puerto = 443
    print("\nIdentificación de puerto")
    if puerto == 22:
        servicio = "SSH"
    elif puerto == 80:
        servicio = "HTTP"
    elif puerto == 443:
        servicio = "HTTPS"
    elif puerto == 3306:
        servicio = "MySQL"
    elif puerto == 3389:
        servicio = "RDP"
    else:
        servicio = "Servicio desconocido"
    print("Puerto", puerto, ":", servicio)
# FINALIZACIÓN DEL EJERCICIO


# --------------------------------------------------
# ===== EJERCICIO 3 - Listar IPs de una subred =====
# --------------------------------------------------
#Listar IPs de una subred (bucle for con range)
#Imprimir todas las direcciones IP de la subred 192.168.1.0/29. Esa subred contiene 8 direcciones:
#192.168.1.0 hasta 192.168.1.7. Usar un bucle for con range().

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización de bucle for con range)
def ejercicio3():
    print("\nListado de ip's de una subred (rango 192.168.1.0 a 192.168.1.7)")
    for i in range(8):
                print(f"192.168.1.{i}")
# FINALIZACIÓN DEL EJERCICIO


# -------------------------------------------------------------
# ===== EJERCICIO 4 - Inventario numerado de dispositivos =====
# -------------------------------------------------------------
#Inventario numerado de dispositivos (for con enumerate)
#Recorrer la siguiente lista de dispositivos con enumerate() y mostrarlos numerados desde 1.
#Datos iniciales:
#dispositivos = ["Router Cisco", "Switch HP", "Firewall Fortinet", "Servidor Dell"]

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización de for con enumerate)
def ejercicio4():
    dispositivos = [ "Router Cisco", "Switch HP", "Firewall Fortinet", "Servidor Dell"]
    print("\nLista de dispositivos")
    for posicion, valor in enumerate(dispositivos, start=1):
        print(f"{posicion}. {valor}")
# FINALIZACIÓN DEL EJERCICIO


# ----------------------------------------------------
# ===== EJERCICIO 5 -Cuenta regresiva de apagado =====
# ----------------------------------------------------
#Cuenta regresiva de apagado (bucle while)
#Un servidor se va a apagar. Imprimir la cuenta regresiva desde 5 hasta 1 usando un while, y al final el
#mensaje "Apagando servidor...". Recuerden actualizar la variable de control en cada vuelta.

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización de bucle while)
def ejercicio5():
    contador = 5
    print("\nCuenta regresiva de apagado...")
    while contador >= 1:
        print(f"Apagado en {contador} ...")
        contador -= 1
    print("Apagando servidor...")
# FINALIZACIÓN DEL EJERCICIO


# ----------------------------------------------
# ===== EJERCICIO 6 -Reintento de conexión =====
# --------------------------------------------------
# Reintento de conexion (while con condicion compuesta)
#Simular el reintento de conexion a un servidor con un maximo de 5 intentos. Usar un while que se
#detenga cuando la conexion sea exitosa (suponer que se conecta en el intento 3) o cuando se agoten
#los 5 intentos. Mostrar el numero de cada intento

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización while con condición compuesta)
def ejercicio6():
    intento = 1
    conectado = False
    print("\nNo. de intetos de conexión al servidor")
    while intento <= 5 and not conectado:
        if intento == 3:
            conectado = True
            print(f"Intento {intento}: CONECTADO")
        else:
            print(f"Intento {intento}: sin respuesta")
        intento += 1
# FINALIZACIÓN DEL EJERCICIO


# ----------------------------------------------
# ===== EJERCICIO 7 -Primer puerto cerrado =====
# ----------------------------------------------
# Primer puerto cerrado (uso de break)
# Recorrer la lista de puertos con sus estados y detener el bucle apenas encontremos el primer puerto en
# estado "cerrado". Usar break.
# Datos iniciales:
# puertos = [21, 22, 23, 25, 80]
# estados = ["abierto", "abierto", "abierto", "cerrado", "abierto"]

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización de break)
def ejercicio7():
    puertos = [21, 22, 23, 25, 80]
    estados = ["abierto", "abierto", "abierto", "cerrado", "abierto"]
    print("\nValidación de puertos estado: abierto/cerrado")
    for puerto, estado in zip(puertos, estados):
        if estado == "cerrado":
            print(f"Primer puerto cerrado: {puerto}")
            break
        else:
            print(f"Puerto {puerto}: {estado}")
# FINALIZACIÓN DEL EJERCICIO


# --------------------------------------------------------
# ===== EJERCICIO 8 -  Filtrar IPs de la lista negra =====
# --------------------------------------------------------
# Filtrar IPs de la lista negra (uso de continue)
# Recorrer la lista ips_log y procesar cada IP, pero saltarse las que esten en blacklist usando
# continue. Imprimir solo las IPs aceptadas y al final cuantas se procesaron.
# Datos iniciales:
# ips_log = ["10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156", "10.0.0.10"]
# blacklist = ["200.0.0.1", "45.33.32.156"]

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización de continue)
def ejercicio8():
    ips_log = [ "10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156", "10.0.0.10" ]
    blacklist = ["200.0.0.1", "45.33.32.156"]
    total = 0
    print("\nValidación de ip´s listas negras")
    print("Listado de ip´s: 10.0.0.5 - 200.0.0.1 - 10.0.0.8 - 45.33.32.156 - 10.0.0.10")
    print("Listas negras: 200.0.0.1 - 45.33.32.156")
    print("\nLista aceptada:")
    for ip in ips_log:
        if ip in blacklist:
            continue
        print(f"Procesando: {ip}")
        total += 1
    print(f"Total procesadas: {total}")
# FINALIZACIÓN DEL EJERCICIO


#-----------------------------------------------------------
# ===== EJERCICIO 9 - Buscar dispositivo en inventario =====
#------------------------------------------------------------
#  Buscar dispositivo en inventario (else en bucle)
# Buscar el nombre de un dispositivo en la lista. Si se encuentra, imprimir "Encontrado". Si NO se
# encuentra, usar la clausula else del for para imprimir "No encontrado en el inventario".
# Datos iniciales:
# inventario = ["Router-01", "Switch-A", "Firewall-FW1", "Servidor-Web"]
# buscar = "Firewall-FW1"

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización de else en bucle)
def ejercicio9():
    inventario = [ "Router-01", "Switch-A", "Firewall-FW1", "Servidor-Web" ]
    buscar = "Firewall-FW1"
    print("\nListado de dispositivos")
    print("Router-01, Switch-A, Firewall-FW1, Servidor-Web")
    print("Dispositivo a encontrar: Firewall-FW1")
    print("\nEquipo:")
    for d in inventario:
        if d == buscar:
            print("Encontrado")
            break
    else:
        print("No encontrado en el inventario")
# FINALIZACIÓN DEL EJERCICIO


# ------------------------------------------------------
# ===== EJERCICIO 10 - Validador de dirección IPv4 =====
# ------------------------------------------------------
# Validador de direccion IPv4 (integrador)
# Validar si una direccion IP es correcta. Reglas: debe tener 4 octetos separados por punto, y cada
# octeto debe ser un numero entre 0 y 255. Combinar if, for y manipulacion de cadenas (.split,
# .isdigit). Probar con varias IPs validas e invalidas

# EJECUCIÓN DEL EJERCICIO
# FUNCION def (Llama al ejercicio) Y PROCESO (Utilización de integrador)
def ejercicio10():
    ips = [ "192.168.1.1", "10.0.0.255", "256.1.1.1", "192.168.1", "192.168.a.1" ]
    print("\nListado de direcciones ip's (IPv4)")
    print("Validación IPv4, octeto debe ser un numero entre 0 y 255)")
    for ip in ips:
        partes = ip.split(".")
        valida = True
        mensaje = "Valida"
        # Verificar cantidad de octetos
        if len(partes) != 4:
            valida = False
            mensaje = "Invalida (faltan octetos)"
        else:
            # Validar cada octeto
            for octeto in partes:
                # Verificar si es numérico
                if not octeto.isdigit():
                    valida = False
                    mensaje = "Invalida (no numerico)"
                    break
                # Verificar rango
                numero = int(octeto)
                if numero < 0 or numero > 255:
                    valida = False
                    mensaje = "Invalida (octeto fuera de rango)"
                    break
        print(f"{ip} -> {mensaje}")
# FINALIZACIÓN DEL EJERCICIO


# ===== MENÚ PRINCIPAL DE LOS 10 EJERCICIOS=====
print ("lENGUAJE DE PROGRAMACIÓN")
print ("TAREA PRÁCTICA SEMANA 3")
# Continua el programa compilando hasta que el usuario decida salir (while true)
while True:
    print("\n--- MENÚ DE EJERCICIOS ---")
    print("Ejercicio 1 - PROTOCOLO SEGURO/INSEGURO - (opción 1)")
    print("Ejercicio 2 - VALIDACIÓN DE PUERTO - (opción 2)")
    print("Ejercicio 3 - LISTADO DE SUBRED - (opción 3)")
    print("Ejercicio 4 - LISTADO DE DISPOSITIVOS - (opción 4)")
    print("Ejercicio 5 - APAGAR SERVIDOR - (opción 5)")
    print("Ejercicio 6 - CONEXIÓN AL SERVIDOR - (opción 6)")
    print("Ejercicio 7 - VALIDACIÓN DE PUERTOS - (opción 7)")
    print("Ejercicio 8 - VALIDACIÓN LISTAS NEGRAS IP'S - (opción 8)")
    print("Ejercicio 9 - VALIDACIÓN DE DISPOSITIVO - (opción 9)")
    print("Ejercicio 10 - VALIDACIÓN DE DIRECCIONES IP'S - (opción 10)")
    print("Salir de los ejercicios - (opción 0)")
    opcion = input("Seleccione una opción: ")
# Estructuras condicionales (if , elif y else)
    if opcion == "1":
        ejercicio1()

    elif opcion == "2":
        ejercicio2()

    elif opcion == "3":
        ejercicio3()

    elif opcion == "4":
        ejercicio4()

    elif opcion == "5":
        ejercicio5()

    elif opcion == "6":
        ejercicio6()

    elif opcion == "7":
        ejercicio7()

    elif opcion == "8":
        ejercicio8()

    elif opcion == "9":
        ejercicio9()

    elif opcion == "10":
        ejercicio10()

    elif opcion == "0":
        print("Programa finalizado")
        break
    else:
        print("Opción inválida")

# ===== FINALIZACIÓN DE LOS EJERCICIOS Y TAREA =====
# ===== GRACIAS LA ATENCIÓN PRESTADA =====