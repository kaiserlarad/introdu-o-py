dado= float(input('Digite o valor em R$: '))
divide= int(dado/50)
resto= divide%50

print('A quantidade de notas de R$50,00 para preencher o valor digitado é:', divide)
print('E irá sobrar R$',resto)
