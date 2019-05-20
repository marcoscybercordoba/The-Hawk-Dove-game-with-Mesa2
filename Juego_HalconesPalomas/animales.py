from Framework_Mesa import Agent
import random

class Animales(Agent):

    edad = 0
    cortejando = 0
    criandoHijo = 0
    edadDeDefuncion = 90 

    def __init__(self, unique_id, model):

        super().__init__(unique_id, model)
        
        self.edad = 0

        self.cortejando = 0
        self.criandoHijo = 0
        self.edadDeDefuncion = 90
