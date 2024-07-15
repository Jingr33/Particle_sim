import numpy as np
import math
import random
import configuration as C

class Conds:
    """Třída nahravá data ze souboru při zpuštění simulace a zpracovává je."""
    def __init__(self, file: str):
        # deklarace základních vlastností
        self.from_file = file
        self.num_of_parts = 0
        self.names = []
        self.numbers = []
        self.masses = []
        self.charges = []
        self.sigmas = []
        self.epsilons = []
        self.colour = []

        #zavolání metody, která nahraje data ze souboru a upraví je dle potřeby
        self.take_data()

        # uloží se počáteční souřadnice částic
        self.scoord = self.start_coord(self.num_of_parts)

    def take_data(self):
        """Nahraává data uložené v souboru."""
        # načtení dat ze souboru
        with open(self.from_file, 'r') as f:
            data = f.readlines()
        #kontrolní výpis
        print("data: \n")
        print(data)

        # odstranění nežádoucích řádků z dat 
        del data[0]
        del data[1]
        print(data)

        # rozdělení dat do jednotlivých polí/proměnných
        text_energy = data[0].split(" ")
        self.names = data[1].split(" ")
        text_numbers = data[2].split(" ")
        text_masses = data[3].split(" ")
        text_charges = data[4].split(" ")
        text_sigmas = data[5].split(" ")
        text_epsilons = data[6].split(" ")
        #kontrolní výpis
        print("\nDATA VE STRINGU")
        print(type(text_energy))
        print(text_energy)
        print(text_numbers)
        print(self.names)

        # okleštění přebytečných stringů
        self.energy = text_energy[0]
        del self.names[0]
        del self.names[-1:]
        for i in range(1, len(text_numbers)-1, 1):
            self.numbers.append(int(text_numbers[i]))
            self.masses.append(int(text_masses[i]))
            self.charges.append(int(text_charges[i]))
            self.sigmas.append(int(text_sigmas[i]))
            self.epsilons.append(int(text_epsilons[i]))

        # přiřazení barev částicím
        for i in range(0, len(self.names)):
            self.colour.append(C.colours[i])

        #kontrolní výpis
        print("_________________________")
        print(self.energy)
        print(self.names)
        print(self.numbers)
        print(self.masses)
        print(self.charges)
        print(self.sigmas)
        print(self.epsilons)
        print("__________________________")

        #####################################################
        # testovací parametry
        self.energy = 71.053 # je to v kJ/mol
        self.names = ["a1", "b2", "c3"]
        self.numbers = [6,7,8]
        self.masses = [10,20,30]
        self.charges = [0,0,0]
        self.sigmas = [3,3.5,4] # je to v angstremech
        self.epsilons = [1, 2, 1.5] # je to v kJ/mol

        #počet částic
        for number in self.numbers:
            self.num_of_parts += number
        #kontrolní výpis
        print(self.num_of_parts)

    def start_coord(self, num_of_part):
        """Metoda vypočítá list startovních souřadnic částic (umístí je do mřížky.)"""
        # velikost mřížky
        self.side = math.ceil(np.sqrt(num_of_part))

        #vytvoření souřadnic
        x_coord = []
        y_coord = []
        for column in range(0, self.side):
            for row in range(0, self.side):
                #vytvoření pole souřadnice
                new_x = C.box_size_x / (self.side + 1) * (column + 1)
                new_y = C.box_size_y / (self.side + 1) * (row + 1)
                # přidání do listu
                x_coord.append(new_x)
                y_coord.append(new_y)

                #odstranění přebytečných prvků
                del x_coord[num_of_part: len(x_coord)]
                del y_coord[num_of_part: len(y_coord)]

        # uložení do listu a vrácení
        s_coord = [x_coord, y_coord]
        return s_coord
    
    def get_num_of_parts(self):
        return self.num_of_parts
    
    def get_numbers(self):
        return self.numbers

    