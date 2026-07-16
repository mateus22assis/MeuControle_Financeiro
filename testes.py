# ==========================
# TESTES
# ==========================

from excel_manager import abrirPlanilha

workbook = abrirPlanilha()

print("Abas encontradas:")

for aba in workbook.sheetnames:
    print("-", aba)


from excel_manager import lerConfiguracoes

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


from excel_manager import gravarResumoFaturas

resumoFaturas = gerarResumoFaturas()

gravarResumoFaturas(resumoFaturas)

print(
    f"{len(resumoFaturas)} faturas foram gravadas na planilha."
)
