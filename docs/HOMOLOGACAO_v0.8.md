# Homologação da Versão v0.8

## Objetivo

Validar todas as funcionalidades implementadas na versão v0.8 utilizando cenários reais de uso, garantindo que as regras de negócio, os cálculos financeiros e a integração com a planilha Excel estejam funcionando corretamente antes da evolução do projeto.

---

## Status


**Situação atual:** ✅ Homologação concluída com sucesso.

### Resultado

Durante a homologação da versão v0.8 foram executados testes utilizando dados reais, contemplando os principais fluxos do sistema.

Até o momento não foram encontrados erros críticos nas regras de negócio ou nos cálculos financeiros.

As melhorias identificadas durante os testes serão tratadas nas próximas subversões, sem comprometer a estabilidade da v0.8.

---

## Funcionalidades validadas

- [x] Cadastro de receitas.
- [x] Cadastro de despesas via PIX.
- [x] Cadastro de despesas via débito.
- [x] Cadastro de despesas em dinheiro.
- [x] Cadastro de despesas no cartão de crédito.
- [x] Compras parceladas no cartão.
- [x] Geração automática das parcelas.
- [x] Exclusão de movimentações.
- [x] Validação de entradas do usuário.
- [x] Cálculo do resumo financeiro.
- [x] Controle do limite do cartão.
- [x] Cálculo da próxima fatura.
- [x] Geração da aba **Faturas**.
- [x] Persistência dos dados na planilha Excel.


---

## Melhorias identificadas

As seguintes melhorias foram identificadas durante a homologação da versão v0.8 e serão avaliadas para as próximas subversões do projeto:

- Atualizar automaticamente a aba **Faturas** pelo fluxo principal (`main.py`), eliminando a necessidade de executar `testes.py`.
- Implementar uma exclusão inteligente para compras parceladas, permitindo remover toda a compra quando desejado.
- Melhorar a usabilidade da exclusão de movimentações na interface em modo texto (CLI).
- Desenvolver a aba **Dashboard** com preenchimento automático.
- Preparar a futura interface de lançamentos, que substituirá a interação atual via terminal.

---

## Conclusão

A versão **v0.8** atingiu o objetivo de consolidar a base financeira do projeto.

As principais regras de negócio foram validadas com cenários reais, incluindo movimentações, parcelamentos, controle de cartão de crédito, cálculo de faturas e integração com a planilha Excel.

Os ajustes identificados durante a homologação são melhorias de usabilidade e evolução do sistema, não comprometendo a estabilidade da versão.

A partir desta versão, o projeto passa a evoluir sobre uma base funcional e homologada, permitindo que as próximas subversões sejam focadas em novas funcionalidades, refatorações e melhorias de experiência do usuário.
