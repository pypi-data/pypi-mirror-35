from stl_tools import numpy2stl
from matplotlib._png import read_png
from skimage.transform import resize
from scipy.ndimage import gaussian_filter
import numpy as np
import matplotlib.pyplot as plt
import sunpy.io as io
import subprocess

def km_per_pixel(arcs_per_pix=1.):
	#this uses known values to approximate the number of km per pixel
	dist_earth_to_sun = 151000000. #in km, changes depending on time
	degree_per_arcsec = 1./3600. 
	rad_per_degree = np.pi/180.
	km_per_pixel = (np.sin((degree_per_arcsec * arcs_per_pix * rad_per_degree / 2.))
	 * dist_earth_to_sun * 2.)
	square_km_per_pixel = km_per_pixel**2.
	return km_per_pixel
	
def stl_file_maker(file, interval=1.5, threshold=0.35, fname='test.stl', gaussian=1):
	'''
	This uses the stl_tools numpy2stl in order to convert an array into a 3D printable
	model. This cannot take xyz dimensions and cannot make the full 3D model. It makes the
	2D image 3D printable.

	Parameters:

	file : str, name of the file, should be png

	interval : float, rate at which points are taken from the image

	threshold : float, minimum threshold for intensity value

	fname : str, name of exported file

	gaussian : int, number of loops of gaussian filtering data goes through
	'''

	earth_radius = 6371 #km

	scale_factor_percent = 0.3

	#Does not work with cropped image 
	#data = io.read_file('2014_05_27__14_38_31_12__SDO_AIA_AIA_304.jp2')	
	header = io.read_file_header(file+'.jp2')

	image = read_png(file+'.png')

	km_per_pixel = km_per_pixel(arcs_per_pix=header[0].__getitem__('IMSCL_MP'))

	#center points for the earth to scale figure

	earth_scale_y = 35
	earth_scale_x = image.shape[1] - 35 #px
	earth_box = 2
	
	earth_radius_px = earth_radius / km_per_pixel 
	
	for xpoint in range(data.shape[0]):
		for ypoint in range(data.shape[1]):
			if (np.sqrt((xpoint - earth_scale_x)**2 + (ypoint - earth_scale_y)**2) <= earth_radius_px):
				data[xpoint][ypoint] = 0.1
			elif (((np.absolute(xpoint - (earth_scale_x - earth_scale_y)) < earth_box) & (ypoint < (2. * earth_scale_y))) 
				or (((np.absolute(ypoint - (2. * earth_scale_y)) < earth_box)) & (xpoint > (earth_scale_x - earth_scale_y)))):
				data[xpoint][ypoint] = 0.05
			elif (data[xpoint][ypoint] <= threshold):
				data[xpoint][ypoint] = 0
			else:
				data[xpoint][ypoint] = (data[xpoint][ypoint] - threshold) / (1 - threshold)

	data = resize(data, (int(data.shape[0]/interval), int(data.shape[1]/interval)))
	
	data = gaussian_filter(data, gaussian)
	
	#dimensions in mm, if scale = 100, then the dimensions will be exact
	numpy2stl(data, fname, scale=100, solid=True, max_width=228.6, 
	max_depth=228.6, max_height=80, force_python=True)	

	subprocess.call(['bash', 'filemover.sh', fname])
	
def TwoDPlot(file, save=False):
	image = read_png(file+'.png')
	#creates figure
	fig = plt.figure(figsize=(10.,10.))
	#2D drawing of the image
	ax = fig.add_subplot(1, 1, 1)
	ax.imshow(image)
	ax.imshow(image)#, cmap=plt.cm.gist_heat, origin='lower')
	if (save):
		plt.savefig('2d.png')
	plt.show()

'''
file = '2012_04_16__17_38_56_12__SDO_AIA_AIA_304'

#TwoDPlot(file, save=False)

stl_file_maker(file, interval=2, threshold=0.35, fname='test.stl', gaussian=1)

#closes all plots
#plt.close('all')
'''