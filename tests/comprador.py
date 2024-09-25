from produto import Produto

class Comprador:

    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 300
        self.sacola = []

    def comprar(self, loja, qtde, nome_produto):
        # existe produto na loja?
        for produto_da_loja in loja.produtos:
            if produto_da_loja.nome == nome_produto:
                # se existir na loja, o comprador já tem o produto na sacola?
                if produto_da_loja in self.sacola:
                    # se tiver, deve só atualizar a quantidade
                    print(self.sacola[produto_da_loja.nome])
                else:
                    novo_produto = Produto(produto_da_loja.nome, produto_da_loja.preco, qtde)
                    produto_da_loja.quantidade -= qtde
                    self.sacola.append(novo_produto)
                    self.dinheiro -= produto_da_loja.preco * qtde
                    loja.caixa += produto_da_loja.preco * qtde

        # for produto in self.sacola:
        #     if produto.nome == nome_produto:
        #         produto.quantidade = qtde

    def report(self):
        print(f'========= {self.nome} =========')
        print(f'Dinheiro:\tR$ {self.dinheiro}')
        for produto in self.sacola:
            print(f'{produto.quantidade}x {produto.nome}')
