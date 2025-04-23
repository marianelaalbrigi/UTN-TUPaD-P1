import os
from time import sleep

print("Ejercicio 1")
# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
list_range = list(range(4, 101, 4))
print("Múltiplos de 4:", list_range)

sleep(3)
os.system('cls')

print("Ejercicio 2")
# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

list_words = ["Puerta", "Casa", "Ventana", "Piso", "Pared"]
print(f"El penúltimo elemento es: {list_words[-2]}")

sleep(2)
os.system('cls')

print("Ejercicio 3")
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por

list_add = []
list_add.append("Hola")
list_add.append("Hello")
list_add.append("Hallo")

# opcion alternativa a append, permite agregar multiples elementos de una sola vez.
# list_add.extend("Hola", "Hello", "Hallo")

print(list_add)
sleep(2)
os.system('cls')

print("Ejercicio 4")
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!

animals = ["perro", "gato", "conejo", "pez"]
animals[1] = "loro"
animals[-1] = "oso"
print("Lista de animales actualizada:", animals)

sleep(2)
os.system('cls')

print("Ejercicio 5")
print("Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza:")
print("Paso 1 > numeros = [8, 15, 3, 22, 7]")
print("Paso 2 > numeros.remove(max(numeros)")
print("Respuesta: en el primer paso se declara la variable numeros con un array/lista de cinco numeros.\n"
      "En el segundo paso a la variable numeros se le aplica el método de remove() y dentro de remove() se aplica \n"
      "la funcion max(), la cual devuelve el valor maximo de nuestra lista, o sea 22. Por lo que remove, eliminará dicho valor.")

sleep(15)
os.system('cls')

print("Ejercicio 6")
# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

list_numbers = list(range(10, 31, 5))
print("La dos primeros numeros de la lista:", list_numbers[0:2])

sleep(3)
os.system('cls')

print("Ejercicio 7")
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["audi", "mercedes"]
print("Lista actualizada de autos:", autos)

sleep(3)
os.system('cls')

print("Ejercicio 8")
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5*2)
dobles.append(dobles[0]*2)
dobles.append(15*2)
print("Los dobles de 5, 10 y 15 son:", dobles)

sleep(3)
os.system('cls')

print("Ejercicio 9")
# Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"],
           ["arroz", "fideos", "salsa"],
           ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print("Lista actualizada de compras:", compras)

sleep(5)
os.system('cls')

print("Ejercicio 10")
# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("La lista anidada:", lista_anidada)
