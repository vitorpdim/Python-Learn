print('VERIFICACAO DE MAIOR OU MENOR')
print()

valor1 = int(input('digite um valor: '))
valor2 = int(input('digite o segundo valor: '))

print()

if valor1 > valor2:
    print(f'{valor1} é maior que {valor2}')
else: print(f'{valor1} é menor que {valor2}')

print()

# -----------------------------------------------

print('VERIFICACAO DE IGUALDADE')
print()

print('=========================\n')

print('Para comparar dois valores, digite-os:\n')

valor3 = int(input('Digite o valor que deseja comparar: '))
valor4 = int(input('Digite o segundo valor que deseja comparar: '))
print()

if valor3 == valor4:
    print(f'{valor3} é igual a {valor4}')
else:
    if valor3 & valor4 == 7:
        print(f'{valor3} e {valor4} é igual a 7! meu numero da sorte pae')
    else:
        print('nao eh igual a nada pae :/')