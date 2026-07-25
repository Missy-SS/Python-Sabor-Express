from models.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(this, nome, preco, descricao):
        super().__init__(nome, preco)
        this._descricao = descricao
    def aplicar_desconto(this):
        this._preco -= (this._preco * 0.05)

#super permite que acessemos informações de outras classes
#class Prato(ItemCardapio) significa que a classe prato vai herdar atributos da classe ItemCardapio
#quando um método é moldado de forma diferente em diferentes classes: Polimorfismo
