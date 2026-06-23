# ==========================
# TESTES
# ==========================

from excel_manager import abrirPlanilha

workbook = abrirPlanilha()

print("Abas encontradas:")

for aba in workbook.sheetnames:
    print("-", aba)