print('TESTE DE IDADE')
print('=================')

idade = int(input('Digite a sua idade: '))

print()

if idade <= 0:
    print("idade invalida")
else:
    if idade <= 12 & idade > 0:
        print("Criança")
    else:
        if idade > 13 & idade <= 17:
            print('Adolescente')
        else:
            print("Adulto")