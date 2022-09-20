from mascota import Mascota


class Ninja(Mascota):
	def __init__(self, nombre, apellido, mascota, premios, comida_mascota):
		self.nombre = nombre
		self.apellido = apellido
		self.mascota = mascota
		self.premios = premios
		self.comida_mascota = comida_mascota
	# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
	def caminar(self):
		self.mascota.jugar()
		return self
	# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
	def alimentar(self):
		self.mascota.comer()
		return self
	# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
	def bañar(self):
		self.mascota.sonar()
		return self