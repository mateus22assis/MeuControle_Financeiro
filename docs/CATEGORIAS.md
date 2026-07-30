# Categorias — Especificação (v0.9)

## Objetivo

As categorias têm como objetivo organizar as movimentações financeiras, permitindo uma melhor visualização dos gastos e receitas, além de servir como base para relatórios, indicadores e gráficos do Dashboard.

Cada movimentação deverá possuir exatamente uma categoria.

---

## Regras Gerais

- Toda movimentação deve possuir uma categoria.
- Uma categoria pertence a apenas um tipo:
  - Receita
  - Despesa
- Categorias não devem ser excluídas, apenas desativadas.
- Categorias desativadas permanecem vinculadas às movimentações antigas.
- O sistema deverá impedir categorias duplicadas.

---

## Categorias padrão

### Receitas

- Salário
- Freelancer
- Investimentos
- Reembolso
- Venda
- Outras Receitas

### Despesas

- Alimentação
- Mercado
- Moradia
- Transporte
- Saúde
- Educação
- Lazer
- Pets
- Equipamentos
- Impostos
- Assinaturas
- Vestuário
- Presentes
- Outros

---

## Operações permitidas

O usuário poderá:

- cadastrar uma categoria;
- editar o nome de uma categoria;
- ativar uma categoria;
- desativar uma categoria;
- consultar categorias cadastradas.

Não será permitido excluir categorias.

---

## Estrutura prevista

Cada categoria deverá possuir os seguintes atributos:

- Nome
- Tipo (Receita ou Despesa)
- Status (Ativa ou Inativa)

Em versões futuras poderão ser adicionados:

- Cor
- Ícone
- Ordem de exibição

---

## Integração com a aplicação

As categorias serão utilizadas em:

- cadastro de movimentações;
- filtros de consultas;
- Dashboard;
- gráficos;
- indicadores financeiros;
- relatórios;
- futura integração com Power BI.

---

## Interface prevista

Na interface gráfica, a categoria deverá ser selecionada por meio de uma lista suspensa (ComboBox), exibindo apenas categorias ativas compatíveis com o tipo da movimentação.

Exemplo:

Receita

▼ Salário

Despesa

▼ Alimentação

---

## Evoluções futuras

Versões futuras poderão permitir:

- categorias favoritas;
- agrupamento de categorias;
- metas por categoria;
- limite mensal por categoria;
- análise histórica por categoria.