"""programa 1"""
lista=range(1,100)
print(lista)

"""programa 2"""
x= int(input("ingresa un numero \n"))
rango=range(1,10)
for i in rango:
	producto=x*i
	print(str(x)+"*"+str(i)+"="+str(producto))

"""programa 3"""
lista1=[4,76,3,12,65,3]
print(lista1)
lista2=[234,222,523,65]
print(lista2)
sumalist=[]

sumalist.extend(lista1)
sumalist.extend(lista1)
print(sumalist)

suma=0
for i in sumalist:
	suma +=i
	print(suma)




