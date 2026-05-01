from dados import (
    adicionarParcelamento,
    carregarDados,
    salvarDados,
    adicionarGastoCartao,
    adicionarGastoParcelado,
    fecharFatura
)

CAMINHO = "data.json"  # caminho do arquivo de dados

# carrega os dados do arquivo
dados = carregarDados(CAMINHO)


#loop principal do programa
while True:
    print("\n--- Menu ---")
    print("1- adiconar  parcelamento existente")
    print("2. Adicionar gasto no cartão a vista")
    print("3. Adicionar gasto parcelado")
    print("4. Ver dados atuais")
    print("5. Fechar fatura")
    print("0. Sair")

    opção = input("Escolha uma opção: ")
    if opção == "0":
        print("Saindo...")
        break
    
    elif opção == "1":
        nome = input("Digite o nome do parcelamento existente: ")
        valorParcela = float(input("Digite o valor da parcela: "))
        quantidadeParcelas = int(input("Digite a quantidade de parcelas restantes: "))
        adicionarParcelamento(dados, nome, valorParcela, quantidadeParcelas)
        salvarDados(CAMINHO, dados)
    


    elif opção == "2":
        valor = float(input("Digite o valor do gasto no cartão: "))
        adicionarGastoCartao(dados, valor)
        salvarDados(CAMINHO, dados)
        print("Gasto adicionado ao cartão.")


    elif opção == "3":
        nome = input("Digite o nome da nova compra parcelada: ")
        valorTotal = float(input("Digite o valor total do gasto: "))
        quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))
        adicionarGastoParcelado(dados, nome, valorTotal, quantidadeParcelas)
        salvarDados(CAMINHO, dados)
        print("compra parcelada adicionada com parcelas.")

    elif opção == "4":
        print("\n--- Dados Atuais ---")

        print("gastos no cartao a vista:", dados["gastosCartao"])

        print ("parcelamentos:")
        for parcela in dados["parcelamentos"]:
            print(f"{parcela['nome']} - parcela: {parcela['valorParcela']} : quantidade de parcelas:{parcela['quantidadeParcelas']}")
    
    elif opção == "5":
        fecharFatura(dados)
        salvarDados(CAMINHO, dados)
        print("Fatura fechada. Gastos do cartão a vista e parcelas foram processados.")

    else:
        print("Opção inválida. Tente novamente.")





    




    
