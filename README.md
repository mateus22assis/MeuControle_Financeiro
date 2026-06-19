# 💰 Controle Financeiro Pessoal

Sistema de controle financeiro desenvolvido em Python com foco em organização de gastos, planejamento financeiro e integração com Excel.

## 📌 Objetivo

O projeto nasceu para auxiliar no controle financeiro pessoal, permitindo registrar gastos, acompanhar parcelamentos, planejar reservas financeiras e visualizar informações consolidadas em uma planilha estruturada.

Atualmente o sistema está passando por uma migração gradual do armazenamento em JSON para uma estrutura baseada em Excel, preparando o terreno para dashboards, relatórios e futuras interfaces gráficas.

---

## Funcionalidades atuais

* Registro de gastos no cartão de crédito à vista
* Registro de compras parceladas
* Controle de parcelamentos existentes
* Fechamento de fatura
* Registro de gastos via PIX
* Registro de gastos via débito
* Registro de gastos em dinheiro
* Histórico de movimentações
* Controle de compromissos mensais
* Controle de receitas financeiras
* Separação entre receitas e despesas
* Controle de percentual de reserva financeira
* Cálculo automático de saldo disponível
* Integração com Excel utilizando OpenPyXL

---

## ▶️ Como executar

### 1. Clonar o repositório

git clone https://github.com/mateus22assis/MeuControle_Financeiro.git

### 2. Acessar a pasta

cd MeuControle_Financeiro

### 3. Instalar dependências

pip install openpyxl

### 4. Executar

python main.py

---

## 📊 Estrutura da planilha

Atualmente o sistema trabalha com as seguintes abas:

* Configuracoes
* Movimentacoes
* Faturas
* Dashboard
* CompromissosMensais

### Estrutura da aba Movimentacoes

Cada movimentação possui:

* Data
* Natureza (receita ou despesa)
* Meio (cartão, PIX, débito, dinheiro, salário, investimento etc.)
* Categoria
* Descrição
* Valor
* Parcelas
* Valor da Parcela

---

## 🚧 Status do Projeto

🚀 Em desenvolvimento

Versão atual: **v0.6.1**

---

## 📦 Versão Atual - v0.6.1 (Receitas Dinâmicas e Estrutura Financeira)

Esta versão consolida a migração da lógica financeira para uma estrutura baseada em movimentações registradas na planilha Excel.

### Implementado

* Leitura da aba Configuracoes
* Leitura da aba Movimentacoes
* Leitura da aba CompromissosMensais
* Registro de movimentações diretamente na planilha
* Separação entre receitas e despesas
* Inclusão dos conceitos de Natureza e Meio
* Cálculo automático de receitas através das movimentações
* Cálculo automático dos compromissos mensais
* Cálculo automático do valor a guardar
* Cálculo automático do saldo disponível
* Refatoração do módulo calculos.py
* Refatoração do módulo excel_manager.py

### Preparado para próximas versões

* Cadastro de receitas pelo menu
* Cadastro de compromissos pelo menu
* Dashboard automático
* Indicadores financeiros
* Relatórios gerenciais

---

## 📈 Histórico de versões

### 🟢 v0.1 — Controle de cartão

* Controle de gastos à vista
* Controle de parcelamentos
* Fechamento de fatura

### 🟡 v0.2 — Usabilidade

* Validação de entradas
* Formatação monetária
* Organização em módulos

### 🔵 v0.3 — Planejamento financeiro

* Receita mensal
* Gastos fixos
* Percentual de reserva
* Saldo disponível

### 🟣 v0.4 — Novos meios de pagamento

* PIX
* Débito
* Dinheiro

### 🟣 v0.5 — Histórico de movimentações

* Registro de movimentações
* Registro automático de datas
* Consulta de histórico

### 🟠 v0.6 — Integração com Excel

* Estrutura inicial da planilha
* Leitura e gravação em Excel
* Compromissos mensais
* Criação do excel_manager.py

### 🟠 v0.6.1 — Receitas Dinâmicas e Estrutura Financeira

* Separação entre receitas e despesas
* Inclusão dos conceitos de Natureza e Meio
* Receitas calculadas pelas movimentações
* Compromissos integrados aos cálculos
* Refatoração dos cálculos financeiros
* Base preparada para dashboards

### 🔴 v0.6.2 — Menus e Cadastros

Planejado:

* Cadastro de receitas pelo menu
* Cadastro de compromissos pelo menu
* Consulta de compromissos
* Início das funções de edição e exclusão

### 🔴 v0.7 — Integração completa

Planejado:

* Movimentações totalmente migradas para Excel
* Parcelamentos totalmente migrados para Excel
* Faturas totalmente migradas para Excel

### 🚀 v0.8

Planejado:

* Dashboard funcional
* Indicadores financeiros
* Gráficos automáticos

### 🚀 v0.9

Planejado:

* Interface para entrada de dados
* Formulários para lançamentos

### 🏁 v1.0

* Aplicação completa
* Executável (.exe)
* Uso por terceiros

---

## 🎯 Finalidade

Projeto criado para estudo prático de programação, organização financeira pessoal e desenvolvimento de software.

---

## 🛠️ Tecnologias

* Python
* OpenPyXL
* Excel

---

## 🤖 Observação

O desenvolvimento do projeto conta com apoio de Inteligência Artificial como ferramenta de aprendizado, revisão de código, discussão de arquitetura e boas práticas de desenvolvimento.
