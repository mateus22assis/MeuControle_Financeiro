import json

#funcoes para tranformar os dados em json
def salvarDados(caminho, dados):
    with open(caminho, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)


def carregarDados(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {
            "parcelamentos":[],
            "gastosCartao":0,
        }

#para gastos que ja existiam, para adicionar um novo gasto ou parcelamento, tem que usar as funcoes abaixo para atualizar os dados
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
        "parcela": valorParcela,
        "restante": quantidadeParcelas
        }
    
    #salvar como parcelamento futuro
    dados["parcelamentos"].append(parcelamento)

    #adiciona a primeira parcela na fatura atual
    dados["gastosCartao"] += valorParcela


#fechammmento das faturas,
def fecharFatura(dados):
    for parcelamento in dados["parcelamentos"]:
        novosParcelamentos = []
        gastosProximaFatura = 0

        for parcelamento in dados["parcelamentos"]:
            parcelamento["restante"] -= 1

            if parcelamento["restante"] > 0:
                novosParcelamentos.append(parcelamento)
                gastosProximaFatura += parcelamento["parcela"]  #adiciona a parcela restante para a proxima fatura

    dados["parcelamentos"] = novosParcelamentos #atualiza a lista de parcelamentos, removendo os que ja foram pagos
    dados["gastosCartao"] = gastosProximaFatura #atualiza os gastos do cartao para a proxima fatura, considerando as parcelas restantes




