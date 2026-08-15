from datetime import datetime
from tkinter import messagebox

from gui.tema import (FUNDO_PRINCIPAL, CARD, CARD_INTERNO, BORDA, AZUL_PRINCIPAL, AZUL_HOVER, TEXTO_PRINCIPAL, TEXTO_SECUNDARIO, CAMPO_SELECAO)

import customtkinter as ctk

from backend.excel_manager import (
    adicionarMovimentacao,
    adicionarMeses,
    anteciparParcelas,
    atualizarPlanilha,
    converterData,
    excluirMovimentacao,
)
from backend.consultas import (
    listarCategoriasAtivasPorNatureza,
    mesesComMovimentacoes,
    movimentacoesMes,
    movimentacoesPeriodoPrincipal,
)
from backend.utils import formatarReal


class Movimentacoes(ctk.CTkFrame):

    PERIODO_PRINCIPAL = "Período principal"

    def __init__(self, parent, ao_atualizar=None):
        super().__init__(parent, fg_color=FUNDO_PRINCIPAL)

        self.ao_atualizar = ao_atualizar
        self.selecoes = {}
        self.frame_adicionar = None

        self.titulo = ctk.CTkLabel(
            self,
            text="Movimentacoes",
            font=("Arial", 24, "bold"),
            fg_color="transparent",
            text_color=TEXTO_PRINCIPAL
            
        )
        self.titulo.pack(pady=20)

        self.frame_controles = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_controles.pack(fill="x", padx=20, pady=10)

        ctk.CTkButton(
            self.frame_controles,
            text="+ Adicionar movimentacao",
            command=self.abrir_formulario_adicao,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER
          
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            self.frame_controles,
            text="Excluir selecionada",
            command=self.excluir_selecionada,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER
          
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            self.frame_controles,
            text="Antecipar parcelas selecionadas",
            command=self.antecipar_selecionadas,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER
            
        ).pack(side="left", padx=8)

        ctk.CTkLabel(
            self.frame_controles,
            text="Visualização:",
            text_color=TEXTO_SECUNDARIO
            
        ).pack(side="left", padx=(20, 8))

        self.visualizacao = ctk.StringVar(value=self.PERIODO_PRINCIPAL)
        self.periodos_disponiveis = {self.PERIODO_PRINCIPAL: None}
        self.menu_visualizacao = ctk.CTkOptionMenu(
            self.frame_controles,
            variable=self.visualizacao,
            values=[self.PERIODO_PRINCIPAL],
            command=self.atualizar_listagem,
            fg_color=CARD,
            button_color=AZUL_PRINCIPAL,
            button_hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL
          
        )
        self.menu_visualizacao.pack(side="left")

        self.frame_lista = ctk.CTkScrollableFrame(self, fg_color=CARD)
        self.frame_lista.pack(fill="both", expand=True, padx=20, pady=10)
        self.frame_lista.grid_columnconfigure(5, weight=1)

        self.mostrar_movimentacoes()

    def mostrar_movimentacoes(self):
        self.atualizar_periodos_disponiveis()
        self.atualizar_listagem()

    def atualizar_periodos_disponiveis(self):
        nomes_meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",
        ]
        periodo_atual = self.visualizacao.get()
        self.periodos_disponiveis = {self.PERIODO_PRINCIPAL: None}

        for mes, ano in mesesComMovimentacoes():
            nome = f"{nomes_meses[mes - 1]}/{ano}"
            self.periodos_disponiveis[nome] = (mes, ano)

        self.menu_visualizacao.configure(values=list(self.periodos_disponiveis))

        if periodo_atual not in self.periodos_disponiveis:
            self.visualizacao.set(self.PERIODO_PRINCIPAL)

    def atualizar_listagem(self, escolha=None):
        self.selecoes = {}
        escolha = escolha or self.visualizacao.get()

        if escolha == self.PERIODO_PRINCIPAL:
            hoje = datetime.now()
            movimentacoes = movimentacoesPeriodoPrincipal(hoje.month, hoje.year)
        else:
            mes, ano = self.periodos_disponiveis[escolha]
            movimentacoes = movimentacoesMes(mes, ano)

        self.preencher_lista(
            self.frame_lista,
            movimentacoes,
            permitir_selecao=True,
        )

    def preencher_lista(self, frame, movimentacoes, permitir_selecao=False):
        for widget in frame.winfo_children():
            widget.destroy()

        cabecalho = ["Data", "Natureza", "Meio", "Categoria", "Descricao", "Valor"]
        coluna_inicial = 0

        if permitir_selecao:
            cabecalho.insert(0, "")
            coluna_inicial = 1

        for coluna, texto in enumerate(cabecalho):
            ctk.CTkLabel(
                frame,
                text=texto,
                font=("Arial", 14, "bold"),
                text_color=TEXTO_SECUNDARIO
            ).grid(row=0, column=coluna, padx=10, pady=10, sticky="w")

        movimentacoes_ordenadas = sorted(
            movimentacoes,
            key=lambda movimentacao: converterData(movimentacao["data"]),
        )

        for indice, movimentacao in enumerate(movimentacoes_ordenadas, start=1):
            if permitir_selecao:
                linha_planilha = movimentacao["linha"]
                selecionada = ctk.BooleanVar(value=False)
                self.selecoes[linha_planilha] = selecionada

                ctk.CTkCheckBox(
                    frame,
                    text="",
                    variable=selecionada,
                    width=24,
                    fg_color=AZUL_PRINCIPAL,
                    hover_color=AZUL_HOVER
                ).grid(row=indice, column=0, padx=10, pady=8)

            dados = [
                self.formatar_data(movimentacao["data"]),
                movimentacao["natureza"],
                movimentacao["meio"],
                movimentacao["categoria"],
                movimentacao["descricao"],
                formatarReal(movimentacao["valor"] or 0),
            ]

            for coluna, valor in enumerate(dados, start=coluna_inicial):
                ctk.CTkLabel(
                    frame,
                    text=str(valor or ""),
                    anchor="w",
                    text_color=TEXTO_PRINCIPAL
                ).grid(row=indice, column=coluna, padx=10, pady=8, sticky="w")

    @staticmethod
    def formatar_data(data):
        if isinstance(data, datetime):
            return data.strftime("%d/%m/%Y")
        return data or ""

    def linhas_selecionadas(self):
        return [linha for linha, selecionada in self.selecoes.items() if selecionada.get()]

    def abrir_formulario_adicao(self):
        if self.frame_adicionar is not None:
            self.frame_adicionar.lift()
            return

        self.frame_adicionar = ctk.CTkFrame(
            self,
            width=450,
            height=550,
            corner_radius=10,
            fg_color=CARD_INTERNO
        )
        self.frame_adicionar.place(relx=0.5, rely=0.55, anchor="center")
        self.frame_adicionar.pack_propagate(False)
        self.frame_adicionar.lift()

        ctk.CTkLabel(
            self.frame_adicionar,
            text="Adicionar movimentacao",
            font=("Arial", 18, "bold"),
            text_color=TEXTO_PRINCIPAL,
            fg_color="transparent",
        ).pack(pady=(20, 4))

        campos = ctk.CTkFrame(self.frame_adicionar, fg_color="transparent")
        campos.pack(fill="both", expand=True, padx=24, pady=(8, 10))

        natureza = ctk.StringVar(value="despesa")
        meio = ctk.StringVar(value="pix")
        categoria = ctk.StringVar()
        descricao = ctk.CTkEntry(campos, placeholder_text="Descricao", fg_color=CARD)
        valor = ctk.CTkEntry(campos, placeholder_text="Valor", fg_color=CARD)
        data = ctk.CTkEntry(campos, fg_color=CARD)
        data.insert(0, datetime.now().strftime("%d/%m/%Y"))
        campo_parcelas = ctk.CTkFrame(campos, fg_color="transparent")
        quantidade_parcelas = ctk.CTkEntry(campo_parcelas, placeholder_text="Quantidade de parcelas", fg_color=CARD)
        quantidade_parcelas.pack(fill="x", pady=(0, 6))

        menu_categoria = ctk.CTkOptionMenu(campos, variable=categoria, fg_color=CAMPO_SELECAO, button_color=AZUL_PRINCIPAL, button_hover_color=AZUL_HOVER, text_color=TEXTO_PRINCIPAL )

        def atualizar_categorias(natureza_escolhida=None):
            categorias = listarCategoriasAtivasPorNatureza(natureza.get())
            nomes = [item["nome"] for item in categorias]

            if nomes:
                menu_categoria.configure(values=nomes)
                categoria.set(nomes[0])
            else:
                menu_categoria.configure(values=["Nenhuma categoria ativa"])
                categoria.set("Nenhuma categoria ativa")

        def atualizar_campo_parcelas(escolha=None):
            if meio.get() == "credito":
                campo_parcelas.pack(fill="x", before=label_categoria)
            else:
                campo_parcelas.pack_forget()

        label_categoria = None
        for texto, widget in [
            ("Natureza", ctk.CTkOptionMenu(
                campos,
                variable=natureza,
                values=["receita", "despesa"],
                command=atualizar_categorias,
                fg_color=CAMPO_SELECAO,
                button_color=AZUL_PRINCIPAL,
                button_hover_color=AZUL_HOVER,
                text_color=TEXTO_PRINCIPAL,
            )),
            ("Meio/origem", ctk.CTkOptionMenu(
                campos,
                variable=meio,
                values=["pix", "debito", "dinheiro", "credito"],
                command=atualizar_campo_parcelas,
                fg_color=CAMPO_SELECAO,
                button_color=AZUL_PRINCIPAL,
                button_hover_color=AZUL_HOVER,
                text_color=TEXTO_PRINCIPAL,
            )),
            ("Categoria", menu_categoria),
            ("Descricao", descricao),
            ("Valor", valor),
            ("Data", data),

        ]:
            label = ctk.CTkLabel(campos, text=texto, text_color=TEXTO_SECUNDARIO)
            label.pack(anchor="w", pady=(6, 0))
            if texto == "Categoria":
                label_categoria = label
            widget.pack(fill="x", pady=(0, 6))

        atualizar_campo_parcelas()
        atualizar_categorias()

        def salvar():
            try:
                valor_informado = float(valor.get().strip().replace(",", "."))
                if valor_informado <= 0:
                    raise ValueError
                converterData(data.get().strip())
            except ValueError:
                messagebox.showerror("Dados invalidos", "Informe valor positivo e data no formato dd/mm/aaaa.", parent=self.frame_adicionar)
                return

            if categoria.get() == "Nenhuma categoria ativa":
                messagebox.showerror(
                    "Dados invalidos",
                    "Cadastre uma categoria ativa para a natureza selecionada.",
                    parent=self.frame_adicionar,
                )
                return

            if not descricao.get().strip():
                messagebox.showerror("Dados invalidos", "Descricao e obrigatoria.", parent=self.frame_adicionar)
                return

            if meio.get() == "credito":
                try:
                    total_parcelas = int(quantidade_parcelas.get().strip())
                    if total_parcelas < 1:
                        raise ValueError
                except ValueError:
                    messagebox.showerror(
                        "Dados invalidos",
                        "Informe uma quantidade de parcelas maior que zero.",
                        parent=self.frame_adicionar,
                    )
                    return

                valor_parcela = round(valor_informado / total_parcelas, 2)

                for parcela in range(total_parcelas):
                    numero_parcela = parcela + 1
                    adicionarMovimentacao(
                        natureza.get(),
                        meio.get(),
                        categoria.get(),
                        f"{descricao.get().strip()} ({numero_parcela}/{total_parcelas})",
                        valor_parcela,
                        f"{numero_parcela}/{total_parcelas}",
                        adicionarMeses(data.get().strip(), parcela),
                    )
            else:
                adicionarMovimentacao(
                    natureza.get(),
                    meio.get(),
                    categoria.get(),
                    descricao.get().strip(),
                    valor_informado,
                    "",
                    data.get().strip(),
                )
            atualizarPlanilha()
            self.fechar_formulario_adicao()
            self.atualizar_tela()

        botoes = ctk.CTkFrame(self.frame_adicionar, fg_color="transparent")
        botoes.pack(fill="x", padx=24, pady=(0, 20))

        ctk.CTkButton(
            botoes,
            text="Cancelar",
            command=self.fechar_formulario_adicao,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL,
        ).pack(side="left", expand=True, padx=(0, 6))

        ctk.CTkButton(
            botoes,
            text="Adicionar",
            command=salvar,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL,
        ).pack(side="right", expand=True, padx=(6, 0))

    def fechar_formulario_adicao(self):
        if self.frame_adicionar is not None:
            self.frame_adicionar.destroy()
            self.frame_adicionar = None

    def excluir_selecionada(self):
        linhas = self.linhas_selecionadas()
        if len(linhas) != 1:
            messagebox.showwarning("Selecao", "Selecione exatamente uma movimentacao para excluir.", parent=self)
            return

        if not messagebox.askyesno("Confirmar exclusao", "Deseja excluir a movimentacao selecionada?", parent=self):
            return

        quantidade = excluirMovimentacao(linhas[0])
        if quantidade:
            self.atualizar_tela()
            messagebox.showinfo("Movimentacoes", f"{quantidade} movimentacao(oes) removida(s).", parent=self)
        else:
            messagebox.showerror("Movimentacoes", "Nao foi possivel excluir a movimentacao.", parent=self)

    def antecipar_selecionadas(self):
        linhas = self.linhas_selecionadas()
        if not linhas:
            messagebox.showwarning("Selecao", "Selecione uma ou mais parcelas para antecipar.", parent=self)
            return

        quantidade = anteciparParcelas(linhas)
        if quantidade:
            self.atualizar_tela()
            messagebox.showinfo("Movimentacoes", f"{quantidade} parcela(s) antecipada(s).", parent=self)
        else:
            messagebox.showwarning("Movimentacoes", "As movimentacoes selecionadas nao sao parcelas validas.", parent=self)

    def atualizar_tela(self):
        self.mostrar_movimentacoes()
        if self.ao_atualizar is not None:
            self.ao_atualizar()
