import math

print("#####################")
print("   Gauss - Jordan   ")
print("##################### \n")

n = int(input("Ingrese la cantidad de variables de la matriz: "))

matriz = []

#Crear Matriz
for i in range(n):
    rows = []

    for j in range(2*n):
        rows.append(0)

    matriz.append(rows)
    matriz[i][n+i] = 1

#Solicitar Informacion
for row in range(n):
    for col in range(n):
        matriz[row][col] = float(input(f"Ingrese un numero entero [{row+1}][{col+1}]: "))


print()
print("Matriz ingresada: \n")
for row in matriz:
    for element in row:
        print(round(element,4), end=" \t")

    print()


for k in range(n):
    for i in range(n):
        if i != k:

            factor = (matriz[i][k])/(matriz[k][k])

            for j in range(2*n):
                matriz[i][j] = matriz[i][j] - (factor*matriz[k][j])

print()
print("Matriz modificada: \n")
for row in matriz:
    for element in row:
        print(round(element,4), end=" \t")

    print()

for i in range(n):
    for j in range(n,2*n):
        matriz[i][j] = (matriz[i][j])/(matriz[i][i])
    
    matriz[i][i] = 1

print()
print("Matriz unitaria: \n")
for row in matriz:
    for element in row:
        print(round(element,4), end=" \t")

    print()
