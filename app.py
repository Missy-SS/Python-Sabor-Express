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

def exibir_opções():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurantes")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizando app")

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)  #append coloca na lista, entre parenteses, o que desejamos colocar na lista
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    
    voltar_ao_menu_principal()


#A função é um bloco de código, que vai realizar uma determinada ação no momento que a chamarmos

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")

    for restaurante in restaurantes:
        print(f".{restaurante}")

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("clear")
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()
    
if __name__ == '__main__':
    main()







#Conteúdos

"""Funcionalidade do match e do if/elif/else
Match simplifica a lógica de código

opcao_escolhida = int(input('Escolha uma opção: '))
match expressão:
    case padrão_1:
        # Código a ser executado se expressão corresponder a padrão_1
    case padrão_2:
        # Código a ser executado se expressão corresponder a padrão_2
    # ... outros casos ...
    case _:
        # Código a ser executado se nenhum dos padrões anteriores corresponder. Isso é útil para tratar casos não específicos.

Dentro de um bloco match, você pode utilizar a instrução case para definir padrões específicos que serão comparados com a expressão que está sendo correspondida.

if: Maneira eficaz de tomar decisões simples ou complexas em nosso código, adaptando o comportamento do programa de acordo com as circunstâncias determinadas. O match simplifica essa lógica do código quando há múltiplos padrões complexos, oferencendo uma estrutura mais legível, especialmente quando há muitos casos a serem tratados.

Listas e Tuplas

listas são definidas com [], tuplas são definidas com ()
listas são mutáveis, é possível modificar seus elementos após sua criação
tuplas são imutáveis, depois de criadas, seus elementos não podem ser modificados
listas são menos eficientes quando há uma manipulação de grandes conjuntos de dados, por sua mutabilidade
listas são ideais quando há a necessidade de uma coleção de elementos que pode ser modificada com o tempo. Exemplo: lista de tarefas
lista = []: cria uma lista
append(): adiciona item à lista;
remove(): remove item da lista;
print()
    for item in lista: exibe os itens da lista
tuplas são apropriadas quando há garantia de que os elementos não serão alterados depois. Possuem um desempenho melhor em operações de leitura e acesso a elementos



"""
