# importy všeho co je potřeba
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,) # pro přenesení matplotlibu do tkintru
from particle import Particle
from setframe import Frame as SetFrame
from initsim import Init_sim
from calculation import Calculation as Calc
import configuration as C
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


class Frame(ctk.CTkFrame):
    """Třida vykreslující Frame se simulací v pravé části okna"""
    def __init__(self, master:ctk.CTkBaseClass, setframe:SetFrame)-> None:
        super().__init__(master)
        # inicializace
        self.particles = []
        self.timestep = 1
        self.setframe = setframe
        # kontrolní výpis
        print(setframe.conds_numbers)

        # zajistí, že při klinutí na "spustit simulaci" se zavolá vykreslovací fce
        setframe.start_sim.bind('<Button-1>', self.sim_run)

        # vytvoření figure
        self.figure = Figure(figsize=(6,4), dpi=(100))
        # převedení do tkinteru
        figure_canvas = FigureCanvasTkAgg(self.figure, self)
        figure_canvas.draw()

        # vytvoření subplotu
        self.dots = self.figure.add_subplot()
        #optimalizace os
        self.dots.axis([0, C.box_size_x, 0, C.box_size_y])

        #vytvoření matplotlibu v tkinteru
        figure_canvas.get_tk_widget().pack(fill=ctk.BOTH, side=ctk.TOP, expand=1)
        
    def sim_run(self, event):
        """Funkce pro vykreselní simulace po stuštění 
        tlačítkem Spustit simulaci (v nastavovacím okně)."""
        #kontrolní výpisy
        print("AKTUÁLNÁ BUG")
        print(self.setframe.conds_numbers)
        print(self.setframe.conds.scoord)
        print(self.setframe.conds.num_of_parts, 'num_of_parts')

        # vytvoření instance Init_sim
        self.init_sim = Init_sim(self.setframe)
        self.particles = self.init_sim.particles # tohle nevím jestli tu má být
        # Zavolání matody, která vytvoří jednotlivé instance objektu Particles (instance částic)

        #kontrolní výpisy
        print(self.init_sim)
        

        # vytvoření souřadnicových listu
        self.xcoord = [0 for i in range(self.setframe.conds.num_of_parts)]
        self.ycoord = [0 for i in range(self.setframe.conds.num_of_parts)]
        #kontrolní výpis
        print(self.xcoord, '2 pole', self.ycoord)

        # naplnění listů s jednotlivými souřadnicemi pro vykreslení
        for i in range(len(self.particles)):
            self.xcoord[i] = self.particles[i].xcoord
            self.ycoord[i] = self.particles[i].ycoord
            #kontrolní výpis
            print(self.xcoord[i], self.ycoord[i], 'TTTTTTTTTTTTTTTTTT')


        ######################################################################
        #self.eb, = self.dots.plot([], [], C.colours[0], markersize=10)
        #self.ea, = self.dots.plot([], [], C.colours[1], markersize=15)
        #self.e = (self.ea, self.eb)
        ######################################################################
        #self.pole = []
        #for i in range(2):
        #    self.elem, = self.dots.plot([], [], C.colours[i], markersize=15)
        #    self.pole.append(self.elem)
        #print(self.pole, ' pole')
        ######################################################################
        # vytvoření listu s jednotlivými typy častic
        self.elems_list = []
        for i in range(len(self.setframe.conds.numbers)):
            dot_size = (self.setframe.conds.sigmas[i] / 2) / C.box_size_x * C.pixel_size_x
            self.elem, = self.dots.plot([], [], C.colours[i], markersize=dot_size)
            self.elems_list.append(self.elem)
            # kontrolní výpis
        print(self.elems_list, ' list')

        #vytvoření tuplu z listu
        ######################################################################
        #self.e = tuple(i for i in self.pole)
        #print(self.e, ' tuple')
        ######################################################################
        # list -> tuple
        ######################################################################
        #vytovření tuplu z listu typů častic (prtože animace chce tuple)
        self.elems_tup = tuple(i for i in self.elems_list)
        print(self.elems_tup, ' tuple')

        # zavolání animační funkce
        self.dots = FuncAnimation(self.figure, self.animation, init_func=self.init, interval=60, blit=True)


    def init(self):
        """Inicializační funkce animace."""
        #for i in range(len(self.e)):
        #    self.e[i].set_data([], [])
        #self.e[0].set_data([], [])
        #self.e[1].set_data([], [])
        #return self.e
        #####################################################
        for i in range(len(self.setframe.conds.numbers)):
            self.elems_tup[i].set_data([], [])
        return self.elems_tup

    #animační funkce
    def animation(self, i):
        """Animační funkce animace. Zde se plní struktury bodů souřadnicemi."""
        print(i*C.timestep)
        #x1 = self.xcoord
        #y1 = self.ycoord
        #x2 = [10, 20, 30 ,40 ,50]
        #y2 = [10, 20, 30, 40, 50]
        #x = [x1, x2]
        #y = [y1, y2]
        #self.e[0].set_data(x, y)
        #self.e[1].set_data(x2, y2)
        #for i in range(len(self.e)):
        #    self.e[i].set_data(x[i], y[i])
        #return self.e
        #########################################################
        calc = Calc(self.particles, self.setframe)
        self.particles = calc.particles
        for k in range(len(self.particles)):
            self.xcoord[k] = self.particles[k].xcoord
            self.ycoord[k] = self.particles[k].ycoord 
        x = self.xcoord
        y = self.ycoord
        j = 0
        for l in range(len(self.setframe.conds.numbers)):
            self.elems_tup[l].set_data(x[j:(j + self.setframe.conds.numbers[l])], y[j:(j + self.setframe.conds.numbers[l])])
            j += self.setframe.conds.numbers[l]

        return self.elems_tup