from biblioteca.py1 import  *
while True:
    opcao = int(input("Qual sua opção: \n"
                      "1. Cadastre.\n"
                      "2. Mostrar. \n"
                      "3. Pesquisar. \n"
                      "4. Sair.\n"))
    match opcao:
        case 1:
            cadastrar(input("Digite um texto"))
        case 2:
            saida()
        case 3:
            pesquisar(input("Nome para pesquisar"))
        case 4:
            break
        case _:
            print("Opção inválida, tente novamente")