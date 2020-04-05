#!/bin/usr/python

def generapares(limite):
    
    num = 1;
    lista = []

    while num<limite:
        lista.append(num*2)
        num = num+1

    return lista

print(generapares(100))
