from dados import (
    carregarDados,
    salvarDados,
    adicionarGastoCartao,
    adicionarGastoParcelado,
    fecharFatura
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
    adicionarMovimentacao,
    lerCompromissosMensais,
    adicionarCompromissoMensal
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

    print("\n======== CONTROLE FINANCEIRO ========")
    print("1 - Adicionar movimentação")
    print("2 - Ver movimentações")
    print("3 - Ver resumo financeiro")
    print("4 - Compromissos mensais")
    print("5 - Cartão de crédito")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # ==========================
    # SAIR
    # ==========================

    if opcao == "0":
        print("Saindo...")
        break

    # ==========================
    # ADICIONAR MOVIMENTAÇÃO
    # ==========================

    elif opcao == "1":

        print("\n1 - Receita")
        print("2 - Despesa")

        tipo = input("Escolha: ")

        # RECEITA

        if tipo == "1":

            meio = lerTexto("Origem da receita: ")
            categoria = lerTexto("Categoria: ")
            descricao = lerTexto("Descrição: ")
            valor = lerFloat("Valor: ")

            adicionarMovimentacao(
                "receita",
                meio,
                categoria,
                descricao,
                valor
            )

            print("Receita registrada.")

        # DESPESA

        elif tipo == "2":

            print("\n1 - PIX")
            print("2 - Débito")
            print("3 - Dinheiro")
            print("4 - Cartão de crédito")

            meioEscolhido = input("Escolha: ")

            categoria = lerTexto("Categoria: ")
            descricao = lerTexto("Descrição: ")
            valor = lerFloat("Valor: ")

            # PIX

            if meioEscolhido == "1":

                adicionarMovimentacao(
                    "despesa",
                    "pix",
                    categoria,
                    descricao,
                    valor
                )

            # DÉBITO

            elif meioEscolhido == "2":

                adicionarMovimentacao(
                    "despesa",
                    "debito",
                    categoria,
                    descricao,
                    valor
                )

            # DINHEIRO

            elif meioEscolhido == "3":

                adicionarMovimentacao(
                    "despesa",
                    "dinheiro",
                    categoria,
                    descricao,
                    valor
                )

            # CARTÃO

            elif meioEscolhido == "4":

                print("\n1 - À vista")
                print("2 - Parcelado")

                tipoCartao = input("Escolha: ")

                # À vista

                if tipoCartao == "1":

                    adicionarGastoCartao(
                        dados,
                        valor
                    )

                    adicionarMovimentacao(
                        "despesa",
                        "cartao de credito",
                        categoria,
                        descricao,
                        valor
                    )

                    salvarDados(
                        CAMINHO,
                        dados
                    )

                # Parcelado

                elif tipoCartao == "2":

                    quantidadeParcelas = lerInt(
                        "Quantidade de parcelas: "
                    )

                    adicionarGastoParcelado(
                        dados,
                        descricao,
                        valor,
                        quantidadeParcelas
                    )

                    adicionarMovimentacao(
                        "despesa",
                        "cartao de credito",
                        categoria,
                        descricao,
                        valor,
                        quantidadeParcelas
                    )

                    salvarDados(
                        CAMINHO,
                        dados
                    )

            print("Movimentação registrada.")

    # ==========================
    # VER MOVIMENTAÇÕES
    # ==========================

    elif opcao == "2":

        movimentacoes = lerMovimentacoes()

        print("\n--- MOVIMENTAÇÕES ---\n")

        print(
            f"{'DATA':<12}"
            f"{'NATUREZA':<12}"
            f"{'MEIO':<20}"
            f"{'CATEGORIA':<15}"
            f"{'VALOR':>12}"
        )

        print("-" * 71)

        for mov in movimentacoes:

            data = str(mov["data"] or "")
            natureza = str(mov["natureza"] or "")
            meio = str(mov["meio"] or "")
            categoria = str(mov["categoria"] or "")
            valor = mov["valor"] or 0

            print(
                f"{data:<12}"
                f"{natureza:<12}"
                f"{meio:<20}"
                f"{categoria:<15}"
                f"{formatarReal(valor):>12}"
    )
    # ==========================
    # RESUMO FINANCEIRO
    # ==========================

    elif opcao == "3":

        resumo = mostrarResumo()

        print("\n--- RESUMO FINANCEIRO ---")

        print(
            "Receitas:",
            formatarReal(
                resumo["receitaTotal"]
            )
        )

        print(
            "Compromissos:",
            formatarReal(
                resumo["gastosFixos"]
            )
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

    # ==========================
    # COMPROMISSOS MENSAIS
    # ==========================

    elif opcao == "4":

        print("\n1 - Adicionar compromisso")
        print("2 - Ver compromissos")

        escolha = input("Escolha: ")

        if escolha == "1":

            descricao = lerTexto(
                "Descrição do compromisso: "
            )

            valor = lerFloat(
                "Valor: "
            )

            adicionarCompromissoMensal(
                descricao,
                valor
            )

            print("Compromisso adicionado.")

        elif escolha == "2":

            compromissos = lerCompromissosMensais()

            total = 0

            print("\n--- COMPROMISSOS MENSAIS ---")

            for compromisso in compromissos:

                print(
                    compromisso["descricao"],
                    "-",
                    formatarReal(
                        compromisso["valor"]
                    )
                )

                total += compromisso["valor"]

            print("-" * 30)

            print(
                "Total:",
                formatarReal(
                    total
                )
            )

    # ==========================
    # CARTÃO DE CRÉDITO
    # ==========================

    elif opcao == "5":

        print("\n1 - Ver fatura atual")
        print("2 - Fechar fatura")

        escolha = input("Escolha: ")

        if escolha == "1":

            totalFatura = dados["gastosCartao"]

            totalParcelamentos = sum(
                parcela["valorParcela"]
                for parcela in dados["parcelamentos"]
            )

            gastosAvista = totalFatura - totalParcelamentos

            print(
                "\nTotal da fatura:",
                formatarReal(
                    totalFatura
                )
            )

            print(
                "Parcelamentos:",
                formatarReal(
                    totalParcelamentos
                )
            )

            print(
                "Gastos à vista:",
                formatarReal(
                    gastosAvista
                )
            )

            print("\nParcelamentos:")

            for parcela in dados["parcelamentos"]:

                print(
                    f"{parcela['nome']} - "
                    f"{formatarReal(parcela['valorParcela'])} "
                    f"({parcela['quantidadeParcelas']} parcelas)"
                )

        elif escolha == "2":

            fecharFatura(
                dados
            )

            salvarDados(
                CAMINHO,
                dados
            )

            print("Fatura fechada.")

    else:

        print("Opção inválida.")