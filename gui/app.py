import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"

class App(ctk.Ctk):
    def __init__(self):
        super().__init__()

        self.title("meu controle financeiro")
        self.geometry("1200x700")
        
        self.minsize(1000, 600)
        self.resizable(True, True)

        self.frame_principal = ctk.CTkFrame(self)
        self.frame_principal.pack(fill="both", expand=True)

app = App()

app.mainloop()



