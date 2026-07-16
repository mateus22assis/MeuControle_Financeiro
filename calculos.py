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

    compromissos = lerCompromissosMensais()

    total = 0

    for compromisso in compromissos:

        valor = compromisso["valor"]

        if valor is not None:
            total += float(valor)

    return total
def somarReceitas():

    movimentacoes = lerMovimentacoes()

    total = 0

    for mov in movimentacoes:

        if mov["natureza"] == "receita":

            valor = mov["valor"]

            if valor is not None:
                total += valor

    return total


def somarDespesas():

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

    configuracoes = lerConfiguracoes()

    limiteCartao = configuracoes["limiteCartao"]

    limiteComprometido = somarDespesasCredito()

    return limiteCartao - limiteComprometido


# ==========================
# RESERVA
# ==========================

def calcularValorGuardar():

    configuracoes = lerConfiguracoes()

    receitaTotal = somarReceitas()

    percentualReserva = configuracoes["percentualReserva"]

    return receitaTotal * (percentualReserva / 100)


# ==========================
# SALDO
# ==========================

def calcularSaldoDisponivel():

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
