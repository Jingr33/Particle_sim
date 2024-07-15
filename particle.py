import numpy as np
import math
import pygame as py
import matplotlib as mpl
import matplotlib.pyplot as plt
from conditions import Conds

class Particle:
    """Třída pro výrobu částic."""
    def __init__(self, type, xcoord, ycoord, xvelocity, yvelocity):
        #self.name = name
        #self.mass = mass
        #self.charge = charge
        #self.sigma = simga
        #self.epsilon = epsilon
        self.type = type
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity

    #def get_x_coord(self):
    #    return self.xcoord



#    def __init__(self):
#        self.names = Conditions.names
#
#        self.get_dots
#
#    def get_dots(self):
#        #vytvoření pole částic
#        particles = [Conditions.num_of_parts]
#        grid_position = 0
#        for index in range(len(Conditions.numbers)): # projede to tolikrát, kolik je typů částic
#            for i in range(Conditions.numbers[index]): # vytvoří částici tolikrát, kolikrát se ná vytvořit
#                self_coord = Conditions.s_coord[grid_position]
#                self_vector = Conditions.s_vectors[grid_position]
#                particle = [Conditions.names[index], Conditions.masses[index], Conditions.charges[index], Conditions.sigmas[index], Conditions.epsilons[index], self_coord, self_vector] # vytvoření té jedné kuličky
#                particles.append(particle) # přidání do seznamu všech kuliček
#                grid_position += 1 #zvýším index v souřadnicích o 1
#        # vrátí pole particles
#        return particles

