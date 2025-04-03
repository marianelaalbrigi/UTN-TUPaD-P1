from statistics import mode, median, mean
import random
import os
from time import sleep

print("EJERCICIO 01")
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

age_user = int(input("Ingrese su edad: "))
if age_user > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

sleep(2)
os.system('cls')

print("EJERCICIO 02")
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

mark_input = float(input("Ingrese su nota: "))
if mark_input >= 6 and mark_input <= 10:
    print("Aprobado")
else:
    print("Desaprobado")

sleep(2)
os.system('cls')

print("EJERCICIO 03")
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

number_input = int(
    input("Ingrese un número para iniciar el ejercicio: "))

while number_input != 0:
    if number_input % 2 == 0:  # Se evalúa si es par
        print("Ha ingresado un número par")
        number_input = int(
            input("Si desea continuar ingrese otro numero, sino ingrese cero: "))
    else:
        number_input = int(
            input("El número ingresado es impar. Ingrese un número par: "))

sleep(2)
os.system('cls')

print("EJERCICIO 04")
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

user_age = int(input("Ingrese su edad: "))

while user_age != 0:
    if user_age >= 30:
        print("Eres adulto mayor")
    elif user_age >= 18 and user_age < 30:
        print("Eres adulto joven")
    elif user_age >= 12 and user_age < 18:
        print("Eres adolescente")
    else:
        print("Eres menor de edad")
    user_age = int(input(
        "Si desea finalizar el ejercicio ingrese cero, si desea continuar ingrese su edad: "))


sleep(2)
os.system('cls')

print("EJERCICIO 05")
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

flag_password = False

while not flag_password:
    password_input = input(
        "Introduzca una contraseña de entre 8 y 14 caracteres: ")
    password_lenght = len(password_input)  # ACTUALIZAMOS LA LONGITUD

    if 8 <= password_lenght <= 14:
        print("Ha ingresado una contraseña correcta")
        flag_password = True
    else:
        print("Ha ingresado una contraseña incorrecta. Inténtelo de nuevo.")

sleep(2)
os.system('cls')

print("EJERCICIO 06")
# Escribir un programa que tome la lista de numeros_aleatorios, calcule su moda,
# su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.

random_listNumbers = [random.randint(1, 100) for i in range(10)]
mean_listNumbers = mean(random_listNumbers)
mode_listNumbers = mode(random_listNumbers)
median_listNumbers = median(random_listNumbers)

print(f"Para la lista de números {random_listNumbers}: ")

if mean_listNumbers > median_listNumbers and mean_listNumbers > mode_listNumbers:
    print("El sesgo es positivo.")
elif mean_listNumbers < median_listNumbers and mean_listNumbers < mode_listNumbers:
    print("El sesgo es negativ.")
elif mean_listNumbers == median_listNumbers and median_listNumbers == mode_listNumbers:
    print("No hay sesgo.")

sleep(4)
os.system('cls')

print("EJERCICIO 07")
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por antalla.

phrase_input = input("Ingrese una palabra o frase: ")
phrase_lower = phrase_input.lower()
last_letter = len(phrase_lower)
last_letter = last_letter - 1

if phrase_lower[last_letter] == "a" or phrase_lower[last_letter] == "e" or phrase_lower[last_letter] == "i" or phrase_lower[last_letter] == "o" or phrase_lower[last_letter] == "u":
    print(f"{phrase_input}!")
else:
    print(f"La frase ingresada \"{phrase_input}\" no finaliza en vocal.")


sleep(4)
os.system('cls')

print("EJERCICIO 08")
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

name_input = input("Ingrese su nombre: ")
option_input = int(input("""Ingrese el número de la opción deseada:
    1: Si desea convertir su nombre a mayúsculas.
    2: Si desea convertir su nombre a minúculas
    3: Si solo quiere convertir la primera letra a mayúsculas.\n
    Opción elegida: """))

while name_input:
    if option_input == 1:
        print(name_input.upper())
        break
    elif option_input == 2:
        print(name_input.lower())
        break
    elif option_input == 3:
        print(name_input.title())
        break
    else:
        option_input = int(
            input("""La opción ingresada es inexistente. Elija 1, 2 ó 3.\n
            Opción elegida: """))

sleep(2)
os.system('cls')

print("EJERCICIO 09")
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla

intensity_quake = int(input("Ingrese la magnitud del terromoto de 0 a 9: "))

if intensity_quake < 3:
    print("Muy leve (imperceptible)")
elif intensity_quake >= 3 and intensity_quake < 4:
    print("Leve (ligeramente imperceptible)")
elif intensity_quake >= 4 and intensity_quake < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif intensity_quake >= 5 and intensity_quake < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif intensity_quake >= 6 and intensity_quake < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


sleep(2)
os.system('cls')

print("EJERCICIO 10")
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisphere_input = input(
    """Indique el hemisferio dónde se encuentra: "N" para hemisferio norte o "S" para hemisferio sur.\n Escriba su opción: """)
hemisphere_input = hemisphere_input.upper()

# Se reitera el ciclo si el usuario ingresa un valor distinto de S o N
while hemisphere_input:
    if hemisphere_input == "N" or hemisphere_input == "S":
        break
    else:
        hemisphere_input = input(
            """La letra introducida es incorrecta. Escriba "N" para hemisferio norte o la letra "S" para hemisferio sur.\n Escriba su opción: """)
        hemisphere_input = hemisphere_input.upper()

date_validation = False  # variable bandera para el ciclo while

# Hasta que los datos ingresados sean correctos (date_validation = True), el ciclo vuelve a pedir el reingreso.
while not date_validation:

    year_input = int(input("Introduzca el año actual: "))

    def year_validation(num):  # Validación rango de año
        while num <= 1800:
            num = int(
                input("Rango ingresado no aceptado. Ingrese un valor superior al año 1800: "))
        return num

    year_input = year_validation(year_input)

    month_input = int(input("Introduzca el número de mes: "))

    def month_validation(num):  # Validacion rango de mes
        while num < 1 or num > 12:
            num = int(input(
                "El valor introducido es incorrecto. Ingrese el número de mes nuevamente: "))
        return num

    month_input = month_validation(month_input)

    day_input = int(input("Introduzca el número de día: "))

    def day_validation(num):  # Validacion rango de dia
        while num >= 32 or num <= 0:
            num = int(
                input("El valor introducido es incorrecto. Ingrese el número de día nuevamente: "))
        while num == 2 and num >= 30:
            num = int(
                input("El valor introducido es incorrecto. Ingrese el número de día nuevamente: "))
        return num

    day_input = day_validation(day_input)

    # Validación bisiesto o no
    if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
        leap_year = True
    else:
        leap_year = False

    # Validación de concordancia de datos entre dia, mes y año
    if month_input == 2:
        if leap_year == False and day_input > 28:
            print(
                "Los datos introducidos para la fecha no concuerdan. Inténtelo nuevamente.")
        elif leap_year == True and day_input > 29:
            print(
                "Los datos introducidos para la fecha no concuerdan. Inténtelo nuevamente.")
        else:
            date_validation = True
    elif (month_input == 4 or month_input == 6 or month_input == 9 or month_input == 11):
        if day_input > 30:
            print(
                "Los datos introducidos para la fecha no concuerdan. Inténtelo nuevamente.")
        if day_input <= 30:
            date_validation = True
    else:
        date_validation = True

# Si los datos ingresados son correctos, se imprime la estacion del año según hemisferio.
if date_validation == True:
    if (month_input == 12 and day_input >= 21) or (month_input == 3 and day_input <= 20) or (month_input == 1 or month_input == 2):
        if hemisphere_input == "S":
            print("La estación del año actual es Verano.")
        if hemisphere_input == "N":
            print("La estación del año actual es Invierno.")
    elif (month_input == 3 and day_input >= 21) or (month_input == 6 and day_input <= 20) or (month_input == 4 or month_input == 5):
        if hemisphere_input == "S":
            print("La estación del año actual es Otoño.")
        if hemisphere_input == "N":
            print("La estación del año actual es Primavera.")
    elif (month_input == 6 and day_input >= 21) or (month_input == 9 and day_input <= 20) or (month_input == 7 or month_input == 8):
        if hemisphere_input == "S":
            print("La estación del año actual es Invierno.")
        if hemisphere_input == "N":
            print("La estación del año actual es Verano.")
    else:
        if hemisphere_input == "S":
            print("La estación del año actual es Primavera.")
        if hemisphere_input == "N":
            print("La estación del año actual es Otoño.")
