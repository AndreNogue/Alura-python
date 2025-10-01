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

email = input('Digite seu email: ')
senha = input('Digite sua senha: ')
email_confirmado = input('Confirme seu email: ')
senha_confirmada = input('Confirme sua senha: ')

if email == email_confirmado and senha == senha_confirmada:
    print('Login realizado com sucesso!')
else:
    print('Email ou senha incorretos!')