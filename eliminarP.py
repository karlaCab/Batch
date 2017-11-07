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

palabra=str(input("¿Que palabra quieres eliminar "))

for i in ListaIM:
	if i==palabra:
		eliminar=ListaIM.remove(palabra)
print(ListaIM)
