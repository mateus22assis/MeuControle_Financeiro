import customtkinter as ctk

from backend.excel_manager import (
    adicionarCategoria,
    alterarStatusCategoria,
    lerCategorias,
)

from gui.tema import (
    FUNDO_PRINCIPAL,
    CARD,
    CAMPO_SELECAO,
    CARD_INTERNO,
    BORDA,
    AZUL_HOVER,
    AZUL_PRINCIPAL,
    TEXTO_DISCRETO,
    TEXTO_PRINCIPAL,
    TEXTO_SECUNDARIO,
)


class Categorias(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=FUNDO_PRINCIPAL
        )

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(2, weight=1)

        # ==========================
        # TÍTULO
        # ==========================

        self.titulo = ctk.CTkLabel(
            self,
            text="Categorias",
            font=("Arial", 24, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        self.titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        # ==========================
        # TÍTULO DA LISTA
        # ==========================

        self.titulo_lista = ctk.CTkLabel(
            self,
            text="Categorias cadastradas",
            font=("Arial", 16, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        self.titulo_lista.grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=(5, 5),
            sticky="w"
        )

        # ==========================
        # TÍTULO DO FORMULÁRIO
        # ==========================

        self.titulo_adicionar = ctk.CTkLabel(
            self,
            text="Adicionar categoria",
            font=("Arial", 16, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        self.titulo_adicionar.grid(
            row=1,
            column=1,
            padx=(10, 20),
            pady=(5, 5),
            sticky="w"
        )

        # ==========================
        # LISTA DE CATEGORIAS
        # ==========================

        self.frame_lista = ctk.CTkScrollableFrame(
            self,
            fg_color=CARD,
            corner_radius=12,
            border_width=1,
            border_color=BORDA
        )
        self.frame_lista.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=(0, 20)
        )

        self.frame_lista.grid_columnconfigure(
            0,
            weight=2
        )
        self.frame_lista.grid_columnconfigure(
            1,
            weight=1
        )
        self.frame_lista.grid_columnconfigure(
            2,
            weight=1
        )

        # ==========================
        # FORMULÁRIO
        # ==========================

        self.frame_adicionar = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=12,
            border_width=1,
            border_color=BORDA
        )
        self.frame_adicionar.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=(0, 20)
        )

        self.frame_adicionar.grid_columnconfigure(
            0,
            weight=1
        )

        self.campo_nome = ctk.CTkEntry(
            self.frame_adicionar,
            placeholder_text="Nome da categoria",
            height=38,
            font=("Arial", 13),
            border_color=BORDA,
            fg_color=CARD_INTERNO,
            text_color=TEXTO_PRINCIPAL
        )
        self.campo_nome.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(25, 10)
        )

        self.natureza = ctk.StringVar(
            value="Despesa"
        )

        self.campo_natureza = ctk.CTkOptionMenu(
            self.frame_adicionar,
            variable=self.natureza,
            values=[
                "Receita",
                "Despesa"
            ],
            height=38,
            font=("Arial", 13),
            fg_color=CARD_INTERNO,
            button_color=AZUL_PRINCIPAL,
            button_hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL
        )
        self.campo_natureza.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        self.botao_adicionar = ctk.CTkButton(
            self.frame_adicionar,
            text="Adicionar categoria",
            command=self.adicionar_categoria,
            height=38,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER
        )
        self.botao_adicionar.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 8)
        )

        self.mostrar_categorias()

    # ==========================
    # LISTAR CATEGORIAS
    # ==========================

    def mostrar_categorias(self):

        for widget in self.frame_lista.winfo_children():
            widget.destroy()

        cabecalho = [
            "Nome",
            "Natureza",
            "Ativa"
        ]

        for coluna, texto in enumerate(cabecalho):

            ctk.CTkLabel(
                self.frame_lista,
                text=texto,
                font=("Arial", 13, "bold"),
                text_color=TEXTO_SECUNDARIO
            ).grid(
                row=0,
                column=coluna,
                padx=20,
                pady=(12, 8),
                sticky="w"
            )

        categorias = lerCategorias()

        for indice, categoria in enumerate(
            categorias,
            start=1
        ):

            ctk.CTkLabel(
                self.frame_lista,
                text=categoria["nome"],
                anchor="w",
                text_color=TEXTO_PRINCIPAL
            ).grid(
                row=indice,
                column=0,
                padx=20,
                pady=8,
                sticky="w"
            )

            ctk.CTkLabel(
                self.frame_lista,
                text=categoria["natureza"],
                anchor="w",
                text_color=TEXTO_PRINCIPAL
            ).grid(
                row=indice,
                column=1,
                padx=20,
                pady=8,
                sticky="w"
            )

            ativo = ctk.BooleanVar(
                value=categoria["ativa"]
            )

            ctk.CTkCheckBox(
                self.frame_lista,
                text="",
                variable=ativo,
                command=lambda
                categoria=categoria,
                ativo=ativo:
                self.alterar_status_categoria(
                    categoria,
                    ativo
                ),
                fg_color=AZUL_PRINCIPAL,
                hover_color=AZUL_HOVER,
                border_color=BORDA
            ).grid(
                row=indice,
                column=2,
                padx=20,
                pady=8,
                sticky="w"
            )

    # ==========================
    # ALTERAR STATUS
    # ==========================

    def alterar_status_categoria(
        self,
        categoria,
        ativo
    ):

        alterarStatusCategoria(
            categoria["nome"],
            categoria["natureza"],
            ativo.get()
        )

    # ==========================
    # ADICIONAR CATEGORIA
    # ==========================

    def adicionar_categoria(self):

        nome = self.campo_nome.get().strip()
        natureza = self.natureza.get()

        if not nome:
            return

        adicionarCategoria(
            nome,
            natureza
        )

        self.campo_nome.delete(
            0,
            "end"
        )

        self.mostrar_categorias()