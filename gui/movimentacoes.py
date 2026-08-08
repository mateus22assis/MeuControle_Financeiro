import customtkinter as ctk


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

        # Área da futura listagem
        self.frame_lista = ctk.CTkFrame(
            self
        )

        self.frame_lista.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )