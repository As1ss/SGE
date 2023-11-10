plantilla_ud_las_palmas = {
    "Brindisi": {
        "posición": "Delantero",
        "nacionalidad": "Argentina",
    },
    "Vicente González": {
        "posición": "Portero",
        "nacionalidad": "Española",
    },
    "Héctor Núñez": {
        "posición": "Delantero",
        "nacionalidad": "Uruguay",
    },
    "Quique Wolff": {
        "posición": "Delantero",
        "nacionalidad": "Argentina",
    },
    "Tonono": {
        "posición": "Centrocampista",
        "nacionalidad": "Española",
    },
    "Ortega": {
        "posición": "Desconocida",
        "nacionalidad": "Española",
    },
    "Juan Guedes": {
        "posición": "Mediocampista",
        "nacionalidad": "Española",
    },
    "Castellano": {
        "posición": "Defensor",
        "nacionalidad": "Española",
    },
    "Cardona": {
        "posición": "Centrocampista",
        "nacionalidad": "Española",
    },
    "Ufarte": {
        "posición": "Centrocampista",
        "nacionalidad": "Francesa",
    },
    "Noly": {
        "posición": "Extremo",
        "nacionalidad": "Italiana",
    },
    "Mesa": {
        "posición": "Extremo",
        "nacionalidad": "Española",
    },
    "Ito": {
        "posición": "Defensor",
        "nacionalidad": "Española",
    },
    "Padrón": {
        "posición": "Defensor",
        "nacionalidad": "Italiana",
    },
    "Soto": {
        "posición": "Defensor",
        "nacionalidad": "Polaca",
    }
}

lista = []


for nombre,atributo in plantilla_ud_las_palmas.items():
    if atributo.get("nacionalidad") not in lista:
        lista.append(atributo.get("nacionalidad"))
    
   
print(lista)
suma =0
k=0


for i in range(0,64):
    suma+=i
    j=2
    k=j*suma
    print(k)
