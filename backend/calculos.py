from calendar import monthrange
from datetime import datetime

from backend.excel_manager import (
    lerConfiguracoes,
    lerCompromissosMensais,
    lerMovimentacoes,
    converterData,
    determinarMesFatura,
    lerAbatimentosFaturas
)


# ==========================
# SOMATÓRIOS
# ==========================

def somarReceitasPorMes(mes, ano):
    """
    Soma todas as movimentações classificadas como receita
    que pertencem ao mês e ano informados.
    """
    movimentacoes = lerMovimentacoes()
    total = 0

    for mov in movimentacoes:
        natureza = str(mov["natureza"]).strip().lower()
        if natureza == "receita" and mov["data"] is not None:
            data_mov = converterData(mov["data"])
            if data_mov.month == mes and data_mov.year == ano:
                valor = mov["valor"]
                if valor is not None:
                    total += valor
    return total

def somarReceitasParaReservaNoMes(mes, ano):
    """
    Soma somente as receitas consideradas renda nova
    no mês informado para o cálculo do valor a guardar.
    """
    movimentacoes = lerMovimentacoes()
    total = 0

    for mov in movimentacoes:
        natureza = str(mov["natureza"]).strip().lower()
        categoria = str(mov["categoria"]).strip().lower()
        
        if natureza == "receita" and categoria in ["salario", "renda extra"] and mov["data"] is not None:
            data_mov = converterData(mov["data"])
            if data_mov.month == mes and data_mov.year == ano:
                valor = mov["valor"]
                if valor is not None:
                    total += valor
    return total

def somarDespesasAVista(mes, ano):
    """
    Soma despesas (meio != credito) de um mês específico.
    """
    movimentacoes = lerMovimentacoes()
    total = 0

    for mov in movimentacoes:
        natureza = str(mov["natureza"]).strip().lower()
        meio = str(mov["meio"]).strip().lower()
        
        if natureza == "despesa" and meio != "credito" and mov["data"] is not None:
            data_mov = converterData(mov["data"])
            if data_mov.month == mes and data_mov.year == ano:
                valor = mov["valor"]
                if valor is not None:
                    total += float(valor)
    return total

def somarFaturaPorMes(mes, ano):
    """
    Soma as despesas de cartão cuja fatura de destino é o mês/ano informado.
    """
    movimentacoes = lerMovimentacoes()
    configuracoes = lerConfiguracoes()
    diaFechamento = configuracoes["diaFechamento"]
    total = 0

    for mov in movimentacoes:
        natureza = str(mov["natureza"]).strip().lower()
        meio = str(mov["meio"]).strip().lower()

        if natureza == "despesa" and meio == "credito" and mov["data"] is not None:
            m_fat, a_fat = determinarMesFatura(mov["data"], diaFechamento)
            if m_fat == mes and a_fat == ano:
                valor = mov["valor"]
                if valor is not None:
                    total += float(valor)
    return total

def somarCompromissosMensais():

    """
    Soma os valores dos compromissos mensais cadastrados.

    Ignora compromissos sem valor informado.

    Retorna o total dos gastos fixos mensais.
    """

    compromissos = lerCompromissosMensais()

    total = 0

    for compromisso in compromissos:

        valor = compromisso["valor"]

        if valor is not None:
            total += float(valor)

    return total


def somarReceitas():
    """
    Soma todas as movimentações classificadas como receita.

    Movimentações sem valor não entram no cálculo.

    Retorna o total de receitas registradas.
    """

    movimentacoes = lerMovimentacoes()

    total = 0

    for mov in movimentacoes:

        natureza = str(mov["natureza"]).strip().lower()

        if natureza == "receita":

            valor = mov["valor"]

            if valor is not None:
                total += valor

    return total

def somarReceitasParaReserva():
    """
    Soma somente as receitas consideradas renda nova
    para o cálculo do valor a guardar.

    Não considera devoluções de empréstimos ou resgates
    de investimentos como base para a reserva.

    Retorna o total de receitas que entram no cálculo da reserva.
    """

    movimentacoes = lerMovimentacoes()

    total = 0

    for mov in movimentacoes:

      natureza = str(mov["natureza"]).strip().lower()
      categoria = str(mov["categoria"]).strip().lower()

      if(
          natureza == "receita" and categoria in[
              "salario", "renda extra"
          ]
      ):

            valor = mov["valor"]

            if valor is not None:
                total += valor

    return total


def somarDespesas():
    """
    Soma as despesas que pertencem ao mês atual.

    Considera somente movimentações classificadas como despesa
    cuja data pertence ao mês e ano atuais.

    Movimentações sem valor ou sem data não entram no cálculo.

    Retorna o total das despesas do mês atual.
    """

    movimentacoes = lerMovimentacoes()

    hoje = datetime.today()

    total = 0

    for mov in movimentacoes:

        natureza = str(mov["natureza"]).strip().lower()

        if (
            natureza == "despesa"
            and mov["data"] is not None
        ):

            dataMovimentacao = converterData(mov["data"])

            if (
                dataMovimentacao.month == hoje.month
                and dataMovimentacao.year == hoje.year
            ):

                valor = mov["valor"]

                if valor is not None:
                    total += float(valor)

    return total


# ==========================
# CARTÃO DE CRÉDITO
# ==========================

def calcularProximaFatura():
    """
    Calcula o total da próxima fatura do cartão.
    """
    hoje = datetime.today()
    configuracoes = lerConfiguracoes()
    diaFechamento = configuracoes["diaFechamento"]

    # Se hoje é 15/03 e fechamento é 03, a próxima fatura é Abril.
    # Se hoje é 01/03 e fechamento é 03, a próxima fatura é Março.
    mes_fat, ano_fat = determinarMesFatura(hoje, diaFechamento)

    valor_fatura = somarFaturaPorMes(mes_fat, ano_fat)

    abatimentos = lerAbatimentosFaturas()

    chave_fatura = f"{mes_fat:02d}/{ano_fat}"

    valor_abatido = abatimentos.get(chave_fatura, 0.0)

    return max(0, valor_fatura - valor_abatido)
 

def calcularCapacidadeComprometimento():
    """
    Calcula quanto ainda se pode gastar no cartão para a próxima fatura.
    Fórmula: Renda Prevista - Reserva - Compromissos - Fatura já comprometida.
    """
    configuracoes = lerConfiguracoes()
    renda = configuracoes["receitaMensal"]
    perc_reserva = configuracoes["percentualReserva"]
    
    reserva = renda * (perc_reserva / 100)
    gastos_fixos = somarCompromissosMensais()
    
    # Próxima fatura
    hoje = datetime.today()
    mes_prox, ano_prox = determinarMesFatura(hoje, configuracoes["diaFechamento"])
    fatura_prox = somarFaturaPorMes(mes_prox, ano_prox)

    abatimentos = lerAbatimentosFaturas()

    nome_fatura = f"{mes_prox:02d}/{ano_prox}"

    valora_abatido = abatimentos.get(nome_fatura, 0.0)

    fatura_em_aberto = (fatura_prox- float(valora_abatido))
    
    capacidade = (renda - reserva - gastos_fixos - fatura_em_aberto)
    return capacidade

def calcularLimiteDisponivel():
    """
    Calcula o limite disponível do cartão de crédito.
    Desconta apenas faturas aberta e futuras.
    """
    configuracoes = lerConfiguracoes()
    limite_total = configuracoes["limiteCartao"]
    diaFechamento = configuracoes["diaFechamento"]
    
    hoje = datetime.today()
    # Fatura aberta (a que ainda recebe compras)
    m_aberta, a_aberta = determinarMesFatura(hoje, diaFechamento)
    
    movimentacoes = lerMovimentacoes()
    comprometido = 0
    
    for mov in movimentacoes:
        natureza = str(mov["natureza"]).strip().lower()
        meio = str(mov["meio"]).strip().lower()
        
        if natureza == "despesa" and meio == "credito" and mov["data"] is not None:
            m_fat, a_fat = determinarMesFatura(mov["data"], diaFechamento)
            # Se a fatura de destino é a aberta ou qualquer futura
            if (a_fat > a_aberta) or (a_fat == a_aberta and m_fat >= m_aberta):
                valor = mov["valor"]
                if valor is not None:
                    comprometido += float(valor)
                    
    return limite_total - comprometido


# ==========================
# RESUMO DE FATURAS
# ==========================

def gerarResumoFaturas():
    """
    Gera o resumo das faturas de cartão por mês de referência.

    Compras realizadas no dia do fechamento ou depois
    pertencem à fatura do mês seguinte.

    Retorna uma lista com valores, vencimentos e status das faturas.
    """

    movimentacoes = lerMovimentacoes()

    configuracoes = lerConfiguracoes()

    abatimentos = lerAbatimentosFaturas()

    diaFechamento = configuracoes["diaFechamento"]
    diaVencimento = configuracoes["diaVencimento"]

    hoje = datetime.today()

    # Determina qual é a fatura atualmente aberta.
    mesFaturaAtual, anoFaturaAtual = determinarMesFatura(
        hoje,
        diaFechamento
    )

    faturas = {}

    for movimentacao in movimentacoes:

        natureza = str(
            movimentacao["natureza"]
        ).strip().lower()

        meio = str(
            movimentacao["meio"]
        ).strip().lower()

        if (
            natureza != "despesa"
            or meio != "credito"
            or movimentacao["data"] is None
            or movimentacao["valor"] is None
        ):
            continue

        mesFatura, anoFatura = determinarMesFatura(
            movimentacao["data"],
            diaFechamento
        )

        if mesFatura is None:
            continue

        chaveFatura = (anoFatura, mesFatura)

        if chaveFatura not in faturas:
            faturas[chaveFatura] = 0.0

        faturas[chaveFatura] += float(
            movimentacao["valor"]
        )

    resumoFaturas = []

    for (anoFatura, mesFatura), valor in sorted(
        faturas.items()
    ):

        ultimoDiaMes = monthrange(
            anoFatura,
            mesFatura
        )[1]

        diaVencimentoFatura = min(
            diaVencimento,
            ultimoDiaMes
        )

        if (anoFatura, mesFatura) < (
            anoFaturaAtual,
            mesFaturaAtual
        ):
            status = "Fechada"

        elif (anoFatura, mesFatura) == (
            anoFaturaAtual,
            mesFaturaAtual
        ):
            status = "Aberta"

        else:
            status = "Prevista"

        resumoFaturas.append({

            "fatura":
                f"{mesFatura:02d}/{anoFatura}",

            "vencimento":
                (
                    f"{diaVencimentoFatura:02d}/"
                    f"{mesFatura:02d}/"
                    f"{anoFatura}"
                ),

            "valor":
                round(max(0, valor - abatimentos.get(f"{mesFatura:02d}/{anoFatura}",0.0)), 2),

            "status":
                status
        })

    return resumoFaturas



# ==========================
# RESERVA
# ==========================

def calcularValorGuardar():
    """
    Calcula o valor mensal reservado para economia baseado nas receitas do mês atual.
    """
    hoje = datetime.today()
    configuracoes = lerConfiguracoes()
    receitaParaReserva = somarReceitasParaReservaNoMes(hoje.month, hoje.year)
    percentualReserva = configuracoes["percentualReserva"]

    return receitaParaReserva * (percentualReserva / 100)


# ==========================
# SALDO
# ==========================

def calcularSaldoDisponivel():
    """
        Calcula o saldo disponível no mês atual.

    Considera:
    - saldo inicial;
    - receitas do mês;
    - valor a guardar;
    - compromissos mensais;
    - fatura que vence no mês;
    - despesas à vista;
    - abatimentos realizados na próxima fatura.
    """
    hoje = datetime.today()
    configuracoes = lerConfiguracoes()
    
    saldo_inicial = configuracoes["saldoInicial"]
    receitas_mes = somarReceitasPorMes(hoje.month, hoje.year)
    reserva_mes = calcularValorGuardar()
    gastos_fixos = somarCompromissosMensais()
    
    # Fatura que vence no mês atual
    fatura_mes = somarFaturaPorMes(hoje.month, hoje.year)

    
    
    # Despesas à vista do mês atual (PIX, Débito, etc)
    despesas_vista = somarDespesasAVista(hoje.month, hoje.year)

    #abatimento realizado na proxima fatura
    mes_proxima_fatura, ano_proxima_fatura = determinarMesFatura(
        hoje,
        configuracoes["diaFechamento"]
    )
    abatimentos = lerAbatimentosFaturas()

    chave_fatura = (
        f"{mes_proxima_fatura:02d}/{ano_proxima_fatura}"

    )

    valor_abatido = abatimentos.get(
        chave_fatura,
        0.0
    )


    return (
        saldo_inicial
        + receitas_mes
        - reserva_mes
        - gastos_fixos
        - fatura_mes
        - despesas_vista
        -valor_abatido
    )



# ==========================
# RESUMO
# ==========================

def mostrarResumo():
    """
    Reúne os principais indicadores financeiros.
    """
    hoje = datetime.today()
    configuracoes = lerConfiguracoes()
    receitas_mes = somarReceitasPorMes(hoje.month, hoje.year)
    receita_para_reserva = somarReceitasParaReservaNoMes(
        hoje.month,
        hoje.year
    )
    saidas_reais = somarDespesasAVista(hoje.month, hoje.year)
    
    return {
        "receitaTotal": receitas_mes,
        "receitaParaReserva": receita_para_reserva,
        "entradasMes": receitas_mes,
        "saidasReaisMes": saidas_reais,
        "gastosFixos": somarCompromissosMensais(),
        "valorGuardar": calcularValorGuardar(),
        "saldoDisponivel": calcularSaldoDisponivel(),
        "faturaProximoMes": calcularProximaFatura(),
        "capacidadeComprometimento": calcularCapacidadeComprometimento(),
        "limiteTotal": configuracoes["limiteCartao"],
        "limiteDisponivel": calcularLimiteDisponivel()
    }
