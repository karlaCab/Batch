print("contador de pares e impares ")
valores=int(input("cuantos valores vas a introducir?  "))
if valores <1:
	print("Imposible")
else:
	pares=0
	for i in range(0,valores):
		numero=int(input("escribe el valor  "+str(i)))
		if numero % 2==0:
			pares +=1
		print("Ha escrito  "+str(pares)+"numeros pares y  "+str(valores-pares)+" numeros impares")
