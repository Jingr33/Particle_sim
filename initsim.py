from particle import Particle
from setframe import Frame as SetFrame
import numpy as np
import random
import time

class Init_sim():
    def __init__(self, setframe: SetFrame):
        # inicializace proměnných
        self.setframe = setframe
        self.num_of_parts = self.setframe.conds.num_of_parts
        self.xc = self.setframe.conds.scoord[0]
        self.yc = self.setframe.conds.scoord[1]
        self.sigmas = self.setframe.conds.sigmas
        self.epsilons = self.setframe.conds.epsilons
        self.masses = self.setframe.conds.masses
        self.numbers = self.setframe.conds.numbers
        self.energy = self.setframe.conds.energy
        self.particles = []

        self.make_particles()

        # kontrolní výpisy
        print(self.potenc_energy(), ' potencialE')
        print(self.kinetic_energy(), ' kinetic')
        print(self.velocity_magnitude(), ' velocity_mag')
        print(self.start_vectors(), ' start vectors')
        
        self.append_vectors()

    def potenc_energy(self):
        """Metoda počítá potenciální energii každé částice"""
        potenc = 0.0
        for i in range(self.num_of_parts):
            sigma_i = self.sigmas[self.particles[i].type]
            epsilon_i = self.epsilons[self.particles[i].type]
            print(sigma_i, 'sigmai', epsilon_i, ' epsiloni')
            for j in range(i + 1, self.num_of_parts):
                 #výpočet vzdálenosti částic
                r = np.sqrt(np.power(self.xc[j] - self.xc[i], 2) + np.power(self.yc[j] - self.yc[i], 2))
                sigma_j = self.sigmas[self.particles[j].type]
                epsilon_j = self.epsilons[self.particles[j].type]

                sigma_ave = (sigma_i + sigma_j) / 2
                epsilon_ave = np.sqrt(epsilon_i*epsilon_j)

                vLJ = 4*epsilon_ave*(np.power(sigma_ave/r, 12) - np.power(sigma_ave/r, 6))
                potenc += vLJ
        return potenc

    def start_vectors(self):
        """Metoda vypočítá list počátečních vektorů."""
        # pole vektorů
        s_vectors = []
        vel_mag_list = self.velocity_magnitude()
        for index in range(len(self.numbers)):
            for i in range(self.numbers[index]):
                # geneování směru vektoru
                direction = random.random()*2*np.pi
                x_velocity = vel_mag_list[index] * np.cos(direction)
                y_velocity = vel_mag_list[index] * np.sin(direction)
                s_vector = np.array([x_velocity, y_velocity])
                s_vectors.append(s_vector)
        return s_vectors
    
    def min_energy(self):
        """Metoda počítá minimalizaci energie. PS: zatím nepočítá nic :D"""
        return self.potenc_energy()

    def kinetic_energy(self):
        """Metoda počítá kinetickou energii soustavy."""
        kin_e = self.energy - self.min_energy()
        return kin_e

    def velocity_magnitude(self):   
        """
        Metoda pro výpočet počáteční velikosti rychlosti pro jednotlivé hmotnosti částic.
        [v(per part) = A / ps]
        """
        # kinetická energie na jednu částici
        kinetic_per_part = self.kinetic_energy() / self.num_of_parts
        # pole kinetických energií pro každou hmotnost částice
        vel_mag_list = []
        for i in range(len(self.masses)):
            # přidá do pole rychlost čátice o dané hmotnosti
            vel_mag_list.append(np.sqrt(2*kinetic_per_part/self.masses[i]) * 0.1*np.sqrt(10))
        return vel_mag_list

    def append_vectors(self):
        """Přiřadí jednotlivým částicím počáteční vektory rychlosti."""
        vectors = self.start_vectors()
        for i in range(len(self.particles)):
            self.particles[i].xvelocity = vectors[i][0]
            self.particles[i].yvelocity = vectors[i][1]
            print(self.particles[i].xvelocity)

    def make_particles(self):
        """Funkce pro vytvoření instancí třídy Particle (jednotlivých částic)"""
        scoord_index = 0 #index přiřazené souřadnice
        # vytvoření jednotlivých částic
        for index in range(len(self.setframe.conds.numbers)):
            for i in range(self.setframe.conds.numbers[index]):
                print(scoord_index)
                part = Particle(index, self.setframe.conds.scoord[0][scoord_index], self.setframe.conds.scoord[1][scoord_index], 0.0, 0.0)
                self.particles.append(part)
                print(part.xcoord)
                print(self.particles[scoord_index].xcoord, 'part[i]')
                scoord_index += 1