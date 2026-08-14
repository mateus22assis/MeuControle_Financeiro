from backend.excel_manager import converterData, lerCategorias, lerMovimentacoes


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

def listarCategoriasAtivasPorNatureza(natureza):
    """
    Lista as categorias ativas da natureza informada.

    A comparação ignora maiúsculas e minúsculas para manter
    compatibilidade com os valores já gravados na planilha.
    """
    natureza_normalizada = str(natureza).strip().lower()

    return [
        categoria
        for categoria in lerCategorias()
        if categoria["ativa"]
        and str(categoria["natureza"]).strip().lower()
        == natureza_normalizada
    ]

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

def _filtrarMovimentacoesPorMeses(meses):
    """Filtra movimentações pelos pares (mês, ano) informados."""
    resultado = []

    for movimentacao in lerMovimentacoes():
        data = movimentacao["data"]

        if data is None:
            continue

        data = converterData(data)

        if (data.month, data.year) in meses:
            resultado.append(movimentacao)

    return resultado

def movimentacoesMes(mes, ano):
    """
    Filtra as movimentações de um mês e ano específicos.

    Ignora registros que não possuem data informada.

    Retorna a lista de movimentações do período.
    """

    return _filtrarMovimentacoesPorMeses({(mes, ano)})


def movimentacoesPeriodoPrincipal(mes, ano):
    """
    Lista movimentações do mês anterior, atual e seguinte.

    Trata a virada de ano sem alterar os registros futuros da planilha.
    """
    meses = set()

    for deslocamento in (-1, 0, 1):
        mes_periodo = mes + deslocamento
        ano_periodo = ano

        if mes_periodo == 0:
            mes_periodo = 12
            ano_periodo -= 1
        elif mes_periodo == 13:
            mes_periodo = 1
            ano_periodo += 1

        meses.add((mes_periodo, ano_periodo))

    return _filtrarMovimentacoesPorMeses(meses)


def mesesComMovimentacoes():
    """Retorna os meses com registros, do mais recente para o mais antigo."""
    meses = set()

    for movimentacao in lerMovimentacoes():
        data = movimentacao["data"]

        if data is not None:
            data = converterData(data)
            meses.add((data.month, data.year))

    return sorted(meses, key=lambda periodo: (periodo[1], periodo[0]), reverse=True)


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
