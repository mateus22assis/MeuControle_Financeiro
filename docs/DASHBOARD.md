# Dashboard — Especificação (v0.9)

## Objetivo

O Dashboard será a tela principal do Controle Financeiro Pessoal.

Seu objetivo é apresentar, de forma simples, clara e objetiva, a situação financeira atual do usuário, permitindo uma rápida compreensão do seu cenário financeiro antes da realização de novos gastos.

Diferentemente de uma tela de consultas ou de relatórios completos, o Dashboard deve destacar apenas as informações mais relevantes para a tomada de decisão diária.

O principal indicador será **"Você ainda pode gastar"**, calculado a partir das receitas, compromissos mensais, reserva financeira, despesas e compras realizadas no cartão de crédito.

Além desse indicador, o Dashboard apresentará informações complementares que auxiliem no planejamento financeiro, como resumo financeiro, situação do cartão de crédito, distribuição dos gastos por categoria, evolução mensal, últimas movimentações e alertas.

O Dashboard será também o ponto inicial de navegação da aplicação, permitindo acesso às demais funcionalidades do sistema.

---

## Princípios

O Dashboard deverá seguir os seguintes princípios durante todo o desenvolvimento:

- Exibir apenas informações relevantes para tomada de decisão.
- Priorizar clareza e simplicidade visual.
- Destacar indicadores mais importantes antes dos indicadores secundários.
- Não substituir telas de consulta detalhada.
- Utilizar informações já existentes no sistema, sem duplicação de regras de negócio.

---

## Regra de Ouro

Toda informação exibida no Dashboard deve responder à seguinte pergunta:

> **"Esta informação me ajuda a decidir se posso gastar dinheiro neste momento?"**

Caso a resposta seja negativa, essa informação deverá ser apresentada em outra tela da aplicação, e não no Dashboard.

## Hierarquia das informações

### Nível 1 – Indicador principal

- Você ainda pode gastar

### Nível 2 – Resumo financeiro

- Receitas
- Compromissos
- Movimentações
- Reserva financeira
- Saldo disponível

### Nível 3 – Cartão de crédito

- Limite total
- Limite utilizado
- Limite disponível
- Próxima fatura

### Nível 4 – Análises

- Gastos por categoria
- Evolução mensal

### Nível 5 – Informações auxiliares

- Últimas movimentações
- Alertas

## Indicadores

### 💰 Você ainda pode gastar

Indicador principal do sistema.

Representa o valor máximo que o usuário pode gastar no mês considerando:

- receitas;
- reserva financeira;
- compromissos mensais;
- despesas já registradas;
- compras realizadas no cartão de crédito.

Este indicador deve possuir o maior destaque visual do Dashboard.

---

### 📈 Receitas

Total das receitas registradas para o período.

---

### 📉 Compromissos

Total dos compromissos mensais cadastrados.

---

### 💸 Movimentações

Total das despesas registradas no período.

---

### 🏦 Reserva Financeira

Valor destinado automaticamente à reserva financeira.

---

### 💵 Saldo Disponível

Valor restante após considerar receitas, reserva, compromissos e movimentações.

---

### 💳 Limite Total

Limite cadastrado para o cartão de crédito.

---

### 💳 Limite Utilizado

Total comprometido em compras no cartão.

---

### 💳 Limite Disponível

Limite restante para novas compras.

---

### 🧾 Próxima Fatura

Valor previsto da próxima fatura do cartão.