"""
Diseñar un programa para que, dados dos números enteros, determine si uno es múltiplo del otro.
750722
"""

#Entrada
numero_1 = int(input("Introdusca un número: "))
numero_2 = int(input("Introduzca otro número: "))

#Proceso
if numero_1 % numero_2 == 0:
    print(f"El número {numero_1} es múltiplo del número {numero_2}")
elif numero_2 % numero_1 == 0:
    print(f"El número {numero_2} es múltiplo del número {numero_1}")
else: 
    print("Ninguno de los números es múltiplo del otro")