from scipy.constants import G
from numpy.matlib import sqrt


r=6371e3
M = 5.972e24

ve=sqrt((2*G*M)/r)

print(round(ve/1000,3))