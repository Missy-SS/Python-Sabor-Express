from models.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(this, nome, preco, descricao):
        super().__init__(nome, preco)
        this._descricao = descricao
        
