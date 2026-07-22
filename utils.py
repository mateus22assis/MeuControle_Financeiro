#funçoes de validação de entrada
# ==========================
# VALIDAÇÃO DE ENTRADA
# ==========================

def lerFloat(mensagem):
    """
    Lê um valor decimal positivo informado pelo usuário.

    Aceita vírgula como separador decimal e solicita nova entrada
    enquanto o valor não for válido.

    Retorna o valor convertido para float.
    """
    while True:
        try:
            valor = input(mensagem).strip()

            valor = valor.replace(",", ".")

            valor = float(valor)

            if valor <= 0:
                print("valor deve ser maior que zero.")
                continue

            return valor

        except ValueError:
            print("valor inválido. Digite um número.")
            
def lerInt(mensagem):
    """
    Lê um número inteiro positivo informado pelo usuário.

    Solicita nova entrada enquanto o valor não for válido.

    Retorna o valor convertido para int.
    """
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("valor inválido. Digite um número inteiro.")

def lerTexto(mensagem):
    """
    Lê um texto válido informado pelo usuário.

    Não aceita textos vazios ou compostos apenas por números.

    Retorna o texto validado.
    """
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("entrada não pode ser vazia. Digite um texto válido.")
        elif texto.isdigit():
            print("entrada não pode conter apenas números. Digite um texto válido.")
        else:
            return texto
            


#função para formatar os valores em reais
# ==========================
# FORMATAÇÃO MONETÁRIA
# ==========================

def formatarReal(valor):
     """
     Formata um valor numérico para exibição em reais.

     Utiliza o padrão brasileiro de milhar e casas decimais.

     Retorna o texto formatado com o símbolo R$.
     """
     return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
