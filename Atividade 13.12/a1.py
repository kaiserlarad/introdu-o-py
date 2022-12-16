#1ª ATIVIDADE

desconto = float(input('Digite o valor do desconto(em %): '))
valor = float(input('Digite o valor da compra: R$'))
valordescontado =  valor-(valor*desconto/100)

print("O valor da compra foi:", valor)
print("O desconto aplicado foi de: ", desconto)
print(" ")
print('O valor total a pagar é de: R$', valordescontado)


