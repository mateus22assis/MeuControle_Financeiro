import customtkinter as ctk
from gui.menu import MenuLateral
from gui.dashboard import Dashboard
from gui.movimentacoes import Movimentacoes
from gui.compromissos import Compromissos
from gui.categorias import Categorias
from gui.configuracoes import Configuracoes
from gui.resumo import ResumoFinanceiro

#backend imports
from backend.calculos import mostrarResumo


ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("meu controle financeiro")
        self.geometry("1200x700")
        
        self.minsize(1000, 600)
        self.resizable(True, True)


#configura o grid da janela
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

#frame principal
        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.grid(row=0, column=0, sticky="nsew")

#configura o grid do frame principal
        self.frame_principal.grid_rowconfigure(0, weight=1)

        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_columnconfigure(1, weight=3)


        # Barra lateral
        self.barra_lateral = ctk.CTkFrame(self.frame_principal)
        self.barra_lateral.grid(row=0, column=0, sticky="nsew")

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
            "Configurações": self.mostrar_configuracoes
        })

        self.menu.pack(fill="both", expand=True)

        # Frame do resumo 
        self.frame_resumo = ResumoFinanceiro(self.barra_lateral, )
        self.frame_resumo.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


        self.atualizar_resumo()

#frame conteudo
        self.frame_conteudo = ctk.CTkFrame(self.frame_principal, fg_color="gray75")
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
            ao_atualizar=self.atualizar_resumo
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

    def mostrar_configuracoes(self):
        self.limpar_frame_conteudo()

        configuracoes = Configuracoes(self.frame_conteudo)
        configuracoes.pack(expand=True, fill="both")

    def limpar_frame_conteudo(self):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()

    def atualizar_resumo(self):
        resumo = mostrarResumo()
        self.frame_resumo.atualizar_valores(
            resumo['saldoDisponivel'],
            resumo['valorGuardar'],
            resumo['faturaProximoMes'],
            resumo['capacidadeComprometimento']
        )

  





