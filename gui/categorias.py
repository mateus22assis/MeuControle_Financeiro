import customtkinter as ctk

class Categorias(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.titulo = ctk.CTkLabel(self, text="Categorias", font=("Arial", 24, "bold"))
        self.titulo.pack(pady=20)