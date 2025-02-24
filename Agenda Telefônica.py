class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        self.contatos[nome] = telefone
        print(f"Contato {nome} adicionado com sucesso!")

    def buscar_contato(self, nome):
        return self.contatos.get(nome, "Contato não encontrado.")

    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print(f"{nome}: {telefone}")

# Criando a agenda
agenda = AgendaTelefonica()

while True:
    print("\n1. Adicionar Contato\n2. Buscar Contato\n3. Listar Contatos\n4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda.adicionar_contato(nome, telefone)
    elif opcao == "2":
        nome = input("Nome do contato: ")
        print(agenda.buscar_contato(nome))
    elif opcao == "3":
        agenda.listar_contatos()
    elif opcao == "4":
        break
    else:
        print("Opção inválida, tente novamente.")
