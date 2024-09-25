from comprador import Comprador
from loja import Loja
from produto import Produto

joao = Comprador('João')
quitanda = Loja('Quitanda', 1000)

# quitanda.comprar_produto(Produto('Melancia', 12, 10))
# quitanda.report()

joao.report()
quitanda.report()

joao.comprar(quitanda, 5, 'maçã')

joao.report()
quitanda.report()
