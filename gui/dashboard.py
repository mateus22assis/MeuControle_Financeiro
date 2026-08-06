import customtkinter as ctk


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.titulo = ctk.CTkLabel(self, text="Dashboard", font=("Arial", 24, "bold"))
        self.titulo.pack(pady=20)

        self.frame_cards = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_cards.pack(fill="x", padx=20, pady=20)

