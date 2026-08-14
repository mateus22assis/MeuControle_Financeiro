import customtkinter as ctk

from backend.calculos import mostrarResumo
from backend.utils import formatarReal


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 24, "bold")
        )
        self.titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20, 10)
        )

        self.frame_comprometimento = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.frame_comprometimento.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=20,
            pady=10,
            sticky="ew"
        )

        self.frame_comprometimento.grid_columnconfigure(
            0,
            weight=1
        )

        self.card_comprometimento = self.criar_card(
            self.frame_comprometimento,
            "Pode comprometer na próxima fatura",
            0,
            0
        )

        self.titulo_cartao = ctk.CTkLabel(
            self,
            text="Cartão",
            font=("Arial", 18, "bold")
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

        self.frame_informacoes = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.frame_informacoes.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=20,
            pady=(15, 10),
            sticky="ew"
        )

        self.receita = ctk.CTkLabel(
            self.frame_informacoes,
            text="Receita do mês: R$ 0,00",
            font=("Arial", 14)
        )
        self.receita.pack(
            side="left",
            padx=10
        )

        self.compromissos = ctk.CTkLabel(
            self.frame_informacoes,
            text="Compromissos: R$ 0,00",
            font=("Arial", 14)
        )
        self.compromissos.pack(
            side="right",
            padx=10
        )

        self.atualizar_dados()

    def criar_card(self, parent, titulo, linha, coluna):

        card = ctk.CTkFrame(
            parent,
            corner_radius=10
        )
        card.grid(
            row=linha,
            column=coluna,
            padx=8,
            pady=8,
            sticky="nsew"
        )

        label_titulo = ctk.CTkLabel(
            card,
            text=titulo,
            font=("Arial", 14)
        )
        label_titulo.pack(
            pady=(15, 5)
        )

        label_valor = ctk.CTkLabel(
            card,
            text="R$ 0,00",
            font=("Arial", 22, "bold")
        )
        label_valor.pack(
            pady=(0, 15)
        )

        return label_valor

    def atualizar_dados(self):

        resumo = mostrarResumo()

        self.card_comprometimento.configure(
            text=formatarReal(
                resumo["capacidadeComprometimento"]
            )
        )

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

        self.receita.configure(
            text=(
                f"Receita do mês: "
                f"{formatarReal(resumo['receitaTotal'])}"
            )
        )

        self.compromissos.configure(
            text=(
                f"Compromissos: "
                f"{formatarReal(resumo['gastosFixos'])}"
            )
        )