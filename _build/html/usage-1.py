import numpy as np
import matplotlib.pyplot as plt
import sys
from skimage.io import imread
from cir_ave.cir_ave import oneD_intensity
import os
from pkg_resources import resource_filename

address = '/Users/jiliangliu/mpi_test/simple_cubic.tif'
im = imread(address)
image_x0 = 1008.88
image_y0 = 1056.78
I = oneD_intensity(im=im,xcenter=image_x0,ycenter=image_y0).cir_ave()
wavelength = 1.24
std = 4.960
pixel_size = 80.5
q = 2*np.pi*np.sin(np.arcsin(80.5*np.arange(0,len(I))*1e-6/4.96))/wavelength

fig,ax = plt.subplots()
ax.imshow(np.log(im))

fig,ax = plt.subplots()
ax.plot(q,np.log(I))
plt.show()