#!/usr/bin/python

# In python everything is an object
# a variable is a reference to an object
# each object has an identity or an ID

x = 1
print(type(x))
print(id(x))
#####################
# class 'int'
# 139113568
####################
# number, string, tuple -> inmutable
# list, dictionary -> mutable 

x = 1
y = 1
print(type(x))
print(id(x))
print(type(y))
print(id(y))

if x==y:
    print("True")
else:
    print("False")
if x is y:
    print("True")
else:
    print("False")

##################
# see the last two lines, both are true # class 'int'
# 139113568
# class 'int'
# 139113568
# True
# True
##################
a = dict(x = 1, y = 1)
print(type(a))
print(id(a))
b = dict(x = 1, y = 1)
print(id(b))
if a == b:
    print("True")
else:
    print("False")
if a is b:
    print("True")
else:
    print("False")


