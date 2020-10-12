#Importing the required libraries
import scipy
import numpy as np
from scipy.integrate import dblquad
from scipy import integrate


def exp_fun(y, x):
    return np.exp(-x-y)


def probability_exp():
    val=dblquad(lambda x, y: np.exp(-x-y), 0, np.inf, lambda y: 0, lambda x: x)
    return val

if __name__=="__main__":
    val = probability_exp()
    print(val)



