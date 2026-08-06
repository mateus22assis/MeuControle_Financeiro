import customtkinter as ctk

class MenuLateral(ctk.CTkFrame):
    def __init__(self, parent, comandos):
        super().__init__(parent, fg_color="transparent")


        self.titulo = ctk.CTkLabel(self, text="Menu", font=("Arial", 14, "bold"))
        self.titulo.pack(pady=(15, 10))

        for texto, comando in comandos.items():
            self.criar_botao(texto, comando)
       

    def criar_botao(self, texto, comando):
        botao = ctk.CTkButton(self, text=texto, command=comando, height=30)
        botao.pack(pady=5, padx=10)