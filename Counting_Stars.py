from astropy.io import fits
import numpy as np
import scipy
from scipy.optimize import curve_fit
import matplotlib.pyplot as pl
from scipy.stats import norm
import pickle
from Creating_Histogram import Gaussian


data = pickle.load(open("data.p", "rb"))
Intensity, mean, sigma = Gaussian(data)
##j = x, i = y
Positions = []
for i in range(0, len(data)):
    for j in range(0, len(data[1])):
        if  (mean + 3*sigma) < data[i, j]:
             Positions.append([i, j])
print(Positions)
