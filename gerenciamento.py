class Usuario:
    def __init__(self, nome_usuario, senha):
        self.nome_usuario = nome_usuario
        self.senha = senha


class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome   
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
       #RELATÓRIO ESTATÍSTICO (funcionalidade: produto mais vendido e produtos com estoque baixo)  
        self.quantidade_vendida = 0

    def vender(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            self.quantidade_vendida += quantidade
            print(f"{quantidade} unidades de {self.nome} vendidas.")
        else:
            print("Quantidade insuficiente em estoque") 



class GerenciadorEstoque:
    def __init__(self):
        self.produtos = []  
        self.usuarios = []  # Lista para armazenar usuários autorizados
        self.usuario_logado = None

    def adcionar_usuario(self, nome_usuario, senha):
        novo_usuario = Usuario(nome_usuario, senha)
        self.usuarios.append(novo_usuario)
        print("Usuário criado com sucesso!")

    def login(self, nome_usuario, senha):
        for usuario in  self.usuarios:
            if usuario.nome_usuario == nome_usuario and usuario.senha == senha:
                print("Login bem-sucedido!")
                self.usuario_logado = usuario
                return True
        print("Usuário ou senha incorretos")
        return False
     
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)  

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                break

    def atualizar_produtos(self, nome, novo_produto):
        for i, produto in enumerate(self.produtos):
            if produto.nome == nome:
                self.produtos[i] = novo_produto
                break

 # RELATÓRIO ESTATÍSTICO (funcionalidade: produto mais vendido e produtos com estoque baixo)            
    def produto_mais_vendido(self): 
        if not self.produtos:
            print("Nenhum produto no estoque.")
            return  
        mais_vendido = max(self.produtos, key=lambda produto: produto.quantidade_vendida, default = None) 
        if mais_vendido: 
            print(f"Produto mais vendido: {mais_vendido.nome} - Quantidade Vendida: {mais_vendido.quantidade_vendida}")
        else:
            print("Nenhum produto vendido ainda")

    def produtos_com_estoque_baixo(self, limite=5):
        produtos_baixo_estoque = [produto for produto in self.produtos if produto.quantidade < limite] 
        if produtos_baixo_estoque:
            print("Produtos com estoque baixo")
            for produto in produtos_baixo_estoque:
                print(f"{produto.nome} - Estoque: {produto.quantidade}")

        else:
            print("Todos os produtos têm estoque suficiente.")


    def menu_principal(self):
        while True:
            print("\n---- Menu Principal ----")
            print("1. Adicionar Produto")
            print("2. Remover Produto")
            print("3. Atualizar Produtos")
            print("4. Listar Produtos")
            print("5. Produto mais vendido")
            print("6. Produtos com estoque baixo")
            print("0. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("Nome do produto: ")
                descricao = input("Descrição: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade em estoque: "))
                novo_produto = Produto(nome, descricao, preco, quantidade)
                self.adicionar_produtos(novo_produto)

            elif escolha == "2":
                nome = input("Nome do produto a ser removido: ")
                self.remover_produto(nome)

            elif escolha == "3":
                nome = input("Nome do produto a ser atualizado: ")
                novo_nome = input("Novo nome: ")
                nova_descricao = input("Nova descrição: ")
                novo_preco = float(input("Novo preço: "))
                nova_quantidade = int(input("Nova quantidade em estoque: "))
                novo_produto = Produto(novo_nome, nova_descricao, novo_preco, nova_quantidade)
                self.atualizar_produtos(nome, novo_produto)

            elif escolha == "4":
                for produto in self.produtos:
                    print(f"{produto.nome}: {produto.descricao} / {produto.preco} / {produto.quantidade} em estoque")

         #RELATÓRIO ESTATÍSTICO (funcionalidade: produto mais vendido e produtos com estoque baixo)  
            elif escolha == "5":
                gerenciador.produto_mais_vendido()

            elif escolha == "6":
                limite_estoque_baixo = int(input("Digite o limite de estoque baixo: "))   
                gerenciador.produtos_com_estoque_baixo(limite_estoque_baixo)         

            elif escolha == "0":
                break

            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso
gerenciador = GerenciadorEstoque()

# Criando um usuário
nome_usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
gerenciador.adcionar_usuario(nome_usuario, senha)

# Fazendo login
while not gerenciador.usuario_logado:
    nome_usuario_login = input("Nome de usuário: ")
    senha_login = input("Senha: ")
    gerenciador.login(nome_usuario_login, senha_login)

# Após o login bem-sucedido, entra no menu principal
gerenciador.menu_principal()
