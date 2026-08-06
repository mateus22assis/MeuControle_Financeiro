from datetime import datetime

from backend.excel_manager import lerMovimentacoes


# ==========================
# CONSULTAS POR NATUREZA
# ==========================

def listarReceitas():
    """
    Lista as movimentações classificadas como receita.

    Consulta os dados atuais registrados na planilha.

    Retorna uma lista de receitas.
    """

    movimentacoes = lerMovimentacoes()

    receitas = []

    for mov in movimentacoes:

        if mov["natureza"] == "receita":

            receitas.append(mov)

    return receitas


def listarDespesas():
    """
    Lista as movimentações classificadas como despesa.

    Consulta os dados atuais registrados na planilha.

    Retorna uma lista de despesas.
    """

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
    """
    Filtra movimentações por uma categoria informada.

    A comparação não diferencia letras maiúsculas de minúsculas.

    Retorna a lista de movimentações encontradas.
    """

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
    """
    Filtra movimentações pelo meio de pagamento informado.

    A comparação não diferencia letras maiúsculas de minúsculas.

    Retorna a lista de movimentações encontradas.
    """

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
    """
    Filtra as movimentações de um mês e ano específicos.

    Ignora registros que não possuem data informada.

    Retorna a lista de movimentações do período.
    """

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
    """
    Seleciona as movimentações mais recentes registradas.

    Inverte a seleção para apresentar o registro mais novo primeiro.

    Retorna uma lista limitada à quantidade solicitada.
    """

    movimentacoes = lerMovimentacoes()

    return movimentacoes[-quantidade:][::-1]


# ==========================
# TOTAIS
# ==========================

def totalReceitas():
    """
    Calcula o total das receitas cadastradas.

    Ignora movimentações de receita sem valor informado.

    Retorna a soma das receitas.
    """

    total = 0

    receitas = listarReceitas()

    for mov in receitas:

        valor = mov["valor"]

        if valor is not None:

            total += valor

    return total


def totalDespesas():
    """
    Calcula o total das despesas cadastradas.

    Ignora movimentações de despesa sem valor informado.

    Retorna a soma das despesas.
    """

    total = 0

    despesas = listarDespesas()

    for mov in despesas:

        valor = mov["valor"]

        if valor is not None:

            total += valor

    return total
