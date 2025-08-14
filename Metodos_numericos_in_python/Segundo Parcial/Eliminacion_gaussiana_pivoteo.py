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
        print(round(element,5), end="\t")

    print()

contador = 0 # contador de pivoteos
for k in range(n-1):
    for i in range(k+1,n):
        #Pivoteo
        factor = 1
        bandera = 0
        z = i
        

        if matriz[k][k] == 0:
            contador += 1
            
            while bandera == 0:
                if matriz[z][k] != 0:
                    for r in range(n+1):
                        aux = matriz[k][r]
                        matriz[k][r] = matriz[z][r]
                        matriz[z][r] = aux

                    bandera = 1
                else:
                    z += 1

                if z >= n:
                    bandera = 2

                z = i

            #Cambio de columnas (en caso de que cambiar renglones falle)
            while bandera == 2:
                if matriz[k][z] != 0:
                    for r in range(n+1):
                        aux = matriz[r][k]
                        matriz[r][k] = matriz[r][z]
                        matriz[r][z] = aux

                    bandera = 1

                else:
                    z += 1
                        
                if z >= n:
                    bandera = 3
                    print("Matriz no valida")
        
        #Fin Pivoteo

        if bandera != 3:
        
            factor = (matriz[i][k])/(matriz[k][k])

            for j in range(n+1):
                matriz[i][j] = matriz[i][j] - (factor*matriz[k][j])

print()
print("Matriz modificada: \n")
for row in matriz:
    for element in row:
        print(round(element,5), end="\t")

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
    print(round(row,5))

print()
print("Determinante:")

det = pow(-1,contador)
for k in range(n):
    det *= matriz[k][k]

print(det)
    

    
