import os

restaurantes = []



def exibir_nome_do_programa():
    print("""
    
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)
    

def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Ativar restaurante')
    print('4 - Sair\n')


def opcao_invalida():
    print('Opção inválida')
    input('Pressione ENTER para continuar...')
    main()


def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastrar novo restaurante')
    nome_restaurante = input('Nome: ')
    restaurantes.append(nome_restaurante) # Adiciona o restaurante à lista
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
    input('Pressione ENTER para voltar ao menu principal...')
    main()


def obter_opcao_escolhida():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            print('Saindo...')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
      os.system('cls')
      print('Aplicação finalizada')
      exit()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    obter_opcao_escolhida()

if __name__ == '__main__':
    main()

