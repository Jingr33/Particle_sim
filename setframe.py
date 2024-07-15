# import ctk a potřebných souborů
import customtkinter as ctk
from tkinter import *
from setpartwin import SetPatrWindown as SPW
from setpartframe import Frame as SPFrame
from conditions import Conds
from conditions import *

class Frame(ctk.CTkFrame):
    """Třída vytvářející Frame s nastavením simulace v levé části okna"""
    def __init__(self, master:ctk.CTkBaseClass) -> None:
        super().__init__(master)
        self.bind('<FocusIn>', self.part_label)      

        # deklarace StringVar porměnných pro získání dat z ctk.Entry
        self.var_energy = ctk.StringVar()
        self.var_from_file = ctk.StringVar()
        self.var_to_file = ctk.StringVar()
        # definice polí pro zapisování do souborů
        self.names = ''
        self.numbers = ''
        self.masses = ''
        self.charges = ''
        self.sigmas = ''
        self.epsilons = ''
        self.karel = 2525
        self.conds_numbers = []

        # zavolání metody, která vytvoří grafické rozhraní SetFramu
        self.gui()
        #kontrolní výpis
        print(self.start_sim)

    def gui(self):
        """Metoda pro  vyrobu widgetů v SetFramu"""
        # skupina widgetů pro název souboru, do kterého se mají parametry uložit
        Label(self, 'Ukládat do souboru:').pack(anchor=ctk.W, padx=5, pady=10)
        Entry(self, self.var_to_file).pack()

        # nastavení energie
        Label(self, 'Energie').pack(anchor=ctk.W, padx=5, pady=10)
        Entry(self, self.var_energy).pack()

        # přidání nové částice
        Label(self, 'Částice').pack(anchor=ctk.W, padx=5, pady=20)
        Button(self, 'Přidat novou částici', self.open_window).pack()

        # skupina widgetů pro nahrání simulace ze souboru a souštění simulace
        self.start_sim = Button(self, 'Spustit simulaci', self.start_sim_click)
        self.start_sim.pack(side=ctk.BOTTOM, padx=10, pady=10, ipadx=10, ipady=10)
        Entry(self, self.var_from_file).pack(side=ctk.BOTTOM, pady=5)        
        Label(self, 'Načíst ze souboru:').pack(anchor=ctk.W, side=ctk.BOTTOM, padx=5, pady=3)


    def open_window(self) -> None:
        """Metoda pro spuštění menšího okna s nastavením parametrů nové částice."""
        SPW(self)

    def start_sim_click(self) -> None:
        """Metoda pro zapsaní dat do souboru a zavolání funkce Conds, která zpracovává vstupní data při spuštění simulace."""
        # definice textových proměnných zadaných uživatelem
        self.text_energy = self.var_energy.get()
        self.from_file = self.var_from_file.get() + ".txt"
        self.to_file = self.var_to_file.get() + ".txt"
        # kontrolní výpisy
        print(self.var_energy.get())
        print(self.to_file)

        # výběr souboru ze kterého se načtou parametry simulace Conds
        # a zároveň aby fungovalo načítání souborů
        if self.from_file == '.txt':
            self.from_file = self.to_file
            self.from_to_file()
            
        # zavolání conds
        self.conds = Conds(self.from_file)
        self.conds_numbers = self.conds.numbers
        #kontrolní výpis
        print("conds_numbers", self.conds_numbers)
        print("TOHLE JE ONO")

    def from_to_file(self):
        """Přepsání dat z interního souboru do souboru pro uživatele."""
        #přečte se soubor z malého okna (okna tvorby částice)
        file_content = []
        f = open('_file.txt', 'r')
        file_content = f.readlines()
        f = open('_file.txt', 'w')
        f.write('')
        # kontrolní výpis
        print(file_content)

        # vymazání nepotřebných znaků ze stringů
        for i in range(0, len(file_content), 1):
            line = file_content[i]
            index = len(line)
            file_content[i] = line[0:index-2]
        # kontrolní výpis
        print(file_content)

        # zapsání do polí pro jednotlivé vlastnosti
        for i in range(0, len(file_content), 6):
            self.names += file_content[i] + " "
            self.numbers += file_content[i+1] + " "
            self.masses += file_content[i+2] + " "
            self.charges += file_content[i+3] + " "
            self.sigmas += file_content[i+4] + " "
            self.epsilons += file_content[i+5] + " "
        # kontrolní výpis
        print("self.names: " + self.names)

        #zápis informací do souboru (veřejného)
        print("self.to_file" + self.to_file)
        with open(self.to_file, 'w') as f:
            f.write("ENERGIE SOUSTAVY:\n")
            f.write(self.text_energy + " \n")
            f.write("PARAMETRY ČÁSTIC:\n")
            f.write("jména: " + self.names + "\n")
            f.write("počty: " + self.numbers + "\n")
            f.write("hmotnosti: " + self.masses + "\n")
            f.write("náboje: " + self.charges + "\n")
            f.write("sigmy: " + self.sigmas + "\n")
            f.write("epsilony: " + self.epsilons + "\n")

    def part_label(self):
        """Funkce pro ty labely."""
        print("part_label")

class Label(ctk.CTkLabel):
    """Třída pro tvorbu ctk.Label"""
    def __init__(self, master: ctk.CTkBaseClass, name: str):
        super().__init__(master)
        self.configure(text=name)

class Entry(ctk.CTkEntry):
    """Třída pro tvorbu ctk.Entry"""
    def __init__(self, master: ctk.CTkBaseClass, value):
        super().__init__(master)
        self.configure(textvariable = value)

class Button(ctk.CTkButton):
    """Třída pro tvorbu ctk.Button"""
    def __init__(self, master: ctk.CTkBaseClass, text: str, command):
        super().__init__(master)
        self.configure(text=text, command=command)

