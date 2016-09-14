from astropy.io import fits
import numpy as np

read1 = []

for i in range(6, 15):
    if i < 10:
        path = "/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/sub/"
        file_name = "Test31_0000%d.fit" %i
        read1.append(file_name)
    else:
        path = "/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/sub/"
        file_name = "Test31_000%d.fit" %i
        read1.append(file_name)

len(read1) 
      
for i in range(0, 9):
	file_name = read1[i]

	hdulist = fits.open(path+file_name)
	image = hdulist[0].data
	#image = image.astype(float) - np.median(image)
	from photutils import daofind
	from astropy.stats import mad_std
	bkg_sigma = mad_std(image)
	sources = daofind(image, fwhm=15., threshold=25.*bkg_sigma)
	#print_line= (file_name+","+str(sources_2)+"\n")
	sources_2 = np.array(sources["id", "xcentroid", "ycentroid", "sharpness", "roundness1", "roundness2", "npix", "sky", "peak", "flux", "mag"])
	print_line= (file_name+","+str(sources_2))
	file= open("/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/code/test31_phot.txt", "a")
	file.write(print_line)
	file.close()

	from photutils import aperture_photometry, CircularAperture
	positions = (sources['xcentroid'], sources['ycentroid'])
	apertures = CircularAperture(positions, r=8.)
	phot_table = aperture_photometry(image, apertures)
	phot_table_2 = np.array(phot_table["aperture_sum", "xcenter", "ycenter"])
	print_line= (","+str(phot_table_2)+"\n")
	file= open("/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/code/test31_phot.txt", "a")
	file.write(print_line)
	file.close()

	import matplotlib.pylab as plt
	im2 = image
	im2[im2<=0]=0.0001
	plt.imshow(im2, cmap='gray', origin='lower')
	apertures.plot(color='blue', lw=1.5, alpha=0.5)
	plt.show()