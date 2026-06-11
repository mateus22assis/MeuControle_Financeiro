from openpyxl import load_workbook

CAMINHO_PLANILHA = "ControleFinanceiro_2026_Prototipo_v3.xlsx"

def testarPlanilha():
    workbook = load_workbook(CAMINHO_PLANILHA)

    print("Abas encontradas:")

    for aba in workbook.sheetnames:
        print("-", aba)

# funcoes para ler a planilha
def lerConfiguracoes():
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_configuracoes = workbook["Configuracoes"]

    configuracoes = {
        "receitaMensal": 0.0,
        "gastosFixos": 0.0,
        "percentualReserva": 30.0
    }

    for linha in aba_configuracoes.iter_rows(min_row=2, values_only=True):
        campo, valor = linha
        
        if campo == "Receita Mensal":
            configuracoes["receitaMensal"] = valor if valor is not None else 0.0

        elif campo == "Gastos Fixos":
            configuracoes["gastosFixos"] = valor if valor is not None else 0.0

        elif campo == "Percentual de Reserva":
            configuracoes["percentualReserva"] = valor if valor is not None else 30.0

    return configuracoes

def lerCompromissosMensais():
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_compromissosMensais = workbook["CompromissosMensais"]

    compromissosMensais = []

    for linha in aba_compromissosMensais.iter_rows(min_row=5, values_only=True):

        descricao = linha[0]
        valor = linha[1]
        
        if descricao is not None:
            compromissosMensais.append({
                "descricao": descricao,
                "valor": valor
            })

    return compromissosMensais



# funçes para adicionar valores na planilha
def salvarReceitaMensal(valor):
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_configuracoes = workbook["Configuracoes"]

    aba_configuracoes["B2"] = valor

    workbook.save(CAMINHO_PLANILHA)

def salvarGastosFixos(valor):
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_configuracoes = workbook["Configuracoes"]

    aba_configuracoes["B3"] = valor

    workbook.save(CAMINHO_PLANILHA)

def salvarPercentualReserva(valor):
    workbook = load_workbook(CAMINHO_PLANILHA)
    aba_configuracoes = workbook["Configuracoes"]

    aba_configuracoes["B4"] = valor

    workbook.save(CAMINHO_PLANILHA)
    
#funçoes para calculos baseados nos dados da planilha(tabelas)

def somarCompromissosMensais():
    compromissos = lerCompromissosMensais()

    total = 0
    
    for compromisso in compromissos:
        total += compromisso["valor"]

    return total