# ==========================
# TESTES
# ==========================
'''
from backend.excel_manager import abrirPlanilha

workbook = abrirPlanilha()

print("Abas encontradas:")

for aba in workbook.sheetnames:
    print("-", aba)


from backend.excel_manager import lerConfiguracoes

config = lerConfiguracoes()

print(config)


from excel_manager import adicionarMeses

print(adicionarMeses("15/07/2026", 1))
print(adicionarMeses("31/01/2026", 1))


from calculos import calcularProximaFatura

print("Próxima fatura:", calcularProximaFatura())


from calculos import gerarResumoFaturas

print("\n--- FATURAS ---")

for fatura in gerarResumoFaturas():
    print(fatura)


from excel_manager import atualizarPlanilha

atualizarPlanilha()

print(
    "Faturas foram atualizadas na planilha."
)


from backend.excel_manager import alterarStatusCategoria, lerCategorias
from backend.excel_manager import adicionarCategoria

adicionarCategoria(
    "Teste",
    "Despesa"
)

print(lerCategorias())

alterarStatusCategoria(
    "Investimentos",
    "Despesa",
    True
)


from backend.excel_manager import (
    alterarCompromissoMensal,
    excluirCompromissoMensal,
)

alterarCompromissoMensal(
    2,
    "Teste alterado",
    150.00
)
'
from backend.excel_manager import excluirCompromissoMensal


excluirCompromissoMensal(2)


'''