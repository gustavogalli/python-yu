from produto import Produto


class Loja:
    def __init__(self, nome, caixa):
        self.nome = nome
        self.caixa = caixa
        self.produtos = [Produto('maçã', 5, 35), Produto('uva', 7, 20)]

    def comprar_produto(self, produto):
        self.caixa -= produto.preco
        self.produtos.append(produto)

    def report(self):
        print(f'\n======= {self.nome} =======')
        print(f'Caixa:\t\tR$ {self.caixa}')
        for produto in self.produtos:
            print(f'{produto.quantidade}x {produto.nome} \tR$ {produto.preco}')
        print(f'========================')
