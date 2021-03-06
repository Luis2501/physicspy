"""
Movimiento rectilineo uniforme 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

lun 22 feb 2021 13:03:42 CST 
"""
import numpy as np 

class MRU:

	def __init__(self, v):

		self.v = v
		
	def __str__(self):
	
		return f"The velocity is v = {self.v} m/s"

	def __call__(self, u, t):

		x, v = u, self.v

		return v
		
	def momentum(self, m):
	
		"""
		This function for get the lineal momentum that given by 
		
		p = mv
		
		where m is the mass of particle
		"""
	
		return m*self.v
		
	def energy(self, m):
	
		"""
		Function for get the energy, in this case the potential energy is zero. 
		The kinetic energy is given by
		
		K = 1/2 m v² 
		"""
	
		return 1/2*m*(self.v**2)

class MRUA:

	def __init__(self, g):

		self.g = g

	def __call__(self, u, t):

		v, g = u, self.g 

		return -g

class Movimiento_friccion:

	def __init__(self, a, b):

		self.a, self.b = a, b

	def __call__(self, u, t):

		v, a, b = u, self.a, self.b 

		return a - b*v

class Tiro_Parabolico:

	def __init__(self, v, g, friccion = False, B = 0):

		self.v, self.g, self.friccion, self.B = v, g, friccion, B

	def __call__(self, u, t):

		x, vx, y, vy = u 
		g, B = self.g, self.B

		if self.friccion == True:

			v = ((vx)**2 + (vy)**2)**(1/2) 	

			return np.array([vx, -B*v*vx, vy, -g - B*v*vy])

		else:

			return np.array([vx, 0, vy, -g]) 
