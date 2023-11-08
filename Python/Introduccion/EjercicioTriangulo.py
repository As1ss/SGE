
"Escribir un progrmar que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo como el de mas abajo, de altura el numero introducido."

"""

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

"""


altura = int(input("Introduce la altura"))

def triangulo(altura):
    if (altura>3):
        for i in range(1,altura+1):
            temp="";
            for j in range(1,i+1):
                temp +=str(j)+" "
            print(temp)
triangulo(altura)


