import json


# ==========================
# SALVAR E CARREGAR JSON
# ==========================

def salvarDados(caminho, dados):

    with open(caminho, "w") as arquivo:
        json.dump(
            dados,
            arquivo,
            indent=4
        )


def carregarDados(caminho):

    try:

        with open(caminho, "r") as arquivo:
            return json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):

        return {
            "parcelamentos": [],
            "gastosCartao": 0
        }


# ==========================
# PARCELAMENTOS EXISTENTES
# ==========================

def adicionarParcelamento(
    dados,
    nome,
    valorParcela,
    quantidadeParcelas
):

    parcelamento = {
        "nome": nome,
        "valorParcela": valorParcela,
        "quantidadeParcelas": quantidadeParcelas
    }

    dados["parcelamentos"].append(
        parcelamento
    )


# ==========================
# GASTO NO CARTÃO À VISTA
# ==========================

def adicionarGastoCartao(
    dados,
    valor
):

    dados["gastosCartao"] += valor


# ==========================
# NOVA COMPRA PARCELADA
# ==========================

def adicionarGastoParcelado(
    dados,
    nome,
    valorTotal,
    quantidadeParcelas
):

    valorParcela = (
        valorTotal / quantidadeParcelas
    )

    parcelamento = {
        "nome": nome,
        "valorParcela": valorParcela,
        "quantidadeParcelas": quantidadeParcelas
    }

    # guarda para as próximas faturas

    dados["parcelamentos"].append(
        parcelamento
    )

    # primeira parcela entra na fatura atual

    dados["gastosCartao"] += valorParcela


# ==========================
# FECHAR FATURA
# ==========================

def fecharFatura(dados):

    novosParcelamentos = []

    gastosProximaFatura = 0

    for parcelamento in dados["parcelamentos"]:

        parcelamento["quantidadeParcelas"] -= 1

        if parcelamento["quantidadeParcelas"] > 0:

            novosParcelamentos.append(
                parcelamento
            )

            gastosProximaFatura += (
                parcelamento["valorParcela"]
            )

    dados["parcelamentos"] = (
        novosParcelamentos
    )

    dados["gastosCartao"] = (
        gastosProximaFatura
    )