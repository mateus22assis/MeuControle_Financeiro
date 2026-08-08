import customtkinter as ctk

from backend.excel_manager import lerMovimentacoes


class Movimentacoes(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.titulo = ctk.CTkLabel(
            self,
            text="Movimentações",
            font=("Arial", 24, "bold")
        )

        self.titulo.pack(pady=20)

        # Área dos controles
        self.frame_controles = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.frame_controles.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.botao_adicionar = ctk.CTkButton(
            self.frame_controles,
            text="+ Adicionar movimentação"
        )

        self.botao_adicionar.pack(
            side="left"
        )

        # Área da listagem
        self.frame_lista = ctk.CTkScrollableFrame(
            self
        )

        self.frame_lista.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.mostrar_movimentacoes()

    def mostrar_movimentacoes(self):

        movimentacoes = lerMovimentacoes()

        # Cabeçalho
        cabecalho = [
            "Data",
            "Natureza",
            "Meio",
            "Categoria",
            "Descrição",
            "Valor"
        ]

        for coluna, texto in enumerate(cabecalho):
            label = ctk.CTkLabel(
                self.frame_lista,
                text=texto,
                font=("Arial", 14, "bold")
            )

            label.grid(
                row=0,
                column=coluna,
                padx=10,
                pady=10,
                sticky="w"
            )

        # Movimentações
        for linha, movimentacao in enumerate(
            movimentacoes,
            start=1
        ):

            dados = [
                movimentacao["data"],
                movimentacao["natureza"],
                movimentacao["meio"],
                movimentacao["categoria"],
                movimentacao["descricao"],
                movimentacao["valor"]
            ]

            for coluna, valor in enumerate(dados):

                label = ctk.CTkLabel(
                    self.frame_lista,
                    text=str(valor or "")
                )

                label.grid(
                    row=linha,
                    column=coluna,
                    padx=10,
                    pady=8,
                    sticky="w"
                )