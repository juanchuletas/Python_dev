#!/bin/usr/python

def generapares(limite):
    
    num = 1;

    while num<limite:

        yield num*2

        num = num+1
devuelvePares = generapares(10) #objeto iterable

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))
