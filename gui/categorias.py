import customtkinter as ctk

from backend.excel_manager import (
    adicionarCategoria,
    alterarStatusCategoria,
    lerCategorias,
)


class Categorias(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.titulo = ctk.CTkLabel(
            self,
            text="Categorias",
            font=("Arial", 24, "bold")
        )
        self.titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        # ==========================
        # LISTA DE CATEGORIAS
        # ==========================

        self.frame_lista = ctk.CTkScrollableFrame(
            self,
            label_text="Categorias cadastradas"
        )
        self.frame_lista.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=(0, 20)
        )

        self.frame_lista.grid_columnconfigure(0, weight=2)
        self.frame_lista.grid_columnconfigure(1, weight=1)
        self.frame_lista.grid_columnconfigure(2, weight=1)

        # ==========================
        # FORMULÁRIO
        # ==========================

        self.frame_adicionar = ctk.CTkFrame(self)
        self.frame_adicionar.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=(0, 20)
        )

        self.frame_adicionar.grid_columnconfigure(0, weight=1)

        self.titulo_adicionar = ctk.CTkLabel(
            self.frame_adicionar,
            text="Adicionar categoria",
            font=("Arial", 18, "bold")
        )
        self.titulo_adicionar.grid(
            row=0,
            column=0,
            padx=20,
            pady=(25, 20)
        )

        self.campo_nome = ctk.CTkEntry(
            self.frame_adicionar,
            placeholder_text="Nome da categoria"
        )
        self.campo_nome.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        self.natureza = ctk.StringVar(value="Despesa")

        self.campo_natureza = ctk.CTkOptionMenu(
            self.frame_adicionar,
            variable=self.natureza,
            values=["Receita", "Despesa"]
        )
        self.campo_natureza.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        self.botao_adicionar = ctk.CTkButton(
            self.frame_adicionar,
            text="Adicionar categoria",
            command=self.adicionar_categoria
        )
        self.botao_adicionar.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=20,
            pady=20
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
                font=("Arial", 14, "bold")
            ).grid(
                row=0,
                column=coluna,
                padx=20,
                pady=10,
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
                anchor="w"
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
                anchor="w"
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
                )
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

        self.campo_nome.delete(0, "end")

        self.mostrar_categorias()