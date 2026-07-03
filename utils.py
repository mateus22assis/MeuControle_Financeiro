#funçoes de validação de entrada
def lerFloat(mensagem):
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
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("entrada não pode ser vazia. Digite um texto válido.")
        elif texto.isdigit():
            print("entrada não pode conter apenas números. Digite um texto válido.")
        else:
            return texto
            


#função para formatar os valores em reais
def formatarReal(valor):
     return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
