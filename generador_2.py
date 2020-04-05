#!/bin/usr/python


#Cuando ponemos un asterisco significa que no sabemos
# cuantos elementos le vamos a pasar a la funcion y lo va 
# recibir en forma de tupla
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento
       # yield elemento
ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
