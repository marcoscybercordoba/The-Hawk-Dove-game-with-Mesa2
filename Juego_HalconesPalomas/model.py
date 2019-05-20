from Framework_Mesa import Model
from Framework_Mesa.space import MultiGrid
from Framework_Mesa.datacollection import DataCollector

from Juego_HalconesPalomas.agentes import Jugadores
from Juego_HalconesPalomas.schedule import RandomActivationByBreed

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
		cantidadDeHalcones = 2,
		cantidadDeParadojicos = 0,
		cantidadDePalomas = 0,
		valorDelRecurso = 1,
		costeDeLesion = 0,
		probabilidadDeQueElMayorGane1 = 50, 
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
		self.cantidadDeHalcones = cantidadDeHalcones
		self.cantidadDePalomas = cantidadDePalomas
		self.cantidadDeParadojicos = cantidadDeParadojicos

		self.valorDelRecurso = valorDelRecurso
		self.costeDeLesion = costeDeLesion
		
		self.edadDeReproduccion = edadDeReproduccion
		
		self.probabilidadDeQueElMayorGane1 = probabilidadDeQueElMayorGane1

		self.schedule = RandomActivationByBreed(self)
		self.grid = MultiGrid(20, 20, torus=True)
		
		self.grid = MultiGrid(self.alto, self.ancho, torus=False)
		self.datacollector = DataCollector(
			{"Total": lambda m: m.schedule.cantidadDeJugadores0(),
			"SiempreEscala_Grande": lambda m: m.schedule.cantidadDeJugadores("siempreEscala", "grande"),
			"SiempreEscala_Chico": lambda m: m.schedule.cantidadDeJugadores("siempreEscala", "chico"),
			"EscalaSiElOtroEsMasGrande_Grande": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "grande"),
			"EscalaSiElOtroEsMasGrande_Chico": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "chico"),
			"SentidoComunGrande": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "grande"),
			"SentidoComunChico": lambda m: m.schedule.cantidadDeJugadores("escalaSiElOtroEsMasGrande", "chico"),
			"NuncaEscala_Grande": lambda m: m.schedule.cantidadDeJugadores("nuncaEscala", "grande"),
			"NuncaEscala_Chico": lambda m: m.schedule.cantidadDeJugadores("nuncaEscala", "chico")})

		self.probabilidadDeQueElMayorGane1 = probabilidadDeQueElMayorGane1 / 100.00
		
		i = 0
		while i < self.cantidadDeHalcones:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "siempreEscala"
			
			localia = None
			if i < round(self.cantidadDeHalcones/2):
				asimetriaAparente = "grande"
			else:
				asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1
		    
		i = 0
		while i < self.cantidadDePalomas:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "nuncaEscala"
			localia = None
			if i < round(self.cantidadDePalomas/2):
				asimetriaAparente = "grande"
			else:
				asimetriaAparente = "chico"
			pos = (x, y)
			jugador1 = Jugadores(id, pos, estrategia, asimetriaAparente, self)
			self.grid.place_agent(jugador1, (x, y))
			self.schedule.add(jugador1)
			
			i = i + 1
			
		i = 0
		while i < self.cantidadDeParadojicos:
			
			x = random.randrange(self.ancho)
			y = random.randrange(self.alto)
			
			id = self.next_id()
			estrategia = "escalaSiElOtroEsMasGrande"
			localia = None
			if i < round(self.cantidadDeParadojicos/2):
				asimetriaAparente = "grande"
			else:
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

				print("La poblacion actual es de " + str(poblacion))
				if (poblacion <= 50):
					print("El jugador que tiene la menor cantidad de puntos hace una copia de si  mismo, el jugador que tiene la mayor cantidad de puntos hace 2 copias de si mismo")
				
				if (poblacion > 50 and poblacion < 100):
					print("El jugador que tiene la menor cantidad de puntos no hace ninguna copia de si mismo, el jugador que tiene la mayor cantidad de puntos hace 2 copias de si mismo")
				
				if (poblacion > 50 and poblacion < 100):
					print("El jugador que tiene la menor cantidad de puntos no hace ninguna copia de si mismo, el jugador que tiene la mayor cantidad de puntos hace 1 sola copias de si mismo")

				puntajeBruto = agente.TotalDePuntos()
				if (not (puntajeMaximo - puntajeMinimo) == 0):
					puntajeRelativo = (puntajeBruto - puntajeMinimo)/(puntajeMaximo - puntajeMinimo) 
				else:
					puntajeRelativo = 0
				
				puntajePorcentual = round(puntajeRelativo * 100)
				print("puntajePorcentual:"+str(puntajePorcentual))
				
				numeroDeCopias = 0
				
				if (poblacion <= 50):
					if puntajePorcentual < 50: 
						numeroDeCopias = 1
					if puntajePorcentual >= 50: 
						numeroDeCopias = 2

					print("numeroDeCopias:"+str(numeroDeCopias))
				
				if (poblacion > 50 and poblacion < 100):
					if puntajePorcentual < 33: 
						numeroDeCopias = 0
					if puntajePorcentual >= 33 and puntajePorcentual < 66: 
						numeroDeCopias = 1
					if puntajePorcentual >= 66: 
						numeroDeCopias = 2

				
				if (poblacion >= 100):
					if puntajePorcentual < 50: 
						numeroDeCopias = 0
					if puntajePorcentual >= 50: 
						numeroDeCopias = 1
				
				posicionDelAgente = agente.pos
				(p0, p1) = posicionDelAgente
				print(" -El jugador "+ agente.Estrategia() + "-" + agente.AsimetriaAparente() + " localizado en (" + str(p0) + "," + str(p1) + ") " +" hizo " + str(numeroDeCopias) + " copias de si mismo y fueron puestos en:")
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
					print("  posicion: (" + str(posCopX) + "," + str(posCopY) + ") ")
			
					i = i + 1
				print("")
				
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

		print("Contiendas:")
		print("-")
		i = 1
		for agenteA in self.schedule.agents:
			(p0, p1) = agenteA.pos
			
			if agenteA.Edad() >= 0 and agenteA.Edad() < self.edadDeReproduccion:
				j = 1
				for agenteB in self.grid.get_neighbors((p0, p1), True, include_center = True, radius = self.distanciaMaximaVecinos):
					if agenteB.Edad() >= 0 and agenteB.Edad() <= self.edadDeReproduccion + 1:
						(p20, p21) = agenteB.pos
							
						if (not (agenteA.unique_id == agenteB.unique_id)) and (agenteB.GetCombatioContraAlguienEnEstaEpoca() == False):

							(agenteA, agenteB) = self.ResultadoDeUnEncuentreEntreDosIndividuos(agenteA, agenteB)

						j = j + 1
						
				agenteA.SetCombatioContraAlguienEnEstaEpoca(True)
				i = i + 1
	            
		self.schedule.step()
		self.datacollector.collect(self)

		print(" ")
		print(" ")
		print(" ")

		self.paso = self.paso + 1

	def ResultadoDeUnEncuentreEntreDosIndividuos(self, agenteA, agenteB):

		print("probabilidadDeQueElMayorGane1:"+str(self.probabilidadDeQueElMayorGane1))
	
		(posA0, posA1) = agenteA.pos
		(posB0, posB1) = agenteB.pos

		costoDePerderUnaPelea = round((-self.costeDeLesion), 2)
		puntosPorGanarUnaPelea = round((self.valorDelRecurso), 2)
		puntosGanadosPorCompartirElRecurso = round((self.valorDelRecurso/2), 2)
		sinPuntosPorRetirarse = 0
		puntosGanadosSinPelear = round((self.valorDelRecurso), 2)

		probabilidadDeQueElMayorGane1 = self.probabilidadDeQueElMayorGane1
		#(puntosPorGanarUnaPelea - costoDePerderUnaPelea-/2

		puntosPorGanarUnaPelea = 1
		costoDePerderUnaPelea = 0
		probabilidadDeQueElMayorGane1 = 0.5
		
		if agenteA.Estrategia() == "siempreEscala":

			# agenteA:siempreEscala y agenteB:nuncaEscala
			if agenteB.Estrategia() == "nuncaEscala":
				agenteA.SumarPuntos(puntosGanadosSinPelear)
				agenteB.SumarPuntos(sinPuntosPorRetirarse)
		
				print("- Resultado de contienda entre " + agenteA.Estrategia() + "-" + agenteA.AsimetriaAparente() + " localizada en (" + str(posA0) + "," + str(posA1) + ") contra " + agenteB.Estrategia()  + "-" +  agenteB.AsimetriaAparente() + " localizado en (" + str(posB0) + "," + str(posB1) + ")")
				print("  - Al primer jugador le sumo " + str(puntosGanadosSinPelear) + " resultado un total de " + str(agenteA.TotalDePuntos()))
				print("  - Al segundo jugador le sumo " + str(sinPuntosPorRetirarse) + " resultado un total de " + str(agenteB.TotalDePuntos()))
				print("")
		
			# agenteA:siempreEscala y agenteB:siempreEscala
			if agenteB.Estrategia() == "siempreEscala":

				# agenteA:siempreEscala y agenteB:siempreEscala
				# agenteA:chico y agenteB:chico
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
					pr = random.random()
					if pr < self.probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(puntosPorGanarUnaPelea)
						agenteB.SumarPuntos(costoDePerderUnaPelea)

					if pr >= self.probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(costoDePerderUnaPelea)
						agenteB.SumarPuntos(puntosPorGanarUnaPelea)

				# agenteA:siempreEscala y agenteB:siempreEscala
				# agenteA:chico y agenteB:grande
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
					pr = random.random()
					print("agenteA.unique_id" + str(agenteA.unique_id) + "probabilidad grande " + str(pr)+" probabilidad grande " + str(probabilidadDeQueElMayorGane1))

					pr = random.random()
					if pr < probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(costoDePerderUnaPelea)
						agenteB.SumarPuntos(puntosPorGanarUnaPelea)

					if pr >= probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(puntosPorGanarUnaPelea)
						agenteB.SumarPuntos(costoDePerderUnaPelea)

				# agenteA:siempreEscala y agenteB:siempreEscala
				# agenteA:grande y agenteB:chico
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
					pr = random.random()
					print("agenteA.unique_id" + str(agenteA.unique_id) + "probabilidad grande " + str(pr)+" probabilidad grande " + str(probabilidadDeQueElMayorGane1))

					pr = random.random()
					if pr < probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(puntosPorGanarUnaPelea)
						agenteB.SumarPuntos(costoDePerderUnaPelea)

					if pr >= probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(costoDePerderUnaPelea)
						agenteB.SumarPuntos(puntosPorGanarUnaPelea)

				# agenteA:siempreEscala y agenteB:siempreEscala
				# agenteA:grande y agenteB:grande
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
					pr = random.random()
					if pr < probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(costoDePerderUnaPelea)
						agenteB.SumarPuntos(puntosPorGanarUnaPelea)

					if pr >= self.probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(puntosPorGanarUnaPelea)
						agenteB.SumarPuntos(costoDePerderUnaPelea)
		
				print("- Resultado de contienda entre " + agenteA.Estrategia() + "-" + agenteA.AsimetriaAparente() + " localizada en (" + str(posA0) + "," + str(posA1) + ") contra " + agenteB.Estrategia()  + "-" +  agenteB.AsimetriaAparente() + " localizado en (" + str(posB0) + "," + str(posB1) + ")")
				print("  - Al primer jugador le sumo " + str(puntosPorGanarUnaPelea) + " resultado un total de " + str(agenteA.TotalDePuntos()))
				print("  - Al segundo jugador le sumo " + str(costoDePerderUnaPelea) + " resultado un total de " + str(agenteB.TotalDePuntos()))
				print("")
		
			# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
			if agenteB.Estrategia() == "escalaSiElOtroEsMasGrande":

				# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:chico y agenteB:chico
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
					agenteA.SumarPuntos(puntosGanadosSinPelear)
					agenteB.SumarPuntos(sinPuntosPorRetirarse)

				# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:chico y agenteB:grande
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
		
					agenteA.SumarPuntos(puntosGanadosSinPelear)
					agenteB.SumarPuntos(sinPuntosPorRetirarse)

				# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:grande y agenteB:chico
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
		
					pr = random.random()
					if pr <= probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(puntosPorGanarUnaPelea)
						agenteB.SumarPuntos(costoDePerderUnaPelea)
		
					if pr > probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(costoDePerderUnaPelea)
						agenteB.SumarPuntos(puntosPorGanarUnaPelea)
		
				# agenteA:siempreEscala y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:grande y agenteB:grande
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
					agenteA.SumarPuntos(puntosGanadosSinPelear)
					agenteB.SumarPuntos(sinPuntosPorRetirarse)
		
		if agenteA.Estrategia() == "nuncaEscala":
		
			# agenteA:nuncaEscala y agenteB:nuncaEscala
			if agenteB.Estrategia() == "nuncaEscala":
				agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
				agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)
		
			# agenteA:nuncaEscala y agenteB:siempreEscala
			if agenteB.Estrategia() == "siempreEscala":
					agenteA.SumarPuntos(sinPuntosPorRetirarse)
					agenteB.SumarPuntos(puntosGanadosSinPelear)
		
			# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
			if agenteB.Estrategia() == "escalaSiElOtroEsMasGrande":
		
				# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:chico y agenteB:chico
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
					agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
					agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

				# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:chico y agenteB:grande
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
					agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
					agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

				# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:grande y agenteB:chico
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
					agenteA.SumarPuntos(puntosGanadosSinPelear)
					agenteB.SumarPuntos(sinPuntosPorRetirarse)

				# agenteA:nuncaEscala y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:grande y agenteB:grande
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
					agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
					agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)
		
		if agenteA.Estrategia() == "escalaSiElOtroEsMasGrande":

			# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
			if agenteB.Estrategia() == "nuncaEscala":

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
				# agenteA:chico y agenteB:chico
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
					agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
					agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
				# agenteA:chico y agenteB:grande
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
					agenteA.SumarPuntos(puntosGanadosSinPelear)
					agenteB.SumarPuntos(sinPuntosPorRetirarse)

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
				# agenteA:grande y agenteB:chico
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
					agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
					agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:nuncaEscala
				# agenteA:grande y agenteB:grande
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
					agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
					agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)
		
			# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
			if agenteB.Estrategia() == "siempreEscala":

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
				# agenteA:chico y agenteB:chico
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
					agenteA.SumarPuntos(puntosGanadosSinPelear)
					agenteB.SumarPuntos(sinPuntosPorRetirarse)

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
				# agenteA:chico y agenteB:grande
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
					pr = random.random()
					if pr <= probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(puntosPorGanarUnaPelea)
						agenteB.SumarPuntos(costoDePerderUnaPelea)
		
					if pr > probabilidadDeQueElMayorGane1:
						agenteA.SumarPuntos(costoDePerderUnaPelea)
						agenteB.SumarPuntos(puntosPorGanarUnaPelea)

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
				# agenteA:grande y agenteB:chico
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
					agenteA.SumarPuntos(puntosGanadosSinPelear)
					agenteB.SumarPuntos(sinPuntosPorRetirarse)

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:siempreEscala
				# agenteA:grande y agenteB:grande
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
					agenteA.SumarPuntos(puntosGanadosSinPelear)
					agenteB.SumarPuntos(sinPuntosPorRetirarse)
		
			# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
			if agenteB.Estrategia() == "escalaSiElOtroEsMasGrande":

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:chico y agenteB:chico
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "chico":
					agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
					agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:chico y agenteB:grande
				if agenteA.AsimetriaAparente() == "chico" and agenteB.AsimetriaAparente() == "grande":
					agenteA.SumarPuntos(puntosGanadosSinPelear)
					agenteB.SumarPuntos(sinPuntosPorRetirarse)

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:grande y agenteB:chico
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "chico":
					agenteA.SumarPuntos(sinPuntosPorRetirarse)
					agenteB.SumarPuntos(puntosGanadosSinPelear)

				# agenteA:escalaSiElOtroEsMasGrande y agenteB:escalaSiElOtroEsMasGrande
				# agenteA:grande y agenteB:grande
				if agenteA.AsimetriaAparente() == "grande" and agenteB.AsimetriaAparente() == "grande":
					agenteA.SumarPuntos(puntosGanadosPorCompartirElRecurso)
					agenteB.SumarPuntos(puntosGanadosPorCompartirElRecurso)
	
		return (agenteA, agenteB)
	
	def run_model(self, step_count = 200):
		a = 10