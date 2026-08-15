import customtkinter as ctk

from gui.tema import (CARD, BORDA, TEXTO_PRINCIPAL, TEXTO_SECUNDARIO, CARD_INTERNO)


class ResumoFinanceiro(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color=CARD)

        self.titulo = ctk.CTkLabel(
            self,
            text="Resumo Financeiro",
            font=("Arial", 18, "bold"),
            text_color=TEXTO_PRINCIPAL
        )

        self.titulo.pack(pady=(15, 10))
#cards
    #card saldo disppnivel
      
        self.valor_saldo =self.criar_card("Saldo Disponível", "R$ 0,00")
    #valor a guardar
        self.valor_guardar = self.criar_card("Meta de guardar (mês)", "R$ 0,00")
    #fatura do cartao de credito
        self.valor_fatura = self.criar_card("Fatura do próximo mês", "R$ 0,00")
        self.valor_comprometimento = self.criar_card(
            "Margem disponível \n próxima fatura",
            "R$ 0,00"
        )
   
        
    #criar card de resumo financeiro
    def criar_card(self, titulo, valor):

        card = ctk.CTkFrame(self,fg_color=CARD_INTERNO,border_color=BORDA, border_width=1, corner_radius=10)
        card.pack(pady=10, padx=10, fill="x")

        label_titulo = ctk.CTkLabel(
            card,
            text=titulo,
            font=("Arial", 14),
            text_color=TEXTO_SECUNDARIO
        )
        label_titulo.pack(pady=(10, 5))

        label_valor = ctk.CTkLabel(
            card,
            text=valor,
            font=("Arial", 22, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        label_valor.pack(pady=(0, 10))
        return  label_valor
#atualizaçao dos valores dos cards
    def atualizar_valores(self, saldo, valor_guardar, fatura, comprometimento):
        self.valor_saldo.configure(text=f"R$ {saldo:,.2f}")
        self.valor_guardar.configure(text=f"R$ {valor_guardar:,.2f}")
        self.valor_fatura.configure(text=f"R$ {fatura:,.2f}")
        self.valor_comprometimento.configure(text=f"R$ {comprometimento:,.2f}")
