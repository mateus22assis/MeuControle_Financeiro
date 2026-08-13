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


class Configuracoes(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)

        self.titulo = ctk.CTkLabel(
            self,
            text="Configurações",
            font=("Arial", 24, "bold")
        )
        self.titulo.grid(
            row=0,
            column=0,
            pady=20
        )

        self.frame_formulario = ctk.CTkFrame(self)
        self.frame_formulario.grid(
            row=1,
            column=0,
            padx=40,
            pady=10,
            sticky="n"
        )

        self.frame_formulario.grid_columnconfigure(0, weight=1)

        self.campo_receita = self.criar_campo(
            "Receita mensal",
            0
        )

        self.campo_reserva = self.criar_campo(
            "Percentual de reserva",
            1
        )

        self.campo_limite = self.criar_campo(
            "Limite do cartão",
            2
        )

        self.campo_fechamento = self.criar_campo(
            "Dia de fechamento",
            3
        )

        self.campo_vencimento = self.criar_campo(
            "Dia de vencimento",
            4
        )

        self.botao_salvar = ctk.CTkButton(
            self.frame_formulario,
            text="Salvar configurações",
            command=self.salvar_configuracoes
        )
        self.botao_salvar.grid(
            row=10,
            column=0,
            padx=20,
            pady=20,
            sticky="ew"
        )

        self.carregar_configuracoes()

    def criar_campo(self, texto, linha):

        ctk.CTkLabel(
            self.frame_formulario,
            text=texto,
            anchor="w"
        ).grid(
            row=linha * 2,
            column=0,
            padx=20,
            pady=(12, 4),
            sticky="w"
        )

        campo = ctk.CTkEntry(
            self.frame_formulario
        )
        campo.grid(
            row=linha * 2 + 1,
            column=0,
            padx=20,
            pady=(0, 6),
            sticky="ew"
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