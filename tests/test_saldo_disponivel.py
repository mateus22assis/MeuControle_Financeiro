from datetime import datetime

import backend.calculos as calculos


def test_saldo_disponivel_em_01_09_2026():
    """
    Cenário real observado na virada de agosto para setembro:

    Saldo disponível em 31/08/2026: R$ 128,89
    Fatura bruta de setembro:       R$ 874,18
    Abatimento da fatura:           R$ 300,00
    Fatura líquida:                 R$ 574,18
    Compromissos de setembro:       R$ 739,78
    Receitas em setembro:           R$ 0,00
    Despesas à vista em setembro:   R$ 0,00

    Saldo esperado:
    128,89 - 574,18 - 739,78 = -1.185,07
    """

    class DataFixa:
        @classmethod
        def today(cls):
            return datetime(2026, 9, 1)

    calculos.datetime = DataFixa

    calculos.lerConfiguracoes = lambda: {
        "receitaMensal": 0.0,
        "percentualReserva": 0.0,
        "saldoInicial": 128.89,
        "limiteCartao": 5000.0,
        "diaFechamento": 3,
        "diaVencimento": 10,
    }

    calculos.somarReceitasPorMes = lambda mes, ano: 0.0
    calculos.calcularValorGuardar = lambda: 0.0
    calculos.somarCompromissosMensais = lambda: 739.78
    calculos.somarDespesasAVista = lambda mes, ano: 0.0

    # Fatura bruta = R$ 874,18
    calculos.somarFaturaPorMes = lambda mes, ano: 874.18

    # Abatimento real registrado = R$ 300,00
    calculos.lerAbatimentosFaturas = lambda: {
        "09/2026": 300.00
    }

    saldo = calculos.calcularSaldoDisponivel()

    saldo_esperado = -1185.07

    assert round(saldo, 2) == saldo_esperado


    def test_diagnostico_saldo_real():
        """
    Mostra no terminal os valores reais usados
    pelo cálculo do saldo disponível.
    """

    class DataFixa:
        @classmethod
        def today(cls):
            return datetime(2026, 9, 1)

    calculos.datetime = DataFixa

    saldo = calculos.calcularSaldoDisponivel()

    print("\n===== DIAGNÓSTICO SALDO =====")
    print("Saldo calculado:", saldo)


    def test_diagnostico_mostrar_resumo():
        class DataFixa:
            @classmethod
            def today(cls):
                return datetime(2026, 9, 1)

    calculos.datetime = DataFixa

    calculos.lerConfiguracoes = lambda: {
        "receitaMensal": 0.0,
        "percentualReserva": 0.0,
        "saldoInicial": 128.89,
        "limiteCartao": 5000.0,
        "diaFechamento": 3,
        "diaVencimento": 10,
    }

    calculos.somarReceitasPorMes = lambda mes, ano: 0.0
    calculos.somarReceitasParaReservaNoMes = lambda mes, ano: 0.0
    calculos.somarDespesasAVista = lambda mes, ano: 0.0
    calculos.calcularValorGuardar = lambda: 0.0
    calculos.somarCompromissosMensais = lambda: 739.78
    calculos.somarFaturaPorMes = lambda mes, ano: 874.18

    calculos.lerAbatimentosFaturas = lambda: {
        "09/2026": 300.00
    }

    resumo = calculos.mostrarResumo()

    print("\n===== DIAGNÓSTICO MOSTRAR RESUMO =====")
    print("saldoDisponivel:", resumo["saldoDisponivel"])


    def test_diagnostico_com_valor_guardar():
        class DataFixa:
            @classmethod
            def today(cls):
                return datetime(2026, 9, 1)

    calculos.datetime = DataFixa

    calculos.lerConfiguracoes = lambda: {
        "receitaMensal": 2000.0,
        "percentualReserva": 30.0,
        "saldoInicial": 0.0,
        "limiteCartao": 5000.0,
        "diaFechamento": 3,
        "diaVencimento": 10,
    }

    calculos.somarReceitasPorMes = lambda mes, ano: 0.0
    calculos.somarReceitasParaReservaNoMes = lambda mes, ano: 0.0
    calculos.somarDespesasAVista = lambda mes, ano: 0.0
    calculos.calcularValorGuardar = lambda: 600.0
    calculos.somarCompromissosMensais = lambda: 739.78
    calculos.somarFaturaPorMes = lambda mes, ano: 874.18

    calculos.lerAbatimentosFaturas = lambda: {
        "09/2026": 300.00
    }

    saldo = calculos.calcularSaldoDisponivel()

    print("\n===== DIAGNÓSTICO COM VALOR A GUARDAR =====")
    print("Valor a guardar:", 600.00)
    print("Saldo calculado:", saldo)