
from models.produtos import Produto
from services.estoque import Estoque

estoque = Estoque()

p1 = Produto("Mouse", 10)
p2 = Produto("Teclado", 15)
p3 = Produto("Monitor", 6)

estoque.adicionar_produto(p1)
estoque.adicionar_produto(p2)
estoque.adicionar_produto(p3)

estoque.listar_produtos()

estoque.buscar_produto("Mouse")
estoque.buscar_produto("batata")

estoque.atualizar_quantidade("Mouse", 75)

estoque.listar_produtos()