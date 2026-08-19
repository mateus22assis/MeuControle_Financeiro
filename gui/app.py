import customtkinter as ctk
from gui.menu import MenuLateral
from gui.dashboard import Dashboard
from gui.movimentacoes import Movimentacoes
from gui.compromissos import Compromissos
from gui.categorias import Categorias
from gui.configuracoes import Configuracoes
from gui.resumo import ResumoFinanceiro
from gui.tema import (FUNDO_PRINCIPAL, MENU_LATERAL, TEXTO_PRINCIPAL)

#backend imports
from backend.calculos import mostrarResumo




ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.configure(fg_color=FUNDO_PRINCIPAL)

        self.title("meu controle financeiro")
        self.geometry("1200x750")
        
        self.minsize(1000, 600)
        self.resizable(True, True)

        self.overlay_configuracoes = None  # Variável para armazenar a referência da janela de configurações


#configura o grid da janela
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

#frame principal
        self.frame_principal = ctk.CTkFrame(self, fg_color=FUNDO_PRINCIPAL)
        self.frame_principal.grid(row=0, column=0, sticky="nsew")

#configura o grid do frame principal
        self.frame_principal.grid_rowconfigure(0, weight=1)

        self.frame_principal.grid_columnconfigure(0, weight=0,  minsize=260)
        self.frame_principal.grid_columnconfigure(1, weight=1)


        # Barra lateral
        self.barra_lateral = ctk.CTkFrame(self.frame_principal, fg_color=MENU_LATERAL)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")

        self.barra_lateral.grid_propagate(False)  # Impede que a barra lateral se expanda automaticamente

        # Configura o grid da barra lateral
        self.barra_lateral.grid_rowconfigure(0, weight=1)
        self.barra_lateral.grid_rowconfigure(1, weight=5)
        self.barra_lateral.grid_columnconfigure(0, weight=1)

        # Frame do menu
        self.frame_menu = ctk.CTkFrame(self.barra_lateral, fg_color="transparent")
        self.frame_menu.grid(row=0, column=0, sticky="nsew")

        # Menu
        self.menu = MenuLateral(self.frame_menu, {
            "Dashboard": self.mostrar_dashboard,
            "Movimentações": self.mostrar_movimentacoes,
            "Compromissos": self.mostrar_compromissos,
            "Categorias": self.mostrar_categorias,
            "Configurações": self.abrir_configuracoes
        })

        self.menu.pack(fill="both", expand=True)

        # Frame do resumo 
        self.frame_resumo = ResumoFinanceiro(self.barra_lateral, )
        self.frame_resumo.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


        self.atualizar_resumo()

#frame conteudo
        self.frame_conteudo = ctk.CTkFrame(self.frame_principal, fg_color=FUNDO_PRINCIPAL)
        self.frame_conteudo.grid(row=0, column=1, sticky="nsew")

        self.mostrar_dashboard()  # Exibe o dashboard por padrão

    def mostrar_dashboard(self):
        self.limpar_frame_conteudo()

        dashboard = Dashboard(self.frame_conteudo)
        dashboard.pack(expand=True, fill="both")

    def mostrar_movimentacoes(self):
        self.limpar_frame_conteudo()

        
        movimentacoes = Movimentacoes(
            self.frame_conteudo,
            ao_atualizar=self.atualizar_resumo,
            
        )
        movimentacoes.pack(expand=True, fill="both")
    
    def mostrar_compromissos(self):
        self.limpar_frame_conteudo()

        compromissos = Compromissos(self.frame_conteudo)
        compromissos.pack(expand=True, fill="both")

    def mostrar_categorias(self):
        self.limpar_frame_conteudo()

        categorias = Categorias(self.frame_conteudo)
        categorias.pack(expand=True, fill="both")

    def abrir_configuracoes(self):

        if self.overlay_configuracoes is not None:
            return

        self.overlay_configuracoes = ctk.CTkFrame(self.frame_conteudo, fg_color= FUNDO_PRINCIPAL)

        self.overlay_configuracoes.place(relx=0, rely=0, relwidth=1, relheight=1)

        frame_configuracoes = ctk.CTkFrame(
            self.overlay_configuracoes,
            width=500,
            height=600
        )

        frame_configuracoes.place(relx=0.5, rely=0.5, anchor="center")  

        frame_configuracoes.pack_propagate(False)  # Impede que o frame se ajuste automaticamente ao conteúdo

        configuracoes = Configuracoes(frame_configuracoes)
        configuracoes.pack(expand=True, fill="both")

        botao_fechar = ctk.CTkButton(
            self.overlay_configuracoes,
            text="X",
            width = 35,
            command=self.fechar_configuracoes
        )

        botao_fechar.place(relx=1, x=-15, y=15, anchor="ne")

        

    def fechar_configuracoes(self):
        if self.overlay_configuracoes is not None:
            self.overlay_configuracoes.destroy()
            self.overlay_configuracoes = None


    def limpar_frame_conteudo(self):
        if self.overlay_configuracoes is not None:
            self.fechar_configuracoes()

        for widget in self.frame_conteudo.winfo_children():
            if widget is not self.overlay_configuracoes:
                widget.destroy()

    def atualizar_resumo(self):
        resumo = mostrarResumo()
        self.frame_resumo.atualizar_valores(
            resumo['saldoDisponivel'],
            resumo['valorGuardar'],
            resumo['faturaProximoMes'],
            resumo['capacidadeComprometimento']
        )

  





