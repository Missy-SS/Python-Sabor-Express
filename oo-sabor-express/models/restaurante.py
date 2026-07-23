class Restaurante:
    restaurantes = []
    def __init__(this, nome, categoria,):
        this._nome = nome.title()
        this._ategoria = categoria.title()
        this._ativo = False
        Restaurante.restaurantes.append(this)
    def __str__(this):
        return f"{this._nome} | {this._categoria}"
    
    def listar_restaurantes():
        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria do Resturante".ljust(25)} | {"Status do Restaurante"}")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}")
    @property
    def ativo(this):
        return "✔️" if this._ativo == True else "✗"
        

restaurante_praca = Restaurante("praça", "gourmet")
restaurante_pizza = Restaurante("pizzaExpress", "italiana")

Restaurante.listar_restaurantes()
