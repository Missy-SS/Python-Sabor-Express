from models.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(this, nome, preco, tamanho):
        super().__init__(nome, preco)
        this._tamanho = tamanhopass
