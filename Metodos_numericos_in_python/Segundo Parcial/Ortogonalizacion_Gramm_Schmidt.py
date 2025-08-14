import math

print("####################################")
print("   Ortogonalizacion Gramm Schmidt   ")
print("#################################### \n")

n = int(input("Ingrese la cantidad de variables de la matriz: "))

matriz = []

#Crear Matriz
for i in range(n):
    rows = []

    for j in range(2*n):
        rows.append(0)

    matriz.append(rows)
    

#Solicitar Informacion
for row in range(n):
    for col in range(n,2*n):
        matriz[row][col] = float(input(f"Ingrese un numero entero [{row+1}][{col+1}]: "))

print()
print("Matriz ingresada: \n")
for row in matriz:
    for element in row:
        print(round(element,4), end=" \t")

    print()

#Producto punto
for i in range(n):
    for j in range(n,2*n):
        suma = 0
        for k in range(n,2*n):
            producto = matriz[i][k] * matriz[j-n][k]
            suma = suma + producto

        matriz[i][j-n] = suma

print()
print("Productos puntos con los vectores ingresados: \n")
for row in matriz:
    for element in row:
        print(round(element,4), end=" \t")

    print()

#Operaciones de Ortogonalizacion (reduccion gaussiana)
for k in range(n-1):
    for i in range(k+1,n):
        factor = (matriz[i][k])/(matriz[k][k])

        for j in range(2*n):
            matriz[i][j] = matriz[i][j] - (factor*matriz[k][j])

print()
print("Vectores Ortogonalizados: \n")
for row in matriz:
    for element in row:
        print(round(element,4), end=" \t")

    print()
