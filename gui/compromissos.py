import customtkinter as ctk
from tkinter import messagebox

from backend.excel_manager import (
    adicionarCompromissoMensal,
    alterarCompromissoMensal,
    excluirCompromissoMensal,
    lerCompromissosMensais,
)
from backend.utils import formatarReal

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


class Compromissos(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=FUNDO_PRINCIPAL
        )

        self.selecao = None
        self.compromissos = []

        # ==========================
        # CONFIGURAÇÃO DO GRID
        # ==========================

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(2, weight=1)

        # ==========================
        # TÍTULO PRINCIPAL
        # ==========================

        self.titulo = ctk.CTkLabel(
            self,
            text="Compromissos",
            font=("Arial", 24, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        self.titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20, 10)
        )

        # ==========================
        # TÍTULO DA LISTA
        # ==========================

        self.titulo_lista = ctk.CTkLabel(
            self,
            text="Compromissos cadastrados",
            font=("Arial", 16, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        self.titulo_lista.grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=(5, 8),
            sticky="w"
        )

        # ==========================
        # TÍTULO DO FORMULÁRIO
        # ==========================

        self.titulo_formulario = ctk.CTkLabel(
            self,
            text="Gerenciar compromisso",
            font=("Arial", 16, "bold"),
            text_color=TEXTO_PRINCIPAL
        )
        self.titulo_formulario.grid(
            row=1,
            column=1,
            padx=(10, 20),
            pady=(5, 8),
            sticky="w"
        )

        # ==========================
        # LISTA DE COMPROMISSOS
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

        # ==========================
        # FORMULÁRIO
        # ==========================

        self.frame_formulario = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=12,
            border_width=1,
            border_color=BORDA
        )
        self.frame_formulario.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=(0, 20)
        )

        self.frame_formulario.grid_columnconfigure(
            0,
            weight=1
        )

        # ==========================
        # CAMPO DESCRIÇÃO
        # ==========================

        self.campo_descricao = ctk.CTkEntry(
            self.frame_formulario,
            placeholder_text="Descrição",
            height=38,
            font=("Arial", 13),
            border_color=BORDA,
            fg_color=CARD_INTERNO,
            text_color=TEXTO_PRINCIPAL,
        )
        self.campo_descricao.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(25, 10)
        )

        # ==========================
        # CAMPO VALOR
        # ==========================

        self.campo_valor = ctk.CTkEntry(
            self.frame_formulario,
            placeholder_text="Valor",
            height=38,
            font=("Arial", 13),
            border_color=BORDA,
            fg_color=CARD_INTERNO,
            text_color=TEXTO_PRINCIPAL,
        )
        self.campo_valor.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        # ==========================
        # BOTÃO ADICIONAR
        # ==========================

        self.botao_adicionar = ctk.CTkButton(
            self.frame_formulario,
            text="Adicionar",
            command=self.adicionar_compromisso
        )
        self.botao_adicionar.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 8)
        )

        # ==========================
        # BOTÃO ALTERAR
        # ==========================

        self.botao_alterar = ctk.CTkButton(
            self.frame_formulario,
            text="Alterar selecionado",
            command=self.alterar_selecionado
        )
        self.botao_alterar.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=20,
            pady=8
        )

        # ==========================
        # BOTÃO EXCLUIR
        # ==========================

        self.botao_excluir = ctk.CTkButton(
            self.frame_formulario,
            text="Excluir selecionado",
            command=self.excluir_selecionado
        )
        self.botao_excluir.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=20,
            pady=8
        )

        self.mostrar_compromissos()

    # ==========================
    # MOSTRAR COMPROMISSOS
    # ==========================

    def mostrar_compromissos(self):

        for widget in self.frame_lista.winfo_children():
            widget.destroy()

        self.selecao = None

        self.compromissos = lerCompromissosMensais()

        cabecalho = [
            "Compromisso",
            "Valor"
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

        for indice, compromisso in enumerate(
            self.compromissos,
            start=1
        ):

            botao_linha = ctk.CTkButton(
                self.frame_lista,
                text=compromisso["descricao"],
                anchor="w",
                fg_color="transparent",
                text_color=("black", "white"),
                hover_color=("gray85", "gray25"),
                command=lambda compromisso=compromisso:
                self.selecionar_compromisso(compromisso)
            )

            botao_linha.grid(
                row=indice,
                column=0,
                padx=10,
                pady=5,
                sticky="ew"
            )

            ctk.CTkLabel(
                self.frame_lista,
                text=formatarReal(compromisso["valor"]),
                anchor="w",
                text_color=TEXTO_PRINCIPAL
            ).grid(
                row=indice,
                column=1,
                padx=20,
                pady=8,
                sticky="w"
            )

    # ==========================
    # SELECIONAR COMPROMISSO
    # ==========================

    def selecionar_compromisso(self, compromisso):

        if self.selecao is compromisso:
            self.limpar_formulario()
            return

        self.selecao = compromisso

        self.campo_descricao.delete(
            0,
            "end"
        )

        self.campo_descricao.insert(
            0,
            compromisso["descricao"]
        )

        self.campo_valor.delete(
            0,
            "end"
        )

        self.campo_valor.insert(
            0,
            str(compromisso["valor"])
        )

    # ==========================
    # ADICIONAR
    # ==========================

    def adicionar_compromisso(self):

        descricao = self.campo_descricao.get().strip()

        try:
            valor = float(
                self.campo_valor.get()
                .strip()
                .replace(",", ".")
            )

            if valor <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Dados inválidos",
                "Informe um valor maior que zero.",
                parent=self
            )

            return

        if not descricao:

            messagebox.showerror(
                "Dados inválidos",
                "Informe a descrição do compromisso.",
                parent=self
            )

            return

        adicionarCompromissoMensal(
            descricao,
            valor
        )

        self.limpar_formulario()
        self.mostrar_compromissos()

    # ==========================
    # ALTERAR
    # ==========================

    def alterar_selecionado(self):

        if self.selecao is None:

            messagebox.showwarning(
                "Seleção",
                "Selecione um compromisso para alterar.",
                parent=self
            )

            return

        descricao = self.campo_descricao.get().strip()

        try:
            valor = float(
                self.campo_valor.get()
                .strip()
                .replace(",", ".")
            )

            if valor <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Dados inválidos",
                "Informe um valor maior que zero.",
                parent=self
            )

            return

        if not descricao:

            messagebox.showerror(
                "Dados inválidos",
                "Informe a descrição do compromisso.",
                parent=self
            )

            return

        alterado = alterarCompromissoMensal(
            self.selecao["linha"],
            descricao,
            valor
        )

        if not alterado:

            messagebox.showerror(
                "Erro",
                "Não foi possível alterar o compromisso.",
                parent=self
            )

            return

        self.limpar_formulario()
        self.mostrar_compromissos()

    # ==========================
    # EXCLUIR
    # ==========================

    def excluir_selecionado(self):

        if self.selecao is None:

            messagebox.showwarning(
                "Seleção",
                "Selecione um compromisso para excluir.",
                parent=self
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            "Deseja excluir o compromisso selecionado?",
            parent=self
        )

        if not confirmar:
            return

        excluido = excluirCompromissoMensal(
            self.selecao["linha"]
        )

        if not excluido:

            messagebox.showerror(
                "Erro",
                "Não foi possível excluir o compromisso.",
                parent=self
            )

            return

        self.limpar_formulario()
        self.mostrar_compromissos()

    # ==========================
    # LIMPAR FORMULÁRIO
    # ==========================

    def limpar_formulario(self):

        self.selecao = None

        self.campo_descricao.delete(
            0,
            "end"
        )

        self.campo_valor.delete(
            0,
            "end"
        )