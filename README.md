# 💰 Controle Financeiro Pessoal

Sistema desenvolvido em Python para gerenciamento financeiro pessoal, utilizando Excel como banco de dados. O projeto permite controlar receitas, despesas, compras parceladas, faturas do cartão de crédito e planejamento financeiro, servindo também como estudo prático de arquitetura de software, organização de código e boas práticas de desenvolvimento.

## 📌 Objetivo

O projeto auxilia no controle financeiro pessoal por meio do registro de movimentações, acompanhamento de compromissos mensais, planejamento de reserva financeira e consulta de informações consolidadas.

Todo o armazenamento é realizado diretamente na planilha Excel `ControleFinanceiro_2026_Prototipo_v3.xlsx`.

---

# 🚀 Funcionalidades

### Movimentações

- Cadastro unificado de receitas e despesas
- Histórico de movimentações com data, categoria, meio de pagamento, descrição e valor
- Categorias informadas pelo usuário
- Diferentes meios de pagamento: PIX, débito, dinheiro e cartão de crédito
- Compras parceladas com geração automática das parcelas
- Exclusão inteligente de compras parceladas, removendo as parcelas relacionadas

### Planejamento financeiro

- Controle de compromissos mensais
- Resumo financeiro de receitas, despesas e compromissos
- Cálculo automático do valor a guardar conforme o percentual de reserva configurado
- Cálculo do saldo disponível

### Cartão de crédito e Excel

- Atualização automática da aba **Faturas** após inclusões e exclusões de movimentações
- Controle do limite do cartão
- Cálculo do limite comprometido e do limite disponível
- Integração completa com Excel por meio do OpenPyXL

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

## 3. Instalar a dependência

```bash
pip install openpyxl
```

## 4. Executar

```bash
python main.py
```

---

# 📂 Estrutura do projeto

```text
.
├── main.py
├── calculos.py
├── excel_manager.py
├── consultas.py
├── utils.py
├── testes.py
├── ControleFinanceiro_2026_Prototipo_v3.xlsx
├── README.md
└── docs/
    ├── ASSISTENTE.md
    ├── BACKLOG_v0.8.5.md
    ├── BACKLOG_v0.9.md
    └── HOMOLOGACAO_v0.8.md
```

- `main.py`: menu principal e interação com a pessoa usuária.
- `calculos.py`: regras de negócio e cálculos financeiros.
- `excel_manager.py`: leitura, gravação, ordenação e atualização da planilha Excel.
- `consultas.py`: consultas e filtros sobre as movimentações.
- `utils.py`: validação de entradas e formatação monetária.
- `testes.py`: apoio a testes do projeto.
- `ControleFinanceiro_2026_Prototipo_v3.xlsx`: base de dados principal.
- `docs/`: documentos de contexto, backlog e homologação.

---

# Arquitetura

```text
main.py
   ↓
calculos.py
   ↓
excel_manager.py
   ↓
ControleFinanceiro_2026_Prototipo_v3.xlsx
```

- `main.py` concentra os menus, a coleta de dados e a apresentação das informações.
- `calculos.py` reúne os cálculos de resumo financeiro, reserva, saldo e limite do cartão.
- `excel_manager.py` é a camada de acesso à planilha: lê, grava, ordena movimentações e atualiza as abas derivadas.
- A planilha Excel persiste as configurações, movimentações, compromissos e faturas do sistema.

---

# 📊 Estrutura da planilha

O sistema utiliza as seguintes abas:

| Aba | Finalidade |
| --- | --- |
| `Configuracoes` | Armazena receita mensal, percentual de reserva, limite do cartão e datas de fechamento e vencimento. |
| `Movimentacoes` | Registra receitas e despesas, incluindo categoria, meio de pagamento, valor e parcelas. |
| `CompromissosMensais` | Mantém os compromissos financeiros recorrentes. |
| `Dashboard` | Aba reservada para a visualização consolidada dos dados financeiros. |
| `Faturas` | Exibe o resumo das faturas do cartão, com vencimento, valor e status. |

## Estrutura da aba `Movimentacoes`

Cada movimentação possui os campos:

- Data
- Natureza (receita ou despesa)
- Meio
- Categoria
- Descrição
- Valor
- Parcelas

---

# 🚧 Status do projeto

**Versão atual:** v0.8.5

Projeto em desenvolvimento ativo.

---

# 🗺️ Roadmap

| Versão | Status | Objetivo |
| --- | --- | --- |
| ✅ v0.8 | Concluída | Controle financeiro completo em Excel |
| 🚧 v0.8.5 | Em desenvolvimento | Estabilização e homologação |
| 📋 v0.9 | Planejada | Dashboard e preparação da interface |
| 📋 v1.0 | Planejada | Primeira versão completa |
| 📋 v1.5 | Planejada | Evolução da experiência do usuário |
| 📋 v2.0 | Futuro | Evolução da arquitetura |

---

# 📈 Histórico de versões

## 🟢 v0.1 — Controle de cartão

- Controle de gastos à vista
- Controle de parcelamentos
- Fechamento de fatura

## 🟡 v0.2 — Usabilidade

- Validação de entradas
- Formatação monetária
- Organização em módulos

## 🔵 v0.3 — Planejamento financeiro

- Receita mensal
- Gastos fixos
- Percentual de reserva
- Saldo disponível

## 🟣 v0.4 — Novos meios de pagamento

- PIX
- Débito
- Dinheiro

## 🟣 v0.5 — Histórico de movimentações

- Registro de movimentações
- Registro automático das datas
- Consulta de histórico

## 🟠 v0.6 — Integração com Excel

- Estrutura inicial da planilha
- Leitura e gravação em Excel
- Criação do `excel_manager.py`

## 🟠 v0.6.5 — Consolidação do Excel

- Movimentações em Excel
- Receitas em Excel
- Compromissos mensais em Excel
- Refatoração do menu principal
- Padronização de natureza e meio
- Refatoração dos módulos principais
- Simplificação da estrutura do projeto

## 🟢 v0.7 — Consolidação da migração para Excel

- Cadastro unificado de movimentações
- Parcelamentos registrados diretamente na planilha
- Ordenação automática por data
- Exclusão de movimentações
- Melhorias na validação de entradas
- Estrutura preparada para controle de faturas

## v0.8

- Controle completo das Faturas
- Controle do limite do cartão
- Aba Faturas
- Melhorias na integração com Excel

## v0.8.5

- Atualização automática da aba Faturas
- Exclusão inteligente de compras parceladas
- Correções encontradas durante a homologação
- Remoção definitiva da estrutura legada baseada em JSON

---

# 🔮 Próximas versões

## v0.9

- Dashboard financeiro
- Interface de lançamentos
- Cadastro de categorias
- Melhorias de usabilidade

## v1.0

Primeira versão considerada completa para uso diário.

- Dashboard integrado
- Interface gráfica
- Executável (`.exe`)
- Documentação consolidada

## v1.5

Foco em experiência do usuário.

- Pesquisa de movimentações
- Filtros por período
- Edição de movimentações
- Relatórios mensais e anuais
- Exportação para PDF
- Melhorias no Dashboard
- Configurações do sistema
- Backup da planilha
- Melhorias na interface

## v2.0

Foco em arquitetura.

- Refatoração para Programação Orientada a Objetos (POO)
- Otimizações de desempenho
- Identificadores persistentes para movimentações
- Suporte a múltiplos cartões
- Evolução da arquitetura
- Preparação para futuras formas de persistência de dados, caso necessário

---

# 🎯 Finalidade

Projeto criado para estudo prático de programação, organização financeira pessoal e desenvolvimento de software.

---

# 🛠️ Tecnologias

- Python
- OpenPyXL
- Microsoft Excel
- Git
- GitHub

---

# 🤖 Observação

O desenvolvimento do projeto conta com apoio de Inteligência Artificial como ferramenta de estudo, revisão de código, discussão de arquitetura, planejamento, testes, documentação e aprendizado.
