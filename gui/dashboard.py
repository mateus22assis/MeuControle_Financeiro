import customtkinter as ctk

from backend.calculos import mostrarResumo
from backend.utils import formatarReal

from gui.tema import (CARD,CARD_INTERNO, BORDA, RECEITA, DESPESA, TEXTO_PRINCIPAL, TEXTO_SECUNDARIO, FUNDO_PRINCIPAL)


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color=FUNDO_PRINCIPAL)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 24, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        self.titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20, 10)
        )

        self.frame_fluxo_mensal = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.frame_fluxo_mensal.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=20,
            pady=10,
            sticky="ew"
        )

        for coluna in range(3):
            self.frame_fluxo_mensal.grid_columnconfigure(coluna, weight=1)

        self.card_receita = self.criar_card(
            self.frame_fluxo_mensal,
            "Receita do mês",
            0,
            0
        )
        self.card_entradas = self.criar_card(
            self.frame_fluxo_mensal,
            "Entradas do mês",
            0,
            1
        )
        self.card_saidas = self.criar_card(
            self.frame_fluxo_mensal,
            "Saídas reais do mês",
            0,
            2
        )

        self.titulo_cartao = ctk.CTkLabel(
            self,
            text="Cartão",
            font=("Arial", 18, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        self.titulo_cartao.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=(20, 10)
        )

        self.frame_cartao = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.frame_cartao.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=20,
            pady=10,
            sticky="ew"
        )
        
        self.frame_cartao.grid_columnconfigure(0, weight=1)
        self.frame_cartao.grid_columnconfigure(1, weight=1)

        self.card_limite_total = self.criar_card(
            self.frame_cartao,
            "Limite total",
            0,
            0
        )
    
        self.card_limite_disponivel = self.criar_card(
            self.frame_cartao,
            "Limite disponível",
            0,
            1
        )

        self.card_compromissos = self.criar_card(
            self.frame_cartao,
            "Compromissos do mês",
            1,
            0,
            colunspan=2
        )

        self.card_receita.configure(text_color=RECEITA)

        self.card_saidas.configure(text_color=DESPESA)

             

        self.atualizar_dados()

    def criar_card(self, parent, titulo, linha, coluna, colunspan=1):

        card = ctk.CTkFrame(
            parent,
            fg_color=CARD,
            border_color=BORDA,
            border_width=1,
            corner_radius=10
        )
        card.grid(
            row=linha,
            column=coluna,
            columnspan=colunspan,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        label_titulo = ctk.CTkLabel(
            card,
            text=titulo,
            font=("Arial", 14),
            text_color=TEXTO_SECUNDARIO
        )
        label_titulo.pack(
            pady=(15, 5)
        )

        label_valor = ctk.CTkLabel(
            card,
            text="R$ 0,00",
            font=("Arial", 22, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        label_valor.pack(
            pady=(0, 15)
        )

        return label_valor

    def atualizar_dados(self):

        resumo = mostrarResumo()

        self.card_receita.configure(
            text=formatarReal(
                resumo["receitaParaReserva"]
            )
        )

        self.card_entradas.configure(text=formatarReal(resumo["entradasMes"]))
        self.card_saidas.configure(text=formatarReal(resumo["saidasReaisMes"]))

        self.card_limite_total.configure(
            text=formatarReal(
                resumo["limiteTotal"]
            )
        )

        self.card_limite_disponivel.configure(
            text=formatarReal(
                resumo["limiteDisponivel"]
            )
        )

        self.card_compromissos.configure(
            text=formatarReal(
                resumo["gastosFixos"]
            )
        )

        self.card_compromissos