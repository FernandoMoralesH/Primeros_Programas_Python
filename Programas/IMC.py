"""Primer Programa: Se realiza Programa para medir el indice de masa muscular (IMC)"""
print('Programa que mide IMC\n****************************')
print('Por favor, coloca los datos que se solicitan')
altura = float(input('Coloca tu altura en m: '))
peso = int (input('Coloca tu peso en KG:'))
_IMC = round(peso/(altura**2),2)
print('Tu IMC es de ', _IMC)