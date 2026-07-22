import json


# ======================================
# ESTRUTURA LEGADA (TEMPORÁRIA)
#
# Responsável por:
# - fatura atual do cartão
# - parcelamentos futuros
#
# Previsto para remoção na v0.7
# ======================================


# ======================================
# SALVAR E CARREGAR JSON
# ======================================

def salvarDados(caminho, dados):
    """
    Salva os dados legados no arquivo JSON informado.

    Mantém a estrutura recebida com indentação para facilitar a leitura.

    Não retorna valor.
    """

    with open(caminho, "w") as arquivo:

        json.dump(
            dados,
            arquivo,
            indent=4
        )


def carregarDados(caminho):
    """
    Carrega os dados legados armazenados em um arquivo JSON.

    Quando o arquivo não existe ou está inválido, utiliza a estrutura
    padrão de parcelamentos e gastos de cartão.

    Retorna os dados carregados ou a estrutura padrão.
    """

    try:

        with open(caminho, "r") as arquivo:

            return json.load(arquivo)

    except (FileNotFoundError, json.JSONDecodeError):

        return {
            "parcelamentos": [],
            "gastosCartao": 0
        }


# ======================================
# PARCELAMENTOS EXISTENTES
# ======================================

def adicionarParcelamento(
    dados,
    nome,
    valorParcela,
    quantidadeParcelas
):
    """
    Adiciona um parcelamento à estrutura legada de dados.

    Registra o nome, o valor de cada parcela e sua quantidade.

    Não retorna valor.
    """

    dados["parcelamentos"].append(
        {
            "nome": nome,
            "valorParcela": valorParcela,
            "quantidadeParcelas": quantidadeParcelas
        }
    )


# ======================================
# GASTO NO CARTÃO À VISTA
# ======================================

def adicionarGastoCartao(
    dados,
    valor
):
    """
    Adiciona um gasto à vista ao total legado do cartão.

    Atualiza somente o valor acumulado da fatura atual.

    Não retorna valor.
    """

    dados["gastosCartao"] += valor


# ======================================
# NOVA COMPRA PARCELADA
# ======================================

def adicionarGastoParcelado(
    dados,
    nome,
    valorTotal,
    quantidadeParcelas
):
    """
    Registra uma compra parcelada na estrutura legada.

    Divide o valor total pela quantidade de parcelas e inclui a primeira
    parcela no gasto atual do cartão.

    Não retorna valor.
    """

    valorParcela = (
        valorTotal / quantidadeParcelas
    )

    dados["parcelamentos"].append(
        {
            "nome": nome,
            "valorParcela": valorParcela,
            "quantidadeParcelas": quantidadeParcelas
        }
    )

    # primeira parcela entra na fatura atual

    dados["gastosCartao"] += valorParcela


# ======================================
# FECHAMENTO DA FATURA
# ======================================

def fecharFatura(dados):
    """
    Fecha a fatura atual na estrutura legada de cartão.

    Reduz as parcelas pendentes e compõe a próxima fatura somente
    com os valores dos parcelamentos ainda ativos.

    Não retorna valor.
    """

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
