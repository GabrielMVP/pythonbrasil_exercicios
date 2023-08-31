#Faça um programa que calcule a área de um quadrado em seguida mostre o dobro dessa área para o usuário.

lado = float(input('Digite o valor do lado do quadrado: '))
area = lado ** 2
area_dobro = 2 * area

print(f'A área do quadrado é {area}')
print(f'O dobro da área do quadrado é {area_dobro}')