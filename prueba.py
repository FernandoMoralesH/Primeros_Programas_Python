import random

mensaje_juego = "La lotería local del pueblo del Espinal, Oaxaca: Presenta: ".center(80) 
mensaje2="Juego de la Loteria".center(80)
print("\n",mensaje_juego,"\n",mensaje2,"\n")

instrucciones_menu="A. Menú con las opciones: \n 1.-Comprar boleto / imprimir boleto \n 2.-Generar número ganador/ con un método(generar números aleatorios) \n 3.-Verificar si gano el boleto comprado \n 4.-Mostrar resultado (si el boleto fue premiado y con cuanto) \n 5.-Salir"
print(instrucciones_menu.rjust(15,"-"))
print("\nPremios de Loteria:\n")
lugares = [{"lugar 1":1,"Numeros de digitos acertados":6,"Monto del Premio":100,"Premio base":30000},
 {"Numeros de digitos acertados":5,"Monto del Premio":0.050,"Premio base":1500},
{"Numeros de digitos acertados":4,"Monto del Premio":0.025,"Premio base":750},
{"Numeros de digitos acertados":3,"Monto del Premio":0.010,"Premio base":300},
{"Numeros de digitos acertados":2,"Monto del Premio":0.0089,"Premio base":267},
{"Numeros de digitos acertados":1,"Monto del Premio":0.00033,"Premio base":10}]
print("+---------------------------------+----------------------+-----------------+")
print("|Números de digitos acertados     |Monto del Premio en % |Premio en $      |")
print("+---------------------------------+----------------------+-----------------+")

for dato in lugares:
    numeros = dato["Numeros de digitos acertados"]
    monto =dato["Monto del Premio"]
    premio = dato["Premio base"]
    
    cadena = "|{:>33}|{:>22.3f}|{:>17.2f}|".format(numeros,monto,premio)
    print(cadena)
print("+---------------------------------+----------------------+-----------------+")