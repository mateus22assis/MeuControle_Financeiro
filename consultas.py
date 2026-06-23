from datetime import datetime

from excel_manager import lerMovimentacoes


# ==========================
# CONSULTAS POR NATUREZA
# ==========================

def listarReceitas():

    movimentacoes = lerMovimentacoes()

    receitas = []

    for mov in movimentacoes:

        if mov["natureza"] == "receita":

            receitas.append(mov)

    return receitas


def listarDespesas():

    movimentacoes = lerMovimentacoes()

    despesas = []

    for mov in movimentacoes:

        if mov["natureza"] == "despesa":

            despesas.append(mov)

    return despesas


# ==========================
# FILTROS
# ==========================

def filtrarCategoria(categoria):

    movimentacoes = lerMovimentacoes()

    resultado = []

    categoria = categoria.lower()

    for mov in movimentacoes:

        if (
            mov["categoria"] is not None
            and mov["categoria"].lower() == categoria
        ):

            resultado.append(mov)

    return resultado


def filtrarMeio(meio):

    movimentacoes = lerMovimentacoes()

    resultado = []

    meio = meio.lower()

    for mov in movimentacoes:

        if (
            mov["meio"] is not None
            and mov["meio"].lower() == meio
        ):

            resultado.append(mov)

    return resultado


# ==========================
# CONSULTAS POR DATA
# ==========================

def movimentacoesMes(mes, ano):

    movimentacoes = lerMovimentacoes()

    resultado = []

    for mov in movimentacoes:

        data = mov["data"]

        if data is None:
            continue

        data = datetime.strptime(
            str(data),
            "%d/%m/%Y"
        )

        if (
            data.month == mes
            and data.year == ano
        ):

            resultado.append(mov)

    return resultado


# ==========================
# ÚLTIMAS MOVIMENTAÇÕES
# ==========================

def ultimasMovimentacoes(
    quantidade=10
):

    movimentacoes = lerMovimentacoes()

    return movimentacoes[-quantidade:][::-1]


# ==========================
# TOTAIS
# ==========================

def totalReceitas():

    total = 0

    receitas = listarReceitas()

    for mov in receitas:

        valor = mov["valor"]

        if valor is not None:

            total += valor

    return total


def totalDespesas():

    total = 0

    despesas = listarDespesas()

    for mov in despesas:

        valor = mov["valor"]

        if valor is not None:

            total += valor

    return total