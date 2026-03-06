print('========= CALCULO DE MEDIA ==========')

print()
nota1 = float(input('Digite a 1st nota: '))
print()
nota2 = float(input('Digite a 2st nota: '))
print()
nota3 = float(input('Digite a 3st nota: '))

media = nota1 + nota2 + nota3 / 3.0 

if media >= 0.0 and media <= 4:
    print('Reprovado!!!!!!')
else: 
    if media >= 4 and media <= 6:
        print('\nvai ter que fazer exame pae')
    else:
            print("aprovado!!!")
            
