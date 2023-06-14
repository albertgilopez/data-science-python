print("******************************")
print("EJERCICIOS PYTHON DATA SCIENCE")
print("******************************")

# Ejercicio 1
print("EJERCICIO 1. Calcula ocho menos 5")

ejercicio1 = 8-5
print("El resultado del ejercicio 1 es {}.".format(ejercicio1))

# Ejercicio 2
print("EJERCICIO 2. Calcula 4 al cuadrado")

ejercicio2 = 4 ** 2
print("El resultado del ejercicio 2 es {}.".format(ejercicio2))

# Ejercicio 3
print("EJERCICIO 3. Comprueba si 8 es diferente de 9")

ejercicio3 = 8 != 9
print("El resultado del ejercicio 3 es {}.".format(ejercicio3))

# Ejercicio 4
print("EJERCICIO 4. En una sola línea asigna 'Albert' a la variable nombre y 'Gil' a la variable apellido, y en otras 2 líneas imprime cada uno")

nombre = "Albert"
apellido = "Gil"
print("El resultado del ejercicio 4 es {} {}.".format(nombre,apellido))

# Ejercicio 5
print("EJERCICIO 5. Usando las variables anteriores imprime de forma dinámica (usando format) la frase 'Me llamo Albert y me apellido Gil'")

nombre = "Albert"
apellido = "Gil"
print("Me llamo {} y mi apellido es {}.".format(nombre,apellido))

# Ejercicio 6
print("EJERCICIO 6. Crea una variable frase que contenga 'Me llamo Albert y me apellido Gil'. Y después pásalo todo a mayúsculas")

ejercicio6 = 'Me llamo Albert y me apellido Gil'
print(ejercicio6.upper())

# Ejercicio 7
print("EJERCICIO 7. Crea una lista (sin picarla a mano) que se llame lista_palabras y que contenga todas las palabras de la frase anterior. Después sácala por consola.")

lista_palabras = ejercicio6.split()
print(lista_palabras)

# Ejercicio 8
print("EJERCICIO 8. Cuenta cuantas palabras hay en lista_palabras")

lista_palabras = len(lista_palabras)
print("El resultado del ejercicio 8 es {}.".format(lista_palabras))

# Ejercicio 9
print("EJERCICIO 9. Convierte 13.14 a un número entero")

entero = int(13.14)
print("El resultado del ejercicio 9 es {}.".format(entero))
print("El tipo de datos es {}".format(type(entero)))

# Ejercicio 10
print("EJERCICIO 10. Convierte 13 a un número real")

real = float(13)
print("El resultado del ejercicio 10 es {}.".format(real))
print("El tipo de datos es {}".format(type(real)))

# Ejercicio 11
print("EJERCICIO 11. Convierte 13 a texto")

texto = str(13)
print("El resultado del ejercicio 11 es {}.".format(texto))
print("El tipo de datos es {}".format(type(texto)))

# Ejercicio 12
print("EJERCICIO 12. Crea una lista de los números impares entre 0 y 30")

lista_impares = list(range(0,30)) # La sintaxis es range (inicio, final, secuencia)
lista_impares = [num for num in lista_impares if num % 2 != 0]
print(lista_impares)

# Ejercicio 13
print("EJERCICIO 13. Crea una  lista llamada amigos que contenga a Juan, Pedro, María y Marta. Y sácala por consola.")

lista_amigos = ["Juan","Pedro","Maria","Marta"]
print(lista_amigos)

# Ejercicio 14
print("EJERCICIO 14. Acaban de conocer a Marcos y Sofía y se han hecho amigos. Añádelos al grupo. Y saca la nueva lista por consola.")

lista_amigos.extend(["Marcos","Sofia"])
print(lista_amigos)

# Ejercicio 15
print("EJERCICIO 15. También han conocido a Paula. Añádela al grupo. Y saca la nueva lista por consola.")

lista_amigos.append("Paula")
print(lista_amigos)

# Ejercicio 16
print("EJERCICIO 16. Al final Paula salió rana. Sácala de la lista e imprime por consola como ha quedado el grupo")

lista_amigos.remove("Paula")
print(lista_amigos)

# Ejercicio 17
print("EJERCICIO 17. ¿Hay algún amigo que se llame Alfredo? (Verdadero/Falso)")
ejercicio17 = "Alfredo" in lista_amigos
print("El resultado del ejercicio 17 es {}.".format(ejercicio17))

# Ejercicio 18
print("EJERCICIO 18. Ordena alfabéticamente la lista de amigos y saca el resultado por consola")
lista_amigos.sort()
print(lista_amigos)

# Ejercicio 19
print("EJERCICIO 19. Saca por consola solo los 3 primeros amigos de la lista.")
print(lista_amigos[:3])

# Ejercicio 20
print("EJERCICIO 20. Localiza en qué posición de la lista está Pedro (empezando por cero)")
ejercicio20 =  lista_amigos.index("Pedro")
print("Pedro se encuentra en la posición {} de la lista".format(ejercicio20))

# Ejercicio 21
print("EJERCICIO 21. Usa list comprehension para sacar por consola sólo los nombres de amigos que empiecen por M")
[print(nombre) for nombre in lista_amigos if nombre.startswith("M")]

# Ejercicio 22
print("EJERCICIO 22. Ahora haz lo mismo pero sin usar list comprehension (con for e if 'clásicos')")
[print(nombre) for nombre in lista_amigos if nombre.startswith("M")]

# Ejercicio 23
print("EJERCICIO 23. Crea un contador de 'nombres que empiecen por M', recorre toda la lista con un for, suma 1 cada vez que encuentres uno e imprime el resultado final.")

contador = 0

for nombre in lista_amigos :
	if nombre.startswith("M") :
		contador = contador + 1

print("El resultado del ejercicio 23 es {}.".format(contador))

# Ejercicio 24
print("EJERCICIO 24. A continuación te paso listas con los chicos y las chicas. Están en orden de quien es pareja de quien. Tienes que crear el diccionario pareja_de donde las claves sean los chicos y los valores las chicas. Finalmente imprímelo por consola.")

chicos = ['Juan','Marcos','Pedro']
chicas = ['Marta','María','Sofía']

print(dict(zip(chicos, chicas)))

# Ejercicio 25
print("EJERCICIO 25. Saca por consola la pareja de Marcos")

diccionario = dict(zip(chicos, chicas))
print(diccionario["Marcos"])

# Ejercicio 26
print("EJERCICIO 26. Al final Marcos y María han roto, y ahora la nueva pareja de Marcos es Paula. Actualízadlo en el diccionario e imprime como queda ahora el diccionario.")

"""del diccionario["Marcos"]
print(diccionario)"""

diccionario["Marcos"] = "Paula"
print(diccionario)

# Ejercicio 27
print("EJERCICIO 27. El grupo se ha puesto de parte de María, así que han echado a Marcos y a su nueva pareja. Sácalos del grupo e imprime cómo queda.")

del diccionario["Marcos"]
print(diccionario)

# Ejercicio 28
print("EJERCICIO 28. Hay que actualizar la lista de chicos y chicas. Hazlo siguiendo estas instrucciones:")

"""Hay que actualizar la lista de chicos y chicas. Hazlo siguiendo estas instrucciones:

Crea nuevas listas vacías de chicos y chicas
Recorre el diccinario pareja_de con un for y mediante tuple unpacking separa cada item del diccionario en chico y chica
Añade chico y chica a sus respectivas listas
Saca por pantalla chicos y chicas"""

lista_chicos = list()
lista_chicas = list()

for chico,chica in diccionario.items() :
	lista_chicos.append(chico)
	lista_chicas.append(chica)


print("La lista de chicos es {}".format(lista_chicos))
print("La lista de chicas es {}".format(lista_chicas))

# Ejercicio 30
print("EJERCICIO 30. Extrae la palabra 'perro' del siguiente objeto.")

obj = [1,2,
		{'nombre':'Manuel','ciudad':'Madrid','vive_con':
			[{'mujer': 'Julia','hijo':'Andres','mascotas':
				['gato','perro']},'ah y un hamster']},4,5]

print(obj[2]["vive_con"][0]["mascotas"][1])

# Ejercicio 31
print("EJERCICIO 31. Crea una función que se llame imc para calcular el índice de masa corporal a partir de la estatura (en metros) y el peso (en kilos).")

# La fórmula es IMC = peso (kg) / estatura (m) al cuadrado.

def imc(peso,altura):
	imc = peso / (altura * altura)
	return(imc)

imc = imc(62,1.76)

print("EL IMC es {}".format(imc))

# Ejercicio 31.BIS
print("EJERCICIO 31.BIS Crea la misma función pero como una lambda que meta el dato en la variable resultado. Pruébala de nuevo.")

# La fórmula es IMC = peso (kg) / estatura (m) al cuadrado.

peso = 62
altura = 1.76

calcular_imc = lambda peso, altura: peso / (altura ** 2)

imc = calcular_imc(peso,altura)

print("Su índice de masa corporal (IMC) es:", imc)

# Ejercicio 32
print("EJERCICIO 32. Crea un pequeño programa que:")

"""1. Pregunte al usuario por su peso en kilos y su estatura en centímetros
2. Llame a la función imc (acuérdate de transformar la estatura a metros)
3. Si imc >25 aconseje al usuario un poco de dieta y ejercicio"""

"""peso = int(input("Ingrese su peso en kilogramos: "))
altura = int(input("Ingrese su altura en centímetros: "))

def imc(peso,altura):
	altura = altura / 100
	print(altura)
	imc = peso / (altura * altura)
	return(imc)

imc = imc(peso,altura)

print(imc)

if imc > 25:
	print("Te recomiendo llevar un estilo de vida más saludable.")
else:
	print("Estas en perfecto estado de salud.")"""

# Ejercicio 33
print("EJERCICIO 33. Importa los módulos random y statistics y crea un programa que:")

"""Importa los módulos random y statistics y crea un programa que:

Cree una lista vacía llamada imcs

Repita 100 veces el siguiente proceso:

    * Calcular aletoriamente un peso entre 50 y 100
    * Calcular aletoriamente una estatura entre 150 y 200 y convertirla a metros
    * Llamar a la función imc y añadir el resultado a la lista imcs
   
Usando funciones del paquete statistics imprima por pantalla la media y la desviación típica de la distribución final obtenida.

Pista: puedes buscar las funciones que te ayuden a hacerlo en:

https://www.w3schools.com/python/module_random.asp

https://www.w3schools.com/python/ref_stat_mean.asp"""

import random as rd
import statistics as st

imcs = list()

for valor in range(100):
	peso = rd.randrange(50,100)
	altura = rd.randrange(150,200)
	altura = altura / 100

	calcular_imc = lambda peso, altura: peso / (altura ** 2)
	imc = calcular_imc(peso,altura)

	imcs.append(imc)
	
media = st.mean(imcs)
desviacion = st.pstdev(imcs)

print("La mediana es {} y la desviación {}".format(media,desviacion))


