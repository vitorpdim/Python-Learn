notasSomadas = 0

for i in range (1,6):
    notas = int(input(f'digite a {i}st nota: '))
    notasSomadas += notas
    
media = notasSomadas / 5

print()

print(f"Sua média é: {media}")

if media >= 0.0 and media <= 4:
    print('Reprovado!!!!!!')
else: 
    if media >= 4 and media <= 6:
        print('\nvai ter que fazer exame pae')
    else:
            print("aprovado!!!")