from dados import (
    carregarDados,
    salvarDados,
    adicionarGastoCartao,
    adicionarGastoParcelado,
    fecharFatura
)

CAMINHO = "data.json"  # caminho do arquivo de dados

# carrega os dados do arquivo
dados = carregarDados(CAMINHO)


# -------- TESTE MÊS 1 --------

print("MÊS 1")

adicionarGastoCartao(dados, 500)  # gasto à vista
adicionarGastoParcelado(dados, "Compra teste", 1000, 5)  # parcelado

print("Antes de fechar fatura:", dados)

# salva estado atual
salvarDados(CAMINHO, dados)

# fecha a fatura (vira o ciclo)
fecharFatura(dados)

print("Depois de fechar fatura:", dados)

# salva após fechamento
salvarDados(CAMINHO, dados)


# -------- TESTE MÊS 2 --------

print("\nMÊS 2")

adicionarGastoCartao(dados, 300)

print("Antes de fechar fatura:", dados)

# fecha novamente
fecharFatura(dados)

print("Depois de fechar fatura:", dados)

# salva estado final
salvarDados(CAMINHO, dados)