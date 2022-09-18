"""Segundo Programa:Identificar el numero Mayor"""
#Variables

num1= int(input("Escribe un numero entero: "))
num2=  int(input("Escribe un numero entero: "))

if num1 >num2:
    print("El numero mayor entre " , num1, "y ", num2, "es: ", num1)
elif num2>num1:
 print("El numero mayor entre " , num1, "y ", num2, "es: ", num2)
else:
    print("Ambos numeros son iguales")