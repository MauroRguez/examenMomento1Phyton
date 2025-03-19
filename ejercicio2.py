frutas = []

for i in range(10):
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

    