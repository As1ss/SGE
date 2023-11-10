"""
Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

"""
print("Hola mundo")

"""
Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

"""

saludo = "¡Hola Mundo!"
print(saludo)

"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla
la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

"""

#nombre = input("Introduce tu nombre: ")
#print(f"¡Hola {nombre}!")


"""
Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
 


"""

operacion = ((3+2)/(2*5))**2
print(str(operacion))


"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


print("Buenas, este es el calculador de dineros por currar")
horas = int(input("¿Cuántas horas has trabajado?"))
costePorHora = int(input("¿Cuánto te pagan la hora?"))
cantidadFinal = horas*costePorHora
print(f"El dinero total por currar es: {str(cantidadFinal)}")

"""

"""
Ejercicio 6
Escribir un programa que lea un entero positivo, 
n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n
. La suma de los n
 primeros enteros positivos puede ser calculada de la siguiente forma:
 

 num = int(input("Introduce un número: "))

suma = num*(num+1)/2

print(f"La suma de los primeros números enteros desde 1 hasta {str(num)} es {str(suma)}")


"""





"""

Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y 
muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.




peso = float(input("Introduce tu peso: "))
altura = float(input("Introduce tu altura: "))
imc = peso/(altura*altura)
print(f"Tu imc es: {round(imc)}")

"""




"""

Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los 
números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.



num1 = float(input("Introduce un número: "))
num2 = float(input("Introduce otro número: "))

cociente = num1/num2
resto = num1%num2

print(f"El número {num1}/{num2} da un cociente de {round(cociente)} y un resto de {round(resto)}")

"""


"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual: "))
numAños = int(input("Introduce el número de años"))

capitalObtenido = cantidad+((cantidad*interes)*numAños)

print(f"El capital obtenido de {str(cantidad)} a {str(interes)} en {str(numAños)} años es de {str(capitalObtenido)}")
"""




"""

Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada 
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

pesoClown = 112
pesoMuñeca = 75

numClowns = int(input("Introduce el número de payasos que quieres pedir: "))
numMuñecas = int(input("Introduce el número de muñecas que deseas pedir: "))

pesoTotal  = (numClowns*pesoClown) + (numMuñecas*pesoMuñeca)

print(f"El peso total de los {str(numClowns)} payasos y {str(numMuñecas)} muñecas es de {str(pesoTotal)}")
"""



"""

Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, 
segundo y tercer años. Redondear cada cantidad a dos decimales.

cantidadAhorros = float(input("Introduce cantidad de la cuenta de ahorros inciial: "))
interes = 0.04
cantidadActualizada = cantidadAhorros+(cantidadAhorros*interes)
cantidadAhorros=cantidadActualizada
print(f"Ahorros despues del primero año: {str(round(cantidadAhorros,2))}")
cantidadActualizada = cantidadAhorros+(cantidadAhorros*interes)
cantidadAhorros=cantidadActualizada
print(f"Ahorros despues del segundo año: {str(round(cantidadAhorros,2))}")
cantidadActualizada = cantidadAhorros+(cantidadAhorros*interes)
cantidadAhorros=cantidadActualizada
print(f"Ahorros despues del tercer año: {str(round(cantidadAhorros,2))}")

"""




"""

Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo 
el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


"""

precioBarraPan = 3.49
numBarras =int(input("Introduce el número de barras de pan: "))
descuento = 0.6
precioNoFreshPanete = precioBarraPan-(precioBarraPan*descuento)
precioFinal = precioNoFreshPanete*numBarras
print(f"El precio del pan es de {str(precioBarraPan)}€ pero como no es fresca el precio de las barras de pan es {str(round(precioFinal,2))}€")