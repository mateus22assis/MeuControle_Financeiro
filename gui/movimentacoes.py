from datetime import datetime
from tkinter import messagebox

import customtkinter as ctk

from gui.tema import (
    FUNDO_PRINCIPAL,
    CARD,
    CARD_INTERNO,
    BORDA,
    AZUL_PRINCIPAL,
    AZUL_HOVER,
    TEXTO_PRINCIPAL,
    TEXTO_SECUNDARIO,
    CAMPO_SELECAO,
)

from backend.excel_manager import (
    adicionarMovimentacao,
    adicionarMeses,
    anteciparParcelas,
    atualizarPlanilha,
    converterData,
    excluirMovimentacao,
    lerAbatimentosFaturas,
    registrarAbatimentoFatura,
)

from backend.calculos import gerarResumoFaturas

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
        self.frame_abatimento = None

        self.titulo = ctk.CTkLabel(
            self,
            text="Movimentacoes",
            font=("Arial", 24, "bold"),
            fg_color="transparent",
            text_color=TEXTO_PRINCIPAL
        )
        self.titulo.pack(pady=20)

        self.frame_controles = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.frame_controles.pack(
            fill="x",
            padx=20,
            pady=10
        )

        ctk.CTkButton(
            self.frame_controles,
            text="+ Adicionar movimentacao",
            command=self.abrir_formulario_adicao,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER
        ).pack(
            side="left",
            anchor="s",
            padx=(0, 8)
        )

        ctk.CTkButton(
            self.frame_controles,
            text="Excluir selecionada",
            command=self.excluir_selecionada,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER
        ).pack(
            side="left",
            anchor="s",
            padx=8
        )

        ctk.CTkButton(
            self.frame_controles,
            text="Antecipar parcelas selecionadas",
            command=self.antecipar_selecionadas,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER
        ).pack(
            side="left",
            anchor="s",
            padx=8
        )

        ctk.CTkButton(
            self.frame_controles,
            text="Abater fatura",
            command=self.abrir_abatimento_fatura,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER
        ).pack(
            side="left",
            anchor="s",
            padx=8
        )

        ctk.CTkLabel(
            self.frame_controles,
            text="Visualização:",
            text_color=TEXTO_SECUNDARIO
        ).pack(
            side="top",
            anchor="w",
            padx=(0, 2)
        )

        self.visualizacao = ctk.StringVar(
            value=self.PERIODO_PRINCIPAL
        )

        self.periodos_disponiveis = {
            self.PERIODO_PRINCIPAL: None
        }

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

        self.frame_lista = ctk.CTkScrollableFrame(
            self,
            fg_color=CARD
        )

        self.frame_lista.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.frame_lista.grid_columnconfigure(
            5,
            weight=1
        )

        self.mostrar_movimentacoes()

    # ==========================================================
    # MOVIMENTAÇÕES
    # ==========================================================

    def mostrar_movimentacoes(self):
        self.atualizar_periodos_disponiveis()
        self.atualizar_listagem()

    def atualizar_periodos_disponiveis(self):
        nomes_meses = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]

        periodo_atual = self.visualizacao.get()

        self.periodos_disponiveis = {
            self.PERIODO_PRINCIPAL: None
        }

        for mes, ano in mesesComMovimentacoes():
            nome = f"{nomes_meses[mes - 1]}/{ano}"
            self.periodos_disponiveis[nome] = (
                mes,
                ano
            )

        self.menu_visualizacao.configure(
            values=list(self.periodos_disponiveis)
        )

        if periodo_atual not in self.periodos_disponiveis:
            self.visualizacao.set(
                self.PERIODO_PRINCIPAL
            )

    def atualizar_listagem(self, escolha=None):
        self.selecoes = {}

        escolha = escolha or self.visualizacao.get()

        if escolha == self.PERIODO_PRINCIPAL:
            hoje = datetime.now()

            movimentacoes = movimentacoesPeriodoPrincipal(
                hoje.month,
                hoje.year
            )

        else:
            mes, ano = self.periodos_disponiveis[escolha]

            movimentacoes = movimentacoesMes(
                mes,
                ano
            )

        self.preencher_lista(
            self.frame_lista,
            movimentacoes,
            permitir_selecao=True,
        )

    def preencher_lista(
        self,
        frame,
        movimentacoes,
        permitir_selecao=False
    ):
        for widget in frame.winfo_children():
            widget.destroy()

        cabecalho = [
            "Data",
            "Natureza",
            "Meio",
            "Categoria",
            "Descricao",
            "Valor"
        ]

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
            ).grid(
                row=0,
                column=coluna,
                padx=10,
                pady=10,
                sticky="w"
            )

        movimentacoes_ordenadas = sorted(
            movimentacoes,
            key=lambda movimentacao:
                converterData(movimentacao["data"]),
        )

        for indice, movimentacao in enumerate(
            movimentacoes_ordenadas,
            start=1
        ):
            if permitir_selecao:
                linha_planilha = movimentacao["linha"]

                selecionada = ctk.BooleanVar(
                    value=False
                )

                self.selecoes[linha_planilha] = selecionada

                ctk.CTkCheckBox(
                    frame,
                    text="",
                    variable=selecionada,
                    width=24,
                    fg_color=AZUL_PRINCIPAL,
                    hover_color=AZUL_HOVER
                ).grid(
                    row=indice,
                    column=0,
                    padx=10,
                    pady=8
                )

            dados = [
                self.formatar_data(
                    movimentacao["data"]
                ),
                movimentacao["natureza"],
                movimentacao["meio"],
                movimentacao["categoria"],
                movimentacao["descricao"],
                formatarReal(
                    movimentacao["valor"] or 0
                ),
            ]

            for coluna, valor in enumerate(
                dados,
                start=coluna_inicial
            ):
                ctk.CTkLabel(
                    frame,
                    text=str(valor or ""),
                    anchor="w",
                    text_color=TEXTO_PRINCIPAL
                ).grid(
                    row=indice,
                    column=coluna,
                    padx=10,
                    pady=8,
                    sticky="w"
                )

    @staticmethod
    def formatar_data(data):
        if isinstance(data, datetime):
            return data.strftime("%d/%m/%Y")

        return data or ""

    def linhas_selecionadas(self):
        return [
            linha
            for linha, selecionada in self.selecoes.items()
            if selecionada.get()
        ]

    # ==========================================================
    # ABATER FATURA
    # ==========================================================

    def obter_fatura_aberta(self):
        """
        Obtém a fatura atualmente aberta e calcula
        quanto ainda está em aberto.

        Retorna:
            {
                "fatura": "09/2026",
                "vencimento": "10/09/2026",
                "valor": 500.0,
                "abatido": 100.0,
                "emAberto": 400.0
            }

        ou None quando não existe fatura aberta.
        """

        resumo_faturas = gerarResumoFaturas()
        abatimentos = lerAbatimentosFaturas()

        for fatura in resumo_faturas:

            if fatura["status"] != "Aberta":
                continue

            nome_fatura = fatura["fatura"]

            valor_previsto = float(
                fatura["valor"] or 0
            )

            valor_abatido = float(
                abatimentos.get(
                    nome_fatura,
                    0
                )
            )

            valor_em_aberto = (
                valor_previsto - valor_abatido
            )

            return {
                "fatura": nome_fatura,
                "vencimento": fatura["vencimento"],
                "valor": valor_previsto,
                "abatido": valor_abatido,
                "emAberto": max(
                    0,
                    valor_em_aberto
                )
            }

        return None

    def abrir_abatimento_fatura(self):

        if self.frame_abatimento is not None:
            self.frame_abatimento.lift()
            return

        fatura = self.obter_fatura_aberta()

        if fatura is None:
            messagebox.showinfo(
                "Abater fatura",
                "Não existe uma fatura aberta no momento.",
                parent=self
            )
            return

        if fatura["emAberto"] <= 0:
            messagebox.showinfo(
                "Abater fatura",
                "A fatura atual não possui valor em aberto.",
                parent=self
            )
            return

        # ======================================================
        # OVERLAY
        # ======================================================

        self.frame_abatimento = ctk.CTkFrame(
            self,
            width=420,
            height=390,
            corner_radius=12,
            border_width=1,
            border_color=BORDA,
            fg_color=CARD_INTERNO
        )

        self.frame_abatimento.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.frame_abatimento.pack_propagate(False)
        self.frame_abatimento.lift()

        # ======================================================
        # TÍTULO
        # ======================================================

        ctk.CTkLabel(
            self.frame_abatimento,
            text="Abater fatura",
            font=("Arial", 20, "bold"),
            text_color=TEXTO_PRINCIPAL
        ).pack(
            pady=(24, 18)
        )

        # ======================================================
        # INFORMAÇÕES DA FATURA
        # ======================================================

        informacoes = ctk.CTkFrame(
            self.frame_abatimento,
            fg_color=CARD,
            corner_radius=8
        )

        informacoes.pack(
            fill="x",
            padx=24,
            pady=(0, 18)
        )

        ctk.CTkLabel(
            informacoes,
            text=f"Fatura {fatura['fatura']}",
            font=("Arial", 15, "bold"),
            text_color=TEXTO_PRINCIPAL
        ).pack(
            anchor="w",
            padx=16,
            pady=(14, 2)
        )

        ctk.CTkLabel(
            informacoes,
            text=f"Vencimento: {fatura['vencimento']}",
            text_color=TEXTO_SECUNDARIO
        ).pack(
            anchor="w",
            padx=16,
            pady=(0, 2)
        )

        ctk.CTkLabel(
            informacoes,
            text=f"Em aberto: {formatarReal(fatura['emAberto'])}",
            font=("Arial", 15, "bold"),
            text_color=TEXTO_PRINCIPAL
        ).pack(
            anchor="w",
            padx=16,
            pady=(4, 14)
        )

        # ======================================================
        # CAMPO DO VALOR
        # ======================================================

        ctk.CTkLabel(
            self.frame_abatimento,
            text="Valor a abater",
            text_color=TEXTO_SECUNDARIO
        ).pack(
            anchor="w",
            padx=24
        )

        valor = ctk.CTkEntry(
            self.frame_abatimento,
            placeholder_text="R$ 0,00",
            fg_color=CARD,
            text_color=TEXTO_PRINCIPAL
        )

        valor.pack(
            fill="x",
            padx=24,
            pady=(6, 20)
        )

        valor.focus()

        # ======================================================
        # AÇÕES
        # ======================================================

        botoes = ctk.CTkFrame(
            self.frame_abatimento,
            fg_color="transparent"
        )

        botoes.pack(
            fill="x",
            padx=24,
            pady=(0, 20)
        )

        ctk.CTkButton(
            botoes,
            text="Cancelar",
            command=self.fechar_abatimento_fatura,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL
        ).pack(
            side="left",
            expand=True,
            padx=(0, 6)
        )

        ctk.CTkButton(
            botoes,
            text="Abater",
            command=lambda: confirmar_abatimento(),
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL
        ).pack(
            side="right",
            expand=True,
            padx=(6, 0)
        )

        def confirmar_abatimento():

            try:
                valor_informado = float(
                    valor.get()
                    .strip()
                    .replace("R$", "")
                    .replace(".", "")
                    .replace(",", ".")
                    .strip()
                )

            except ValueError:
                messagebox.showerror(
                    "Valor inválido",
                    "Informe um valor numérico válido.",
                    parent=self.frame_abatimento
                )
                return

            if valor_informado <= 0:
                messagebox.showerror(
                    "Valor inválido",
                    "O valor a abater deve ser maior que zero.",
                    parent=self.frame_abatimento
                )
                return

            if valor_informado > fatura["emAberto"]:
                messagebox.showerror(
                    "Valor inválido",
                    (
                        "O valor informado é maior que o "
                        f"valor em aberto ({formatarReal(fatura['emAberto'])})."
                    ),
                    parent=self.frame_abatimento
                )
                return

            sucesso = registrarAbatimentoFatura(
                valor_informado
            )

            if not sucesso:
                messagebox.showerror(
                    "Abater fatura",
                    "Não foi possível registrar o abatimento.",
                    parent=self.frame_abatimento
                )
                return

            self.fechar_abatimento_fatura()

            self.atualizar_tela()

            messagebox.showinfo(
                "Abater fatura",
                (
                    f"Abatimento de "
                    f"{formatarReal(valor_informado)} "
                    "registrado com sucesso."
                ),
                parent=self
            )

    def fechar_abatimento_fatura(self):

        if self.frame_abatimento is not None:
            self.frame_abatimento.destroy()
            self.frame_abatimento = None

    # ==========================================================
    # ADICIONAR MOVIMENTAÇÃO
    # ==========================================================

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

        self.frame_adicionar.place(
            relx=0.5,
            rely=0.55,
            anchor="center"
        )

        self.frame_adicionar.pack_propagate(False)
        self.frame_adicionar.lift()

        ctk.CTkLabel(
            self.frame_adicionar,
            text="Adicionar movimentacao",
            font=("Arial", 18, "bold"),
            text_color=TEXTO_PRINCIPAL,
            fg_color="transparent",
        ).pack(
            pady=(20, 4)
        )

        campos = ctk.CTkFrame(
            self.frame_adicionar,
            fg_color="transparent"
        )

        campos.pack(
            fill="both",
            expand=True,
            padx=24,
            pady=(8, 10)
        )

        natureza = ctk.StringVar(
            value="despesa"
        )

        meio = ctk.StringVar(
            value="pix"
        )

        categoria = ctk.StringVar()

        descricao = ctk.CTkEntry(
            campos,
            placeholder_text="Descricao",
            fg_color=CARD
        )

        valor = ctk.CTkEntry(
            campos,
            placeholder_text="Valor",
            fg_color=CARD
        )

        data = ctk.CTkEntry(
            campos,
            fg_color=CARD
        )

        data.insert(
            0,
            datetime.now().strftime("%d/%m/%Y")
        )

        campo_parcelas = ctk.CTkFrame(
            campos,
            fg_color="transparent"
        )

        quantidade_parcelas = ctk.CTkEntry(
            campo_parcelas,
            placeholder_text="Quantidade de parcelas",
            fg_color=CARD
        )

        quantidade_parcelas.pack(
            fill="x",
            pady=(0, 6)
        )

        menu_categoria = ctk.CTkOptionMenu(
            campos,
            variable=categoria,
            fg_color=CAMPO_SELECAO,
            button_color=AZUL_PRINCIPAL,
            button_hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL
        )

        def atualizar_categorias(
            natureza_escolhida=None
        ):
            categorias = listarCategoriasAtivasPorNatureza(
                natureza.get()
            )

            nomes = sorted(
                (
                    item["nome"]
                    for item in categorias
                ),
                key=str.casefold
            )

            if nomes:
                menu_categoria.configure(
                    values=nomes
                )
                categoria.set(nomes[0])

            else:
                menu_categoria.configure(
                    values=["Nenhuma categoria ativa"]
                )

                categoria.set(
                    "Nenhuma categoria ativa"
                )

        def atualizar_campo_parcelas(
            escolha=None
        ):
            if meio.get() == "credito":
                campo_parcelas.pack(
                    fill="x",
                    before=label_categoria
                )
            else:
                campo_parcelas.pack_forget()

        label_categoria = None

        for texto, widget in [
            (
                "Natureza",
                ctk.CTkOptionMenu(
                    campos,
                    variable=natureza,
                    values=[
                        "receita",
                        "despesa"
                    ],
                    command=atualizar_categorias,
                    fg_color=CAMPO_SELECAO,
                    button_color=AZUL_PRINCIPAL,
                    button_hover_color=AZUL_HOVER,
                    text_color=TEXTO_PRINCIPAL,
                )
            ),
            (
                "Meio/origem",
                ctk.CTkOptionMenu(
                    campos,
                    variable=meio,
                    values=[
                        "pix",
                        "debito",
                        "dinheiro",
                        "credito"
                    ],
                    command=atualizar_campo_parcelas,
                    fg_color=CAMPO_SELECAO,
                    button_color=AZUL_PRINCIPAL,
                    button_hover_color=AZUL_HOVER,
                    text_color=TEXTO_PRINCIPAL,
                )
            ),
            (
                "Categoria",
                menu_categoria
            ),
            (
                "Descricao",
                descricao
            ),
            (
                "Valor",
                valor
            ),
            (
                "Data",
                data
            ),
        ]:

            label = ctk.CTkLabel(
                campos,
                text=texto,
                text_color=TEXTO_SECUNDARIO
            )

            label.pack(
                anchor="w",
                pady=(6, 0)
            )

            if texto == "Categoria":
                label_categoria = label

            widget.pack(
                fill="x",
                pady=(0, 6)
            )

        atualizar_campo_parcelas()
        atualizar_categorias()

        def salvar():

            try:
                valor_informado = float(
                    valor.get()
                    .strip()
                    .replace(",", ".")
                )

                if valor_informado <= 0:
                    raise ValueError

                converterData(
                    data.get().strip()
                )

            except ValueError:
                messagebox.showerror(
                    "Dados invalidos",
                    (
                        "Informe valor positivo e data "
                        "no formato dd/mm/aaaa."
                    ),
                    parent=self.frame_adicionar
                )
                return

            if categoria.get() == "Nenhuma categoria ativa":
                messagebox.showerror(
                    "Dados invalidos",
                    (
                        "Cadastre uma categoria ativa "
                        "para a natureza selecionada."
                    ),
                    parent=self.frame_adicionar,
                )
                return

            if not descricao.get().strip():
                messagebox.showerror(
                    "Dados invalidos",
                    "Descricao e obrigatoria.",
                    parent=self.frame_adicionar
                )
                return

            if meio.get() == "credito":

                try:
                    total_parcelas = int(
                        quantidade_parcelas
                        .get()
                        .strip()
                    )

                    if total_parcelas < 1:
                        raise ValueError

                except ValueError:
                    messagebox.showerror(
                        "Dados invalidos",
                        (
                            "Informe uma quantidade de "
                            "parcelas maior que zero."
                        ),
                        parent=self.frame_adicionar,
                    )
                    return

                valor_parcela = round(
                    valor_informado / total_parcelas,
                    2
                )

                for parcela in range(
                    total_parcelas
                ):

                    numero_parcela = parcela + 1

                    adicionarMovimentacao(
                        natureza.get(),
                        meio.get(),
                        categoria.get(),
                        (
                            f"{descricao.get().strip()} "
                            f"({numero_parcela}/{total_parcelas})"
                        ),
                        valor_parcela,
                        f"{numero_parcela}/{total_parcelas}",
                        adicionarMeses(
                            data.get().strip(),
                            parcela
                        ),
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

        botoes = ctk.CTkFrame(
            self.frame_adicionar,
            fg_color="transparent"
        )

        botoes.pack(
            fill="x",
            padx=24,
            pady=(0, 20)
        )

        ctk.CTkButton(
            botoes,
            text="Cancelar",
            command=self.fechar_formulario_adicao,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL,
        ).pack(
            side="left",
            expand=True,
            padx=(0, 6)
        )

        ctk.CTkButton(
            botoes,
            text="Adicionar",
            command=salvar,
            fg_color=AZUL_PRINCIPAL,
            hover_color=AZUL_HOVER,
            text_color=TEXTO_PRINCIPAL,
        ).pack(
            side="right",
            expand=True,
            padx=(6, 0)
        )

    def fechar_formulario_adicao(self):

        if self.frame_adicionar is not None:
            self.frame_adicionar.destroy()
            self.frame_adicionar = None

    # ==========================================================
    # EXCLUSÃO
    # ==========================================================

    def excluir_selecionada(self):

        linhas = self.linhas_selecionadas()

        if len(linhas) != 1:
            messagebox.showwarning(
                "Selecao",
                (
                    "Selecione exatamente uma "
                    "movimentacao para excluir."
                ),
                parent=self
            )
            return

        if not messagebox.askyesno(
            "Confirmar exclusao",
            (
                "Deseja excluir a "
                "movimentacao selecionada?"
            ),
            parent=self
        ):
            return

        quantidade = excluirMovimentacao(
            linhas[0]
        )

        if quantidade:
            self.atualizar_tela()

            messagebox.showinfo(
                "Movimentacoes",
                (
                    f"{quantidade} movimentacao(oes) "
                    "removida(s)."
                ),
                parent=self
            )

        else:
            messagebox.showerror(
                "Movimentacoes",
                (
                    "Nao foi possivel excluir "
                    "a movimentacao."
                ),
                parent=self
            )

    # ==========================================================
    # ANTECIPAÇÃO
    # ==========================================================

    def antecipar_selecionadas(self):

        linhas = self.linhas_selecionadas()

        if not linhas:
            messagebox.showwarning(
                "Selecao",
                (
                    "Selecione uma ou mais parcelas "
                    "para antecipar."
                ),
                parent=self
            )
            return

        quantidade = anteciparParcelas(
            linhas
        )

        if quantidade:
            self.atualizar_tela()

            messagebox.showinfo(
                "Movimentacoes",
                (
                    f"{quantidade} parcela(s) "
                    "antecipada(s)."
                ),
                parent=self
            )

        else:
            messagebox.showwarning(
                "Movimentacoes",
                (
                    "As movimentacoes selecionadas "
                    "nao sao parcelas validas."
                ),
                parent=self
            )

    # ==========================================================
    # ATUALIZAÇÃO
    # ==========================================================

    def atualizar_tela(self):
        self.mostrar_movimentacoes()

        if self.ao_atualizar is not None:
            self.ao_atualizar()