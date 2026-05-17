print ("ALGORITMOS Y FUNDAMENTOS DE PROGRAMACIÓN")
print ("EVALUACIÓN PRÁCTICA 2")
print ("ALexis Añamise")
print ("EJERCICIO 3")
print ("Desarrolle un programa en Python que:")
print (" - Defina una función calcular_factorial(n)")
print (" - Use un ciclo for para calcular el factorial")
print (" - Solicite el número al usuario y muestre el resultado")
print ("")
print ("CALCULO FACTORIAL")
#PROCESO
def cal_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
num = int(input("Ingrese un número entero positivo: "))
resul = cal_factorial (num)
print("El factorial de", num, "es:", resul)
print("")
print ("FINALIZACIÓN DEL EJERCICIO")
#FINALIZACIÓN DE LA EVALUACIÓN