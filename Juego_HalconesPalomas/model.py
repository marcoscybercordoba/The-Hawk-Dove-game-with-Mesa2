from Framework_Mesa import Model
from Framework_Mesa.space import MultiGrid
from Framework_Mesa.datacollection import DataCollector

from Juego_HalconesPalomas.agentes import Jugadores
from Juego_HalconesPalomas.schedule import RandomActivationByBreed

from Juego_HalconesPalomas.ResultadoDeEncuentroEntreDosIndividuos import ResultadoDeEncuentroEntreDosIndividuos

import random

class Ambiente(Model):
	height = 20
	width = 20

	distanciaMaximaVecinos = 1 
	cantidadDeHalcones = 2
	cantidadDeParadojicos = 2
	cantidadDePalomas = 2
	valorDelRecurso = 2
	costeDeLesion = 10
	probabilidadDeQueElMayorGane1 = 50
	edadDeReproduccion = 20

	minGlobal = None
	maxGlobal = 0
	
	epoca = 1
	
	description = 'Un modelo descripto por Richard DawkinsA model for simulating wolf and sheep (predator-prey) ecosystem modelling.'
	
	def __init__(self, 
		alto = 20,
		ancho = 20,
		distanciaMaximaVecinos = 20, 
		cantidadDeHalconesChicos = 2,
		cantidadDeHalconesGrandes = 2,
		cantidadDeParadojicosChicos = 0,
		cantidadDeParadojicosGrandes = 0,
		cantidadDeSentidoComunChicos = 0,
		cantidadDeSentidoComunGrandes = 0,
		cantidadDePalomasChicos = 0,
		cantidadDePalomasGrandes = 0,
		valorDelRecurso = 1,
		costeDeLesion = 0,
		porcentajeDeQueElMayorGane = 50, 
		edadDeReproduccion = 2
		):
		
		super().__init__()
		self.paso = 1
		
		self.epoca = 1
		
		self.minGlobal = None
		self.maxGlobal = None
		
		self.alto = alto
		self.ancho = ancho
		
		self.distanciaMaximaVecinos = distanciaMaximaVecinos
		self.cantidadDeHalconesChicos = cantidadDeHalconesChicos
		self.cantidadDeHalconesGrandes = cantidadDeHalconesGrandes
		self.cantidadDePalomasChicos = cantidadDePalomasChicos
		self.cantidadDePalomasGrandes = cantidadDePalomasGrandes
		self.cantidadDeParadojicosChicos = cantidadDeParadojicosChicos
		self.cantidadDeParadojicosGrandes = cantidadDeParadojicosGrandes

		self.cantidadDeSentidoComunChicos = cantidadDeSentidoComunChicos
		self.cantidadDeSentidoComunGrandes = cantidadDeSentidoComunGrandes

		self.valorDelRecurso = valorDelRecurso
		self.costeDeLesion = costeDeLesion
		
		self.edadDeReproduccion = edadDeReproduccion
		
		self.schedule = RandomActivationByBreed(self)
		self.grid = MultiGrid(20, 20, torus=True)
		
		self.grid = MultiGrid(self.alto, self.ancho, torus=False)
		self.datacollector = DataCollector(
			{"Total": lambda m: m.schedule.cantidadDeJugadores0(),
			"SiempreEscala_Grande": lambda m: m.schedule.cantidadDeJugadores("siempreEscala", "grande"),
			"SiempreEscala_Chico": lambda m: m.schedule.cantidadDeJugadores("siempreEscala", "chico"),
			"EscalaSiElOtroEsMasGrande_Grande": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "grande"),
			"EscalaSiElOtroEsMasGrande_Chico": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "chico"),
			"EscalaSiElOtroEsMasChico_Grande": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasChico", "grande"),
			"EscalaSiElOtroEsMasChico_Chico": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasChico", "chico"),
			"NuncaEscala_Grande": lambda m: m.schedule.cantidadDeJugadores("nuncaEscala", "grande"),
			"NuncaEscala_Chico": lambda m: m.schedule.cantidadDeJugadores("nuncaEscala", "chico")})

		self.probabilidadDeQueElMayorGane1 = porcentajeDeQueElMayorGane / 100.00
		
		i = 0
		while i < self.cantidadDeHalconesChicos:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "siempreEscala"
			
			localia = None
			#asimetriaAparente = "grande"
			asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1
		    
		i = 0
		while i < self.cantidadDeHalconesGrandes:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "siempreEscala"
			
			localia = None
			asimetriaAparente = "grande"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1

		i = 0
		while i < self.cantidadDePalomasChicos:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "nuncaEscala"
			localia = None
			asimetriaAparente = "grande"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1

		i = 0
		while i < self.cantidadDePalomasGrandes:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "nuncaEscala"
			localia = None
			#asimetriaAparente = "grande"
			asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1

			
		i = 0
		while i < self.cantidadDeParadojicosChicos:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "escalaSiElOtroEsMasGrande"
			localia = None
			asimetriaAparente = "grande"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1
			
		i = 0
		while i < self.cantidadDeParadojicosGrandes:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "escalaSiElOtroEsMasGrande"
			localia = None
			asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1


		i = 0
		while i < self.cantidadDeSentidoComunChicos:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "escalaSiElOtroEsMasChico"
			localia = None
			asimetriaAparente = "grande"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1
			
		i = 0
		while i < self.cantidadDeSentidoComunGrandes:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "escalaSiElOtroEsMasChico"
			localia = None
			asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1


		self.datacollector.collect(self)     
		self.running = True
	
	def step(self):

		print("Paso: " + str(self.paso))
		print("")
			
		puntajeMinimo = None
		puntajeMaximo = None
		
		for agente in self.schedule.agents:
			
			agente.SetCombatioContraAlguienEnEstaEpoca(False)
			
			puntajeBruto = agente.TotalDePuntos()
			
			if puntajeMinimo == None:
				puntajeMinimo = puntajeBruto
			
			if puntajeMaximo == None:
				puntajeMaximo = puntajeBruto
			
			if puntajeBruto < puntajeMinimo:
				puntajeMinimo = puntajeBruto
			
			if puntajeBruto > puntajeMaximo:
				puntajeMaximo = puntajeBruto
		

		poblacion = self.schedule.cantidadDeJugadores0()

		eliminoIndividiosAlternativos = True
		k = 1
		for agente in self.schedule.agents:
			
			# W(H) = pE(H,H) + (1-p)E(H,D)
			# W(D) = pE(D,H) + (1-p)E(D,D)
			
			# W = pW(H) + (1-p)W(D)
			# pNew = pW(H)/W
			
			# E(D,D)<E(H,D)
			
			# 1/2(V-C) > 0 or
			# V > C
			
			# pNew = V/C
			
			# E(H,I) = E(D,I)
			# pE(H,H) + (1-p)E(H,D) = pE(D,H) + (1-p)E(D,D)
			
			# p(1/2)(V-C) + (1-p)V = (1/2)(1/2)V

			# Cuando un individuo llega a la edad de reproducci&#xF3;n hace copias de s&#xED; mismo. La cantidad de copias que el individuo va a hacer depende no solo de su pontaje sino que depende tambi&#xE9;n de la cantidad de individuos que hay en la poblaci&#xF3;n. Los puntos que los individuos obtuvieron en los combates  se convierten a una escala del 0 al 100. Los que tienen 100 son los individuos que m&#xE1;s puntos obtuvieron y los que tienen 0 son los individuos que menos puntos obtuvieron. 
			
			# Si la poblaci&#xF3;n es de menos de 50 individuos y el sujeto obtiene menos de 50 en la generaci&#xF3;n siguiente habr&#xE1; una sola copia de s&#xED; mismo, si tiene m&#xE1;s de 50 puntos hace 2 copias de s&#xED; mismo. 
			
			# Si la poblaci&#xF3;n esta entra 50 y 100 y el sujeto obtiene menos de 33 no hace copias de s&#xED; mismo, si tiene entre 33 y 66 hace 1 copia de s&#xED; mismo, si tiene m&#xE1;s de 66 hace dos copias de s&#xED; mismo.
			
			# Los descendientes heredan la misma estrategia que los padres. Si los padres son de escalar sus descendientes tienen las mismas estrategias de resoluci&#xF3;n de conflicto.
			
			# Luego de la reproducci&#xF3;n el individuo muere.

			if agente.Edad() == self.edadDeReproduccion:

				#print("La poblacion actual es de " + str(poblacion))
				#if (poblacion <= 50):
				#	print("El jugador que tiene la menor cantidad de puntos hace una copia de si  mismo, el jugador que tiene la mayor cantidad de puntos hace 2 copias de si mismo")
				
				#if (poblacion > 50 and poblacion < 100):
				#	print("El jugador que tiene la menor cantidad de puntos no hace ninguna copia de si mismo, el jugador que tiene la mayor cantidad de puntos hace 2 copias de si mismo")
				
				#if (poblacion > 50 and poblacion < 100):
				#	print("El jugador que tiene la menor cantidad de puntos no hace ninguna copia de si mismo, el jugador que tiene la mayor cantidad de puntos hace 1 sola copias de si mismo")

				puntajeBruto = agente.TotalDePuntos()
				if (not (puntajeMaximo - puntajeMinimo) == 0):
					puntajeRelativo = (puntajeBruto - puntajeMinimo)/(puntajeMaximo - puntajeMinimo) 
				else:
					puntajeRelativo = 0
				
				puntajePorcentual = round(puntajeRelativo * 100)
				#print("puntajePorcentual:"+str(puntajePorcentual))
				
				numeroDeCopias = 0
				
				if (poblacion <= 50):
					if puntajePorcentual < 50: 
						numeroDeCopias = 1
					if puntajePorcentual >= 50: 
						numeroDeCopias = 2

					#print("numeroDeCopias:"+str(numeroDeCopias))
				
				if (poblacion > 50 and poblacion < 200):
					if puntajePorcentual >= 0 and puntajePorcentual < 60: 
						numeroDeCopias = 1
					if puntajePorcentual >= 60: 
						numeroDeCopias = 2

				
				if (poblacion >= 200):
					if(eliminoIndividiosAlternativos == True):
						numeroDeCopias = 0
						eliminoIndividiosAlternativos = False
					else:
						numeroDeCopias = 1
						eliminoIndividiosAlternativos = True
				
				posicionDelAgente = agente.pos
				(p0, p1) = posicionDelAgente
				print("paso:" + str(self.paso) + " poblacion:" + str(poblacion) + " puntajePorcentual:" + str(puntajePorcentual) + " numeroDeCopias:" + str(numeroDeCopias) + " -El jugador "+ agente.Estrategia() + "-" + agente.AsimetriaAparente() + " localizado en (" + str(p0) + "," + str(p1) + ") " +" hizo " + str(numeroDeCopias) + " copias de si mismo y fueron puestos en:")
				i = 0
				while i < numeroDeCopias:
					
					posicionesVecinas  = self.grid.get_neighborhood(posicionDelAgente, True, True)
					posicionElejida = random.choice(posicionesVecinas)
					posCopX = posicionElejida[0]
					posCopY = posicionElejida[1]
					
					estrategia = agente.Estrategia()
					asimetriaAparente = agente.AsimetriaAparente()
					jugador1 = Jugadores(self.next_id(), posicionElejida, estrategia, asimetriaAparente, self)
					self.grid.place_agent(jugador1, posicionElejida)
					self.schedule.add(jugador1)
					#print("  posicion: (" + str(posCopX) + "," + str(posCopY) + ") ")
			
					i = i + 1
				#print("")
				
			if agente.Edad() > self.edadDeReproduccion - 1:
				
				(posX, posY) = agente.pos
				
				self.grid.remove_agent(agente)
				self.schedule.remove(agente)

				print("  -El jugador "+ agente.Estrategia() + "-" + agente.AsimetriaAparente() + " localizado en (" + str(posX) + "," + str(posY) + ") " +" fue eliminado por tener mas de " + str(self.edadDeReproduccion + 1))
				print("")
				
			if agente.Edad() >= 0 and agente.Edad() < self.edadDeReproduccion:
				
				(posX, posY) = agente.pos
				posicionesVecinas  = self.grid.get_neighborhood((posX, posY), True, True)
				posicionElejida = random.choice(posicionesVecinas)
				self.grid.move_agent(agente, posicionElejida)

		#print("Contiendas:")
		#print("-")
		i = 1
		for agenteA in self.schedule.agents:
			(p0, p1) = agenteA.pos
			
			if agenteA.Edad() >= 0 and agenteA.Edad() < self.edadDeReproduccion:
				j = 1
				for agenteB in self.grid.get_neighbors((p0, p1), True, include_center = True, radius = self.distanciaMaximaVecinos):
					if agenteB.Edad() >= 0 and agenteB.Edad() <= self.edadDeReproduccion + 1:
						(p20, p21) = agenteB.pos
							
						if (not (agenteA.unique_id == agenteB.unique_id)) and (agenteB.GetCombatioContraAlguienEnEstaEpoca() == False):

							(agenteA, agenteB) = ResultadoDeEncuentroEntreDosIndividuos(agenteA, agenteB, self.valorDelRecurso, self.costeDeLesion, self.probabilidadDeQueElMayorGane1)

						j = j + 1
						
				agenteA.SetCombatioContraAlguienEnEstaEpoca(True)
				i = i + 1
	            
		self.schedule.step()
		self.datacollector.collect(self)

		print(" ")
		print(" ")
		print(" ")

		self.paso = self.paso + 1

	
	def run_model(self, step_count = 200):
		a = 10
