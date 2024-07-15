# importy
import customtkinter as ctk
import tkinter as tk

class Frame(ctk.CTkFrame):
    """Tvoří Frame v okně s nastavením parametrů nových částic."""
    def __init__(self, master: ctk.CTkBaseClass):
        super().__init__(master)
        #list dat
        self.data = []
        # tvorba mřížky
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        # textové proměnné
        self.var_name = ctk.StringVar()
        self.var_number = ctk.StringVar()
        self.var_mass = ctk.StringVar()
        self.var_charge = ctk.StringVar()
        self.var_sigma = ctk.StringVar()
        self.var_epsilon = ctk.StringVar()

        self.gui() # tvorba grafiky

    def gui(self):
        """Metoda pro vytvoření widgetů ve Framu."""
        Label(self, 'Název částice').grid(column=0, row=0, sticky=ctk.E)
        Entry(self, self.var_name).grid(column=1, row=0)
        Label(self, 'Počet částic').grid(column=2, row=0, sticky=ctk.E)
        Entry(self, self.var_number).grid(column=3, row=0)
        Label(self, 'Hmotnost').grid(column=0, row=1, sticky=ctk.E)
        Entry(self, self.var_mass).grid(column=1, row=1)
        Label(self, 'Náboj').grid(column=2, row=1, sticky=ctk.E)
        Entry(self, self.var_charge).grid(column=3, row=1)
        Label(self, 'Sigma').grid(column=0, row=2, sticky=ctk.E)
        Entry(self, self.var_sigma).grid(column=1, row=2)
        Label(self, 'Epsilon').grid(column=2, row=2, sticky=ctk.E)
        Entry(self, self.var_epsilon).grid(column=3, row=2)

        button = Button(self, 'Uložit', self.button_click).grid(column=2, row=3, columnspan=2, pady=10)
    
    def button_click(self):
        """Funkce uloží data do souboru při kliknutí na tlačítko uložit."""
        # přenesení proměnných StringVar do stringů
        self.text_name = self.var_name.get()
        self.text_number = self.var_number.get()
        self.text_mass = self.var_mass.get()
        self.text_charge = self.var_charge.get()
        self.text_sigma = self.var_sigma.get()
        self.text_epsilon = self.var_epsilon.get()
        #vytvoření lsitu dat
        part_data = [self.text_name, self.text_number, self.text_mass, self.text_charge, self.text_sigma, self.text_epsilon]
        # přidání do listu dat s informacemi o všech částicích
        self.data.append(part_data)

        #kontrolní výpisy
        print(self.var_name.get())
        print(self.var_number.get())
        print(self.var_mass.get())
        print(self.var_charge.get())
        print(self.var_sigma.get())
        print(self.var_epsilon.get())

        # zavolání metody, která data uloží do souboru
        self.save_to_file()

    def save_to_file(self):
        """Metoda ukládající data do souboru."""
        text = [self.var_name.get() + " \n",self.var_number.get() + " \n" ,self.var_mass.get() + " \n" ,self.var_charge.get() + " \n" ,self.var_sigma.get() + " \n" ,self.var_epsilon.get() + " \n", ""]
        with open("_file.txt", "a") as f:
            f.writelines(text)

    def get_data(self):
        return self.data


class Label(ctk.CTkLabel):
    """Třída pro tvorbu ctk.Label"""
    def __init__(self, master:ctk.CTkBaseClass, text: str):
        super().__init__(master)
        self.configure(text=text)

class Entry(ctk.CTkEntry):
    """Třída pro tvorbu ctk.Entry"""
    def __init__(self, master:ctk.CTkBaseClass, value):
        super().__init__(master)
        self.configure(textvariable = value)
    
class Button(ctk.CTkButton):
    """Třída pro tvorbu ctk.Button"""
    def __init__(self, master:ctk.CTkBaseClass, text :str, command):
        super().__init__(master)
        self.configure(text=text, command = command)
        


