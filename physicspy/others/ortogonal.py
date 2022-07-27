import numpy as np

def H(x, n):

	if n==0:

		return np.ones(len(x))
    
	elif n==1:

		return 2*x

	else:

		return 2*x*H(x,n-1)-2*(n-1)*H(x,n-2)

def P(x, n):

	if n == 0: 

		return np.ones(len(x))

	elif n == 1:

		return x

	else:

		return  (( x*(1+ 2*(n-1))*P(x, n - 1) - (n-1)*P(x, n - 2) )/(n))
