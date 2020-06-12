dicto={"gato":"chat","perro":"chien","caballo":"cheval"}
numeroTel={"Jefe":5552324,"Suszy":244353533423}
diccionarioVacio={}
print(dicto)
print(numeroTel)
print(diccionarioVacio)
print("gato...",dicto["gato"])
print("\n")

#Creando una lista de busquedad
palabras=["gato","leon","caballo"]
for palabra in palabras:
	if palabra in dicto:
		print(palabra," => ",dicto[palabra])
	else:
		print(palabra,"No esta en el diccionario")

#Metodo KEYS
for clave in dicto.keys():
	print(clave," -> ",dicto[clave])
#Metodo Shorted
for key in dicto.keys():
	print(key," -> ",dicto[key])
print("\nMetodo Ordenado\n")
for key in sorted(dicto.keys()):
	print(key," -> ",dicto[key])

#Items que regresa un par de tuplas
print("Usando items\n")

for palEsp,palFra in dicto.items():
	print(palEsp," -> ",palFra)

print("Con VALUES muestra una lista \n")
#Con values que regresa una lista
for french in dicto.values():
	print(french)
#Modificar un diccionario
dicto["gato"]= "minou"
print(dicto)
#Agregar-----
dicto["cisne"]="cygne"
dicto.update({"pato":"canard"})
print(dicto)
#Eliminar------Verificar que exista el elemento
del dicto["perro"]
print(dicto)
#------Elimina el ultimo elemento
dicto.popitem()

def funDicc(dict):
	print("Desde el metodo\n")
	print(dicto)
funDicc(dicto)
