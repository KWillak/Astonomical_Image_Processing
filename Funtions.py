from astropy.io import fits
import numpy as np
import scipy
from scipy.optimize import curve_fit
import matplotlib.pyplot as pl
from scipy.stats import norm
import pickle



def Gaussian(data):
    # creating a 1D array that stores all pixel values

    for i in range(len(data)):
        for j in range(len(data[1])):
            if 3390 < data[i, j] < 3445:
                 Intensity.append(data[i, j])

    # best fit of data
    (mu, sigma) = norm.fit(Intensity)

    return Intensity, mu, sigma
