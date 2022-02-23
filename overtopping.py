def plot_overtop(alpha, Tp, factor_berm, 
                factor_roughness, factor_waves, factor_wall, factor_combi, H_sig, design_water_level=design_water_level, max_q=10):
  import numpy as np 
  import matplotlib.pyplot as plt
  surcharge=0.6
  discharge = np.linspace(0.1,200, 100) / 1000
  overtop_discharge = max_q / 1000
  A=0.026 
  B=2.5
  g = 9.81
  Tm_10 = 0.9*Tp
  irribaren = np.tan(alpha) / np.sqrt(H_sig/ (1.56*Tm_10**2))
  Overtop_height = (factor_berm * factor_roughness * factor_waves * factor_wall 
                  * irribaren * H_sig * (1/1.35) 
                  * np.power(-1*np.log(discharge * np.sqrt( np.tan(alpha)) / 
                  (A * factor_berm * irribaren * np.sqrt(g*H_sig**3))), 1/1.3))
  Overtop_height_x = (factor_berm * factor_roughness * factor_waves * factor_wall 
                  * irribaren * H_sig * (1/1.35) 
                  * np.power(-1*np.log(overtop_discharge * np.sqrt( np.tan(alpha)) / 
                  (A * factor_berm * irribaren * np.sqrt(g*H_sig**3))), 1/1.3))
  overtop_height_nb = (factor_roughness * factor_waves * factor_combi 
                  * H_sig * (1/B) 
                  * np.power(-1*np.log(discharge / 
                  (0.1035 * np.sqrt(g*H_sig**3))), 1/1.3))
  overtop_height_nb_x = (factor_roughness * factor_waves * factor_combi 
                  * H_sig * (1/B) 
                  * np.power(-1*np.log(overtop_discharge / 
                  (0.1035 * np.sqrt(g*H_sig**3))), 1/1.3))
  total_x = np.minimum(Overtop_height_x, overtop_height_nb_x)
  total_q = np.minimum(Overtop_height, overtop_height_nb)
  design_crest_level = total_q + design_water_level + surcharge
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,10))
  fig.suptitle('Overtopping height and design crest height')
  ax1.plot(overtop_discharge*1000, total_x, 'ro')
  ax1.plot(discharge*1000, total_q, lw=4)
  ax2.plot(discharge*1000, design_crest_level, lw=4)
  ax1.set_title('Overtopping height')
  ax2.set_title('Design crest height')
  plt.setp(ax1, xlabel='Overtopping discharge [l/s/m]')
  plt.setp(ax2, xlabel='Overtopping discharge [l/s/m]')
  plt.setp(ax1, ylabel='Overtopping height [m]')
  plt.setp(ax2, ylabel='Design crest height [m+NAP]')
  plt.xlim([0, 200])
  ax1.set_ylim([0, 5])
  ax2.set_ylim([5, 10])
  ax1.legend(['Overtopping height for max q'])
  return
  

