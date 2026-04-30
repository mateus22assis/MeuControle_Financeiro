#calcular quanto vai guardar com base no que vc recebeu no mes somando tudo(salario, renda extra, etc) 
def calcularValorGuardado(receita):
    percentual= 30
    valor = receita * percentual / 100
    return valor

#calcular o valor total das parcelas futuras, somando todas as parcelas que tem que pagar
def calcularParcelasFuturas(parcelamentos):
    total = 0
    for parcela in parcelamentos:
        total += parcela["parcela"]
    return total


#funçao para calcular limite que pode ser gasto no cartao para proxima fatura
def calcularLimite(receita, gastosFixos, investimentos, gastosCartao,pracelamentos):
    valorGuardado = calcularValorGuardado(receita)
    ParcelasFuturas = calcularParcelasFuturas(pracelamentos)
    limiteBase = receita - gastosFixos - valorGuardado - investimentos

    limiteReal = limiteBase - gastosCartao
    return{
        "valorGuardado": valorGuardado,
        "ParcelasFuturas": ParcelasFuturas,
        "limiteBase": limiteBase,
        "limiteReal": limiteReal
    }
