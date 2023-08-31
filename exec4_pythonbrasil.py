# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def main():
    numero1 = float(input('Digite a primeira nota: '))
    numero2 = float(input('Digite a segunda nota: '))
    numero3 = float(input('Digite a terceira nota: '))
    numero4 = float(input('Digite a quarta nota: '))
    media = (numero1, numero2, numero3, numero4/4)
    print(f'A média é {media}')
    
main()