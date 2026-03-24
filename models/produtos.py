class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
    
    def adicionar(self, valor):
        self.quantidade += valor
        
    def remover(self, valor):
        self.quantidade -= valor