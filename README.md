# 💰 Sistema Bancário em Python (Desafio de Programação)

Este repositório contém a implementação de um sistema bancário simples em Python, desenvolvido como parte de um desafio de programação. A aplicação simula operações básicas de uma conta bancária, incluindo **depósito**, **saque** e **visualização de extrato**.

## 🧠 Requisitos do Desafio

- ✅ Permitir **depósitos** de valores positivos.
- ✅ Permitir **saques** com as seguintes regras:
  - Limite de **3 saques diários**.
  - Valor máximo de **R$ 500,00 por saque**.
  - Não permitir saque se o **saldo for insuficiente**.
- ✅ A operação de **extrato** deve:
  - Exibir todos os depósitos e saques realizados.
  - Mostrar o **saldo atual** da conta.
  - Exibir a mensagem *"Não foram realizadas movimentações."* caso não haja nenhuma operação.
- ✅ Exibir os valores no formato: `R$ xxx.xx`

## 🧾 Funcionalidades

- `Depositar`: Adiciona um valor positivo ao saldo da conta.
- `Sacar`: Permite até 3 saques por dia com limite de R$ 500 por saque.
- `Extrato`: Lista todas as movimentações (depósitos e saques) e o saldo atual.

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Luiz0tavi0/dio-desafio00
   cd dio-desafio00
   python3 py_bank.py
   ```
