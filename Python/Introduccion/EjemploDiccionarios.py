
frutas ={"plátano":1.35,
         "manzana":0.80,
         "pera":0.85,
         "naranja":0.70
}

for i in frutas:
            print(i)

while True:
    print("Menú:")
    print("1. Consultar el precio de una fruta")
    print("2. Añadir una nueva fruta y su precio")
    print("3. Salir del programa")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
         # Consultar precio de una fruta
         fruta = input("Introduce el nombre de la fruta.")
         precio = frutas.get(fruta)
         if (precio is None):
             print("La fruta introducida {frutaName} no existe")
             
         else:
             print("El precio de la {frutaName} es {precio}")

         fruta=None
         precio=None
         
    elif opcion == '2':
        # Añadir una nueva fruta y su precio
        fruta = input("Introduce el nombre de la fruta.")
        precio = float(input("Introduce el precio de la fruta."))
        frutas[fruta] = precio
       

      




        pass

    elif opcion == '3':
        # Salir del programa
        pass

    else:
        print("Opción no válida. Por favor, elige una opción del menú.")






