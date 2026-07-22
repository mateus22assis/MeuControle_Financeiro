from calendar import monthrange
from datetime import datetime

from excel_manager import (
    lerConfiguracoes,
    lerCompromissosMensais,
    lerMovimentacoes
)

# ==========================
# SOMATÓRIOS
# ==========================

def somarCompromissosMensais():
    """
    Soma os valores dos compromissos mensais cadastrados.

    Ignora compromissos sem valor informado.

    Retorna o total dos gastos fixos mensais.
    """

    compromissos = lerCompromissosMensais()

    total = 0

    for compromisso in compromissos:

        valor = compromisso["valor"]

        if valor is not None:
            total += float(valor)

    return total


def somarReceitas():
    """
    Soma todas as movimentações classificadas como receita.

    Movimentações sem valor não entram no cálculo.

    Retorna o total de receitas registradas.
    """

    movimentacoes = lerMovimentacoes()

    total = 0

    for mov in movimentacoes:

        if mov["natureza"] == "receita":

            valor = mov["valor"]

            if valor is not None:
                total += valor

    return total


def somarDespesas():
    """
    Soma todas as movimentações classificadas como despesa.

    Movimentações sem valor não entram no cálculo.

    Retorna o total de despesas registradas.
    """

    movimentacoes = lerMovimentacoes()

    total = 0

    for mov in movimentacoes:

        if mov["natureza"] == "despesa":

            valor = mov["valor"]

            if valor is not None:
                total += valor

    return total


# ==========================
# CARTÃO DE CRÉDITO
# ==========================

def somarDespesasCredito():
    """
    Soma as despesas pagas com cartão de crédito.

    Considera somente movimentações de natureza despesa
    cujo meio de pagamento é crédito.

    Retorna o valor comprometido no cartão.
    """

    movimentacoes = lerMovimentacoes()

    total = 0

    for mov in movimentacoes:

        if (
            mov["natureza"] == "despesa"
            and mov["meio"] == "credito"
        ):

            valor = mov["valor"]

            if valor is not None:
                total += valor

    return total


def calcularProximaFatura():
    """
    Calcula o total da próxima fatura do cartão.

    Compras após o dia de fechamento são atribuídas ao mês
    seguinte, respeitando a virada de ano.

    Retorna o valor total da próxima fatura.
    """

    movimentacoes = lerMovimentacoes()

    configuracoes = lerConfiguracoes()

    hoje = datetime.today()

    diaFechamento = configuracoes["diaFechamento"]

    if hoje.day > diaFechamento:

        mesFatura = hoje.month + 1
        anoFatura = hoje.year

        if mesFatura > 12:
            mesFatura = 1
            anoFatura += 1

    else:

        mesFatura = hoje.month
        anoFatura = hoje.year

    total = 0

    for mov in movimentacoes:

        if (
            mov["natureza"] == "despesa"
            and mov["meio"] == "credito"
            and mov["data"] is not None
        ):

            dataMovimentacao = mov["data"]

            if isinstance(dataMovimentacao, datetime):
                dataMovimentacao = dataMovimentacao
            else:
                dataMovimentacao = datetime.strptime(
                    str(dataMovimentacao),
                    "%d/%m/%Y"
                )

            mesMovimentacao = dataMovimentacao.month
            anoMovimentacao = dataMovimentacao.year

            if dataMovimentacao.day > diaFechamento:
                mesMovimentacao += 1

                if mesMovimentacao > 12:
                    mesMovimentacao = 1
                    anoMovimentacao += 1

            if (
                mesMovimentacao == mesFatura
                and anoMovimentacao == anoFatura
            ):
                valor = mov["valor"]

                if valor is not None:
                    total += float(valor)

    return float(total)


def gerarResumoFaturas():
    """
    Gera o resumo das faturas de cartão por mês de referência.

    A data da compra posterior ao fechamento compõe a fatura
    seguinte; cada fatura é classificada como aberta, fechada ou prevista.

    Retorna uma lista com valores, vencimentos e status das faturas.
    """

    movimentacoes = lerMovimentacoes()

    configuracoes = lerConfiguracoes()

    diaFechamento = configuracoes["diaFechamento"]
    diaVencimento = configuracoes["diaVencimento"]

    hoje = datetime.today()

    mesFaturaAtual = hoje.month
    anoFaturaAtual = hoje.year

    if hoje.day > diaFechamento:

        mesFaturaAtual += 1

        if mesFaturaAtual > 12:
            mesFaturaAtual = 1
            anoFaturaAtual += 1

    faturas = {}

    for movimentacao in movimentacoes:

        if (
            movimentacao["meio"] != "credito"
            or movimentacao["data"] is None
            or movimentacao["valor"] is None
        ):
            continue

        dataMovimentacao = movimentacao["data"]

        if not isinstance(dataMovimentacao, datetime):
            dataMovimentacao = datetime.strptime(
                str(dataMovimentacao),
                "%d/%m/%Y"
            )

        mesFatura = dataMovimentacao.month
        anoFatura = dataMovimentacao.year

        if dataMovimentacao.day > diaFechamento:

            mesFatura += 1

            if mesFatura > 12:
                mesFatura = 1
                anoFatura += 1

        chaveFatura = (anoFatura, mesFatura)

        if chaveFatura not in faturas:
            faturas[chaveFatura] = 0.0

        faturas[chaveFatura] += float(movimentacao["valor"])

    resumoFaturas = []

    for (anoFatura, mesFatura), valor in sorted(faturas.items()):

        ultimoDiaMes = monthrange(anoFatura, mesFatura)[1]
        diaVencimentoFatura = min(diaVencimento, ultimoDiaMes)

        if (anoFatura, mesFatura) < (anoFaturaAtual, mesFaturaAtual):
            status = "Fechada"
        elif (anoFatura, mesFatura) == (anoFaturaAtual, mesFaturaAtual):
            status = "Aberta"
        else:
            status = "Prevista"

        resumoFaturas.append({
            "fatura": f"{mesFatura:02d}/{anoFatura}",
            "vencimento": (
                f"{diaVencimentoFatura:02d}/{mesFatura:02d}/{anoFatura}"
            ),
            "valor": round(valor, 2),
            "status": status
        })

    return resumoFaturas


def calcularLimiteDisponivel():
    """
    Calcula o limite disponível do cartão de crédito.

    Utiliza o limite real cadastrado e desconta as despesas
    registradas em crédito, sem considerar a renda.

    Retorna o limite ainda disponível para uso.
    """

    configuracoes = lerConfiguracoes()

    limiteCartao = configuracoes["limiteCartao"]

    limiteComprometido = somarDespesasCredito()

    return limiteCartao - limiteComprometido


# ==========================
# RESERVA
# ==========================

def calcularValorGuardar():
    """
    Calcula o valor mensal reservado para economia.

    Aplica o percentual de reserva configurado sobre o total
    de receitas registradas.

    Retorna o valor que deve ser guardado.
    """

    configuracoes = lerConfiguracoes()

    receitaTotal = somarReceitas()

    percentualReserva = configuracoes["percentualReserva"]

    return receitaTotal * (percentualReserva / 100)


# ==========================
# SALDO
# ==========================

def calcularSaldoDisponivel():
    """
    Calcula o saldo disponível no mês.

    Subtrai das receitas a reserva financeira, os compromissos
    mensais e as despesas registradas.

    Retorna o saldo disponível após os descontos.
    """

    receitaTotal = somarReceitas()

    valorGuardar = calcularValorGuardar()

    gastosFixos = somarCompromissosMensais()

    despesas = somarDespesas()

    return (
        receitaTotal
        - valorGuardar
        - gastosFixos
        - despesas
    )


# ==========================
# RESUMO
# ==========================

def mostrarResumo():
    """
    Reúne os principais indicadores financeiros do usuário.

    Inclui receitas, despesas, reserva, saldo e informações
    do limite do cartão de crédito.

    Retorna um dicionário com os valores do resumo.
    """

    return {

        "receitaTotal":
            somarReceitas(),

        "gastosFixos":
            somarCompromissosMensais(),

        "valorGuardar":
            calcularValorGuardar(),

        "gastosMovimentacoes":
            somarDespesas(),

        "saldoDisponivel":
            calcularSaldoDisponivel(),

        "limiteComprometido":
            somarDespesasCredito(),

        "limiteDisponivel":
            calcularLimiteDisponivel()

        # "proximaFatura":
        #     calcularProximaFatura()
    }
