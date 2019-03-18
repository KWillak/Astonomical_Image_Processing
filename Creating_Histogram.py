from astropy.io import fits
import numpy as np
import scipy
from scipy.optimize import curve_fit
import matplotlib.pyplot as pl
from scipy.stats import norm
import pickle
import Funtions as F

hdulist = fits.open(r"C:\Users\Kamil\Documents\Imperial\3rd year lab\Astronomical image processing\Pictures\A1_mosaic\A1_mosaic.fits")
hdulist[0].header
data = hdulist[0].data
# i = y, j = x , setting all dead pixels to zero
for i in range(4510, len(data)):
    for j in range(0, len(data[1])):      #top side
        data[i, j] = 0
for i in range(0, len(data)):             #right side
    for j in range(2470, len(data[1])):
        data[i, j] = 0
for i in range(0, len(data)):             #left side
    for j in range(0, 100):
        data[i, j] = 0
for i in range(0, 100):                   #bottom side
    for j in range(0, len(data[1])):
        data[i, j] = 0
pickle.dump(data, open("data.p", "wb+"))

Intensity = []


Intensity, mu, sigma = F.Gaussian(data)
# the histogram of the data
n, bins, patches = pl.hist(Intensity, 54, normed=1, facecolor='green', alpha=0.75)
# add a 'best fit' line
y = pl.mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--', linewidth=2)
pl.show()
