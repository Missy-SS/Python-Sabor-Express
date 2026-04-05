import os

print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

print("1. Cadastrar restaurante")
print("2. Listar restaurantes")
print("3. Ativar restaurantes")
print("4. Sair\n")

opcao_escolhida = int(input('Escolha uma opção: '))
print(f"Você escolheu a opção {opcao_escolhida}!")

#A função é um bloco de código, que vai realizar uma determinada ação no momento que a chamarmos
def finalizar_app():
    os.system('clear')
    print("Finalizando o app\n")

if opcao_escolhida == 1:
    print("Cadastrar restaurante")
elif opcao_escolhida == 2:
    print("Listar restaurantes")
elif opcao_escolhida == 3:
    print("Ativar restaurantes")
else:
    print("Encerramento do programa")
