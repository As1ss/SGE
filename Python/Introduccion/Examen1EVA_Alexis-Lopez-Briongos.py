
"""

1. (2 puntos) Operaciones:

Escribe un programa llamado operaciones que, dados dos números, realice las operaciones de suma, 
resta, multiplicación y división, e imprima los resultados  de una de las dos maneras que te muestro a continuación:

operaciones(5,2) -> "Suma: 7, Resta: 3, Multiplicación: 10, División: 2.5"
operaciones(5,2) -> "Suma: 7"
                   "Resta: 3"
                   "Multiplicación: 10"
                   "División: 2.5"

"""

num1 = 5
num2= 2

def operaciones(num1,num2):
    suma= num1+num2
    resta = num1-num2
    mult = num1*num2
    divi= num1/num2
    return f"Suma: {str(suma)}, Resta: {str(resta)}, Multiplicación: {str(mult)}, División: {str(divi)}"

print(operaciones(num1,num2))


"""

2. (2.5 puntos) Números Primos:

Escribe un programa llamado es_primo() que determine si es primo o no, devolviendo verdadero si lo es y falso si no

es_primo(3) -> True
es_primo(121) -> False

"""

num3=80
num4=213

def es_primo(n):
  if n%2==0 and n!=2:
   return False
  else:
       return True
   
     
              
              

print(es_primo(num3))
print(es_primo(num4))

"""
3. (2.5 puntos) Listas: 

Implementa una función llamada utilidades_listas() que tome una lista de números y realice las siguientes operaciones:

Muestra la lista original.
Calcula la suma de los elementos.
Encuentra el valor máximo y mínimo.
Imprime la lista ordenada de menor a mayor.
utilidades_listas([2, 5, 1]) -> "Lista original: [2, 5, 1]"
                              "Suma de sus elementos: 8"
                              "Valor máximo: 5"
                              "Valor mínimo: 1"
                              "Lista ordenada: [1, 2, 5]"

"""

numeros = [2,5,1]

salir = False

def utilidades_lista(numeros):
    print(f"Lista original: {numeros}")
    suma = numeros[0]+numeros[1]+numeros[2]
    print(f"Suma de sus elementos: {suma}")
    numeros.sort()
    numMax = numeros[2]
    numMin = numeros[0]
    print(f"Valor máximo: {numMax}")
    print(f"Valor mínimo: {numMin}")
    print(f"Lista ordenada: {numeros}")

utilidades_lista(numeros)
       
    
"""

4. (3 puntos) Diccionarios:

Desarrolla un programa que simule una agenda de contactos. Utiliza un diccionario donde las 
claves son los nombres y los valores son sus números de teléfono. Permite al usuario agregar 
nuevos contactos, buscar un número de teléfono por nombre y eliminar contactos.

Apóyate en este código para que te sea más sencillo:


"""
agenda = {}

salir = False
while (salir==False):
    print("\n*** Menú de Agenda ***")
    print("1. Agregar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        nombre=input("Introduce el nombre del contacto que deseas agregar: ")
        numTlf = input("Introduce el número del teléfono del nuevo contacto: ")
        agenda[nombre]= numTlf
        print("El contacto ha sido añadido")

    elif opcion == "2":
        nombre=input("Introduce el nombre del contacto que deseas consultar: ")
        for nombreC,telefono in agenda.items():
            if (nombre==nombreC):
                print(f"Nombre: {nombreC} Teléfono: {telefono}")
            else:
                print("El contacto introducido no existe")

    elif opcion == "3":
        nombre = input("Introduce el nombre del contacto que desea eliminar: ")
        for nombreC,telefono in agenda.items():
            if (nombre==nombreC):
                del agenda[nombre]
                print("El contacto ha sido eliminado")
                print(agenda)
            else:
                print("El contacto introducido no existe")
           
    elif opcion == "4":
        for nombreC,telefono in agenda.items():
            print(f"Nombre: {nombreC} Teléfono: {telefono}")
    elif opcion == "5":
	    salir=True
else:
            print("Opción no válida, seleccione del 1 al 5")

   
    
   


