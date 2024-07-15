"""
import matplotlib.pyplot as plt
from conditions import Conds
from particle import Particle

# třída vtvářející jednotlivé kuličky
class Scene:
    def __init__(self):
        self.particles = []
        
        #self.make_particles(self)

    #funkce pro vytvoření objektů částic
    def make_particles(self):
        print('********************')
        #coord_list = Conds.start_coord(Conds, Conds.num_of_parts)

        #scoord_index = 0 #index přiřazené souřadnice
        # vytvoření jednotlivých "kuliček"
        for index in Conds.numbers:
            for i in range(Conds.numbers[index]):
                part = Particle( 0, 0, 0, 0.0, 0.0)
                self.particles.append(part)
                scoord_index += 1

        print('fffffffffffffffffffffff')

    def get_particles(self):
        karel = self.karel
        return karel
        """
