import customtkinter as ctk
from tkinter import messagebox

from backend.excel_manager import (
    lerConfiguracoes,
    salvarReceitaMensal,
    salvarPercentualReserva,
    salvarLimiteCartao,
    salvarDiaFechamento,
    salvarDiaVencimento,
)

from gui.tema import (
    FUNDO_PRINCIPAL,
    CARD,
    CARD_INTERNO,
    BORDA,
    AZUL_PRINCIPAL,
    AZUL_HOVER,
    TEXTO_PRINCIPAL,
    TEXTO_SECUNDARIO,
)


class Configuracoes(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=FUNDO_PRINCIPAL
        )

        self.grid_columnconfigure(0, weight=1)

        # ======================================================
        # TÍTULO
        # ======================================================

        self.titulo = ctk.CTkLabel(
            self,
            text="Configurações",
            font=("Arial", 24, "bold"),
            text_color=TEXTO_PRINCIPAL,
        )
        self.titulo.grid(
            row=0,
            column=0,
            padx=20,
            pady=(24, 4),
        )

        self.subtitulo = ctk.CTkLabel(
            self,
            text="Configure os valores utilizados nos cálculos financeiros.",
            font=("Arial", 13),
            text_color=TEXTO_SECUNDARIO,
        )
        self.subtitulo.grid(
            row=1,
            column=0,
            padx=20,
            pady=(0, 20),
        )

        # ======================================================
        # CARD PRINCIPAL
        # ======================================================

        self.frame_formulario = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=12,
            border_width=1,
            border_color=BORDA,
        )

        self.frame_formulario.grid(
            row=2,
            column=0,
            padx=30,
            pady=10,
            sticky="ew",
        )

        self.frame_formulario.grid_columnconfigure(0, weight=1)
        self.frame_formulario.grid_columnconfigure(1, weight=1)
        self.frame_formulario.grid_columnconfigure(2, weight=1)

        # ======================================================
        # SEÇÃO FINANCEIRA
        # ======================================================

        ctk.CTkLabel(
            self.frame_formulario,
            text="Financeiro",
            font=("Arial", 17, "bold"),
            text_color=TEXTO_PRINCIPAL,
        ).grid(
            row=0,
            column=0,
            columnspan=3,
            padx=24,
            pady=(22, 2),
            sticky="w",
        )

        ctk.CTkLabel(
            self.frame_formulario,
            text="Valores utilizados para calcular seu saldo disponível.",
            font=("Arial", 12),
            text_color=TEXTO_SECUNDARIO,
        ).grid(
            row=1,
            column=0,
            columnspan=3,
            padx=24,
            pady=(0, 14),
            sticky="w",
        )

        self.campo_receita = self.criar_campo(
            "Receita mensal",
            2,
            0
        )

        self.campo_reserva = self.criar_campo(
            "Percentual de reserva",
            2,
            1
        )

        # ======================================================
        # SEÇÃO CARTÃO
        # ======================================================

        ctk.CTkLabel(
            self.frame_formulario,
            text="Cartão de crédito",
            font=("Arial", 17, "bold"),
            text_color=TEXTO_PRINCIPAL,
        ).grid(
            row=5,
            column=0,
            columnspan=3,
            padx=24,
            pady=(22, 2),
            sticky="w",
        )

        ctk.CTkLabel(
            self.frame_formulario,
            text="Configure os dados utilizados no controle das faturas.",
            font=("Arial", 12),
            text_color=TEXTO_SECUNDARIO,
        ).grid(
            row=6,
            column=0,
            columnspan=3,
            padx=24,
            pady=(0, 14),
            sticky="w",
        )

        self.campo_limite = self.criar_campo(
            "Limite do cartão",
            7,
            0
        )

        self.campo_fechamento = self.criar_campo(
            "Dia de fechamento",
            7,
            1
        )

        self.campo_vencimento = self.criar_campo(
            "Dia de vencimento",
            7,
            2
        )

        # ======================================================
        # BOTÃO
        # ======================================================

        self.botao_salvar = ctk.CTkButton(
            self.frame_formulario,
            text="Salvar configurações",
            command=self.salvar_configuracoes,
            height=42,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL,
            font=("Arial", 13, "bold"),
        )

        self.botao_salvar.grid(
            row=9,
            column=0,
            columnspan=3,
            padx=24,
            pady=(22, 24),
            sticky="ew",
        )

        self.carregar_configuracoes()

    def criar_campo(self, texto, linha, coluna):

        ctk.CTkLabel(
            self.frame_formulario,
            text=texto,
            font=("Arial", 13),
            text_color=TEXTO_SECUNDARIO,
            anchor="center",
        ).grid(
            row=linha,
            column=coluna,
            padx=10,
            pady=(4, 5),
            sticky="ew",
        )

        campo = ctk.CTkEntry(
            self.frame_formulario,
            height=38,
            fg_color=CARD_INTERNO,
            border_color=BORDA,
            text_color=TEXTO_PRINCIPAL,
            font=("Arial", 13),
        )

        campo.grid(
            row=linha + 1,
            column=coluna,
            padx=10,
            pady=(0, 4),
            sticky="ew",
        )

        return campo

    def carregar_configuracoes(self):

        configuracoes = lerConfiguracoes()

        self.campo_receita.insert(
            0,
            str(configuracoes["receitaMensal"])
        )

        self.campo_reserva.insert(
            0,
            str(configuracoes["percentualReserva"])
        )

        self.campo_limite.insert(
            0,
            str(configuracoes["limiteCartao"])
        )

        self.campo_fechamento.insert(
            0,
            str(configuracoes["diaFechamento"])
        )

        self.campo_vencimento.insert(
            0,
            str(configuracoes["diaVencimento"])
        )

    def salvar_configuracoes(self):

        try:
            receita = float(
                self.campo_receita.get()
                .strip()
                .replace(",", ".")
            )

            percentual = float(
                self.campo_reserva.get()
                .strip()
                .replace(",", ".")
            )

            limite = float(
                self.campo_limite.get()
                .strip()
                .replace(",", ".")
            )

            fechamento = int(
                self.campo_fechamento.get().strip()
            )

            vencimento = int(
                self.campo_vencimento.get().strip()
            )

        except ValueError:
            messagebox.showerror(
                "Dados inválidos",
                "Verifique os valores informados.",
                parent=self
            )
            return

        if receita < 0:
            messagebox.showerror(
                "Dados inválidos",
                "A receita mensal não pode ser negativa.",
                parent=self
            )
            return

        if percentual < 0 or percentual > 100:
            messagebox.showerror(
                "Dados inválidos",
                "O percentual de reserva deve estar entre 0 e 100.",
                parent=self
            )
            return

        if limite < 0:
            messagebox.showerror(
                "Dados inválidos",
                "O limite do cartão não pode ser negativo.",
                parent=self
            )
            return

        if fechamento < 1 or fechamento > 31:
            messagebox.showerror(
                "Dados inválidos",
                "O dia de fechamento deve estar entre 1 e 31.",
                parent=self
            )
            return

        if vencimento < 1 or vencimento > 31:
            messagebox.showerror(
                "Dados inválidos",
                "O dia de vencimento deve estar entre 1 e 31.",
                parent=self
            )
            return

        salvarReceitaMensal(receita)
        salvarPercentualReserva(percentual)
        salvarLimiteCartao(limite)
        salvarDiaFechamento(fechamento)
        salvarDiaVencimento(vencimento)

        messagebox.showinfo(
            "Configurações",
            "Configurações salvas com sucesso.",
            parent=self
        )