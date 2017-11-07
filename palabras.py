print("Palabras en una lista")
ListaIM=[]

valores=int(input("cuantos valores vas a introducir en tu lista? "))
if valores <1:
	print("Imposible")
else:
	for i in range(0,valores):
		numeroL=str(input("Escribe la palabra "))
		ListaIM.append(numeroL)
print(ListaIM)
print("Tiene {} ".format(len(ListaIM)))

palabra=str(input("¿Que palabra quieres buscar? "))
BUSCAR=(ListaIM.index(palabra))


sustituir=str(input("¿Con que palabra quiere sustituir\n"))
ListaIM[BUSCAR]=sustituir
print(ListaIM)













		