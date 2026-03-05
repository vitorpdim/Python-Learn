coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}

coleta.items()
for especie, num_especimes in coleta.items():
    print(f'Especie: {especie}, numero da especie: {num_especimes}')

biomoleculas = ('proteina', 'acido nucleicos', 'carboidrato', 'lipideo', 'acido nucleicos', 'carboidrato')
print()
print(set(biomoleculas)) # funcao para nao imprimir elementos repetidos

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection

print(c3)

# diferenca entre os conjuntos:

c1.difference(c2)
c2.difference(c1)