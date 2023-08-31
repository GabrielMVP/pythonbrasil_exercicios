# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

def main():
    circulo = float(input('Qual o valor do circulo C: '))
    raio = circulo / (2 * math.pi)
    
    area = math.pi * raio ** 2
    
    print(f'A raio do circulo é: {raio}')
    print(f'A área do círculo é: {area}')
    
main()