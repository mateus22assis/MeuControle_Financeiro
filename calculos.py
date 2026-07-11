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
    }