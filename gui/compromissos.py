import customtkinter as ctk
from tkinter import messagebox

from backend.excel_manager import (
    adicionarCompromissoMensal,
    alterarCompromissoMensal,
    excluirCompromissoMensal,
    lerCompromissosMensais,
)
from backend.utils import formatarReal


class Compromissos(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.selecao = None
        self.compromissos = []

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.titulo = ctk.CTkLabel(
            self,
            text="Compromissos",
            font=("Arial", 24, "bold")
        )
        self.titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        self.frame_lista = ctk.CTkScrollableFrame(
            self,
            label_text="Compromissos cadastrados"
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

        self.frame_formulario = ctk.CTkFrame(self)
        self.frame_formulario.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=(0, 20)
        )

        self.frame_formulario.grid_columnconfigure(0, weight=1)

        self.titulo_formulario = ctk.CTkLabel(
            self.frame_formulario,
            text="Gerenciar compromisso",
            font=("Arial", 18, "bold")
        )
        self.titulo_formulario.grid(
            row=0,
            column=0,
            padx=20,
            pady=(25, 20)
        )

        self.campo_descricao = ctk.CTkEntry(
            self.frame_formulario,
            placeholder_text="Descrição"
        )
        self.campo_descricao.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        self.campo_valor = ctk.CTkEntry(
            self.frame_formulario,
            placeholder_text="Valor"
        )
        self.campo_valor.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=10
        )

        self.botao_adicionar = ctk.CTkButton(
            self.frame_formulario,
            text="Adicionar",
            command=self.adicionar_compromisso
        )
        self.botao_adicionar.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 8)
        )

        self.botao_alterar = ctk.CTkButton(
            self.frame_formulario,
            text="Alterar selecionado",
            command=self.alterar_selecionado
        )
        self.botao_alterar.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=20,
            pady=8
        )

        self.botao_excluir = ctk.CTkButton(
            self.frame_formulario,
            text="Excluir selecionado",
            command=self.excluir_selecionado
        )
        self.botao_excluir.grid(
            row=5,
            column=0,
            sticky="ew",
            padx=20,
            pady=8
        )

        self.mostrar_compromissos()

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
                font=("Arial", 14, "bold")
            ).grid(
                row=0,
                column=coluna,
                padx=20,
                pady=10,
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
                command=lambda
                compromisso=compromisso:
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
                anchor="w"
            ).grid(
                row=indice,
                column=1,
                padx=20,
                pady=8,
                sticky="w"
            )

    def selecionar_compromisso(self, compromisso):

        self.selecao = compromisso

        self.campo_descricao.delete(0, "end")
        self.campo_descricao.insert(
            0,
            compromisso["descricao"]
        )

        self.campo_valor.delete(0, "end")
        self.campo_valor.insert(
            0,
            str(compromisso["valor"])
        )

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

    def limpar_formulario(self):

        self.selecao = None

        self.campo_descricao.delete(0, "end")
        self.campo_valor.delete(0, "end")