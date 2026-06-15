from openpyxl import load_workbook
from datetime import datetime

# ==========================
# CONFIGURAÇÕES
# ==========================

CAMINHO_PLANILHA = "ControleFinanceiro_2026_Prototipo_v3.xlsx"

# ==========================
# TESTES
# ==========================

def testarPlanilha():
    workbook = load_workbook(CAMINHO_PLANILHA)

    print("Abas encontradas:")

    for aba in workbook.sheetnames:
        print("-", aba)

# ==========================
# LEITURA DA PLANILHA
# ==========================

def lerConfiguracoes():
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_configuracoes = workbook["Configuracoes"]

    configuracoes = {
        "receitaMensal": 0.0,
        "percentualReserva": 30.0
    }

    for linha in aba_configuracoes.iter_rows(min_row=2, values_only=True):

        campo, valor = linha

        if campo == "Receita Mensal":
            configuracoes["receitaMensal"] = valor if valor is not None else 0.0

        elif campo == "Percentual de Reserva":
            configuracoes["percentualReserva"] = valor if valor is not None else 30.0

    return configuracoes


def lerCompromissosMensais():
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_compromissos = workbook["CompromissosMensais"]

    compromissos = []

    for linha in aba_compromissos.iter_rows(min_row=5, values_only=True):

        descricao = linha[0]
        valor = linha[1]

        if descricao is not None:

            compromissos.append({
                "descricao": descricao,
                "valor": valor
            })

    return compromissos


def lerMovimentacoes():
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_movimentacoes = workbook["Movimentacoes"]

    movimentacoes = []

    for linha in aba_movimentacoes.iter_rows(min_row=2, values_only=True):

        data = linha[0]
        natureza = linha[1]
        meio = linha[2]
        categoria = linha[3]
        descricao = linha[4]
        valor = linha[5]
        parcelas = linha[6]
        valorParcela = linha[7]

        if descricao is not None:

            movimentacoes.append({
                "data": data,
                "Natureza": natureza,
                "Meio": meio,
                "Categoria": categoria,
                "Descricao": descricao,
                "Valor": valor,
                "Parcelas": parcelas,
                "ValorParcela": valorParcela
            })

    return movimentacoes

# ==========================
# ESCRITA NA PLANILHA
# ==========================

# aba Configuracoes

def salvarReceitaMensal(valor):
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_configuracoes = workbook["Configuracoes"]

    aba_configuracoes["B2"] = valor

    workbook.save(CAMINHO_PLANILHA)


def salvarPercentualReserva(valor):
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_configuracoes = workbook["Configuracoes"]

    aba_configuracoes["B4"] = valor

    workbook.save(CAMINHO_PLANILHA)


# aba Movimentacoes

def adicionarMovimentacao(
    natureza,
    meio,
    categoria,
    descricao,
    valorTotal,
    parcelas="",
    valorParcela=""
):

    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_movimentacoes = workbook["Movimentacoes"]

    proximaLinha = aba_movimentacoes.max_row + 1

    aba_movimentacoes[f"A{proximaLinha}"] = datetime.now().strftime("%d/%m/%Y")
    aba_movimentacoes[f"B{proximaLinha}"] = natureza
    aba_movimentacoes[f"C{proximaLinha}"] = meio
    aba_movimentacoes[f"D{proximaLinha}"] = categoria
    aba_movimentacoes[f"E{proximaLinha}"] = descricao
    aba_movimentacoes[f"F{proximaLinha}"] = valorTotal
    aba_movimentacoes[f"G{proximaLinha}"] = parcelas
    aba_movimentacoes[f"H{proximaLinha}"] = valorParcela

    workbook.save(CAMINHO_PLANILHA)

# ==========================
# CÁLCULOS BASEADOS NA PLANILHA
# ==========================

def somarCompromissosMensais():

    compromissos = lerCompromissosMensais()

    total = 0

    for compromisso in compromissos:

        valor = compromisso["valor"]

        if valor is not None:
            total += valor

    return total


def somarReceitas():

    movimentacoes = lerMovimentacoes()

    total = 0

    for mov in movimentacoes:

        if mov["Natureza"] == "receita":

            valor = mov["Valor"]

            if valor is not None:
                total += valor

    return total