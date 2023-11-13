peliculas={
    "Pesadilla antes de navidad": "Tim Burton",
    "Kill Bill": "Quentin Tarantino",
    "Los odiosos ocho": "Quentin Tarantino",
    "Django": "Quentin Tarantino",
    "Reservoir Dogs": "Quentin Tarantino",
    "Cerrado hasta el amanecer": "Quentin Tarantino",
    "Pulp fiction": "Quentin Tarantino",
    "Eduardo Manostijeras": "Tim Burton",
    "HellBoy": "Guillermo del Toro",
}

# print(peliculas.keys())

#Modo clave,valor
for pelicula,director in peliculas.items():
    if director == "Quentin Tarantino":
        print(f"Pelicula: {pelicula}")

#Modo comparar las claves
for i in peliculas.keys():
    if peliculas[i] =="Quentin Tarantino":
        print(f"Pelicula: {i}")
    if peliculas.get(i)=="Quentin Tarantino":
        print(f"Peliculasss: {i}")