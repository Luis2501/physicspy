"""


Note:

This module

"""

import numpy as np 

class EquationsSolver:

	"""
	This class allows 
	"""

	def __init__(self, f, df = None):

		self.df = df

		if isinstance(f, (int, float)):

			self.f = lambda x: f 

		elif callable(f): 

			self.f = f

		else: 

			raise Exception("The function is not defined")
			
	def __str__(self):
	
		try:
	
			return f"The interval or point: {self.x0}"

		except:
		
			raise Exception("Parametrs is not defined")

	def initial_conditions(self, x0, tol, maxiter = None):
	
		if tol <=0 or maxiter <=0:
		
			raise Exception("La toleracia o las iteraciones estan mal definidas") 

		if isinstance(x0, (int, float)):
	
			self.point, self.interval = True, False
			x0 = float(x0)

		elif isinstance(x0, (list, tuple)):

			self.point, self.interval = False, True
			x0 = list(x0)

		else:
		
			raise Exception("The interval or point is not defined")

		self.x0, self.tol, self.maxiter = x0, tol, maxiter

class Bisection(EquationsSolver):

	def Solve(self):

		if isinstance(self.x0, (int, float)):
	
			raise ValueError("The interval is not defined")

		a, b  = self.x0 
		f, tol = self.f, self.tol
		
		if a > b:

        		raise ValueError("Intervalo mal definido")

		if f(a) * f(b) >= 0.0:
        
			raise ValueError("La función debe cambiar de signo en el intervalo")

		if tol <= 0:

        		raise ValueError("La cota de error debe ser un número positivo")
		
		x = (a + b) / 2.0

		while True:

			if b - a < tol:

				return x
      
			elif np.sign(f(a)) * np.sign(f(x)) > 0:
	
            			a = x

			else:
				b = x
			
			x = (a + b) / 2.0

class Newton_Rhapson(EquationsSolver):

	def Solve(self):
   
		x, f, df, maxiter, tol = self.x0, self.f, self.df, self.maxiter, self.tol 
	
		if df(x) == 0:

			raise ValueError("Division by zero. The method ended.")
    		
		for i in range(maxiter):

		        dx = -f(x) / df(x) 

		        x = x + dx

		        if abs(dx / x) < tol and abs(f(x)) < tol:

		            return x

		raise RuntimeError(f"There was no convergence after {maxiter} iterations")

class Secant(EquationsSolver):

	def Solve(self):

		f, maxiter, tol = self.f, self.maxiter, self.tol 
		a, b = self.x0	

		i = 0

		while i < maxiter:
			
			try: 
		
				x = b - float(f(b))/(float(f(b) - f(a))/(b - a))

				er = abs(x-b)/abs(x)

			except ZeroDivisionError:

				print("Error en el denominador, para x = ", x)

				break

			if er < tol:

				return x

			a = b
			b = x
			i += 1
    		
		return x
