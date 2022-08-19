
#legendre polynomial
#(2) n*P(n,x) = x*P'(n,x)-P'(n-1,x)

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=int(input("Enter the n: "))
def f(x):
    return legendre(n)(x)
def g(x):
    return legendre(n-1)(x)

LHS=n*(legendre(n)(x))
RHS=x*derivative(f,x,order=15)-derivative(g,x,order=15)
print("LHS: ",LHS)
print("RHS: ",RHS)
