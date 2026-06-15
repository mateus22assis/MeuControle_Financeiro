
# ==========================
    # testes
# ==========================
from excel_manager import lerMovimentacoes

movimentacoes = lerMovimentacoes()

print(movimentacoes)

from excel_manager import adicionarMovimentacao
'''
adicionarMovimentacao(
    "receita",
    "salario",
    "trabalho",
    "salario junho",
    5000
)

adicionarMovimentacao(
    "despesa",
    "cartao de credito",
    "lazer",
    "netflix",
    100
)
'''
from calculos import calcularGastosMovimentacoes

print("Gastos Movimentacoes:", calcularGastosMovimentacoes())

from excel_manager import somarReceitas

print("Receitas:", somarReceitas())

from calculos import mostrarResumo

print("Resumo:", mostrarResumo())