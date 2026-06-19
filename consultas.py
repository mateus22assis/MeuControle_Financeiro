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

    for mov in movimentacoes:

        if mov["categoria"].lower() == categoria.lower():

            resultado.append(mov)

    return resultado


def filtrarMeio(meio):

    movimentacoes = lerMovimentacoes()

    resultado = []

    for mov in movimentacoes:

        if mov["meio"].lower() == meio.lower():

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

        data = datetime.strptime(str(data), "%d/%m/%Y")

        if data.month == mes and data.year == ano:

            resultado.append(mov)

    return resultado


# ==========================
# ÚLTIMAS MOVIMENTAÇÕES
# ==========================

def ultimasMovimentacoes(quantidade=10):

    movimentacoes = lerMovimentacoes()

    return movimentacoes[-quantidade:]