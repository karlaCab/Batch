#!/usr/bin/python
#-*- coding: utf-8 -*-

x= int(input("ingresa un numero X \n"))
y= int(input("ingresa un numero Y \n"))

print(type(x))
 
if x == 3  and  y == 3:
 	print("se cumplio AND")
else:
 	print("NO")

if x == 3 or y ==3:
 	print("se cumplio OR")
else:
 	print("NO")

