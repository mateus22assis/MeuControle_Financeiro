from datetime import datetime

from backend.excel_manager import (
    lerConfiguracoes,
    lerMovimentacoes,
    lerCompromissosMensais,
    lerAbatimentosFaturas,
    converterData,
    determinarMesFatura,
)


MES = 8
ANO = 2026


def dinheiro(valor):
    return f"R$ {float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def mostrar_movimentacoes(titulo, movimentacoes):
    print()
    print("=" * 80)
    print(titulo)
    print("=" * 80)

    total = 0.0

    for mov in movimentacoes:
        valor = float(mov["valor"] or 0)

        print(
            f'Linha {mov["linha"]:>3} | '
            f'{converterData(mov["data"]).strftime("%d/%m/%Y")} | '
            f'{str(mov["natureza"]):<8} | '
            f'{str(mov["meio"]):<10} | '
            f'{str(mov["categoria"]):<25} | '
            f'{dinheiro(valor):>12} | '
            f'{mov["descricao"]}'
        )

        total += valor

    print("-" * 80)
    print(f"TOTAL: {dinheiro(total)}")

    return total


print()
print("=" * 80)
print("              DIAGNÓSTICO DO SALDO")
print("              AGOSTO / 2026")
print("=" * 80)


# ============================================================
# CONFIGURAÇÕES
# ============================================================

configuracoes = lerConfiguracoes()

print()
print("CONFIGURAÇÕES")
print("-" * 80)

for chave, valor in configuracoes.items():
    print(f"{chave:<25}: {valor}")


# ============================================================
# MOVIMENTAÇÕES
# ============================================================

movimentacoes = lerMovimentacoes()

movimentacoes_agosto = []

for mov in movimentacoes:
    if mov["data"] is None:
        continue

    data = converterData(mov["data"])

    if data.month == MES and data.year == ANO:
        movimentacoes_agosto.append(mov)


# ============================================================
# SEPARAÇÃO
# ============================================================

receitas = []
despesas_vista = []
despesas_credito = []

for mov in movimentacoes_agosto:

    natureza = str(mov["natureza"]).strip().lower()
    meio = str(mov["meio"]).strip().lower()

    if natureza == "receita":
        receitas.append(mov)

    elif natureza == "despesa" and meio == "credito":
        despesas_credito.append(mov)

    elif natureza == "despesa":
        despesas_vista.append(mov)


# ============================================================
# RECEITAS
# ============================================================

total_receitas = mostrar_movimentacoes(
    "RECEITAS DE AGOSTO",
    receitas
)


# ============================================================
# DESPESAS À VISTA
# ============================================================

total_despesas_vista = mostrar_movimentacoes(
    "DESPESAS À VISTA DE AGOSTO",
    despesas_vista
)


# ============================================================
# CARTÃO
# ============================================================

print()
print("=" * 80)
print("COMPRAS NO CARTÃO REGISTRADAS EM AGOSTO")
print("=" * 80)

total_fatura_agosto = 0.0

for mov in despesas_credito:

    mes_fatura, ano_fatura = determinarMesFatura(
        mov["data"],
        configuracoes["diaFechamento"]
    )

    valor = float(mov["valor"] or 0)

    print(
        f'Linha {mov["linha"]:>3} | '
        f'{converterData(mov["data"]).strftime("%d/%m/%Y")} | '
        f'Fatura {mes_fatura:02d}/{ano_fatura} | '
        f'{dinheiro(valor):>12} | '
        f'{mov["descricao"]}'
    )

    if mes_fatura == MES and ano_fatura == ANO:
        total_fatura_agosto += valor

print("-" * 80)
print(f"TOTAL FATURA AGOSTO: {dinheiro(total_fatura_agosto)}")


# ============================================================
# ABATIMENTOS
# ============================================================

abatimentos = lerAbatimentosFaturas()

print()
print("=" * 80)
print("ABATIMENTOS DAS FATURAS")
print("=" * 80)

if not abatimentos:
    print("Nenhum abatimento encontrado.")
else:
    for fatura, valor in abatimentos.items():
        print(
            f"Fatura {fatura:<10} -> {dinheiro(valor)}"
        )


# ============================================================
# COMPROMISSOS
# ============================================================

compromissos = lerCompromissosMensais()

print()
print("=" * 80)
print("COMPROMISSOS MENSAIS")
print("=" * 80)

total_compromissos = 0.0

for compromisso in compromissos:
    valor = float(compromisso["valor"] or 0)

    print(
        f'Linha {compromisso["linha"]:>3} | '
        f'{compromisso["descricao"]:<50} | '
        f'{dinheiro(valor):>12}'
    )

    total_compromissos += valor

print("-" * 80)
print(f"TOTAL COMPROMISSOS: {dinheiro(total_compromissos)}")


# ============================================================
# RESERVA
# ============================================================

receitas_para_reserva = 0.0

for mov in receitas:

    categoria = str(mov["categoria"]).strip().lower()

    if categoria in ["salario", "renda extra"]:
        receitas_para_reserva += float(mov["valor"] or 0)


percentual = float(configuracoes["percentualReserva"])

valor_guardar = receitas_para_reserva * (percentual / 100)


print()
print("=" * 80)
print("RESERVA")
print("=" * 80)

print(
    f"Receitas para reserva : {dinheiro(receitas_para_reserva)}"
)

print(
    f"Percentual             : {percentual:.2f}%"
)

print(
    f"Valor a guardar        : {dinheiro(valor_guardar)}"
)


# ============================================================
# RESUMO MATEMÁTICO
# ============================================================

saldo_atual = (
    total_receitas
    - valor_guardar
    - total_compromissos
    - total_fatura_agosto
    - total_despesas_vista
)


print()
print("=" * 80)
print("RECONSTRUÇÃO DO SALDO DE AGOSTO")
print("=" * 80)

print(f"Receitas                 + {dinheiro(total_receitas)}")
print(f"Valor a guardar          - {dinheiro(valor_guardar)}")
print(f"Compromissos             - {dinheiro(total_compromissos)}")
print(f"Fatura agosto            - {dinheiro(total_fatura_agosto)}")
print(f"Despesas à vista         - {dinheiro(total_despesas_vista)}")
print("-" * 80)
print(f"SALDO CALCULADO          = {dinheiro(saldo_atual)}")


# ============================================================
# COMPARAÇÃO
# ============================================================

saldo_esperado = 128.89

diferenca = saldo_atual - saldo_esperado

print()
print("=" * 80)
print("COMPARAÇÃO")
print("=" * 80)

print(f"Saldo calculado          : {dinheiro(saldo_atual)}")
print(f"Saldo esperado           : {dinheiro(saldo_esperado)}")
print(f"Diferença                : {dinheiro(diferenca)}")


# ============================================================
# INVESTIMENTOS
# ============================================================

print()
print("=" * 80)
print("MOVIMENTAÇÕES RELACIONADAS A INVESTIMENTOS")
print("=" * 80)

palavras_investimento = [
    "investimento",
    "investir",
    "aplicação",
    "aplicacao",
    "resgate",
    "imposto",
]

total_investimentos = 0.0

for mov in movimentacoes_agosto:

    texto = (
        f'{mov["categoria"]} '
        f'{mov["descricao"]}'
    ).lower()

    if any(palavra in texto for palavra in palavras_investimento):

        valor = float(mov["valor"] or 0)

        print(
            f'Linha {mov["linha"]:>3} | '
            f'{converterData(mov["data"]).strftime("%d/%m/%Y")} | '
            f'{mov["natureza"]:<8} | '
            f'{mov["meio"]:<10} | '
            f'{dinheiro(valor):>12} | '
            f'{mov["descricao"]}'
        )

        total_investimentos += valor

print("-" * 80)
print(
    f"TOTAL BRUTO DESSAS MOVIMENTAÇÕES: "
    f"{dinheiro(total_investimentos)}"
)


print()
print("=" * 80)
print("FIM DO DIAGNÓSTICO")
print("=" * 80)


print()
print("=" * 80)
print("FATURA QUE VENCEU EM AGOSTO / 2026")
print("=" * 80)

total_fatura_vencimento_agosto = 0.0

for mov in movimentacoes:

    if mov["data"] is None:
        continue

    natureza = str(mov["natureza"]).strip().lower()
    meio = str(mov["meio"]).strip().lower()

    if natureza != "despesa" or meio != "credito":
        continue

    mes_fatura, ano_fatura = determinarMesFatura(
        mov["data"],
        configuracoes["diaFechamento"]
    )

    if mes_fatura == 8 and ano_fatura == 2026:

        valor = float(mov["valor"] or 0)

        print(
            f'Linha {mov["linha"]:>3} | '
            f'{converterData(mov["data"]).strftime("%d/%m/%Y")} | '
            f'{dinheiro(valor):>12} | '
            f'{mov["categoria"]} | '
            f'{mov["descricao"]}'
        )

        total_fatura_vencimento_agosto += valor

print("-" * 80)

print(
    f"TOTAL FATURA 08/2026: "
    f"{dinheiro(total_fatura_vencimento_agosto)}"
)


print()
print("=" * 80)
print("MOVIMENTAÇÕES PEQUENAS / POSSÍVEL DIFERENÇA")
print("=" * 80)

for mov in movimentacoes_agosto:

    valor = float(mov["valor"] or 0)

    if valor <= 50:

        print(
            f'Linha {mov["linha"]:>3} | '
            f'{converterData(mov["data"]).strftime("%d/%m/%Y")} | '
            f'{mov["natureza"]:<8} | '
            f'{mov["meio"]:<10} | '
            f'{dinheiro(valor):>12} | '
            f'{mov["categoria"]} | '
            f'{mov["descricao"]}'
        )


        print()
print("=" * 100)
print("TODAS AS MOVIMENTAÇÕES DE AGOSTO - EFEITO NO SALDO")
print("=" * 100)

saldo_movimentacoes = 0.0

for mov in sorted(
    movimentacoes_agosto,
    key=lambda x: converterData(x["data"])
):

    natureza = str(mov["natureza"]).strip().lower()
    meio = str(mov["meio"]).strip().lower()
    valor = float(mov["valor"] or 0)

    if natureza == "receita":
        efeito = valor
        sinal = "+"

    elif natureza == "despesa" and meio != "credito":
        efeito = -valor
        sinal = "-"

    elif natureza == "despesa" and meio == "credito":
        mes_fatura, ano_fatura = determinarMesFatura(
            mov["data"],
            configuracoes["diaFechamento"]
        )

        if mes_fatura == MES and ano_fatura == ANO:
            efeito = -valor
            sinal = "-"
        else:
            efeito = 0.0
            sinal = "0"

    else:
        efeito = 0.0
        sinal = "0"

    saldo_movimentacoes += efeito

    print(
        f'Linha {mov["linha"]:>3} | '
        f'{converterData(mov["data"]).strftime("%d/%m/%Y")} | '
        f'{mov["natureza"]:<8} | '
        f'{mov["meio"]:<10} | '
        f'{mov["categoria"]:<25} | '
        f'{mov["descricao"]:<45} | '
        f'{sinal} {dinheiro(abs(efeito)):>12} | '
        f'Acumulado: {dinheiro(saldo_movimentacoes)}'
    )

print("-" * 100)
print(
    f"Efeito líquido das movimentações: "
    f"{dinheiro(saldo_movimentacoes)}"
)

print()
print("=" * 100)
print("TESTE DA DIFERENÇA DE R$ 16,81")
print("=" * 100)

print("Saldo encontrado pelo cálculo atual: R$ 445,70")
print("Menos abatimento pago em agosto:      R$ 300,00")
print("Resultado:                            R$ 145,70")
print("Saldo real informado:                R$ 128,89")
print("Diferença restante:                   R$ 16,81")
