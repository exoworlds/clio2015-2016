import astropy.io.fits
import numpy
import pyds9

read1 = []
write1 = []

for i in range(1, 15):
    if i < 10:
        readfile1 = "/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/raw/Test31_0000%d.fit" %i
        writefile1 = "/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/sub/Test31_0000%d.fit" %i
        read1.append(readfile1)
        write1.append(writefile1)
    else:
        readfile1 = "/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/raw/Test31_000%d.fit" %i
        writefile1 = "/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/sub/Test31_000%d.fit" %i
        read1.append(readfile1)
        write1.append(writefile1)
        

read2 = []
write2 = []

for i in range(1, 15):
 if
    i2 = (i-1) % 4 + 1
    readfile2 = "/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/raw/Test31sky_0000%d.fit" %i2
    writefile2 = "/Users/jennifervezilj/mypy/Python/data/clio_20141130_01/sub/Test31sky_0000%d.fit" %i2
    read2.append(readfile2)
    write2.append(writefile2)

for i in range(0, 14):
	file1 = read1[i]
	file2 = read2[i]

	print file1
	print file2 

for i in range(0, 14):
	print i, readfile1
	readfile1 = read1[i]
	readfile2 = read2[i]

	
#	  path plus the file : astropy.io.fits.open(clio_20141102_03/TrapNarrowHunsat00001)
	hdulist1 = astropy.io.fits.open(readfile1)
	hdulist2 = astropy.io.fits.open(readfile2)
	hdulist1.info()
	hdulist2.info()
        
#Create a new FITS file for the answer
	hdulist1sub = hdulist1
	hdulist2sub = hdulist2
	hdulist1sub[0].data = hdulist1[0].data - hdulist2[0].data
	hdulist2sub[0].data = hdulist2[0].data - hdulist1[0].data
	writefile1 = write1 [i]
	writefile2 = write2 [i]
	hdulist1sub.writeto(writefile1, clobber=True)
        
    
    
# Alternate way to do it: Copy the HDUlist
# 
#    # Display the new HDU list in ds9
#     print pyds9.ds9_targets()
#    - If says "None" this means you do not have a ds9 session running - start up ds9
#    - Should say something like " ['DS9:ds9 c0a8000f:50436']"
#     d = pyds9.DS9()
#     d.set_pyfits(hdu_sub)  #This will display the image in ds9
# 
#     return hdu_sub