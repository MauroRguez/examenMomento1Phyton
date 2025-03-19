#Ejercicio 2: Ordenamiento de Frutas en un Salpicón
#En este ejercicio, se requiere desarrollar un programa en Python que
#permita registrar y organizar un conjunto de frutas con sus respectivos
#precios dentro de un salpicón.
#ngreso de frutas:
#El programa debe solicitar al usuario el ingreso de 10 frutas, cada una con
#su nombre y precio.
#Almacenar la información en una lista de diccionarios.
#Ordenamiento:
#Una vez ingresadas las 10 frutas, el programa deberá ordenarlas de mayor
#a menor precio y mostrar la lista en pantalla.
#Deben asegurarse de implementar un algoritmo de ordenamiento
#adecuado para organizar las frutas correctamente y presentar los
#resultados de forma clara.

frutas = []

for i in range(4):
    fruta = {}  
    fruta["nombre"] = input(f"Ingrese el nombre de la fruta {i + 1}: ")
    fruta["precio"] = int(input(f"Ingrese el precio de la fruta {i + 1}: "))
    print("----------------------")
    frutas.append(fruta)


for fruta in frutas:
    print(f"Nombre: {fruta['nombre']}, Precio: {fruta['precio']}")

# Ordenar las frutas de mayor a menor precio
for i in range(len(frutas) - 1):
    for j in range(len(frutas) - 1):
        if frutas[j]["precio"] < frutas[j + 1]["precio"]:
            frutas[j], frutas[j + 1] = frutas[j + 1], frutas[j]
print("_________________________")            
print("Frutas ordenadas de mayor a menor precio:")
for fruta in frutas:
    print(f"Nombre: {fruta['nombre']}, Precio: {fruta['precio']}")

    