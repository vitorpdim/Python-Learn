numeros = []

for i in range (1, 6):
    num = int(input(f'Digite o {i}st numero: '))
    numeros.append(num)
        
soma = 0
for num in numeros:
    soma += num
print(f'soma total: {soma}')