print('CALCULO DE GASTO DE COMBUSTIVEL SIMPLES')
print('---------------------------------------')
print()


tempo = float(input('digite quanto tempo durou a viagem: '))

print()

velocidade = float(input('digite a velocidade que o veiculo percorreu durante a viagem: '))

print()

distancia = tempo * velocidade 
litros_usados = distancia / 12
litros_usados = round(litros_usados, 2)

print()
print('Velocidade média: ', velocidade)
print('Tempo gasto na viagem: ', tempo)
print('Distancia percorrida: ', distancia)
print('Quantidade de litros de combustivel: ', litros_usados)