from datetime import datetime

from calculos import mostrarResumo

from utils import (
    lerFloat,
    lerInt,
    formatarReal,
    lerTexto
)

from excel_manager import (
    adicionarMeses,
    lerMovimentacoes,
    adicionarMovimentacao,
    lerCompromissosMensais,
    adicionarCompromissoMensal,
    excluirMovimentacao,
    lerConfiguracoes
)

# ==========================
# MENU PRINCIPAL
# ==========================

while True:

    print("\n======== CONTROLE FINANCEIRO ========")
    print("1 - Adicionar movimentação")
    print("2 - Ver movimentações")
    print("3 - Ver resumo financeiro")
    print("4 - Compromissos mensais")
    print("5 - excluir movimentação")
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

        # ======================
        # RECEITA
        # ======================

        if tipo == "1":

            meio = lerTexto("Origem da receita: ")
            categoria = lerTexto("Categoria: ")
            descricao = lerTexto("Descrição: ")
            valor = lerFloat("Valor: ")

            dataMovimentacao = input(
                "Data (dd/mm/aaaa) [Enter = hoje]: "
            ).strip()

            if dataMovimentacao == "":
                dataMovimentacao = datetime.now().strftime("%d/%m/%Y")

            adicionarMovimentacao(
                "receita",
                meio,
                categoria,
                descricao,
                valor,
                "",
                dataMovimentacao
            )

            print("Receita registrada.")

        # ======================
        # DESPESA
        # ======================

        elif tipo == "2":

            print("\n1 - PIX")
            print("2 - Débito")
            print("3 - Dinheiro")
            print("4 - Cartão de crédito")

            meioEscolhido = input("Escolha: ")

            categoria = lerTexto("Categoria: ")
            descricao = lerTexto("Descrição: ")
            valor = lerFloat("Valor: ")

            dataCompra = input(
                "Data (dd/mm/aaaa) [Enter = hoje]: "
            ).strip()

            if dataCompra == "":
                dataCompra = datetime.now().strftime("%d/%m/%Y")

            # ==================
            # PIX
            # ==================

            if meioEscolhido == "1":

                adicionarMovimentacao(
                    "despesa",
                    "pix",
                    categoria,
                    descricao,
                    valor,
                    "",
                    dataCompra
                )

            # ==================
            # DÉBITO
            # ==================

            elif meioEscolhido == "2":

                adicionarMovimentacao(
                    "despesa",
                    "debito",
                    categoria,
                    descricao,
                    valor,
                    "",
                    dataCompra
                )

            # ==================
            # DINHEIRO
            # ==================

            elif meioEscolhido == "3":

                adicionarMovimentacao(
                    "despesa",
                    "dinheiro",
                    categoria,
                    descricao,
                    valor,
                    "",
                    dataCompra
                )

            # ==================
            # CARTÃO
            # ==================

            elif meioEscolhido == "4":

                quantidadeParcelas = lerInt(
                    "Quantidade de parcelas: "
                )

                if quantidadeParcelas < 1:
                    quantidadeParcelas = 1

                valorParcela = round(
                    valor / quantidadeParcelas,
                    2
                )

                for parcela in range(quantidadeParcelas):

                    dataParcela = adicionarMeses(
                        dataCompra,
                        parcela
                    )

                    adicionarMovimentacao(
                        "despesa",
                        "credito",
                        categoria,
                        f"{descricao} ({parcela + 1}/{quantidadeParcelas})",
                        valorParcela,
                        f"{parcela + 1}/{quantidadeParcelas}",
                        dataParcela
                    )

            else:
                print("Meio de pagamento inválido.")
                continue

            print("Movimentação registrada.")

    # ==========================
    # VER MOVIMENTAÇÕES
    # ==========================

    elif opcao == "2":

        movimentacoes = lerMovimentacoes()

        print("\n--- MOVIMENTAÇÕES ---\n")

        print(
            f"{'LINHA':<7}"
            f"{'DATA':<12}"
            f"{'NATUREZA':<12}"
            f"{'MEIO':<20}"
            f"{'DESCRIÇÃO':<30}"
            f"{'VALOR':>12}"
            )
        

        print("-" * 76)

        for mov in movimentacoes:

            data = str(mov["data"] or "")
            natureza = str(mov["natureza"] or "")
            meio = str(mov["meio"] or "")
            categoria = str(mov["categoria"] or "")
            descricao = str(mov["descricao"] or "")
            valor = mov["valor"] or 0

            print(
                f"{mov['linha']:<7}"
                f"{data:<12}"
                f"{natureza:<12}"
                f"{meio:<20}"
                f"{descricao:<30}"
                f"{formatarReal(valor):>12}"
            )

    # ==========================
    # RESUMO FINANCEIRO
    # ==========================

    elif opcao == "3":

        resumo = mostrarResumo()

        configuracoes = lerConfiguracoes()

        print("\n========== RESUMO FINANCEIRO ==========\n")

        print(
        "Receitas:              ",
        formatarReal(resumo["receitaTotal"])
    )

        print(
        "Compromissos:          ",
        formatarReal(resumo["gastosFixos"])
    )

        print(
            "Movimentações:         ",
            formatarReal(resumo["gastosMovimentacoes"])
        )

        print(   
            "Valor a guardar:       ",
            formatarReal(resumo["valorGuardar"])
        )  
         

        print(
            "Saldo disponível:      ",
            formatarReal(resumo["saldoDisponivel"])
        )

        print("\n========== CARTÃO ==========\n")

        print(
            "Limite total:          ",
            formatarReal(configuracoes["limiteCartao"])
        )

        print(
            "Limite comprometido:   ",
            formatarReal(resumo["limiteComprometido"])
        )

        print(
            "Limite disponível:     ",
            formatarReal(resumo["limiteDisponivel"])
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


    elif opcao == "5":

        print("\n--- EXCLUIR MOVIMENTAÇÃO ---")

        linha = lerInt(
                "Digite o número da linha da movimentação a ser excluída: "
            )
        if linha<2:
            print("Linha inválida. A linha deve ser maior ou igual a 2.")
            continue
        
        confirmacao = input(f"Tem certeza que deseja excluir a movimentação na linha {linha}? (s/n): ")

        if confirmacao == "s":

            if excluirMovimentacao(linha):
                print(f"Movimentação na linha {linha} excluída com sucesso.")
            else:
                print("Erro ao excluir movimentação.")
        else:
            print("Exclusão cancelada.")

    # ==========================
    # OPÇÃO INVÁLIDA
    # ==========================

    else:

        print("Opção inválida.")        