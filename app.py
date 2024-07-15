# importy ctk a potřebných souborů
import customtkinter as ctk
from setframe import Frame as SetFrame
from animationframe import Frame as AniFrame

class App(ctk.CTk):
    """Třída pracující s hlavním oknem aplikace."""
    def __init__(self) -> None:
        """Inicializace hlavního kona aplikace."""
        super().__init__()
        self.title('Simulace částic')
        self.geometry('950x750')
        self.minsize(800, 600)
        self.load_main_gui()
#        self.init_variables() # tahle funkce ani není potřeba
        self.protocol('WM_DELETE_WINDOW', self._kill)
        self.sFrame
        self.aFrame
    
#    def init_variables(self):
        #self.entry_name = ctk.StringVar(self, 'default', 'entry_name')
        #self.entry_number = ctk.StringVar(self, 'default', 'entry_number')
        #self.entry_mass = ctk.StringVar(self, 'default', 'entry_mass')
        #self.entry_charge = ctk.StringVar(self, 'default', 'entry_charge')
        #self.entry_epsilon = ctk.StringVar(self, 'default', 'entry_epsilon')
        #self.entry_sigma = ctk.StringVar(self, 'default', 'entry_sigma')
        #self.entry_file = ctk.StringVar(self, 'default', 'entry_file')

    def _kill(self):
        self.destroy()

    def load_main_gui(self) -> None:
        """Funkce tvořící SetFrame a AnimationFrame uvnitř okna."""
        self.sFrame = SetFrame(self)
        self.sFrame.pack(side=ctk.LEFT, fill=ctk.Y, ipadx=5, ipady=5, padx=3, pady=3)
        self.aFrame = AniFrame(self, self.sFrame).pack(fill=ctk.BOTH, expand=True, padx=3, pady=3)
