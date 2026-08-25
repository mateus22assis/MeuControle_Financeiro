# 💰 Meu Controle Financeiro

Sistema desenvolvido em Python para gerenciamento financeiro pessoal, utilizando Excel como base de dados.

O projeto permite registrar receitas, despesas, compras parceladas, faturas do cartão de crédito, compromissos mensais, categorias e configurações financeiras, além de apresentar um resumo do planejamento financeiro por meio de uma interface gráfica.

O projeto também foi desenvolvido como estudo prático de programação, organização de código, arquitetura, Programação Orientada a Objetos, boas práticas e evolução incremental de software.

---

## 🎯 Objetivo

Auxiliar no controle financeiro pessoal por meio do registro de movimentações, acompanhamento de compromissos, controle de compras no cartão de crédito e planejamento financeiro.

O sistema busca mostrar não apenas o quanto ainda existe de limite no cartão, mas também quanto pode ser comprometido considerando a capacidade financeira prevista para o próximo ciclo.

---

## 🚀 Status do projeto

**Versão atual: v1.0 — concluída.**

A v1.0 representa a primeira versão completa do sistema para uso diário.

Nesta versão foram consolidados:

* Backend financeiro;
* Persistência dos dados em Excel;
* Interface gráfica com CustomTkinter;
* Cadastro e gerenciamento de movimentações;
* Controle de compras parceladas;
* Controle de faturas;
* Controle de categorias;
* Controle de compromissos mensais;
* Configurações financeiras;
* Resumo financeiro;
* Planejamento financeiro;
* Geração do executável Windows.

---

# ✨ Funcionalidades

## 🖥️ Interface gráfica

A aplicação possui uma interface desenvolvida com CustomTkinter e organizada em módulos:

* Dashboard;
* Resumo Financeiro;
* Movimentações;
* Categorias;
* Compromissos;
* Configurações.

A interface utiliza Programação Orientada a Objetos para organizar os componentes e o estado das diferentes telas.

---

## 💸 Movimentações

Permite registrar e gerenciar movimentações financeiras.

Funcionalidades:

* Cadastro de receitas;
* Cadastro de despesas;
* PIX;
* Débito;
* Dinheiro;
* Cartão de crédito;
* Categorias;
* Registro de datas;
* Compras parceladas;
* Geração automática das parcelas;
* Exclusão de movimentações;
* Exclusão inteligente de compras parceladas;
* Antecipação de parcelas.

As movimentações são armazenadas na aba `Movimentacoes` da planilha.

---

## 🏷️ Categorias

Permite organizar as movimentações por categorias.

Funcionalidades:

* Cadastro de categorias;
* Categorias de receita;
* Categorias de despesa;
* Ativação e desativação de categorias;
* Integração com o cadastro de movimentações.

As categorias são armazenadas na aba `Categorias` do Excel.

---

## 📅 Compromissos mensais

Permite cadastrar despesas recorrentes que fazem parte do planejamento financeiro.

Funcionalidades:

* Cadastro;
* Alteração;
* Exclusão;
* Integração com os cálculos financeiros.

Os compromissos são armazenados na aba `CompromissosMensais`.

---

## ⚙️ Configurações

Permite configurar os principais parâmetros financeiros do sistema:

* Receita mensal;
* Percentual de reserva;
* Limite do cartão;
* Dia de fechamento da fatura;
* Dia de vencimento da fatura.

Essas informações são armazenadas na aba `Configuracoes`.

---

## 💳 Controle de cartão

O sistema possui regras próprias para o controle do cartão de crédito.

Funcionalidades:

* Determinação automática da fatura de cada compra;
* Controle de compras parceladas;
* Cálculo das próximas faturas;
* Controle do limite total;
* Cálculo do limite disponível;
* Registro de abatimentos de fatura;
* Antecipação de parcelas;
* Integração das compras com o planejamento financeiro.

O dia de fechamento e o dia de vencimento podem ser configurados pelo usuário.

---

# 📊 Planejamento financeiro

O sistema apresenta informações consolidadas para auxiliar na tomada de decisão financeira.

Entre elas:

* Receita mensal;
* Valor a guardar;
* Saldo disponível;
* Gastos fixos;
* Fatura do próximo mês;
* Capacidade de comprometimento da próxima fatura;
* Limite total do cartão;
* Limite disponível do cartão.

---

## 🧮 Conceitos financeiros

O sistema diferencia a capacidade financeira pessoal do limite de crédito disponibilizado pelo banco.

| Conceito                               | Significado                                                                                           |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Saldo disponível**                   | Valor disponível considerando o planejamento financeiro do ciclo atual.                               |
| **Fatura do próximo mês**              | Valor já comprometido em compras que serão cobradas na próxima fatura.                                |
| **Pode comprometer na próxima fatura** | Valor que ainda pode ser acrescentado à próxima fatura considerando a capacidade financeira prevista. |
| **Limite total**                       | Limite de crédito disponibilizado pelo banco.                                                         |
| **Limite disponível**                  | Crédito que ainda está disponível para utilização no cartão.                                          |

A capacidade de comprometimento considera a relação entre renda, reserva, compromissos e valores já comprometidos.

De forma simplificada:

```text
Renda prevista
- Reserva
- Compromissos
- Fatura já comprometida
= Capacidade de comprometimento restante
```

Compras realizadas no cartão não são descontadas imediatamente do saldo financeiro. Elas são consideradas como compromissos futuros por meio da fatura correspondente.

---

# 📁 Estrutura do projeto

```text
MeuControle_Financeiro/
│
├── main.py
├── main_cli.py
├── testes.py
├── README.md
├── .gitignore
├── MeuControleFinanceiro.ico
├── MeuControleFinanceiro.spec
│
├── ControleFinanceiro_2026_Exemplo.xlsx
│
├── backend/
│   ├── __init__.py
│   ├── calculos.py
│   ├── consultas.py
│   ├── excel_manager.py
│   └── utils.py
│
├── gui/
│   ├── app.py
│   ├── categorias.py
│   ├── compromissos.py
│   ├── configuracoes.py
│   ├── dashboard.py
│   ├── menu.py
│   ├── movimentacoes.py
│   ├── resumo.py
│   └── tema.py
│
└── docs/
    ├── ALERTAS.md
    ├── BACKLOG_v0.8.5.md
    ├── BACKLOG_v0.9.md
    ├── CATEGORIAS.md
    ├── DASHBOARD.md
    ├── HOMOLOGACAO_v0.8.md
    ├── UX.md
    └── WIREFRAMES.md
```

---

# 🧩 Organização do código

### `main.py`

Ponto de entrada principal da aplicação gráfica.

### `main_cli.py`

Ponto de entrada da versão de linha de comando utilizada durante etapas anteriores do desenvolvimento.

### `gui/`

Contém a interface gráfica desenvolvida com CustomTkinter.

Cada tela principal da aplicação possui seu próprio módulo.

### `backend/calculos.py`

Concentra as principais regras de negócio e cálculos financeiros.

### `backend/consultas.py`

Responsável por consultas e filtros relacionados aos dados financeiros.

### `backend/excel_manager.py`

Responsável pela comunicação com a planilha Excel, incluindo:

* Leitura;
* Gravação;
* Atualização;
* Ordenação;
* Cadastro;
* Alteração;
* Exclusão;
* Controle das faturas.

### `backend/utils.py`

Contém funções auxiliares, principalmente relacionadas à validação e formatação de dados.

### `gui/tema.py`

Centraliza configurações relacionadas ao tema e aparência da interface.

---

# 📊 Estrutura da planilha

A aplicação utiliza um arquivo Excel como camada de persistência.

| Aba                   | Finalidade                                        |
| --------------------- | ------------------------------------------------- |
| `Configuracoes`       | Armazena os parâmetros financeiros do sistema.    |
| `Movimentacoes`       | Registra receitas, despesas e compras parceladas. |
| `CompromissosMensais` | Armazena compromissos financeiros recorrentes.    |
| `Categorias`          | Armazena categorias e seu status.                 |
| `Faturas`             | Exibe o resumo das faturas do cartão.             |

A antiga aba `Dashboard` da planilha não é utilizada para a visualização principal.

O Dashboard atual é calculado dinamicamente pelo backend e apresentado pela interface gráfica.

---

## 📋 Aba `Movimentacoes`

Cada movimentação possui informações como:

* Data;
* Natureza;
* Meio de pagamento;
* Categoria;
* Descrição;
* Valor;
* Parcelas.

---

# 🗂️ Dados pessoais

O arquivo:

```text
ControleFinanceiro_2026.xlsx
```

contém os dados financeiros pessoais do usuário e **não é enviado ao GitHub**.

O repositório disponibiliza apenas:

```text
ControleFinanceiro_2026_Exemplo.xlsx
```

como modelo inicial.

Para utilizar o sistema:

1. Faça uma cópia de `ControleFinanceiro_2026_Exemplo.xlsx`;
2. Renomeie a cópia para `ControleFinanceiro_2026.xlsx`;
3. Mantenha o arquivo na raiz do projeto;
4. Cadastre seus próprios dados;
5. Execute a aplicação.

O arquivo pessoal é ignorado pelo Git por meio do `.gitignore`.

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

## 3. Instalar as dependências

```bash
pip install openpyxl customtkinter
```

## 4. Preparar a planilha

Copie:

```text
ControleFinanceiro_2026_Exemplo.xlsx
```

para:

```text
ControleFinanceiro_2026.xlsx
```

## 5. Executar

```bash
python main.py
```

---

# 🪟 Executável Windows

A versão v1.0 também possui uma versão compilada para Windows utilizando PyInstaller.

O projeto utiliza:

```text
MeuControleFinanceiro.spec
```

para configurar a geração do executável.

O executável possui ícone próprio:

```text
MeuControleFinanceiro.ico
```

A distribuição compilada é gerada na pasta:

```text
dist/MeuControleFinanceiro/
```

A planilha utilizada pela aplicação deve acompanhar o executável quando a versão compilada for utilizada.

---

# 🏗️ Arquitetura

```text
┌─────────────────────────────────┐
│        Interface Gráfica        │
│         CustomTkinter           │
│              POO                │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│             Backend             │
│                                 │
│  cálculos | consultas | utils   │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│        excel_manager.py         │
│                                 │
│   Leitura / gravação / Excel    │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│       ControleFinanceiro        │
│             .xlsx               │
└─────────────────────────────────┘
```

A separação entre GUI, regras de negócio e persistência permite que cada parte do sistema tenha uma responsabilidade mais definida.

A interface é responsável pela interação com o usuário, o backend concentra as regras financeiras e o `excel_manager.py` realiza a comunicação com o Excel.

---

# 🧪 Testes

O projeto possui o arquivo:

```text
testes.py
```

utilizado durante o desenvolvimento para apoiar a validação das regras e comportamentos do sistema.

Além dos testes, a aplicação passou por etapas de homologação e validação durante a evolução das versões.

---

# 🛣️ Roadmap

| Versão   | Status          | Objetivo                                                     |
| -------- | --------------- | ------------------------------------------------------------ |
| v0.1     | ✅ Concluída     | Controle inicial do cartão                                   |
| v0.2     | ✅ Concluída     | Melhorias de usabilidade                                     |
| v0.3     | ✅ Concluída     | Planejamento financeiro                                      |
| v0.4     | ✅ Concluída     | Novos meios de pagamento                                     |
| v0.5     | ✅ Concluída     | Histórico de movimentações                                   |
| v0.6     | ✅ Concluída     | Integração com Excel                                         |
| v0.6.5   | ✅ Concluída     | Consolidação do Excel                                        |
| v0.7     | ✅ Concluída     | Consolidação da migração para Excel                          |
| v0.8     | ✅ Concluída     | Controle completo das faturas                                |
| v0.8.5   | ✅ Concluída     | Estabilização e homologação                                  |
| v0.9     | ✅ Concluída     | Planejamento e arquitetura da GUI                            |
| v0.9.5   | ✅ Concluída     | Primeira base funcional da GUI                               |
| **v1.0** | **✅ Concluída** | **Primeira versão completa para uso diário**                 |
| v1.5     | 🔮 Planejada    | Melhorias de experiência e novas funcionalidades             |
| v2.0     | 🔮 Futuro       | Possíveis mudanças arquiteturais e evolução do armazenamento |

---

# 📜 Histórico de versões

## v0.1 — Controle de cartão

* Controle de gastos à vista;
* Controle de parcelamentos;
* Fechamento de fatura.

## v0.2 — Usabilidade

* Validação de entradas;
* Formatação monetária;
* Organização em módulos.

## v0.3 — Planejamento financeiro

* Receita mensal;
* Gastos fixos;
* Percentual de reserva;
* Saldo disponível.

## v0.4 — Novos meios de pagamento

* PIX;
* Débito;
* Dinheiro.

## v0.5 — Histórico de movimentações

* Registro de movimentações;
* Registro automático das datas;
* Consulta de histórico.

## v0.6 — Integração com Excel

* Estrutura inicial da planilha;
* Leitura e gravação em Excel;
* Criação do `excel_manager.py`.

## v0.6.5 — Consolidação do Excel

* Movimentações em Excel;
* Receitas em Excel;
* Compromissos mensais em Excel;
* Refatoração do menu principal;
* Padronização de natureza e meio;
* Refatoração dos módulos principais;
* Simplificação da estrutura do projeto.

## v0.7 — Consolidação da migração para Excel

* Cadastro unificado de movimentações;
* Parcelamentos registrados diretamente na planilha;
* Ordenação automática por data;
* Exclusão de movimentações;
* Melhorias na validação de entradas;
* Estrutura preparada para controle de faturas.

## v0.8 — Controle completo das faturas

* Controle completo das faturas;
* Controle do limite do cartão;
* Criação da aba `Faturas`;
* Melhorias na integração com Excel.

## v0.8.5 — Estabilização e homologação

* Atualização automática da aba `Faturas`;
* Exclusão inteligente de compras parceladas;
* Correções encontradas durante a homologação;
* Remoção definitiva da estrutura legada baseada em JSON.

## v0.9 — Planejamento e arquitetura da GUI

* Definição da stack tecnológica com CustomTkinter;
* Criação dos documentos de UX e wireframes;
* Definição da arquitetura POO para a interface;
* Implementação da estrutura base da aplicação;
* Migração do Dashboard da planilha para visualização em tempo real na interface;
* Consolidação do backend como suporte para a GUI.

## v0.9.5 — Primeira base funcional da GUI

* Dashboard;
* Resumo financeiro;
* Movimentações;
* Categorias;
* Compromissos;
* Configurações;
* Cadastro e gestão de movimentações;
* Parcelamentos;
* Exclusão inteligente;
* Antecipação de parcelas;
* Cadastro e controle de categorias;
* Cadastro, alteração e exclusão de compromissos;
* Configurações financeiras acessíveis pela GUI;
* Planejamento financeiro integrado ao Dashboard e ao resumo.

## v1.0 — Primeira versão completa

* Consolidação da interface gráfica;
* Organização final dos módulos principais;
* Integração entre GUI e backend;
* Controle de movimentações;
* Controle de categorias;
* Controle de compromissos;
* Controle de faturas;
* Planejamento financeiro;
* Configurações financeiras;
* Controle de compras parceladas;
* Antecipação de parcelas;
* Abatimentos de fatura;
* Geração do executável Windows;
* Ícone próprio da aplicação;
* Documentação final da versão.

---

# 🔮 Próximos passos

A v1.0 encerra o primeiro ciclo de desenvolvimento do projeto.

As próximas versões poderão explorar melhorias como:

* Pesquisa e filtros;
* Edição mais completa de movimentações;
* Melhorias na experiência de uso;
* Relatórios;
* Gráficos;
* Exportação de dados;
* Melhorias de organização interna;
* Evolução da persistência dos dados;
* Outras melhorias identificadas durante o uso diário.

Essas funcionalidades fazem parte de uma evolução futura e não são necessárias para considerar a v1.0 completa.

---

# 🛠️ Tecnologias

* Python;
* CustomTkinter;
* OpenPyXL;
* Microsoft Excel;
* Git;
* GitHub;
* PyInstaller.

---

# 📚 Finalidade do projeto

O **Meu Controle Financeiro** foi criado como um projeto pessoal de estudo e desenvolvimento.

Além de seu objetivo financeiro, o projeto serviu como laboratório prático para aprender e aplicar:

* Python;
* Programação Orientada a Objetos;
* Separação de responsabilidades;
* Organização de projetos;
* Arquitetura de software;
* Git e GitHub;
* Desenvolvimento de interfaces gráficas;
* Manipulação de arquivos Excel;
* Testes e homologação;
* Refatoração;
* Boas práticas de programação;
* Desenvolvimento incremental.

A evolução do projeto ocorreu de forma progressiva, começando como uma aplicação simples de controle de cartão e chegando a uma aplicação gráfica integrada na versão 1.0.

---

# 🤖 Uso de Inteligência Artificial

O desenvolvimento do projeto contou com apoio de Inteligência Artificial como ferramenta de estudo e desenvolvimento.

A IA foi utilizada para auxiliar em atividades como:

* Revisão de código;
* Discussão de arquitetura;
* Explicação de conceitos;
* Planejamento;
* Identificação de problemas;
* Sugestões de melhoria;
* Testes;
* Documentação;
* Aprendizado.

A implementação, decisões de projeto, testes e validação foram realizados ao longo do processo de desenvolvimento.

---

## 📌 Versão

**Meu Controle Financeiro — v1.0**

Primeira versão completa do sistema para uso diário.
