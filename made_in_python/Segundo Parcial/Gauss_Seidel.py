import math

print("#####################")
print("   Gauss - Seidel   ")
print("##################### \n")

n = int(input("Ingrese la cantidad de variables de la matriz: "))

matriz = []
mxant = []
mxact = []
merrors = []

#Crear Matriz
for i in range(n):
    rows = []

    for j in range(n+1):
        rows.append(0)

    mxant.append(0)
    mxact.append(0)
    merrors.append(1)
    matriz.append(rows)
    

#Solicitar Informacion
for row in range(n):
    for col in range(n+1):
        matriz[row][col] = float(input(f"Ingrese un numero entero [{row+1}][{col+1}]: "))


#Gauss Seidel
print()
print("Matriz ingresada: \n")
for row in matriz:
    for element in row:
        print(round(element,4), end=" \t")

    print()

error = 1
ep = pow(10,-6)

ite = 0
itmax = 100

bandera = 0

cont = 0
suma = 0

for i in range(n):
    for j in range(n):
        if i != j:
            suma = suma + matriz[i][j]

    if abs(matriz[i][i]) > abs(suma):
        cont += 1

if cont == n:
    bandera = 1

else:
    print("Falla por convergencia \n")

while bandera == 1 and error > ep and ite < itmax:
    for i in range(n):
        suma = 0

        for j in range(n):
            if i != j:
                suma = suma + (matriz[i][j]*mxant[j])

        mxact[i] = (matriz[i][n] - suma)/matriz[i][i]

    aux = 0

    for i in range(n):
        merrors[i] = abs((mxact[i] - mxant[i])/mxact[i])

        if merrors[i] > aux:
            aux = merrors[i]

    error = aux
    ite += 1
    for i in range(n):
        mxant[i] = mxact[i]

#Presentar resultados

print("Errores:")

for i in range(n):
    print(merrors[i])
    
print()

print("Resultados:")

for i in range(n):
    print(mxact[i])
    
print()

print(f"Operaciones realizadas: {ite*n*(n-1)} \n")
print(f"Operaciones si se hubiera utilizado gauss: {n*(pow(n,2)-1)}")

                

