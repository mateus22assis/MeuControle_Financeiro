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
* Definição de receita mensal
* Definição de percentual de reserva financeira
* Histórico de movimentações
* Controle de compromissos mensais
* Integração inicial com Excel utilizando OpenPyXL

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

---

## 🚧 Status do Projeto

🚀 Em desenvolvimento

Versão atual: **v0.6**

---

## 📦 Versão Atual - v0.6 (Migração para Excel)

Esta versão marca o início da transição do sistema para uma arquitetura baseada em planilhas Excel.

### Implementado

* Leitura da aba Configuracoes
* Escrita de configurações na planilha
* Leitura da aba CompromissosMensais
* Cálculo automático do total de compromissos mensais
* Separação entre regras de negócio e manipulação da planilha
* Criação do módulo excel_manager.py

### Em andamento

* Migração gradual das funções do dados.py
* Integração completa das movimentações com Excel
* Alimentação automática do Dashboard

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

* Estrutura de planilha criada
* Leitura e gravação em Excel
* Compromissos mensais
* Separação da camada de dados

### 🔴 v0.7 — Integração completa

Planejado:

* Movimentações diretamente no Excel
* Parcelamentos diretamente no Excel
* Faturas diretamente no Excel

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

O desenvolvimento do projeto conta com apoio de Inteligência Artificial como ferramenta de aprendizado, revisão e discussão de arquitetura.
