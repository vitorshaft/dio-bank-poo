import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import getpass


class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco, senha):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf  # CPF já armazenado sem separadores
        self.endereco = endereco
        self.senha = senha
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\nAgência:\t{self.agencia}\nConta:\t\t{self.numero}\nTitular:\t{self.cliente.nome}"""


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu_preliminar():
    print("\n=============== MENU PRELIMINAR ===============")
    print("[1] Criar Novo Perfil")
    print("[2] Login")
    print("[q] Sair")
    return input("Escolha uma opção: ")


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def selecionar_conta(cliente):
    """Permite ao cliente selecionar uma conta se ele possuir mais de uma."""
    if len(cliente.contas) == 1:
        return cliente.contas[0]

    print("\nSelecione a conta:")
    for i, conta in enumerate(cliente.contas, start=1):
        print(f"{i}. Agência: {conta.agencia} | Conta: {conta.numero} | Saldo: R$ {conta.saldo:.2f}")

    indice = int(input("Informe o número da conta: ")) - 1
    if 0 <= indice < len(cliente.contas):
        return cliente.contas[indice]
    else:
        print("Opção inválida!")
        return None


def login(clientes):
    cpf = input("Informe o CPF: ").strip()
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return None
    senha = getpass.getpass("Informe a senha: ")
    if cliente.senha != senha:
        print("\n@@@ Senha incorreta! @@@")
        return None
    print("\n=== Login realizado com sucesso! ===")
    return cliente


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ").strip()
    if filtrar_cliente(cpf, clientes):
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    senha = getpass.getpass("Crie uma senha: ")

    cliente = Cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco, senha=senha)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")
    return cliente


def depositar(cliente_logado):
    conta = selecionar_conta(cliente_logado)
    if not conta:
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    cliente_logado.realizar_transacao(conta, transacao)


def sacar(cliente_logado):
    conta = selecionar_conta(cliente_logado)
    if not conta:
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    cliente_logado.realizar_transacao(conta, transacao)


def exibir_extrato(cliente_logado):
    conta = selecionar_conta(cliente_logado)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_conta(contas, cliente_logado):
    numero_conta = len(contas) + 1  # Número sequencial de conta
    conta = ContaCorrente(numero=numero_conta, cliente=cliente_logado)
    cliente_logado.contas.append(conta)
    contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")
    return conta


def listar_contas(cliente_logado):
    for conta in cliente_logado.contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []
    cliente_logado = None

    while True:
        if not cliente_logado:
            opcao = menu_preliminar()

            if opcao == "1":
                cliente_logado = criar_cliente(clientes)
                if cliente_logado:
                    criar_conta(contas, cliente_logado)

            elif opcao == "2":
                cliente_logado = login(clientes)

            elif opcao == "q":
                break

            else:
                print("\n@@@ Operação inválida! Tente novamente. @@@")


        else:
            opcao = menu()

            if opcao == "d":
                depositar(cliente_logado)

            elif opcao == "s":
                sacar(cliente_logado)

            elif opcao == "e":
                exibir_extrato(cliente_logado)

            elif opcao == "nc":
                criar_conta(contas, cliente_logado)

            elif opcao == "lc":
                listar_contas(cliente_logado)

            elif opcao == "q":
                cliente_logado = None  # Logout
                print("\n=== Logout realizado com sucesso! ===")

            else:
                print("\n@@@ Operação inválida! Tente novamente. @@@")


if __name__ == "__main__":
    main()
