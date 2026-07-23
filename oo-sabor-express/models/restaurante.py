class Restaurante:
    restaurantes = []
    def __init__(this, nome, categoria, capacidade=0, avaliacao=0):
        this.nome = nome
        this.categoria = categoria
        this.ativo = False
        this.capacidade = capacidade
        this.avaliacao = avaliacao
        
        Restaurante.restaurantes.append(this)
    def __str__(this):
        return f"{this.nome} | {this.categoria}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} | {restaurante.capacidade} | {restaurante.avaliacao}")
        

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("PizzaExpress", "Italiana")

Restaurante.listar_restaurantes()
