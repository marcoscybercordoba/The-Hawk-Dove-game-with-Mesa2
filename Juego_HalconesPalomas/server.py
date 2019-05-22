from Framework_Mesa.visualization.ModularVisualization import ModularServer
from Framework_Mesa.visualization.modules import CanvasGrid, ChartModule
from Framework_Mesa.visualization.UserParam import UserSettableParameter

from Juego_HalconesPalomas.agentes import Jugadores
from Juego_HalconesPalomas.model import Ambiente

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

import random

from Framework_Mesa.visualization.ModularVisualization import VisualizationElement
import numpy as np

from Framework_Mesa.visualization.ModularVisualization import ModularServer
from Framework_Mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from Framework_Mesa.visualization.UserParam import UserSettableParameter

#import tornado.web.RequestHandler

from Framework_Mesa.visualization.TextVisualization import (
    TextData, TextGrid, TextVisualization
)

class HistogramModule(VisualizationElement):
    #package_includes = ["<script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.1.4/Chart.min.js'></script>"]
    #package_includes = "<script src='Framework_Mesa1/visualization/templates/js/Chart.bundle.min.js'></script>"
    #package_includes  = ["Framework_Mesa/visualization/templates/js/Chart.bundle.min.js"]

    local_includes = ["Framework_Mesa/visualization/templates/js/HistogramModule6.js"]

    def __init__(self, bins, canvas_height, canvas_width):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.bins = bins
        new_element = "new HistogramModule({}, {}, {})"
        new_element = new_element.format(bins,
                                         canvas_width,
                                         canvas_height)
        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        #wealth_vals = [agent.wealth for agent in model.schedule.agents]
        #hist = np.histogram(wealth_vals, bins=self.bins)[0]
        #return [int(x) for x in hist]    

        porcentajeDeHalconesGrande = model.schedule.porcentajeDeJugadores("siempreEscala", "grande")

        porcentajeDeHalconesChico = model.schedule.porcentajeDeJugadores("siempreEscala", "chico")

        porcentajeDePalomasGrande = model.schedule.porcentajeDeJugadores("nuncaEscala", "grande")

        porcentajeDePalomasChico = model.schedule.porcentajeDeJugadores("nuncaEscala", "chico")

        porcentajeDeParadojicosGrande = model.schedule.porcentajeDeJugadores("escalaSiElOtroEsMasGrande", "grande")
        
        porcentajeDeParadojicosChico = model.schedule.porcentajeDeJugadores("escalaSiElOtroEsMasGrande", "chico")

        return [porcentajeDeHalconesGrande, porcentajeDeHalconesChico, porcentajeDePalomasGrande, porcentajeDePalomasChico, porcentajeDeParadojicosGrande, porcentajeDeParadojicosChico]

def personalizacionDelAmbiente(agent):
    if agent is None:
        return

    portrayal = {}
        
    if agent.estrategia == "siempreEscala" and agent.asimetriaAparente == "grande":
        portrayal["Shape"] = "Juego_HalconesPalomas/resources/halconGrande.png"
        # https://icons8.com/web-app/36821/German-Shepherd
        portrayal["Estrategia"] = agent.estrategia
        portrayal["Asimetria"] = agent.asimetriaAparente
        portrayal["Edad"] = round(agent.edad, 1)
        portrayal["Puntos"] = agent.TotalDePuntos()
        portrayal["Layer"] = 1
        portrayal["text_color"] = "#08088A"

    if agent.estrategia == "siempreEscala" and agent.asimetriaAparente == "chico":
        portrayal["Shape"] = "Juego_HalconesPalomas/resources/halconChico3.png"
        # https://icons8.com/web-app/36821/German-Shepherd
        portrayal["Estrategia"] = agent.estrategia
        portrayal["Asimetria"] = agent.asimetriaAparente
        portrayal["Edad"] = round(agent.edad, 1)
        portrayal["Puntos"] = agent.TotalDePuntos()
        portrayal["Layer"] = 1
        portrayal["text_color"] = "#5858FA"

    if agent.estrategia == "nuncaEscala" and agent.asimetriaAparente == "grande":
        portrayal["Shape"] = "Juego_HalconesPalomas/resources/palomaGrande3.png"
        # https://icons8.com/web-app/36821/German-Shepherd
        portrayal["Estrategia"] = agent.estrategia
        portrayal["Asimetria"] = agent.asimetriaAparente
        portrayal["Edad"] = round(agent.edad, 1)
        portrayal["Puntos"] = agent.TotalDePuntos()
        portrayal["Layer"] = 1
        portrayal["text_color"] = "#8A0829"

    if agent.estrategia == "nuncaEscala" and agent.asimetriaAparente == "chico":
        portrayal["Shape"] = "Juego_HalconesPalomas/resources/palomaChica3.png"
        # https://icons8.com/web-app/36821/German-Shepherd
        portrayal["Estrategia"] = agent.estrategia
        portrayal["Asimetria"] = agent.asimetriaAparente
        portrayal["Edad"] = round(agent.edad, 1)
        portrayal["Puntos"] = agent.TotalDePuntos()
        portrayal["Layer"] = 1
        portrayal["text_color"] = "#FA5882"
        
    if agent.estrategia == "escalaSiElOtroEsMasGrande" and agent.asimetriaAparente == "grande":
        portrayal["Shape"] = "Juego_HalconesPalomas/resources/paradojicoGrande.png"
        # https://icons8.com/web-app/36821/German-Shepherd
        portrayal["Estrategia"] = agent.estrategia
        portrayal["Asimetria"] = agent.asimetriaAparente
        portrayal["Edad"] = round(agent.edad, 1)
        portrayal["Puntos"] = agent.TotalDePuntos()
        portrayal["Layer"] = 1
        portrayal["text_color"] = "#868A08"
        
    if agent.estrategia == "escalaSiElOtroEsMasGrande" and agent.asimetriaAparente == "chico":
        portrayal["Shape"] = "Juego_HalconesPalomas/resources/paradojicoChico.png"
        # https://icons8.com/web-app/36821/German-Shepherd
        portrayal["Estrategia"] = agent.estrategia
        portrayal["Asimetria"] = agent.asimetriaAparente
        portrayal["Edad"] = round(agent.edad, 1)
        portrayal["Puntos"] = agent.TotalDePuntos()
        portrayal["Layer"] = 1
        portrayal["text_color"] = "#F2F5A9"
            
    return portrayal

canvas_element = CanvasGrid(personalizacionDelAmbiente, 20, 20, 500, 500)
chart_element = ChartModule([{"Label": "SiempreEscala_Grande", "Color": "#08088A"},
                             {"Label": "SiempreEscala_Chico", "Color": "#5858FA"},
                             {"Label": "EscalaSiElOtroEsMasGrande_Grande", "Color": "#868A08"},
                             {"Label": "EscalaSiElOtroEsMasGrande_Chico", "Color": "#F2F5A9"},
                             {"Label": "NuncaEscala_Grande", "Color": "#8A0829"},
                             {"Label": "NuncaEscala_Chico", "Color": "#FA5882"}])


#a = Request.get_query_argument()

#if RequestHandler.get_argument('CostoDeLesion', None) != None:
#	CostoDeLesion = int(RequestHandler.get_argument('CostoDeLesion', None))

#print("CostoDeLesion:" + str(CostoDeLesion))

model_params = {
                "distanciaMaximaVecinos": UserSettableParameter('slider', 'Distancia dentro de la cual se consideran adversarios', 20, 1, 20),
                "cantidadDeHalconesChicos": UserSettableParameter('slider', 'Cantidad inicial de individuos chicos que siempren escalan', 1, 0, 10),
                "cantidadDeHalconesGrandes": UserSettableParameter('slider', 'Cantidad inicial de individuos grandes que siempren escalan', 1, 0, 10),
                "cantidadDePalomasChicos": UserSettableParameter('slider', 'Cantidad inicial de individuos chicos que nunca escalan', 6, 0, 10), 
                "cantidadDePalomasGrandes": UserSettableParameter('slider', 'Cantidad inicial de individuos grandes que nunca escalan', 6, 0, 10), 
                "cantidadDeParadojicosChicos": UserSettableParameter('slider', 'Cantidad inicial de individuos chicos que escalan solo si el adversario es mayor', 0, 0, 10),
                "cantidadDeParadojicosGrandes": UserSettableParameter('slider', 'Cantidad inicial de individuos grandes que escalan solo si el adversario es mayor', 0, 0, 10),
                "valorDelRecurso": UserSettableParameter('slider', 'Valor de un recurso', 1, 0, 10), 
                "costeDeLesion": UserSettableParameter('slider', 'Costo de una lesion', 2, 0, 10), 
                "probabilidadDeQueElMayorGane1": UserSettableParameter('slider', 'Probabilidad de que el mayor gane el combate', 50, 0, 100), 
                "edadDeReproduccion": UserSettableParameter('slider', 'Paso en que se produce la reproduccion y mueren', 5, 0, 1000) 
                }

#                "probabilidadDeQueElMayorGane2": UserSettableParameter('slider', 'Probabilidad de que el mayor gane el combate', {{ProbabilidadDeQueElMayorGane}}, 0, 100), 

histogram = HistogramModule(list(range(10)), 200, 500)

#                "costeDeLesion": UserSettableParameter('slider', 'Costo de una lesion', 10, 0, 50), 
#                "costeDeLesion1": UserSettableParameter('slider', 'Costo de una lesion', 10, 0, 50), 
#                "probabilidadDeQueElMayorGane1": UserSettableParameter('slider', 'Probabilidad de que el mayor gana el combate', 50, 0, 100)


# Asimetria arbitraria
# Se pueden diferenciar entre residentes e intrusos
# pero esta diferencia no influye en nada en el resultado del combate.

# residente-intruso
# estrategia paradojica

# Estrategia condicional de sentido comun
# El residente gana, el intruso se retira
# Estrategia condicional paradojica
# Pagina 92

server = ModularServer(Ambiente, [canvas_element, chart_element, histogram], "Machos galanteadores y fieles. Hembras faciles y esquivas", model_params)

#server.port = 8257
server.port = int(os.environ.get("PORT", 5000))

server.launch()
