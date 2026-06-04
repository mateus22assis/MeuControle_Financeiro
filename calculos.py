#calcular quanto vai guardar com base no que vc recebeu no mes somando tudo(salario, renda extra, etc) 
def calcularValorGuardar(dados):
    return dados["receitaMensal"] * (dados["percentualReserva"] / 100)


#calcular o valor total das parcelas futuras, somando todas as parcelas que tem que pagar
def somarParcelasMensais(parcelamentos):
    total = 0
    for parcela in parcelamentos:
        total += parcela["valorParcela"]
    return total


   

#quanto sobra depois de pagar os gastos fixos e o valor guardado, para gastar no cartao ou investir
def calcularSaldoDisponivel(dados):
    valorAGuardar = calcularValorGuardar(dados)

    return (
        dados["receitaMensal"]
        - valorAGuardar
        - dados["gastosFixos"]
        - dados["gastosCartao"]
        - dados["gastosPix"]
        - dados["gastosDebito"]
        - dados["gastosDinheiro"]

    )

#resumoFinal, quanto guardar, quanto sobra para gastar no cartao ou investir

def mostrarResumo(dados):
    valorGuardar = calcularValorGuardar(dados)    
    saldoDisponivel = calcularSaldoDisponivel (dados)

    gastosAvista = (
    dados ["gastosPix"] + dados["gastosDebito"] + dados["gastosDinheiro"])
  

    return {
        "valorGuardar": valorGuardar,
        "saldoDisponivel": saldoDisponivel,
        "gastosCartao": dados["gastosCartao"],
        "gastosAvista": gastosAvista,
        "gastosFixos": dados["gastosFixos"],
        "receitaMensal": dados["receitaMensal"]
        
    }