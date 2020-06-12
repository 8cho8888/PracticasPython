#Hace algo y no imprime nin
def Entrada():
	global lista
	lista = []
	for i in range(0,3,1):
		nom=input("Agrega un nombre ")
		lista.append(nom)
def Mostrar():
	print(lista)

Entrada()
Mostrar()

