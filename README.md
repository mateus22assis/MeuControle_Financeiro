# 💰 Controle Financeiro Pessoal

Este projeto é um sistema simples de controle financeiro desenvolvido em Python.

## 📌 Objetivo

O objetivo principal é auxiliar no controle de gastos, especialmente no uso de cartão de crédito, incluindo:

* Controle de gastos na fatura
* Gerenciamento de compras parceladas
* Simulação de fechamento de fatura

---
▶️ Como executar o projeto
sistema executavel via terminal (CLI)

Siga os passos abaixo para rodar o sistema localmente:

📥 1. Clonar o repositório
git clone https://github.com/mateus22assis/MeuControle_Financeiro.git
📂 2. Acessar a pasta do projeto
cd MeuControle_Financeiro
▶️ 3. Executar o programa
python main.py
🧪 4. Testar funcionalidades

No menu interativo, você poderá:

Adicionar gastos no cartão à vista
Criar compras parceladas
Visualizar o resumo da fatura
Fechar a fatura mensal
⚠️ Observações
O sistema utiliza o arquivo data.json para salvar os dados
Caso queira reiniciar os testes, basta apagar ou limpar esse arquivo
Certifique-se de ter o Python instalado (versão 3.x)

---

## 🚧 Status do Projeto

🚀 Em desenvolvimento  
📌 Versão atual: **v0.2**

---

## 📦 Versão Atual - v0.2 (Usabilidade)

Esta versão melhora a experiência do usuário e a robustez do sistema.

### Funcionalidades:
* Validação de entrada de dados (números e textos)
* Bloqueio de valores inválidos (negativos ou zero)
* Formatação de valores no padrão brasileiro (R$)
* Melhor organização do código (utils.py)
* Melhor exibição das informações no terminal

👉 Esta versão foca na usabilidade e na clareza do sistema.

---

## 📈 Histórico de Versões

### 🟢 v0.1 — Controle de cartão 
* Sistema base funcionando
* Controle de gastos à vista
* Controle de parcelamentos
* Lógica de fechamento de fatura

### 🟡 v0.2 — Usabilidade (atual)
* Validação de entrada de dados
* Formatação de valores (R$)
* Melhorias nas mensagens e exibição
* Organização do código em módulos

### 🔵 v0.3 — Cálculo financeiro completo (planejado)
* Integração com `calculos.py`
* Receita mensal
* Gastos fixos
* Percentual para guardar
* Cálculo de saldo disponível

### 🟣 v0.4 — Outros tipos de pagamento
* PIX
* Débito
* Dinheiro

### 🟠 v0.5 — Organização interna
* Refatoração do código
* Melhor separação de responsabilidades

### 🔥 v0.6 — Integração com Excel
* Leitura de dados via Excel
* Geração de relatórios

### 🚀 v1.0 — Versão final (produto)
* Sistema utilizável por terceiros
* Geração de executável (.exe)
* Modelo de planilha integrado

---

## 🎯 Finalidade

Este projeto foi criado para uso pessoal e também como forma de estudo prático em programação.

---

## 🤖 Observação

Por se tratar de um projeto de aprendizado, o desenvolvimento conta com o auxílio de Inteligência Artificial para apoio na construção e entendimento do código.

---

## 🛠️ Tecnologias utilizadas

* Python