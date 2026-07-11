# 💰 Controle Financeiro Pessoal

Sistema de controle financeiro desenvolvido em Python com foco em organização financeira, planejamento e integração com Excel.

## 📌 Objetivo

O projeto nasceu para auxiliar no controle financeiro pessoal, permitindo registrar receitas, despesas, acompanhar parcelamentos, planejar reservas financeiras e visualizar informações consolidadas em uma planilha estruturada.

Atualmente o sistema está passando por uma migração gradual do armazenamento em JSON para uma estrutura baseada em Excel, preparando o terreno para dashboards, relatórios e futuras interfaces gráficas.

---

# 🚀 Funcionalidades atuais

### Movimentações

* Registro de receitas
* Registro de despesas
* Separação entre receitas e despesas
* Histórico de movimentações
* Registro automático da data
* Categorias personalizadas
* Diferentes meios de pagamento

### Cartão de crédito

* Registro de gastos à vista
* Registro de compras parceladas
* Controle de parcelamentos existentes
* Fechamento de fatura

### Planejamento financeiro

* Controle de compromissos mensais
* Percentual de reserva financeira
* Cálculo automático do valor a guardar
* Cálculo automático do saldo disponível
* Resumo financeiro consolidado

### Integração com Excel

* Leitura e gravação em Excel utilizando OpenPyXL
* Movimentações armazenadas em planilha
* Compromissos mensais armazenados em planilha
* Estrutura preparada para dashboards

---

# ▶️ Como executar

## 1. Clonar o repositório

```bash
git clone https://github.com/mateus22assis/MeuControle_Financeiro.git
```

## 2. Entrar na pasta

```bash
cd MeuControle_Financeiro
```

## 3. Instalar dependências

```bash
pip install openpyxl
```

## 4. Executar

```bash
python main.py
```

---

# 📂 Estrutura do projeto

## main.py

Menu principal da aplicação.

## excel_manager.py

Responsável pela leitura e gravação da planilha.

## calculos.py

Regras de negócio e cálculos financeiros.

## consultas.py

Funções auxiliares para consultas dos dados.

## dados.py

Parte legada responsável pelo cartão de crédito e parcelamentos.

## testes.py

Arquivo utilizado para testes.

## data.json

Estrutura temporária para cartão e parcelamentos.

## ControleFinanceiro_2026_Prototipo_v3.xlsx

Banco de dados principal do projeto.

---

# 📊 Estrutura da planilha

Atualmente o sistema trabalha com as seguintes abas:

* Configuracoes
* Movimentacoes
* CompromissosMensais
* Dashboard
* Faturas

---

## Estrutura da aba Movimentacoes

Cada movimentação possui:

* Data
* Natureza (receita ou despesa)
* Meio
* Categoria
* Descrição
* Valor
* Parcelas
* Valor da Parcela

Exemplos de meios:

* PIX
* Débito
* Dinheiro
* Cartão de crédito
* Salário
* Investimento

---

# 🚧 Status do Projeto

🚀 Em desenvolvimento

Versão atual:

## v0.7

---

# 📦 Versão Atual — v0.7

Esta versão consolida a migração do projeto para Excel, eliminando a dependência do fluxo principal baseado em JSON e preparando o sistema para o gerenciamento completo de faturas.

## Implementado

### Excel

- Movimentações em Excel
- Receitas em Excel
- Compromissos mensais em Excel
- Configurações em Excel
- Ordenação automática das movimentações por data

### Movimentações

- Cadastro unificado de receitas e despesas
- Registro de compras parceladas
- Geração automática das parcelas
- Exclusão de movimentações
- Melhorias na validação das entradas

### Estrutura

- Menu principal simplificado
- Separação entre regras de negócio e acesso aos dados
- Migração quase completa do JSON para Excel

# 📈 Histórico de versões

## 🟢 v0.1 — Controle de cartão

* Controle de gastos à vista
* Controle de parcelamentos
* Fechamento de fatura

---

## 🟡 v0.2 — Usabilidade

* Validação de entradas
* Formatação monetária
* Organização em módulos

---

## 🔵 v0.3 — Planejamento financeiro

* Receita mensal
* Gastos fixos
* Percentual de reserva
* Saldo disponível

---

## 🟣 v0.4 — Novos meios de pagamento

* PIX
* Débito
* Dinheiro

---

## 🟣 v0.5 — Histórico de movimentações

* Registro de movimentações
* Registro automático das datas
* Consulta de histórico

---

## 🟠 v0.6 — Integração com Excel

* Estrutura inicial da planilha
* Leitura e gravação em Excel
* Criação do excel_manager.py

---

## 🟠 v0.6.5 — Consolidação do Excel

* Movimentações em Excel
* Receitas em Excel
* Compromissos mensais em Excel
* Refatoração do menu principal
* Padronização de Natureza e Meio
* Refatoração dos módulos principais
* Simplificação da estrutura do projeto

## 🟢 v0.7 — Consolidação da migração para Excel

- Cadastro unificado de movimentações
- Parcelamentos registrados diretamente na planilha
- Ordenação automática por data
- Exclusão de movimentações
- Melhorias na validação de entradas
- Estrutura preparada para controle de faturas

---

# 🔮 Próximas versões

## 🔵 v0.8

Planejado:

- Controle completo do limite do cartão
- Cálculo do limite disponível
- Consulta de faturas
- Integração da aba Faturas

---

## 🟣 v0.9

Planejado:

- Dashboard financeiro
- Indicadores
- Gráficos automáticos

---

## 🏁 v1.0

- Sistema totalmente baseado em Excel
- Dashboard integrado
- Interface gráfica
- Executável (.exe)

# 🎯 Finalidade

Projeto criado para estudo prático de programação, organização financeira pessoal e desenvolvimento de software.

---

# 🛠️ Tecnologias

* Python
* OpenPyXL
* Excel

---

# 🤖 Observação

O desenvolvimento do projeto conta com apoio de Inteligência Artificial como ferramenta de aprendizado, revisão de código, discussão de arquitetura e boas práticas de desenvolvimento.
