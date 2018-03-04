import numpy as np
import matplotlib.pyplot as plt
from standard import get_standard_atmosphere_1d
from standard import get_standard_atmosphere_2d
from standard import get_standard_atmosphere_3d

# 1d "profile" example
z = np.arange(1,80000,100)
p, t = get_standard_atmosphere_1d(z)
figs, axs = plt.subplots(nrows = 1, ncols = 2, figsize=(8,4))
axs[0].plot(p,z)
axs[0].set_title('Pressure Profile')
axs[0].set_xlabel('Pressure (Pa)')
axs[0].set_ylabel('Height (km)')
axs[1].plot(t,z)
axs[1].set_title('Temperature Profile')
axs[1].set_xlabel('Temperature (K)')
axs[1].set_ylabel('Height (km)')
plt.tight_layout()
plt.show()
