import math
def Entrada():
	global op,num,aux
	num=int(input("Introduce un número entero. "))
	aux= num
	op=int(input("Introduce una opcion \n 1.Números Pares.\n 2.Calcular raíz de un número \n 3.Calcular Año Biciesto. \n 4.Calcular el factorial de un número "))

#Números Pares
def Pares():
	if op == 1:
		if num == 0:
			print("El número ",aux, " es par. ")
		elif num%2 == 0:
			print("El número ",aux," es par. ")
		else:
			print("El número",aux,"es impar. ")  		
#Raíz Cuadrada
def Raiz():
	if op == 2:
		print("La raiz Cuadrada de: ",aux," es ")
		print(math.sqrt(num))
#Año Biciesto
def Biciesto():
	if op == 3:
		if num % 4 == 0:
			if num % 100 == 0:
				if num % 400 == 0:
					print("El año",num,"es bisiesto")
				else:
					print("El año ",num," no es bisiesto")
			else:
				print("El año ",num," es bisiesto.")
		else:
			print("El año ",num," no es bisiesto.")
#Números factoriales
def Factorial():
	if op == 4:
		numaux=num
		aux2=aux
		print("Factorial de  Y sus resultados")
		for x in range(numaux,1,-1):
			aux2=aux2-1
			print(numaux," * ",aux2," = ",numaux*aux2)
			numaux=numaux*aux2
#Salidas	
Entrada()
Pares()
Raiz()
Biciesto()
Factorial()
