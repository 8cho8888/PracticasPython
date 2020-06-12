#Hace algo y no imprime ningun valor
def Ejemplo():
	print("Imprime algo")
#Ejemplo con parametros
def Ejemplo2(num1,num2):
	s=num1+num2
	print(s)
#Ejemplo con retorno sin parametro
def Ejemplo3():
	s=5+8
	return s
#Ejemplo con parametros y retorno	
def Ejemplo4(num1,num2):
	s=num1+num2
	return s
Ejemplo2(9,9)
y=Ejemplo3()
print(y)
print(Ejemplo3())

y=Ejemplo4(8,8)
print(y)
