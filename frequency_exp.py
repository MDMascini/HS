import numpy as np
import scipy.optimize as so

def frequency(water_level_freq, C, D):
    return np.exp(-(water_level_freq - C)/D)

def fit_func(waterlevels_f, frequencies, initial_guess=(2,2)):
  parameters, k = so.curve_fit(frequency, waterlevels_f, 
                          frequencies, initial_guess);
  C = parameters[0]
  D = parameters[1]
  return C, D

f = np.linspace(1/100000, 1, 1000)

def water_level(f, C, D):
  return -np.log(f)*D + C 

def make_plot(f, water_levels, waterlevels_f, frequencies):
  plt.plot(frequencies, waterlevels_f, 'ro')
  plt.plot(f, water_levels)
  plt.xscale('log')
  plt.ylabel('Water level [NAP+m]')
  plt.xlabel('frequency [1/year]')
  plt.title('Water level - frequency curve');
  print('The 4000 year return water level is',np.round(water_level(1/4000, C, D), 2), 
        'm + NAP')
