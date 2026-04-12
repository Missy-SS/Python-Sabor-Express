import os


restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]



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
    print("3. Açternar estado do restaurante")
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
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False} 
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    
    voltar_ao_menu_principal()


#A função é um bloco de código, que vai realizar uma determinada ação no momento que a chamarmos

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
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
""" 
.ljust(), no Python, que nos permite definir um determinado número de caracteres à direita ou à esquerda. 
Dicionário: dentro dos [], abre e fecha as {} adiciona uma , e abre e fecha {} novamente
    chave e valor
"""
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
