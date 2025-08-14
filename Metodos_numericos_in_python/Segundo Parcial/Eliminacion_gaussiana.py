import math

print("#####################")
print("Eliminacion Gaussiana")
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


for k in range(n-1):
    for i in range(k+1,n):
        factor = (matriz[i][k])/(matriz[k][k])

        for j in range(n+1):
            matriz[i][j] = matriz[i][j] - (factor*matriz[k][j])

print()
print("Matriz modificada: \n")
for row in matriz:
    for element in row:
        print(element, end="\t")

    print()

mx[n-1] = (matriz[n-1][n])/matriz[n-1][n-1]

for i in range(n-2,-1,-1):
    suma = 0
    

    for j in range(n-1,i,-1):
        
        suma = suma + (matriz[i][j] * mx[j])

    mx[i]=(matriz[i][n] - suma)/matriz[i][i]

print()
print("Matriz de valores dependientes: \n")
for row in mx:
    print(row)
    
    
