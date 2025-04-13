import math
import random
import os
from time import sleep

print("EJERCICIO N°1")
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for x in range(0, 101):
    print(x)

sleep(4)
os.system('cls')

print("EJERCICIO N°2")
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num_input = int(input("Ingrese un número entero:\n"))
digits = 0

if num_input == 0:  # Si el numero ingresado es cero, entonces se trata de un solo dígito.
    digits = 1
    print(f"El número ingresado tiene: {digits} dígitos")
else:  # Si el numero ingresado es distinto de cero, se calcula el número de digitos que tiene.
    while num_input != 0:
        digits += 1  # Por cada vuelta, sumamos un dígito
        # En cada vuelta dividimos al numero por diez hasta alcanzar cero y no poder iterar más. # Cant. vueltas = Cant digitos
        digits_divider = math.trunc(num_input/10)
        num_input = digits_divider

print(f"El número ingresado tiene: {digits} dígitos")

sleep(2)
os.system('cls')

print("EJERCICIO N°3")
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1_input = int(input("Ingrese el primer valor: \n"))
num2_input = int(input("Ingrese el segundo valor: \n"))
addition_num = 0

# Comparamos los numeros y determinamos cuál es menor y mayor.
if num1_input > num2_input:
    major = num1_input
    minor = num2_input
else:
    major = num2_input
    minor = num1_input

# le sumo uno a la variable menor para excluirla de la iteracion.
for num in range(minor + 1, major):
    addition_num = addition_num + num

print("El resultado de la suma es: ", addition_num)

sleep(2)
os.system('cls')

print("EJERCICIO N°4")
# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar
# el total acumulado cuando el usuario ingrese un 0.

sequence_input = int(
    input("Ingrese un número entero para iniciar o cero para finalizar:\n"))
sequence_sum = 0

while sequence_input != 0:
    sequence_sum += sequence_input
    sequence_input = int(
        input("Ingrese otro número entero o cero para finalizar: \n"))

print("La suma de los números ingresados es:", sequence_sum)

sleep(2)
os.system('cls')

print("EJERCICIO N°5")
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar
# cuántos intentos fueron necesarios para acertar el número.

random_num = random.randint(0, 10)
user_num = int(input("Adivina qué número del 0 al 9 estoy pensando: \n"))
attempts = 0

while user_num != random_num:  # mientras que el usuario no adivine el numero, se le dara un intento nuevo al usuario
    print("No adivinaste! Intentalo nuevamente.")
    user_num = int(input("Ingresá otro número: \n"))
    attempts += 1

if user_num == random_num:
    print("Adivinaste! Lo lograste en:", attempts, "intentos.")

sleep(2)
os.system('cls')

print("EJERCICIO N°6")
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for numbers in range(98, 0, -2):  # se itera desde el 98 al 2, restando -2 en cada iteración
    print(numbers)

sleep(4)
os.system('cls')

print("EJERCICIO N°7")
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

number_input = int(input("Ingrese un número: \n"))
sum_number = 0

for n in range(0, number_input):
    sum_number += n

print(
    f"La suma de los números comprendidos entre 0 y {number_input} es: {sum_number}")

sleep(2)
os.system('cls')

print("EJERCICIO N°8")
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números
#  son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

sum_values = 0
even = 0
odd = 0
positiv = 0
negativ = 0

for value in range(1, 5):
    print("Ingrese el valor N°", value, ":")
    numbers_user = int(input())

    if numbers_user >= 0:
        positiv += 1
    else:
        negativ += 1

    if numbers_user % 2 == 0:
        even += 1
    else:
        odd += 1

print("Total de positivos ingresados: ", positiv)
print("Total de negativos ingresados: ", negativ)
print("Total de pares ingresados: ", even)
print("Total de impares ingresados: ", odd)

sleep(4)
os.system('cls')

print("EJERCICIO N°9")
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

sum_elem = 0
# declaramos una variable limite para la iteracion. Esta puede tener el valor que se quiera.
limit = 10

print("A continuación deberá ingresar:", limit, "números.")

for elem in range(0, limit):  # se itera desde cero hasta el valor indicado en la variable limite
    print("Ingrese el valor N°", elem + 1, ":")
    numbers = int(input())
    sum_elem += numbers

mean_elem = sum_elem / limit

print("La promedio de los números ingresados es:", mean_elem)

sleep(2)
os.system('cls')

print("EJERCICIO N°10")
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario
# ingresa 547, el programa debe mostrar 745.

user_number = int(input("Ingrese un número entero: \n"))
invert_num = 0
first_zero = False
i = 0

while user_number > 0:
    module_number = user_number % 10

    # en la primera vuelta determinamos si el ultimo digito del numero original es cero.
    if i == 0 and module_number == 0:
        first_zero = True
    else:
        # sumamos uno a la variable, ya que solo nos interesa usarla para la primera vuelta.
        i += 1

    invert_num = (invert_num * 10) + module_number
    user_number = (user_number - module_number) // 10

if first_zero:  # si el ultimo numero del numero original resulta ser cero, no podra imprimirse como primer numero del numero invertido, por lo que lo imprimimos como string
    print(f"0{invert_num}")
else:
    print(invert_num)
