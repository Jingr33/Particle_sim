# importy
import customtkinter as ctk
from setpartframe import Frame as SPFrame

class SetPatrWindown(ctk.CTkToplevel):
    """Tvoří malé okénko při tvorbě nové částice."""
    def __init__(self, master: ctk.CTkBaseClass):
        super().__init__(master)
        self.grab_set()
        self.title('Nová částice')
        self.geometry('520x200')
        self.minsize(300, 200)
        self.load_setpart_gui()
        self.protocol('WM_DELETE_WINDOW', self._kill)

    def _kill(self):
        self.destroy()

    def load_setpart_gui(self) -> None:
        """Volá třídu pro vytvoření Framu uvnitř okna."""
        SPFrame(self).pack(fill=ctk.BOTH, ipadx=5, ipady=5, padx=3, pady=3)
