#Impar ou par
print("Digite um numero de 1 a 10")
numero = int(input('Digite o numero aqui: '))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#Classificação de idade
print("Digite sua idade:")
idade = int(input())
if idade >= 0 and idade <=12:
    print("Você é uma criança.")
elif idade > 12 and idade < 18:
    print("Você é um adolescente.")
else:
    print("Você é maior de idade.")

#Teste de cadastro
print('Digite seu email: \n')
email = input()
print('Digite sua senha: \n')
senha = input()
if email == email and senha == senha:
    print('Login realizado com sucesso!')
else:
    print('Email ou senha incorretos!')