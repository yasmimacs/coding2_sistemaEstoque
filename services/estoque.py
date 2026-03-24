class Estoque:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.quantidade)
    
    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                print("\nProduto encontrado:")
                print(f"Nome: {produto.nome}")
                print(f"Quantidade: {produto.quantidade}")
                return 
        
        print(f"\nProduto '{nome}' não encontrado.")
        return None
    
    def atualizar_quantidade(self, nome, nova_quantidade):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                produto.quantidade = nova_quantidade
                print(f"\nQuantidade do produto '{produto.nome}' atualizada para {nova_quantidade}")
            return
    
        print(f"\nProduto '{produto.nome}' não encontrado.")