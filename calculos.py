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

    receitaTotal = somarReceitas()

    percentualReserva = configuracoes["percentualReserva"]

    return receitaTotal * (percentualReserva / 100)


# ==========================
# MOVIMENTAÇÕES
# ==========================

def calcularGastosMovimentacoes():

    movimentacoes = lerMovimentacoes()

    total = 0

    for mov in movimentacoes:
        
        if mov ["Natureza"] == "despesa":

          valor = mov["Valor"]

          if valor is not None:
            total += valor

    return total


# ==========================
# SALDO
# ==========================

def calcularSaldoDisponivel():

    configuracoes = lerConfiguracoes()

    receitaTotal = somarReceitas()

    valorGuardar = calcularValorGuardar()

    gastosFixos = somarCompromissosMensais()

    gastosMovimentacoes = calcularGastosMovimentacoes()

    return (
        receitaTotal
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

        "receitaTotal":
            somarReceitas(),

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