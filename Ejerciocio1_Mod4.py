def Opcion():
	global opcion
	opcion=int(input("Elige una opción \n1.Tupla\n2.-Lista "))
def EntradaLista():
	global lista,op
	op=3
	lista=[]
	if(opcion==1):
		for i in range(0,4,1):
			nom=input("Introduce 10 nombres ")
			lista.append(nom)
def EntradaTupla():
	global miTupla,opi
	opi=0
	miTupla=('')	
	if(opcion==2):
		opi=4
		for i in range(0,3,1):
			entrada=input("Escibe precios de productos ")
			miTupla=miTupla+" "+(entrada)
def SalidaLista():
	if(op==3):

		print("Utilizando el metodo for ")
		for element in lista:
			print (element)
		print(lista[1:2])
		print(lista[1:3])
		print(lista[1:4:2])
def SalidaTuplas():
	if(opi==4):

		print("Tupla Completa ",miTupla)
		print("Longitud ",len(miTupla))
		print("Lo que contiene t1 ",miTupla)
		print("Lo que contiene t2",miTupla)
		print("posicion 0 ",miTupla[0])
		print("posicion 1 ",miTupla[1])
		print("posicion despues de 1 ",miTupla[2:])
		print("posicion desde ña -2 ",miTupla[:-2])

Opcion()
EntradaLista()
EntradaTupla()
SalidaLista()
SalidaTuplas()
