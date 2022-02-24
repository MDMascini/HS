import numpy as np
import scipy.optimize as so

def frequency(water_level_freq, C, D):
    return np.exp(-(water_level_freq - C)/D)

def fit_func(waterlevels_f, frequencies, initial_guess=(2,2)):
  parameters, k = so.curve_fit(frequency, [water_level_100y, water_level_1000y], 
                          [f_100, f_1000], initial_guess);
  C = parameters[0]
  D = parameters[1]
  return C, D

f = np.linspace(1/100000, 1, 1000)

def water_level(f, C, D):
  return -np.log(f)*D + C 
