"""

EJERICCIOS BASICOS


"""

"""Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!."""

print("¡Hola Mundo!.")


"""

Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
"""

saludo = "¡Hola Mundo!."

print(saludo)


"""

Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

"""

##nombre = input("Introduce tu nombre: ")
##print(f"¡Hola {nombre}!")


"""

Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
 
.

"""

operacion = ((3+2)/(2*5))**2
print(f"Operacion: {str(operacion)}")


"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

"""
##horasTrabajadas = int(input("Introduce las horas trabajadas: "))
##costePorHora = int(input("Introduce el coste por hora trabajada: "))
##print(f"La paga que te corresponde es de: {horasTrabajadas*costePorHora}")

"""

Ejercicio 6
Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
. La suma de los 
 primeros enteros positivos puede ser calculada de la siguiente forma:

"""

#num = int(input("Introduce un número: "))

#suma  = num*(num+1)/2

##print(f"Ejercicio 6 suma: {str(suma)}")

"""

Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

"""

#peso = float(input("Introduce tu peso: "))
#altura = float(input("Introduce tu altura: "))

#imc=peso/(altura**2)

#print(f"Tu imc es: {round(imc,2)}")

"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> 
donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

"""

#num1 = int(input("Introduce un número: "))
#num2 = int(input("Introduce otro número: "))
#cociente = num1/num2
#resto = num1%num2
#print(f"El {num1}/{num2} da de cociente {cociente} y de resto {resto}")


"""

Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

"""

##cantidadInvertir = int(input("Introduce una cantidad a invertir: "))
##interesAnual = float(input("Introduce el interés anual: "))
##numAños = int(input("Introduce los años: "))
##capitalObtenido = cantidadInvertir+((cantidadInvertir *interesAnual) *numAños)

##print(f"El capital {cantidadInvertir} a interés de {interesAnual} en {numAños} es {capitalObtenido}")


"""

EJERCICIOS LISTAS

"""

"""
Ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

"""

asignaturas = ["Matemáticas","Física","Químca","Historia","Lengua"]

print(asignaturas)

"""

Ejercicio 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista 
y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

"""

for i in asignaturas:
    
    print(f"Yo estudio la asignatura: {i}")

"""
Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


notas = []
for i in asignaturas:
    nota = int(input(f"Introduce la nota de {i}: "))
    notas.append(nota)

for i in range(len(asignaturas)):
    print(f"Has sacado un {notas[i]} en {asignaturas[i]}")
"""




"""
Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.



numerosPremiados = []

for i in range(10):
    numero=int(input(f"{i+1} Introduce el numero premiado: "))
    numerosPremiados.append(numero)

numerosPremiados.sort()

for num in numerosPremiados:
    print(num)
"""



"""
Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

"""


listaNum = []
for i in range(10):
    listaNum.append(i+1)
listaNum.reverse()
for i in listaNum:
    print(i,end=",")

print()

"""

Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


asignaturas = ["Matemáticas","Física","Químca","Historia","Lengua"]


asignaturasSuspensas=[]

for i in asignaturas:
    nota = int(input(f"Introduce la nota de {i} "))
    if (nota>=5):
        None
    else:
       asignaturasSuspensas.append(i) 

print("Las siguientes asignaturas tienes que repetir")
for i in asignaturasSuspensas:
    print(f"Asingatura: {i}")




"""






"""

EJERCICIOS DICCIONARIOS

"""

"""

Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa 
y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

"""

divisas = {"Euro":"€", "Dollar":"$","Yen":"¥"}

divisa = input("Introduce la divisa para ver el símbolo: " )


def devolverSimbolo(moneda):
    
    for nombre,simbolo in divisas.items():
        if (nombre==divisa):
            return simbolo
    return "La divisa introducida no está"
        


        
print(devolverSimbolo(divisa))


"""
Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y 
lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje 
<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.



alumnos = {}

nombre = input(f"Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
direccion = input("Introduce tu dirección")
telefono = input("Introduce tu número: ")


alumnos[nombre]={"Edad":edad,"Direccion":direccion,"Telefono":telefono}

for i in alumnos:
    print(i)
    print(f"Edad: {alumnos[i]['Edad']}")
    print(f"Direccion: {alumnos[i]['Direccion']}")
    print(f"Telefono: {alumnos[i]['Telefono']}")
"""




"""

Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la 
tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla
 el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.


"""

frutas= {"Pera":0.85,"Platano":1.35,"Manzana":0.80,"Naranja":0.70}

salir = True

while(salir):
    print("1) Comprar fruta")
    print("2) Añadir fruta")
    print("3) Borra fruta")
    print("4) Salir.")
    opcion = int(input("Introduce una opción válida: "))
    print()
    if(opcion==1):
        fruta = input("Introduce el nombre de la fruta: ")
        for i in frutas:
            if(fruta==i):
                kilos = int(input("Introduce el peso en kg"))
        precio = frutas[i] *kilos
        print(f"El precio de la compra es de : {str(precio)}")
    if(opcion==2):
        fruta = input("Introduce el nombre de la fruta: ")
        precio =float(input("Introduce el precio de la fruta: "))
        if (fruta in frutas):
            print("La fruta ya existe compa")
        else:
            frutas[fruta] =precio
            print(frutas)
    if(opcion==3):
        fruta =input("Introduce la fruta que quieres borrar")
        if (fruta in fruta):
            del frutas[fruta]
        else:
            print("Esa fruta no existe compa")
    if (opcion==4):
        salir=False

"""

Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha
 en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

"""

fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")



meses = {"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio",
         "07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}












dia = fecha[0:2]
mes = fecha[3:5]
año = fecha[6:10]

print(f"{dia} de {meses[str(mes)]} de {año}")



