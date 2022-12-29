print('*'*13)
print('Calculadora')

numero_1=(int(input("Digita tus numeros: ")))
operacion = input('Que operacion realizo: ')
numero_2=(int(input("Digita tus numeros: ")))

if operacion == '+':
    print(numero_1 + numero_2)
elif operacion =='-':
    print(numero_1 - numero_2)
elif operacion =='*':
    print(numero_1 * numero_2)
elif operacion =='/':
    print(numero_1 / numero_2)
else: 
    print('Cambiar Operacion')