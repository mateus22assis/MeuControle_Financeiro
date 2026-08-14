# 💰 Controle Financeiro Pessoal

Sistema desenvolvido em Python para gerenciamento financeiro pessoal, utilizando Excel como base de dados. O projeto permite registrar receitas, despesas, compras parceladas, faturas do cartão de crédito, compromissos mensais e planejamento financeiro, além de servir como estudo prático de arquitetura de software, organização de código e boas práticas de desenvolvimento.

Todo o armazenamento é realizado diretamente na planilha Excel `ControleFinanceiro_2026_Exemplo.xlsx`.

## Objetivo

Auxiliar no controle financeiro pessoal por meio do registro de movimentações, acompanhamento de compromissos mensais, planejamento de reserva financeira e consulta de informações consolidadas em uma interface gráfica.

## Status do projeto

**Versão atual: v0.9.5 — concluída.**

A v0.9.5 encerra a primeira base funcional da GUI. O projeto agora entra em uma etapa de consolidação, revisão e preparação para a v1.0, que será a primeira versão considerada completa para uso diário.

## Funcionalidades atuais

### GUI

- Dashboard
- Resumo Financeiro
- Movimentações
- Categorias
- Compromissos
- Configurações

### Movimentações

- Cadastro de receitas e despesas
- Meios de pagamento: PIX, débito, dinheiro e cartão de crédito
- Compras parceladas com geração automática das parcelas
- Exclusão de movimentações
- Exclusão inteligente de compras parceladas, removendo as parcelas relacionadas
- Antecipação de parcelas selecionadas

### Categorias

- Cadastro pela GUI
- Categorias de receita e despesa
- Controle de categoria ativa/inativa
- Dados armazenados na aba `Categorias` do Excel

### Compromissos

- Cadastro pela GUI
- Alteração de valores
- Exclusão
- Integração com os cálculos financeiros

### Configurações

- Receita mensal
- Percentual de reserva
- Limite do cartão
- Dia de fechamento
- Dia de vencimento

### Planejamento financeiro

- Valor a guardar
- Saldo disponível
- Fatura do próximo mês
- Capacidade de comprometimento da próxima fatura

## Conceitos financeiros

O sistema diferencia a capacidade financeira pessoal do limite de crédito concedido pelo banco:

| Conceito | Significado |
| --- | --- |
| **Saldo disponível** | Dinheiro disponível para o ciclo atual. |
| **Fatura do próximo mês** | Compras de cartão já comprometidas para a próxima fatura. |
| **Pode comprometer na próxima fatura** | Valor que ainda pode ser acrescentado à próxima fatura sem comprometer excessivamente a capacidade financeira prevista do próximo ciclo. |
| **Limite total** | Limite de crédito fornecido pelo banco. |
| **Limite disponível** | Crédito que ainda está disponível no cartão. |

A capacidade de comprometimento da próxima fatura é calculada a partir de:

```text
Renda prevista - reserva - compromissos - fatura já comprometida
= capacidade de comprometimento restante
```

Compras novas no cartão de crédito não são descontadas imediatamente do saldo disponível: elas serão pagas por meio da fatura correspondente.

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/mateus22assis/MeuControle_Financeiro.git
```

### 2. Entrar na pasta

```bash
cd MeuControle_Financeiro
```

### 3. Instalar as dependências

```bash
pip install openpyxl customtkinter
```

### 4. Configurar a planilha

O repositório contém uma planilha de exemplo:

`ControleFinanceiro_2026_Exemplo.xlsx`

Para utilizar o sistema:

1. Faça uma cópia da planilha de exemplo.
2. Renomeie a cópia para `ControleFinanceiro_2026.xlsx`.
3. Mantenha esse arquivo na raiz do projeto.
4. Cadastre seus próprios dados nessa planilha.

A planilha `ControleFinanceiro_2026.xlsx` é ignorada pelo Git para evitar que dados financeiros pessoais sejam enviados ao repositório.

### 5. Executar

```bash
python main.py
```

## Estrutura do projeto

```text
.
├── main.py
├── testes.py
├── ControleFinanceiro_2026_Prototipo_v3.xlsx
├── README.md
├── backend/
│   ├── calculos.py
│   ├── consultas.py
│   ├── excel_manager.py
│   └── utils.py
├── gui/
│   ├── app.py
│   ├── dashboard.py
│   ├── resumo.py
│   ├── movimentacoes.py
│   ├── compromissos.py
│   ├── categorias.py
│   ├── configuracoes.py
│   └── componentes.py
└── docs/
```

- `main.py`: ponto de entrada e inicialização da aplicação.
- `gui/`: interface gráfica em CustomTkinter, organizada com Programação Orientada a Objetos (POO).
- `backend/calculos.py`: regras de negócio e cálculos financeiros.
- `backend/consultas.py`: consultas e filtros sobre movimentações.
- `backend/excel_manager.py`: leitura, gravação, ordenação e atualização da planilha Excel.
- `backend/utils.py`: validação de entradas e formatação monetária.
- `testes.py`: apoio a testes do projeto.
- `docs/`: documentos de UX, wireframes, backlog e homologação.

## Arquitetura

```text
Interface Gráfica (CustomTkinter / POO)
                ↓
       Backend modular
 (cálculos | consultas | utilitários)
                ↓
         excel_manager.py
                ↓
ControleFinanceiro_2026_Prototipo_v3.xlsx
```

A GUI utiliza POO para organizar componentes e estados da interface. O backend permanece modular, com funções e módulos independentes para as regras de negócio, consultas e manipulação dos dados. A planilha Excel persiste as configurações, movimentações, compromissos, categorias e faturas do sistema.

## Estrutura da planilha

| Aba | Finalidade |
| --- | --- |
| `Configuracoes` | Armazena receita mensal, percentual de reserva, limite do cartão e dias de fechamento e vencimento. |
| `Movimentacoes` | Registra receitas e despesas, incluindo categoria, meio de pagamento, valor e parcelas. |
| `CompromissosMensais` | Mantém os compromissos financeiros recorrentes. |
| `Categorias` | Armazena as categorias de receita e despesa e seu status de atividade. |
| `Faturas` | Exibe o resumo das faturas do cartão, com vencimento, valor e status. |

> A antiga aba `Dashboard` da planilha não é mais utilizada para visualização. O Dashboard é processado dinamicamente e exibido pela GUI.

### Estrutura da aba `Movimentacoes`

Cada movimentação possui os campos:

- Data
- Natureza (receita ou despesa)
- Meio
- Categoria
- Descrição
- Valor
- Parcelas

## Roadmap

| Versão | Status | Objetivo |
| --- | --- | --- |
| v0.8 | Concluída | Controle financeiro completo em Excel. |
| v0.8.5 | Concluída | Estabilização e homologação. |
| v0.9 | Concluída | Planejamento e arquitetura da GUI. |
| v0.9.5 | **CONCLUÍDA** | Primeira base funcional da GUI. |
| v1.0 | Próxima etapa | Primeira versão considerada completa para uso diário. |
| v1.5 | Planejada | Melhorias de experiência do usuário, filtros, pesquisa, edição, relatórios, gráficos, exportação e outras melhorias. |
| v2.0 | Futuro | Possíveis mudanças arquiteturais e evolução do armazenamento. |

### Possíveis objetivos da v1.0

- Revisão e organização final do código
- Melhorias visuais da GUI
- Melhorias de layout e responsividade
- Testes finais
- Documentação final
- Geração do executável `.exe`

## Histórico de versões

### v0.1 — Controle de cartão

- Controle de gastos à vista
- Controle de parcelamentos
- Fechamento de fatura

### v0.2 — Usabilidade

- Validação de entradas
- Formatação monetária
- Organização em módulos

### v0.3 — Planejamento financeiro

- Receita mensal
- Gastos fixos
- Percentual de reserva
- Saldo disponível

### v0.4 — Novos meios de pagamento

- PIX
- Débito
- Dinheiro

### v0.5 — Histórico de movimentações

- Registro de movimentações
- Registro automático das datas
- Consulta de histórico

### v0.6 — Integração com Excel

- Estrutura inicial da planilha
- Leitura e gravação em Excel
- Criação do `excel_manager.py`

### v0.6.5 — Consolidação do Excel

- Movimentações em Excel
- Receitas em Excel
- Compromissos mensais em Excel
- Refatoração do menu principal
- Padronização de natureza e meio
- Refatoração dos módulos principais
- Simplificação da estrutura do projeto

### v0.7 — Consolidação da migração para Excel

- Cadastro unificado de movimentações
- Parcelamentos registrados diretamente na planilha
- Ordenação automática por data
- Exclusão de movimentações
- Melhorias na validação de entradas
- Estrutura preparada para controle de faturas

### v0.8 — Controle completo das faturas

- Controle completo das faturas
- Controle do limite do cartão
- Aba `Faturas`
- Melhorias na integração com Excel

### v0.8.5 — Estabilização e homologação

- Atualização automática da aba `Faturas`
- Exclusão inteligente de compras parceladas
- Correções encontradas durante a homologação
- Remoção definitiva da estrutura legada baseada em JSON

### v0.9 — Planejamento e arquitetura da GUI

- Definição da stack tecnológica com CustomTkinter
- Criação de documentos de UX e wireframes
- Definição da arquitetura POO para a interface
- Implementação da estrutura base da aplicação
- Migração do Dashboard da planilha para visualização em tempo real na interface
- Backend consolidado como suporte para a GUI

### v0.9.5 — Primeira base funcional da GUI

- Dashboard, resumo financeiro, movimentações, categorias, compromissos e configurações disponíveis na GUI
- Cadastro e gestão de movimentações, incluindo parcelamentos, exclusão inteligente e antecipação de parcelas
- Cadastro e controle de status de categorias pela GUI
- Cadastro, alteração e exclusão de compromissos pela GUI
- Configurações financeiras acessíveis pela GUI
- Planejamento financeiro integrado ao Dashboard e ao resumo

## Tecnologias

- Python
- CustomTkinter (interface gráfica)
- OpenPyXL (manipulação de Excel)
- Microsoft Excel (base de dados)
- Git / GitHub

## Finalidade

Projeto criado para estudo prático de programação, organização financeira pessoal e desenvolvimento de software.

## Observação sobre IA

O desenvolvimento do projeto conta com apoio de Inteligência Artificial como ferramenta de estudo, revisão de código, discussão de arquitetura, planejamento, testes, documentação e aprendizado.
