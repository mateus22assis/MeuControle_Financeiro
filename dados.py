import json

#funcoes para tranformar os dados em json
def salvarDados(caminho, dados):
    with open(caminho, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)


def carregarDados(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return {
            "parcelamentos":[],
            "gastosCartao":0,
            "receitaMensal":0,
            "gastosFixos":0,
            "percentualReserva":30,
            
        }

#para gastos que ja existiam
def adicionarParcelamento(dados, nome, valorParcela, quantidadeParcelas):
    parcelamento = {
        "nome": nome,
        "valorParcela": valorParcela,
        "quantidadeParcelas": quantidadeParcelas
    }
    
    dados["parcelamentos"].append(parcelamento)

#para gastos do cartao a vista no cartao
def adicionarGastoCartao(dados, valor):
    dados["gastosCartao"] += valor

#novas comprars parceladas
def adicionarGastoParcelado(dados, nome, valorTotal, quantidadeParcelas):
    valorParcela = valorTotal / quantidadeParcelas


    parcelamento = {
        "nome": nome,
        "valorParcela": valorParcela,
        "quantidadeParcelas": quantidadeParcelas
        }
    
    #salvar como parcelamento futuro
    dados["parcelamentos"].append(parcelamento)

    #adiciona a primeira parcela na fatura atual
    dados["gastosCartao"] += valorParcela


#fechammmento das faturas,
def fecharFatura(dados):
    novosParcelamentos = []
    gastosProximaFatura = 0

    for parcelamento in dados["parcelamentos"]:
            parcelamento["quantidadeParcelas"] -= 1

            if parcelamento["quantidadeParcelas"] > 0:
                novosParcelamentos.append(parcelamento)
                gastosProximaFatura += parcelamento["valorParcela"]  #adiciona a parcela restante para a proxima fatura

    dados["parcelamentos"] = novosParcelamentos #atualiza a lista de parcelamentos, removendo os que ja foram pagos
    dados["gastosCartao"] = gastosProximaFatura #atualiza os gastos do cartao para a proxima fatura, considerando as parcelas restantes


#receita mensal
def definirReceitaMensal(dados, valor):
    dados["receitaMensal"] = valor

#gastos fixos
def definirGastosFixos(dados, valor):
    dados["gastosFixos"] = valor

#percentual de reserva
def definirPercentualReserva(dados, valor):
    dados["percentualReserva"] = valor




