from dados import (
    adicionarParcelamento,
    carregarDados,
    salvarDados,
    adicionarGastoCartao,
    adicionarGastoParcelado,
    fecharFatura,
    definirReceitaMensal,
    definirGastosFixos,
    definirPercentualReserva

)
from calculos import mostrarResumo

from utils import lerFloat, lerInt, formatarReal, lerTexto

CAMINHO = "data.json"  # caminho do arquivo de dados

# carrega os dados do arquivo
dados = carregarDados(CAMINHO)


#loop principal do programa
while True:
    print("\n--- Menu ---")
    print("1- adiconar parcelamento existente")
    print("2. Adicionar gasto no cartão a vista")
    print("3. Adicionar gasto parcelado")
    print("4. Ver dados atuais")
    print("5. Fechar fatura")
    print("6. Definir receita mensal")
    print("7. Definir gastos fixos")
    print("8. Definir percentual de reserva")
    print("9. ver resumo financeiro")
    print("0. Sair")

    opção = input("Escolha uma opção: ")
    if opção == "0":
        print("Saindo...")
        break
    
    elif opção == "1":
        nome = lerTexto("Digite o nome do parcelamento existente: ")
        valorParcela = lerFloat("Digite o valor da parcela: ")
        quantidadeParcelas = lerInt("Digite a quantidade de parcelas restantes: ")
        adicionarParcelamento(dados, nome, valorParcela, quantidadeParcelas)
        salvarDados(CAMINHO, dados)
    


    elif opção == "2":
        valor = lerFloat("Digite o valor do gasto no cartão: ")
        adicionarGastoCartao(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Gasto adicionado ao cartão.")


    elif opção == "3":
        nome = lerTexto("Digite o nome da nova compra parcelada: ")
        valorTotal = lerFloat("Digite o valor total do gasto: ")
        quantidadeParcelas = lerInt("Digite a quantidade de parcelas: ")
        adicionarGastoParcelado(dados, nome, valorTotal, quantidadeParcelas)
        salvarDados(CAMINHO, dados)
        print("compra parcelada adicionada com sucesso.")

    elif opção == "4":
        print("\n--- Dados Atuais ---")

        totalFatura = dados["gastosCartao"]
        totalParcelamentos = sum(parcelamento["valorParcela"] for parcelamento in dados["parcelamentos"])
        gastosAvista = totalFatura - totalParcelamentos

        print("Total da fatura:", formatarReal(totalFatura))
        print("Total de parcelamentos:", formatarReal(totalParcelamentos))
        print("Gastos à vista:", formatarReal(gastosAvista))

        print ("parcelamentos:")
        for parcela in dados["parcelamentos"]:
            print(f"{parcela['nome']} - parcela: {formatarReal(parcela['valorParcela'])} : quantidade de parcelas:{parcela['quantidadeParcelas']}")
    
    elif opção == "5":
        fecharFatura(dados)
        salvarDados(CAMINHO, dados)
        print("Fatura fechada. Gastos do cartão a vista e parcelas foram processados.")

    elif opção == "6":
        valor = lerFloat("Digite o valor da receita mensal: ")
        definirReceitaMensal(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Receita mensal definida com sucesso.")

    elif opção == "7":
        valor = lerFloat("Digite o valor dos gastos fixos: ")
        definirGastosFixos(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Gastos fixos definidos com sucesso.")

    elif opção == "8":
        valor = lerInt("Digite o percentual para guardar(%): ")
        definirPercentualReserva(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Percentual de reserva definido com sucesso.")

    elif opção == "9":
        resumo = mostrarResumo(dados)
        print("\n--- Resumo Financeiro ---")
        print("receita mensal:", formatarReal(resumo["receitaMensal"]))
        print("gastos fixos:", formatarReal(resumo["gastosFixos"]))
        print("fatura atual:", formatarReal(resumo["gastosCartao"]))
        print("valor a ser guardado:", formatarReal(resumo["valorGuardar"]))
        print("saldo disponível:", formatarReal(resumo["saldoDisponivel"]))

    else:
        print("Opção inválida. Tente novamente.")





    




    
