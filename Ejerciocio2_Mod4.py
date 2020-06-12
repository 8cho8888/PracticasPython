#Definiendo Valores
def Telefonos():
	global tel 
	tel={}
#Ciclo 
def Ciclo():
	global op
	op=int(input("Introduce una opción.\n1.Agregar números\n2.Mostar Datos del diccionario.\n3.-Eliminar Datos\n4.Modificar Datos\n0. Para terminar"))
	while op!= 0:
		if(op==1):
			Agregar(op)
			op=int(input("Que deseas hacer 1.ADD  2.LIST  3.DELETE  4.UPDATE "))
		if(op==2):
			Mostrar(op)
			op=int(input("Que deseas hacer 1.ADD  2.LIST  3.DELETE  4.UPDATE "))
		if(op==3):
			Eliminar(op)
			op=int(input("Que deseas hacer 1.ADD  2.LIST  3.DELETE  4.UPDATE "))
		if (op==4):
			Editar(op)
			op=int(input("Que deseas hacer 1.ADD  2.LIST  3.DELETE  4.UPDATE "))
	print("Fin del ciclo")		
#ADD
def Agregar(op):
	cont=input("Agrega el nombre de contacto ")
	numero=int(input("Introduce un número nuevo "))
	valor= tel.setdefault(cont,numero)
#LIST
def Mostrar(op):	
	print("Esta es la lista ",tel)
#DELETE
def Eliminar(op):
	print("Lista Actual ",tel)
	el=input("Introduzca el contacto que desea eliminar")
	del tel[el]
	print("Se elimino correcta el elemento ",el," de la lista.\n",tel)
#UPDATE
def Editar(op):
	print("Lista Actual ",tel)
	update=input("Introduzca el contacto que desea actualizar")
	new=input("Introduzca el nuevo nombre")
	tel[update]=new
	print("Se actualizo correctamente el elemento ",update," y cambio a ",new," de la lista.\n",tel)
#Salida
Telefonos()
Ciclo()
