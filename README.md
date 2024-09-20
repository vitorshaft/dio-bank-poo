# dio-bank-poo: Sistema Simples de Gerenciamento Bancário

Este é um sistema bancário desenvolvido em Python 3.9, pensado para facilitar o gerenciamento de contas de forma intuitiva. Com ele, você pode realizar operações como depósito, saque, consulta de extrato e até gerenciar várias contas ao mesmo tempo. Tudo isso em um ambiente simulado e interativo, usando o terminal.

O projeto foi criado com o objetivo de oferecer um exemplo prático de como desenvolver um sistema bancário básico em Python, utilizando conceitos de Programação Orientada a Objetos (POO), autenticação de usuários e controle de transações.

## Funcionalidades Principais

- **Depósito**: Adiciona dinheiro à sua conta.
- **Saque**: Permite retirar dinheiro da conta, respeitando o limite de saques diários e o saldo disponível.
- **Extrato**: Mostra todas as transações feitas na conta, com detalhes como data e valor.
- **Gerenciamento de Múltiplas Contas**: Se você tiver mais de uma conta, pode alternar entre elas para realizar operações.
- **Histórico Completo de Transações**: Todas as contas possuem um histórico detalhado de suas movimentações.
- **Login Seguro**: O acesso ao sistema é feito via CPF e senha, e todas as operações precisam ser autenticadas.
- **Interface de Texto Simples e Intuitiva**: O usuário pode navegar facilmente pelo sistema através de menus interativos no terminal.

## Como Iniciar

### Requisitos

- Ter o **Python 3.9** ou superior instalado no seu computador.
- Um terminal ou linha de comando para executar o programa.

### Executando o Sistema

1. Faça o clone deste repositório no seu computador:

    ```sh
    git clone https://github.com/vitorshaft/dio-bank-poo.git
    ```

2. Acesse o diretório do projeto:

    ```sh
    cd dio-bank-poo
    ```

3. Execute o sistema com o seguinte comando:

    ```sh
    python main.py
    ```

## Como Usar

Ao rodar o programa, você verá um **menu preliminar** onde poderá criar um novo perfil de usuário ou fazer login com um perfil existente. Depois de logado, você terá acesso a várias opções para gerenciar suas contas bancárias.

### Menu Preliminar:

- `[1]` Criar um Novo Perfil
- `[2]` Fazer Login
- `[q]` Sair

Após fazer login, você terá um menu completo com as seguintes opções:

### Menu Principal:

- `[d]` Depositar dinheiro em uma conta.
- `[s]` Sacar dinheiro da conta.
- `[e]` Ver o extrato da conta atual.
- `[nc]` Criar uma nova conta bancária.
- `[lc]` Listar todas as suas contas.
- `[mc]` Alternar entre as contas que você possui.
- `[q]` Fazer logout do sistema.

### Operações Disponíveis:

- **Depósito**: Permite adicionar um valor ao saldo da conta que você está utilizando no momento.
- **Saque**: Permite retirar dinheiro da conta, respeitando os limites de saldo e o número máximo de saques permitidos por dia.
- **Extrato**: Mostra todas as transações feitas na conta, com a data e o valor de cada uma.
- **Mudar Conta**: Se você tiver mais de uma conta, pode usar essa opção para mudar entre elas.
- **Listar Contas**: Exibe todas as suas contas com os respectivos saldos.

## Exemplo de Como Funciona

```sh
================= MENU ==================
[d]    Depositar
[s]    Sacar
[e]    Extrato
[nc]   Nova Conta
[lc]   Listar Contas
[mc]   Mudar Conta
[q]    Sair
=========================================
=> d
Informe o valor do depósito: 1000.00

=== Depósito realizado com sucesso! ===

================ EXTRATO ================
14-09-2024 11:57:58
Depósito:
        R$ 1000.00
Saldo:
        R$ 1000.00
=========================================
```
### Versão 1.1
- Agora, clientes que possuem mais de uma conta podem alternar entre elas para realizar operações.
- O extrato foi aprimorado para mostrar a data e a hora das transações.
- Limitações de saldo e número de saques diários foram implementadas.

### Versão 1.0
- Seleção de Conta: Agora, o cliente pode selecionar uma conta caso possua mais de uma. Se o cliente tiver apenas uma conta, ela será automaticamente usada.
- Formatação do Extrato: O extrato agora inclui a data de cada transação e apresenta as informações de forma mais organizada.