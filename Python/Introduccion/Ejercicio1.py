
"1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!."

print("Hola mundo!")

"2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable."
var ="Hola mundo!"
print(var)

"""
3.- Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca 
muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""
nombre = input("Ingrese su nombre: ")
print("Hola",nombre)

"4.- Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2)/(2*5)**2."
print((3+2)/(2*5)**2)

"5.-Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde."
horasTrabajadas = input("¿Cuántas horas has trabajado?")
costePorHora = input("¿Cuánto cobrabas por hora?")
print("Tu salario es de "+str(int(horasTrabajadas)*int(costePorHora))+"€")

"""6.- Escribir un programa que lea un entero positivo, n
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
n. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:"""

num = int(input("Introduce un número: "))
sumaTotal =0
for i in range(1,num+1):
    sumaTotal+=i

print("La solución es "+str(sumaTotal))

"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
estatura = float(input("Escribe tu altura en m: "))
peso = float(input("Escribe tu peso: "))
imc = peso/(estatura**2)
print(f"Tu IMC es: {round(imc,2)}%")


"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
 y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""


"Escribir un progrmar que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo como el de mas abajo, de altura el numero introducido."

"""

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

"""


altura = input(int("Introduce la altura"))

def triangulo(altura):
    if (altura>3):
        for i in range(1,altura):
            print(i)

triangulo(altura)
