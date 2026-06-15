from dados import (
    adicionarGastoDebito,
    adicionarGastoPix,
    adicionarGastoDinheiro,
    adicionarParcelamento,
    carregarDados,
    salvarDados,
    adicionarGastoCartao,
    adicionarGastoParcelado,
    fecharFatura,
    definirReceitaMensal,
    definirGastosFixos,
    definirPercentualReserva
)

from calculos import mostrarResumo

from utils import (
    lerFloat,
    lerInt,
    formatarReal,
    lerTexto
)

from excel_manager import (
    lerMovimentacoes,
    adicionarMovimentacao
)





# ==========================
# DADOS LEGADOS (JSON)
# ==========================

CAMINHO = "data.json"

dados = carregarDados(CAMINHO)

# ==========================
# MENU PRINCIPAL
# ==========================

while True:

    print("\n--- Menu ---")
    print("1 - Adicionar parcelamento existente")
    print("2 - Adicionar gasto no cartão de crédito à vista")
    print("3 - Adicionar gasto parcelado no cartão")
    print("4 - Adicionar gasto no PIX")
    print("5 - Adicionar gasto no débito")
    print("6 - Adicionar gasto no dinheiro")
    print("7 - Ver dados atuais")
    print("8 - Fechar fatura")
    print("9 - Definir receita mensal")
    print("10 - Definir gastos fixos")
    print("11 - Definir percentual de reserva")
    print("12 - Ver resumo financeiro")
    print("13 - Ver movimentações")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # ==========================
    # SAIR
    # ==========================

    if opcao == "0":
        print("Saindo...")
        break

    # ==========================
    # PARCELAMENTOS (JSON)
    # ==========================

    elif opcao == "1":

        nome = lerTexto("Digite o nome do parcelamento existente: ")
        valorParcela = lerFloat("Digite o valor da parcela: ")
        quantidadeParcelas = lerInt(
            "Digite a quantidade de parcelas restantes: "
        )

        adicionarParcelamento(
            dados,
            nome,
            valorParcela,
            quantidadeParcelas
        )

        salvarDados(CAMINHO, dados)

    elif opcao == "2":

        descricao = lerTexto(
            "Digite a descrição do gasto no cartão: "
        )

        valor = lerFloat(
            "Digite o valor do gasto no cartão: "
        )

        adicionarGastoCartao(dados, valor)

        salvarDados(CAMINHO, dados)

        print("Gasto adicionado ao cartão.")

    elif opcao == "3":

        nome = lerTexto(
            "Digite o nome da nova compra parcelada: "
        )

        valorTotal = lerFloat(
            "Digite o valor total do gasto: "
        )

        quantidadeParcelas = lerInt(
            "Digite a quantidade de parcelas: "
        )

        adicionarGastoParcelado(
            dados,
            nome,
            valorTotal,
            quantidadeParcelas
        )

        salvarDados(CAMINHO, dados)

        print("Compra parcelada adicionada com sucesso.")

    # ==========================
    # MOVIMENTAÇÕES (EXCEL)
    # ==========================

    elif opcao == "4":

        categoria = lerTexto("Categoria: ")
        descricao = lerTexto("Descrição: ")
        valor = lerFloat("Valor: ")

        adicionarMovimentacao(
            "pix",
            categoria,
            descricao,
            valor
        )

        print("Movimentação registrada.")

    elif opcao == "5":

        categoria = lerTexto("Categoria: ")
        descricao = lerTexto("Descrição: ")
        valor = lerFloat("Valor: ")

        adicionarMovimentacao(
            "debito",
            categoria,
            descricao,
            valor
        )

        print("Movimentação registrada.")

    elif opcao == "6":

        categoria = lerTexto("Categoria: ")
        descricao = lerTexto("Descrição: ")
        valor = lerFloat("Valor: ")

        adicionarMovimentacao(
            "dinheiro",
            categoria,
            descricao,
            valor
        )

        print("Movimentação registrada.")

    # ==========================
    # CONSULTAS
    # ==========================

    elif opcao == "7":

        print("\n--- Dados Atuais ---")

        totalFatura = dados["gastosCartao"]

        totalParcelamentos = sum(
            parcelamento["valorParcela"]
            for parcelamento in dados["parcelamentos"]
        )

        gastosAvista = (
            totalFatura - totalParcelamentos
        )

        print(
            "Total da fatura:",
            formatarReal(totalFatura)
        )

        print(
            "Total de parcelamentos:",
            formatarReal(totalParcelamentos)
        )

        print(
            "Gastos à vista:",
            formatarReal(gastosAvista)
        )

        print("Parcelamentos:")

        for parcela in dados["parcelamentos"]:

            print(
                f"{parcela['nome']} - "
                f"Parcela: {formatarReal(parcela['valorParcela'])} "
                f"- Quantidade: {parcela['quantidadeParcelas']}"
            )

    elif opcao == "8":

        fecharFatura(dados)

        salvarDados(CAMINHO, dados)

        print(
            "Fatura fechada. "
            "Gastos do cartão processados."
        )

    # ==========================
    # CONFIGURAÇÕES (LEGADO)
    # ==========================

    elif opcao == "9":

        valor = lerFloat(
            "Digite o valor da receita mensal: "
        )

        definirReceitaMensal(dados, valor)

        salvarDados(CAMINHO, dados)

        print("Receita mensal definida.")

    elif opcao == "10":

        valor = lerFloat(
            "Digite o valor dos gastos fixos: "
        )

        definirGastosFixos(dados, valor)

        salvarDados(CAMINHO, dados)

        print("Gastos fixos definidos.")

    elif opcao == "11":

        valor = lerInt(
            "Digite o percentual para guardar (%): "
        )

        definirPercentualReserva(dados, valor)

        salvarDados(CAMINHO, dados)

        print("Percentual definido.")

    # ==========================
    # RESUMO (EXCEL)
    # ==========================

    elif opcao == "12":

        resumo = mostrarResumo()

        print("\n--- Resumo Financeiro ---")

        print(
            "Receita mensal:",
            formatarReal(resumo["receitaMensal"])
        )

        print(
            "Compromissos mensais:",
            formatarReal(resumo["gastosFixos"])
        )

        print(
            "Movimentações:",
            formatarReal(
                resumo["gastosMovimentacoes"]
            )
        )

        print(
            "Valor a guardar:",
            formatarReal(
                resumo["valorGuardar"]
            )
        )

        print(
            "Saldo disponível:",
            formatarReal(
                resumo["saldoDisponivel"]
            )
        )

    elif opcao == "13":

        movimentacoes = lerMovimentacoes()

        print("\n--- Movimentações ---")

        if len(movimentacoes) == 0:

            print(
                "Nenhuma movimentação registrada."
            )

        else:

            for mov in movimentacoes:

                print("-" * 50)

                print("Data:", mov["data"])
                print("Tipo:", mov["tipo"])
                print("Categoria:", mov["categoria"])
                print("Descrição:", mov["descricao"])
                print(
                    "Valor:",
                    formatarReal(mov["valor"])
                )

    else:

        print("Opção inválida.")

