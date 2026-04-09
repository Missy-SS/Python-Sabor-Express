import os

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opções():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurantes")
    print("4. Sair\n")



#A função é um bloco de código, que vai realizar uma determinada ação no momento que a chamarmos
def finalizar_app():
    os.system('clear')
    print("Finalizando o app\n")

def opcao_invalida():
    print("Opção inválida!\n")
    input("Digite uma tecla voltada ao menu principal")
    main()

def escolher_opcao():

    opcao_escolhida = int(input("Escolha uma opção: "))
    print(f"Você escolheu a opção {opcao_escolhida}!")

    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restaurantes")
    elif opcao_escolhida == 3:
        print("Ativar restaurantes")
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        opcao_invalida()

def main():
    os.system("clear")
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()
    
if __name__ == '__main__':
    main()

#A principal finalidade da instrução match é simplificar a lógica de código ao facilitar o trabalho com diferentes padrões de dados

"""Funcionalidade do match e do if/elif/else
if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restaurantes")
    elif opcao_escolhida == 3:
        print("Ativar restaurantes")
    else:
        finalizar_app()

Utilizando o match fica:

opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _: Essa instrução equivale a um curinga corresponde a qualquer valor que não tenha sido correspondido pelos casos anteriores, ou seja, equivalente ao else da condicional anterior.
        print('Opção inválida!')

Será feito um comparativo com todos os valores determinados pelos blocos de case



Dentro de um bloco match, você pode utilizar a instrução case para definir padrões específicos que serão comparados com a expressão que está sendo correspondida.


match expressão:
    case padrão_1:
        # Código a ser executado se expressão corresponder a padrão_1
    case padrão_2:
        # Código a ser executado se expressão corresponder a padrão_2
    # ... outros casos ...
    case _:
        # Código a ser executado se nenhum dos padrões anteriores corresponder. Isso é útil para tratar casos não específicos.

Enquanto o if nos proporciona uma maneira eficaz de tomar decisões simples ou complexas em nosso código, adaptando o comportamento do programa de acordo com as circunstâncias determinadas. O match simplifica essa lógica do código quando há múltiplos padrões complexos, oferencendo uma estrutura mais legível, especialmente quando há muitos casos a serem tratados.
"""

