counter=0
number_positive=int(input("Escribe un numero positivo mayor a 1: "))

while number_positive <= 1:
    print("Vuelve a escoger un numero positivo mayor que 1: ")
    number_positive=int(input("Escribe un numero positivo mayor a 1: "))

if number_positive >=2: print("-"*35,"\nNumero con que se empieza: ", number_positive)

while  number_positive !=1 and number_positive >=1:
    if  number_positive%2==0:
        number_positive=number_positive//2
        print(number_positive)
        counter+=1
    elif number_positive%2==1:
        number_positive=(number_positive*3)+1
        print(number_positive)
        counter+=1
print("Numero total de iteraciones: ", counter, "conteos")