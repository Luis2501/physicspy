import numpy as np 

class Pendulo:

	def __init__(self, g, l, m, q = 0, Fd = 0, omega = 0, Linear = True):

		self.g, self.l, self.m = g, l, m
		self.q, self.Fd, self.omega = q, Fd, omega

	def __call__ (self, u, t):

		theta, vtheta = u
		g,l,  = self.g, self.l 
		q, Fd, omega = self.q, self.Fd, self.omega 
				
		if Linear:

			return np.array([vtheta, (-g/l)*theta - q*vtheta + Fd*np.sin(omega*t)])

		else: 

			return np.array([vtheta, (-g/l)*np.sin(theta) - q*vtheta + Fd*np.sin(omega*t)])
	
