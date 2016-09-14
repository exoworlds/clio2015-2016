from astropy.io import fits
import numpy as np
file_name= "Test31_00007.fit"
hdulist = fits.open(file_name)
image = hdulist[0].data
#image = image.astype(float) - np.median(image)
from photutils import daofind
from astropy.stats import mad_std
bkg_sigma = mad_std(image)
sources = daofind(image, fwhm=15., threshold=25.*bkg_sigma)
print(sources)

from photutils import aperture_photometry, CircularAperture
positions = (sources['xcentroid'], sources['ycentroid'])
apertures = CircularAperture(positions, r=8.)
phot_table = aperture_photometry(image, apertures)
print (phot_table)

import matplotlib.pylab as plt
im2 = image
im2[im2<=0]=0.0001
plt.imshow(im2, cmap='gray', origin='lower')
apertures.plot(color='blue', lw=1.5, alpha=0.5)
plt.show()