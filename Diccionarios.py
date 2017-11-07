diccionario={'nombre':'Carlos','edad':22,'cursos':['python','Flask']} #por medio de las keys se manejan los diccionarios

print(diccionario)
print(diccionario['nombre'])
print(diccionario['cursos'][0])

dic=dict(nombre='nestro',apellido='juarez',edad=22)
#print(dic['nombre'])
print('----------------------------------------')

#iterar un diccionario
for key,value in diccionario.items():
	print(key+":"+str(value))

lista_cursos=diccionario['cursos']#esta variable esta dentro ya
lista_cursos.append('java')
print(lista_cursos)
print(diccionario)

print('----------------------------------------')

print(len(diccionario))

#devuelve una lista con las claves del diccionario-metodo
print(diccionario.keys())
#devuelve una lista con los valores del diccionario-metodo
print(diccionario.values())

#traer valores con su clave o trae uno por default
print(diccionario.get("nombre","juanito"))

#insertar elementos al diccionario
diccionario['key']='value'
print(diccionario)

#borrar elemento con la clave
diccionario.pop('key')
print(diccionario)
#devuelve la copia del diccionario
diccionario2=diccionario.copy()
print(diccionario2)
#añade los elementos de un diccionario
diccionario.update(dic)
print(diccionario)
