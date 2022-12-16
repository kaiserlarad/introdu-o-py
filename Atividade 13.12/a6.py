RNome= (input('Digite o seu nome: '))
Sobrenome=(input('Digite o seu sobrenome: '))
cpf= (input('Digite o seu CPF: '))
valor1= float(input('Digite o valor em R$ que foi recebido com a venda do Fiat Uno 99: '))
valor2= float(input('Digite o valor em R$ que foi recebido com a venda da X1: '))
valor3= float(valor1+valor2)

print(cpf+" / "+Nome+' '+Sobrenome)
print('Quantidade de digitos do CPF: ',len(cpf))
print('Última letra do nome: ',Nome[-1])
print(' ')

print('Eu '+Nome+' '+Sobrenome+' do documento '+cpf+' declaro que recebi no mês de novembro de 2022 a quantia de R$',valor1,' na venda do Fiat Uno 99 e a quantia de R$',valor2,' na venda da moto X1, somando a quantia de R$',valor3)