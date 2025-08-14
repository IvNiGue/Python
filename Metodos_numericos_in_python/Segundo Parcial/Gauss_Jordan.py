import math

print("#####################")
print("   Gauss - Jordan   ")
print("##################### \n")

n = int(input("Ingrese la cantidad de variables de la matriz: "))

matriz = []
mx = []

for row in range(n):
    rows = []
    for col in range(n+1):
        rows.append(float(input(f"Ingrese un numero entero [{row+1}][{col+1}]: ")))

    matriz.append(rows)
    mx.append(0)

print()
print("Matriz ingresada: \n")
for row in matriz:
    for element in row:
        print(element, end="\t")

    print()


for k in range(n):
    for i in range(n):
        if i != k:

            factor = (matriz[i][k])/(matriz[k][k])

            for j in range(n+1):
                matriz[i][j] = matriz[i][j] - (factor*matriz[k][j])

print()
print("Matriz modificada: \n")
for row in matriz:
    for element in row:
        print(element, end="\t")

    print()

for i in range(n):
    matriz[i][n] = (matriz[i][n])/(matriz[i][i])
    matriz[i][i] = 1

print()
print("Matriz unitaria: \n")
for row in matriz:
    for element in row:
        print(element, end="\t")

    print()
    
