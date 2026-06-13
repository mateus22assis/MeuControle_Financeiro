from excel_manager import (
    lerConfiguracoes,
    somarCompromissosMensais,
    somarReceitas,
    lerMovimentacoes
)

# ==========================
# RECEITAS
# ==========================

def calcularValorGuardar():

    configuracoes = lerConfiguracoes()

    receitaMensal = configuracoes["receitaMensal"]
    percentualReserva = configuracoes["percentualReserva"]

    return receitaMensal * (percentualReserva / 100)


# ==========================
# MOVIMENTAÇÕES
# ==========================

def calcularGastosMovimentacoes():

    movimentacoes = lerMovimentacoes()

    total = 0

    for mov in movimentacoes:

        valor = mov["valor"]

        if valor is not None:
            total += valor

    return total


# ==========================
# SALDO
# ==========================

def calcularSaldoDisponivel():

    configuracoes = lerConfiguracoes()

    receitaMensal = configuracoes["receitaMensal"]

    valorGuardar = calcularValorGuardar()

    gastosFixos = somarCompromissosMensais()

    gastosMovimentacoes = calcularGastosMovimentacoes()

    return (
        receitaMensal
        - valorGuardar
        - gastosFixos
        - gastosMovimentacoes
    )


# ==========================
# RESUMO
# ==========================

def mostrarResumo():

    configuracoes = lerConfiguracoes()

    return {

        "receitaMensal":
            configuracoes["receitaMensal"],

        "gastosFixos":
            somarCompromissosMensais(),

        "valorGuardar":
            calcularValorGuardar(),

        "gastosMovimentacoes":
            calcularGastosMovimentacoes(),

        "saldoDisponivel":
            calcularSaldoDisponivel()
    }

if __name__ == "__main__":
    print(mostrarResumo())