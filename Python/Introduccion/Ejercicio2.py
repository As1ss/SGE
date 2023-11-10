"""
Ejercicio 1:
Desarrolla un programa que ofrezca un menú con las siguientes opciones:

Consultar el precio de una fruta.
Añadir una nueva fruta y su precio al diccionario de precios.
Salir del programa.
El programa deberá guardar en un diccionario los precios de las frutas previamente definidas. Cuando el usuario seleccione la opción 1, 
el programa deberá preguntar al usuario por el nombre de la fruta y la cantidad en kilos que desea comprar, y 
luego mostrará por pantalla el precio total de esa cantidad de fruta. Si la fruta no está en el diccionario, 
se mostrará un mensaje informando al usuario. Si elige la opción 2, el programa le pedirá ingresar el nombre de la nueva fruta y 
su precio por kilo, y la añadirá al diccionario de precios. La opción 3 permitirá al usuario salir del programa.

Puedes usar esta tabla como ejemplo:

"""
frutas = {"Plátano":1.35,
          "Manzana":0.80,
          "Pera":0.85,
          "Naranja":0.70}

ejecucion = True

while(ejecucion):
    print("1) Comprar fruta.")
    print("2) Añadir fruta.")
    print("3) Salir.")
    opcion = int(input("Introduce una opción: "))

    if(opcion==1):
        frutaNombre=input("Introduce el nombre de la fruta que deseas comprar: ")
        precioFinal=0
        for fruta, precio in frutas.items():
            print(f"{str(fruta)} {str(precio)}")
            if fruta==frutaNombre:
                print("ESTA DENTRO")
            """
            if frutaNombre==fruta:
                cantidad=int(input("Introduce la cantidad a comprar"))
                precioFinal = precio*cantidad
                break
            else:
                print("La fruta introducida no existe")
            """
            
    print(f"El precio de la compra es: {str(precioFinal)}")

    if (opcion==3):
        ejecucion=False


