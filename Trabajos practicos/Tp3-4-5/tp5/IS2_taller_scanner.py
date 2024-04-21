import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

	def scan(self):

		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

	def memorize(self, station):
		self.stations.append(station)

#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

	def memorize(self, station):
		self.stations.append(station)


#*--------- Construye la radio con todas sus formas de sintonía
class Radio:


	def __init__(self):

		self.fmstate = FmState(self)
		self.amstate = AmState(self)

#*--- Inicialmente en FM

		self.state = self.fmstate

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

	def memorize_station(self, station):
		self.state.memorize(station)

	def switch_station(self, index):
			if isinstance(self.state, FmState):
				if index < len(self.fmstate.stations):
					self.fmstate.pos = index
					print("Cambiando a estación memorizada FM: {} {}".format(self.fmstate.stations[index], self.fmstate.name))
			elif isinstance(self.state, AmState):
				if index < len(self.amstate.stations):
					self.amstate.pos = index
					print("Cambiando a estación memorizada AM: {} {}".format(self.amstate.stations[index], self.amstate.name))

#*---------------------

if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
	actions *= 2

#*---- Recorre las acciones ejecutando la acción

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()

