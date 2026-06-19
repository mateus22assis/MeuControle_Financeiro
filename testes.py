# ==========================
# TESTES
# ==========================

from excel_manager import (
    abrirPlanilha,
    lerMovimentacoes,
    lerCompromissosMensais,
  
)

from calculos import (
    somarReceitas,
    somarCompromissosMensais,
   
    mostrarResumo
)


# ==========================
# TESTE ABRIR PLANILHA
# ==========================

workbook = abrirPlanilha()

print("Abas encontradas:")

for aba in workbook.sheetnames:
    print("-", aba)

# ==========================
# TESTE MOVIMENTAÇÕES
# ==========================

print("\nMovimentações:")
print(lerMovimentacoes())

# ==========================
# TESTE COMPROMISSOS
# ==========================

print("\nCompromissos:")
print(lerCompromissosMensais())

# ==========================
# TESTE SOMATÓRIOS
# ==========================

print("\nReceitas:")
print(somarReceitas())

print("\nCompromissos Mensais:")
print(somarCompromissosMensais())



# ==========================
# TESTE RESUMO
# ==========================

print("\nResumo:")

resumo = mostrarResumo()

for chave, valor in resumo.items():
    print(f"{chave}: {valor}")