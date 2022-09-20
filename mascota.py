class Mascota:
	def __init__(self, name, tipo, golosinas, sonido):
		self.name = name
		self.tipo = tipo
		self.golosinas = golosinas
		self.salud = 10
		self.energia = 10
		self.sonido = sonido
	# dormir() - incrementa la energía de la mascota en 25
	def dormir(self):
		self.energia = self.energia + 25
		return self
	# comer() - incrementa la energía de la mascota en 5 y la salud en 10
	def comer(self):
		self.energia = self.energia + 5
		self.salud = self.salud + 10
		return self
	# jugar() - incrementa la salud de la mascota en 5
	def jugar(self):
		self.salud = self.salud + 5
		return self
	# ruido() - imprime el sonido que produce la mascota
	def sonar(self):
		print (self.sonido)
		return