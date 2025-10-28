import os
import math
import random

def calculadora():
    print("---CALCULADORA---")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multipliacação")
    print("4 - divisão")
    print("5 - potenciação")
    print("6 - raiz quadrada")
    escolha = float(input("Selecione a operação a ser feita"))
    if escolha == '1':
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        print(num1 + num2)
    elif escolha =='2':
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        print(num1 - num2)
    elif escolha =='3':
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        print(num1 * num2)
    elif escolha =='4':
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        print(num1/num2)
    elif escolha =='5':
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        resultado = math.pow(num1, num2)
        print("a potencia de {num1} elevado a {num2} é {resultado}")