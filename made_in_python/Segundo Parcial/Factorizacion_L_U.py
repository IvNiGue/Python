import math

print("#################################")
print("   Factorizacion Lower - Upper   ")
print("################################# \n")

n = int(input("Ingrese la cantidad de variables de la matriz: "))

matriz = []
mlow = []
mupr = []

#Crear Matriz
for i in range(n):
    rows = []

    for j in range(n):
        rows.append(0)

    matriz.append(rows)   

#Solicitar Informacion
for i in range(n):
    for j in range(n):
        matriz[i][j] = float(input(f"Ingrese un numero [{i+1}][{j+1}]: "))

#Crear matriz lower
for i in range(n):
    rows2 = []

    for j in range(n):
        rows2.append(0)

    mlow.append(rows2)

for i in range(n):
    mlow[i][i] = 1

#Crear matriz upper
for i in range(n):
    rows3 = []

    for j in range(n):
        rows3.append(0)

    mupr.append(rows3)

#Presentacion matrices creadas
print()
print("Matriz ingresada: \n")
for row in range(n):
    for col in range(n):
        print(round(matriz[row][col],4), end=" \t")

    print()

"""print()
print("Matriz low: \n")
for row2 in range(n):
    for col2 in range(n):
        print(mlow[row2][col2], end=" \t")

    print()"""

#Gauss
for k in range(n-1):
    for i in range(k+1,n):
        factor = (matriz[i][k])/(matriz[k][k])

        mlow[i][k] = factor

        for j in range(n):
            matriz[i][j] = matriz[i][j] - (factor*matriz[k][j])

#Presentar matrices
print()
print("Matriz Upper: \n")
for row in matriz:
    for element in row:
        print(round(element,4), end=" \t")

    print()

print()
print("Matriz lower: \n")
for row in mlow:
    for element in row:
        print(round(element,4), end=" \t")

    print()

#Comprobacion
for i in range(n):
    for j in range(n):
        suma = 0
        for k in range(n):
            producto = mlow[i][k] * matriz[k][j]
            suma = suma + producto

        mupr[i][j] = suma

print()
print("Comprobacion: \n")
for row in mupr:
    for element in row:
        print(round(element,4), end=" \t")

    print()
