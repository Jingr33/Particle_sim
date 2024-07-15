# Particle Simulator
The Particle Simulator is a simple programm for visualizing interactions between particles in 2D endless system.

## Technologies
* programming language: Python 3.11.9
* library: Tkinter, Customtkinter
* library: Matplotlib

## Launch the app
Open a repository in your development environment and launch application using a main.py file. In config.py can user change more specific settings.

## How to manage the app?
In the left column you can load a simulation or save an actual simulation for later use.
If you want to create a new system of particles set "Energie" input and add an arbitrary amount of particles with specific characteristics (setted in a new displayed window). You can add more more types of particles. Press "Spustit simulaci" button if you want to start a simulation.

## Simulation plot
There is a 2D plot in an angstrom scale. If the simulation is turned on you will see colorful circles. Each color is one specific type of particle. If the particle leaves the displayed box, the same particle comes from the other side of the plot. 

## Explanation of terms
* Energie - total energy of the system, it is spread out between potential and kinetic energy in the simulation.
* sigma - a constat of the particle in Lennard-Jones potential equation.
* epsilon - a constat of the particle in Lennard-Jones potential equation.
