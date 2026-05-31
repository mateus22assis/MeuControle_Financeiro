from dados import (
    adicionarGastoDebito,
    adicionarGastoPix,
    adicionarGastoDinheiro,
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
    print("2. Adicionar gasto no cartão de credito a vista")
    print("3. Adicionar gasto parcelado no cartao de credito")
    print("4. adicionar gasto no pix")
    print("5. adicionar gasto no debito")
    print("6. adicionar gasto no dinheiro")
    print("7. Ver dados atuais")
    print("8. Fechar fatura")
    print("9. Definir receita mensal")
    print("10. Definir gastos fixos")
    print("11. Definir percentual de reserva")
    print("12. ver resumo financeiro")
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
        valor = lerFloat("Digite o valor do gasto no pix: ")
        adicionarGastoPix(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Gasto no pix adicionado com sucesso.")


    elif opção == "5":
        valor = lerFloat("Digite o valor do gasto no debito: ")
        adicionarGastoDebito(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Gasto no debito adicionado com sucesso.")


    elif opção == "6":
        valor = lerFloat("Digite o valor do gasto no dinheiro: ")
        adicionarGastoDinheiro(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Gasto no dinheiro adicionado com sucesso.")


    elif opção == "7":
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
    
    elif opção == "8":
        fecharFatura(dados)
        salvarDados(CAMINHO, dados)
        print("Fatura fechada. Gastos do cartão a vista e parcelas foram processados.")

    elif opção == "9":
        valor = lerFloat("Digite o valor da receita mensal: ")
        definirReceitaMensal(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Receita mensal definida com sucesso.")

    elif opção == "10":
        valor = lerFloat("Digite o valor dos gastos fixos: ")
        definirGastosFixos(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Gastos fixos definidos com sucesso.")

    elif opção == "11":
        valor = lerInt("Digite o percentual para guardar(%): ")
        definirPercentualReserva(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Percentual de reserva definido com sucesso.")

    elif opção == "12":
        resumo = mostrarResumo(dados)
        print("\n--- Resumo Financeiro ---")
        print("receita mensal:", formatarReal(resumo["receitaMensal"]))
        print("gastos fixos:", formatarReal(resumo["gastosFixos"]))
        print("fatura atual:", formatarReal(resumo["gastosCartao"]))
        print("gastos à vista:", formatarReal(resumo["gastosAvista"]))
        print("valor a ser guardado:", formatarReal(resumo["valorGuardar"]))
        print("saldo disponível:", formatarReal(resumo["saldoDisponivel"]))

    else:
        print("Opção inválida. Tente novamente.")





    




    
