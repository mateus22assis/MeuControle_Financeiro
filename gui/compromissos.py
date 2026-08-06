import customtkinter as ctk

class Compromissos(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.titulo = ctk.CTkLabel(self, text="Compromissos", font=("Arial", 24, "bold"))
        self.titulo.pack(pady=20)