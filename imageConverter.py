from matplotlib.image import imread
import matplotlib.pyplot as plt
# from PIL import Image, ImageDraw
import numpy as np
import scipy.misc as smp

RGB_MAX = 255



class ImageConverter:


	def __init__(self, imgName):
		self.imgName = imgName

	def rgbToHsi(self):
		print("Starting convertion of image: " + self.imgName + " to format HSI...")
		print("At the end, you'll be able to see the normalized image.")

		exit("hsi")

	def rgbToCmyk(self):
		print("Starting convertion of image: " + self.imgName + " to format CMYK...")
		print("At the end, you'll be able to see the normalized image.")
		
		img = imread(self.imgName)

		x = len(img)
		y = len(img[0])
		data = np.zeros((x,y,3), dtype=np.uint8 )
		originalData = data
		for i in range(len(img)):
			for j in range(len(img[i])):
				pixel = self.__rgbToCmykPix(img[i][j][0], img[i][j][1], img[i][j][2])
				newPixel = self.__cmykRgbNormalizer(pixel)
				data[i][j] = newPixel
				
		# print(img[0][0])
		imgPlot = plt.imshow(data)
		
		plt.show()
		# plt.show()

	def __rgbToCmykPix(self, r, g, b):
		if(r,g,b) == (0,0,0):
			return 0,0,0,1
		
		# Getting cmy
		c = 1 - r / RGB_MAX
		m = 1 - g / RGB_MAX
		y = 1 - b / RGB_MAX
		
		# Getting k
		minCmy = min(c,m,y)
		c = (c - minCmy) / (1 - minCmy)
		m = (m - minCmy) / (1 - minCmy)
		y = (y - minCmy) / (1 - minCmy)
		k = minCmy

		return c, m, y, k
	
	def __cmykRgbNormalizer(self, cmyk):
		k = cmyk[3]
		r = (cmyk[0] + k) * 255
		g = (cmyk[1] + k) * 255
		b = (cmyk[2] + k) * 255
		tupla = [r,g,b]
		return tupla