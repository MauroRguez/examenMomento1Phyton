import random
helados = []
conjuntoID = set()
opcion = 0

while opcion != 5:
    print("1. Crear un helado")
    print("2. Ver la lista de helados")
    print("3. Modificar un helado")
    print("4. Eliminar un helado")
    print("5. Salir")
    opcion = int(input("Ingresa la opcion que deseas realizar: "))

    if opcion == 1:
        print("Crear un helado")
        helado = {}
        while True:
            helado["id"] = random.randint(1, 100)
            if helado["id"] not in conjuntoID:
                conjuntoID.add(helado["id"])
                break
        helado["nombre"] = input("Ingresa el nombre de tu helado: ")
        helado["descripcion"] = input("Ingresa la descripcion de tu helado: ")
        helado["precio"] = int(input("Ingresa el precio de tu helado: "))
        helados.append(helado)

    elif opcion == 2:
        print("Ver la lista de helados")
        for heladoIngresados in helados:
            print('ID:'+ {heladoIngresados["id"]})
            print('Nombre: '+{heladoIngresados["nombre"]})
            print('Descripcion: '+{heladoIngresados["descripcion"]})
            print('Precio: '+{heladoIngresados["precio"]})
            print("__________**********___________")
    elif opcion ==3:
        print("Modificar un helado")
        id = int(input("Ingresa el ID del helado que deseas modificar: "))
        for heladoIngresados in helados:
            if heladoIngresados["id"] == id:
                while True:
                    print("1. Modificar nombre")
                    print("2. Modificar descripcion")
                    print("3. Modificar precio")
                    print("4. Salir")
                    opcion = int(input("Ingresa la opcion que deseas realizar: "))
                    if opcion == 1:
                        heladoIngresados["nombre"] = input("Ingresa el nuevo nombre: ")
                    elif opcion == 2:
                        heladoIngresados["descripcion"] = input("Ingresa la nueva descripcion: ")
                    elif opcion == 3:
                        heladoIngresados["precio"] = int(input("Ingresa el nuevo precio: "))
                    elif opcion == 4:
                        break;
    elif opcion  ==4:
        print("Eliminar un helado")
        id = int(input("Ingresa el ID del helado que deseas eliminar: "))
        for heladoIngresados in helados:
            if heladoIngresados["id"] == id:
                helados.remove(heladoIngresados)
                break;
