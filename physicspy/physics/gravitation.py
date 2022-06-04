import numpy as np

class Orbit:
	
	"""
	Clase que permité calcular las órbitas
	de cualquier planeta.
	"""

	def __init__(self):

		self.GM = -4*(np.pi**2)

	def __call__(self, u, t):	

		x, y, vx, vy = u 
		GM, r = self.GM, (np.sqrt(x**2 + y**2))**3

		return np.array([vx, vy, (GM*x)/r, (GM*y)/r])
		
class Elliptical_Orbit:
	
	"""
	Clase que permité calcular las órbitas
	de cualquier planeta.
	"""

	def __init__(self):

		self.GM = -4*(np.pi**2)

	def __call__(self, u, t):	

		x, y, vx, vy = u 
		GM, r = self.GM, (np.sqrt(x**2 + y**2))**3

		return np.array([vx, vy, (GM*x)/r, (GM*y)/r])
		
class Three_body_problem:

	def __init__(self, Ms, Mp0, Mp1):

		self.GM = 4*(np.pi**2)
		self.GMp0, self.GMp1 = self.GM*(Mp0/Ms), self.GM*(Mp1/Ms)

	def __call__(self, u, t):	

		x0, y0, x1, y1, vx0, vy0, vx1, vy1 = u 

		GM, r0 = self.GM, (np.sqrt(x0**2 + y0**2))**3
		GMp0, r01 = self.GMp0, (np.sqrt((x0 - x1)**2 + (y0 - y1)**2))**3
		GMp1, r1 = self.GMp1, (np.sqrt(x1**2 + y1**2))**3

		return np.array([vx0,	vy0,	vx1,	vy1, 
				-(GM*x0)/(r0) - (GMp0*(x0 - x1))/(r01), 
				-(GM*y0)/(r0) - (GMp0*(y0 - y1))/(r01), 
				-(GM*x1)/(r1) - (GMp1*(x1 - x0))/(r01), 
				-(GM*y1)/(r1) - (GMp1*(y1 - y0))/(r01) ])
