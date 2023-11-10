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
        if frutaNombre in frutas:

         for fruta, precio in frutas.items():
            if frutaNombre==fruta:
                cantidad=int(input("Introduce la cantidad a comprar: "))
                precioFinal = precio*cantidad
                break;
        else:
           print("La fruta introducida no existe")
        print(f"El precio de la compra es: {str(precioFinal)}€")

    if (opcion==2):
        frutaNombre= input("Introduce el nombre de la fruta que deseas añadir: ")
        precio = float(input("Introduce el precio de la fruta: "))
        frutas[frutaNombre]=precio
        print(f"La fruta {frutaNombre} con el precio {str(precio)} ha sido añadida a frutas")
            
    if (opcion==3):
        ejecucion=False


"""

Ejercicio 2:
Desarrolla un programa que ofrezca un menú con las siguientes opciones:

Agregar un nuevo contacto.
Buscar un contacto por nombre.
Salir del programa.
El programa deberá gestionar un listín telefónico y permitir al usuario realizar las siguientes acciones:

Cuando el usuario seleccione la opción 1, el programa le pedirá ingresar el nombre y el número de teléfono del nuevo contacto, y lo añadirá al listín telefónico.

Si el usuario selecciona la opción 2, el programa le solicitará ingresar el nombre del contacto que desea buscar. Luego, mostrará por pantalla el nombre y 
el número de teléfono del contacto si se encuentra en el listín, o mostrará un mensaje informando que el contacto no está en el listín.

La opción 3 permitirá al usuario salir del programa.


"""

contactos ={}
abrirAgenda=True

while(abrirAgenda):
   print("1) Añadir contacto")
   print("2) Mostrar contacto")
   print("3) Salir.")
   opcion = int(input("Introduce una opción."))
   if(opcion==1):
      nombreContacto = input("Introduce el nombre del contacto: ")
      numeroTlf = int(input("Introduce el número de teléfono: "))
      contactos[nombreContacto]= numeroTlf
   if (opcion==2):
      
      nombreContacto=input("Introduce el nombre dl contacto a consultar: ")
      if nombreContacto in contactos: 
        for nombre,telefono in contactos.items():
         if nombreContacto==nombre:
            print(f"Nombre: {nombre} Teléfono: {str(telefono)}")
            break;
      else:
        print("El nombre itroducido no existe.")
   if (opcion==3):
      abrirAgenda=False
      
  
      
   
      

      


