# dio-bank-poo: Sistema de Gerenciamento Bancário

Bem-vindo ao dio-bank-poo, um sistema bancário simples e funcional, feito em Python 3.9, onde você pode simular operações bancárias como depósito, saque, extrato, e gerenciar várias contas com facilidade. Ele foi criado com o objetivo de ajudar no aprendizado de Programação Orientada a Objetos (POO) e a lidar com operações bancárias de forma prática.

## Funcionalidades

- **Depósito**: Adiciona dinheiro ao saldo da conta selecionada.
- **Saque**: Permite retirar dinheiro da conta, com verificações de saldo, limites de saque e número máximo de saques diários.
- **Extrato**: Exibe todas as transações realizadas na conta, incluindo depósitos e saques, com detalhes de data e valor.
- **Múltiplas Contas**: Um usuário pode ter mais de uma conta bancária e alternar entre elas para realizar operações.
- **Histórico de Transações**: Cada conta mantém um histórico completo de todas as transações realizadas.
- **Autenticação**: O sistema exige login por CPF e senha, além de validar a senha antes de cada operação.
- **Menu Interativo**: Interface baseada em texto, onde o usuário pode navegar e realizar as operações bancárias.

## Como Começar

### Pré-requisitos

- Python 3.9 ou superior instalado
- Um terminal ou linha de comando para rodar o programa.

### Executando o Programa

1. Clone este repositório:

    ```sh
    git clone https://github.com/vitorshaft/dio-bank-poo.git
    ```

2. Navegue até o diretório do projeto:

    ```sh
    cd dio-bank-poo
    ```

3. Execute o programa:

    ```sh
    python main.py
    ```

## Uso

Ao executar o programa, será exibido um **menu preliminar**, onde o usuário poderá criar um novo perfil ou fazer login. Após o login, será apresentada uma série de opções para realizar operações bancárias, como depósito, saque e extrato.

### Operações Disponíveis:

- **Depósito**: O usuário pode adicionar um valor ao saldo da conta ativa.
- **Saque**: O usuário pode retirar dinheiro da conta, respeitando os limites de saque e saldo.
- **Extrato**: Exibe todas as transações realizadas na conta ativa, com data, tipo (depósito/saque) e valor.
- **Mudar Conta**: Se o usuário tiver mais de uma conta, pode alternar entre elas usando esta opção.
- **Listar Contas**: Exibe todas as contas associadas ao usuário logado.

## Exemplo de Operação

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

## Atualizações
### Versão 1.0
- Seleção de Conta: Agora, o cliente pode selecionar uma conta caso possua mais de uma. Se o cliente tiver apenas uma conta, ela será automaticamente usada.
- Formatação do Extrato: O extrato agora inclui a data de cada transação e apresenta as informações de forma mais organizada.